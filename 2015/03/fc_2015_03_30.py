#!/usr/bin/env python3
# imports go here
import csv

#
# Free Coding session for 2015-03-30
# Written by Matt Warren
#

# raw data downloaded from Stats Can:
# http://www5.statcan.gc.ca/cansim/a26?lang=eng&retrLang=eng&id=1110008&paSer=&pattern=&stByVal=1&p1=1&p2=37&tabMode=dataTable&csid=

# 2015 tax rates from: http://www.cra-arc.gc.ca/tx/ndvdls/fq/txrts-eng.html
# TODO: rewrite with namedtubple
CANADA = ((44701, 0.15), (44700, 0.22), (49185, 0.26), (float('inf'), 0.29))
NL = ((35008, 0.077), (35007, 0.125), (float('inf'), 0.133))
NS = ((29590, 0.0879), (29590, 0.1495), (33820, 0.1667), (57000, 0.175), (float('inf'), 0.21))
PEI = ((31984, 0.098), (31985, 0.138), (float('inf'), 0.167))
NB = ((39973, 0.0968), (39973, 0.1482), (50029, 0.1652), (float('inf'), 0.1784))
ON = ((40922, 0.0505), (40925, 0.0915), (68153, 0.1116), (70000, 0.1216), (float('inf'), 0.1316))
MB = ((31000, 0.108), (36000, 0.1275), (float('inf'), 0.174))
SK = ((44028, 0.11), (81767, 0.13), (float('inf'), 0.15))
AB = ((float('inf'), 0.1),)
BC = ((37869, 0.0506), (37871, 0.077), (11218, 0.105), (18634, 0.1229), (45458, 0.147), (float('inf'), 0.168))

PROVINCES = {'NL': NL,
             'NS': NS,
             'PEI': PEI,
             'NB': NB,
             'ON': ON,
             'MB': MB,
             'SK': SK,
             'AB': AB,
             'BC': BC
             }


def tier_tax(income, tiers):
    tax_amt = 0
    amt = income
    for tier in tiers:
        partial_amt = min(tier[0], amt)
        tax_amt = tax_amt + (partial_amt * tier[1])
        amt = amt - partial_amt
    return tax_amt


def slice_data(year, province):
    with open('01110008-eng.csv', "r", encoding='Cp1252') as csvfile:
        datareader = csv.reader(csvfile)
        for row in datareader:
            if row[0] == year and row[1] == province and row[3] == 'Both sexes' and row[4] == 'All age groups' and row[5].startswith('Persons with income of'):
                yield row

if __name__ == '__main__':
    # query out the data we want
    data = []
    for line in slice_data('2012', 'Alberta'):
        data.append(line)
        # print(line)

    # NOTE: I've assumed an average income 1/2 way between each bucket, and avg above $250K at $500K
    buckets = [7500, 12500, 17500, 22500, 30000, 42500, 62500, 87500, 125000, 175000, 225000, 500000]

    # produce (avg_income, num_of_people)
    avg_income_counts = []
    for i in range(1, len(buckets)):
        prev_count = float(data[i-1][8])
        avg_income_counts.append((buckets[i-1], prev_count - float(data[i][8])))
    avg_income_counts.append((buckets[-1], float(data[-1][8])))

    # print(avg_income_counts)

    # NOTE: the absolute number here is off by about 30-50% from reported in annual budget
    # not sure how much is due to tax deductions, or mis-calculation
    total_income = 0
    for income, population in avg_income_counts:
        total_income += (tier_tax(income, AB) * population)

    print("Estimated Alberta income: %f", total_income)

    for province, tiers in PROVINCES.items():
        scheme_total = 0
        for income, population in avg_income_counts:
            scheme_total += (tier_tax(income, tiers) * population)
        difference = ((scheme_total - total_income) / total_income) * 100
        print("Using %s Tax scheme income is %.1f%% %s" % (province, abs(difference), 'more' if difference > 0 else 'less'))
    print(total_income)




    # incomes = list(range(20000, 500000, 5000))
    # after_tax_amount = [tax2015(amt) for amt in incomes]
    # line = Scatter(x=incomes, y=after_tax_amount)
    # data = Data([line])
    # layout = Layout(
    #     title='Federal Income Tax Amount - Canada 2015 tax rules',
    #     xaxis=XAxis(
    #         title='Income',
    #         showgrid=False,
    #         zeroline=False
    #     ),
    #     yaxis=YAxis(
    #         title='Income Tax',
    #         showline=False
    #     )
    # )
    # fig = Figure(data=data, layout=layout)
    # plot_url = py.plot(fig, filename='Federal Tax Amount - Canada 2015 tax rules')
    # print(plot_url)
