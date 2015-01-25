#!/usr/bin/env python3
# imports go here
import sys

#
# Free Coding session for 2015-01-24
# Written by Matt Warren
#

# all the numbers come from https://www.cdnpay.ca/imis15/pdf/pdfs_rules/standard_005.pdf


def read_a_record(line):
    if line[0] != 'A':
        raise Exception("First line must be 'A' record")
    if line[1:9] != '000000001':
        raise Exception("First line must be record 1")
    return {
        'record type': line[0],
        'line number': line[1:9],
        'originator id': line[10:19],
        'file creation number': line[20:23],
        'creation date': line[24:29],
        'destination data centre': line[30:34],
        'reserved customer-direct communcation area': line[35:54],
        'currency': line[55:57],
    }


def read_cd_segment(segment):
    if segment[0:2] == '   ':
        return None
    return {
        'Transaction Type': segment[0:2],
        'Amount': segment[3:13],
        'Date Funds to be Available': segment[14:20],
        'Institutional Identification No.': segment[21:30],
        'Payee Account No.': segment[31:43],
        'Item Trace No.': segment[44:66],
        'Stored Transaction Type': segment[67:70],
        'Originator\'s Short Name': segment[71:86],
        'Payee Name': segment[87:117],
        'Originator\'s Long Name': segment[118:148],
        'Originating Direct Clearer\'s User\'s ID': segment[149:159],
        'Originator\'s Cross Reference No.': segment[160:179],
        'Institutional ID Number for Returns': segment[180:189],
        'Account No. for Returns': segment[190:202],
        'Originator\'s Sundry Information': segment[203:218],
        'Originator-Direct Clearer Settlement code': segment[230:232],
        'Invalid Data Element I.D.': segment[233:244]
    }


def read_cd_record(line):
    assert_line_length(line)
    if line[0] != 'C' or line[0] != 'D':
        raise Exception("Should start with C or D")
    transactions = [read_cd_segment(line[24:263]),
                    read_cd_segment(line[264:504]),
                    read_cd_segment(line[505:744]),
                    read_cd_segment(line[745:984]),
                    read_cd_segment(line[985:1224]),
                    read_cd_segment(line[1225:1464])]
    transactions = [i for i in transactions if not None]
    if line[0] == 'C':
        transaction_type = 'credits'
    else:
        transaction_type = 'debits'
    return {
        'record type': line[0],
        'line number': line[1:9],
        'Origination Control Data': line[10:23],
        transaction_type: transactions
    }
    pass


def read_z_record(line):
    if line[0] != 'Z':
        raise Exception("Last line must be 'Z' record")
    assert_line_length(line)
    return {
        'record type': line[0],
        'line number': line[1:9],
        'Origination Control Data': line[10:23],
        'Total Value of Debit Transactions': line[24:37],
        'Total Number of Debit Transactions': line[38:45],
        'Total Value of Credit Transactions': line[46:59],
        'Total Number of Credit Transactions': line[60:67],
        'Total Value of Error Corrections "E"': line[68:81],
        'Total Number of Error Corrections "E"': line[82:89],
        'Total Value of Error Corrections "F"': line[90:103],
        'Total Number of Error Corrections "F"': line[104:111]
    }


def assert_line_length(line):
    if len(line) != 1464:
        raise Exception("Line length is not equal to 1464")


def parse_file(filename):
    with open(filename) as f:
        lines = f.readlines()

        print(read_a_record(lines[0]))
        for line in lines[1:-1]:
            if line[0] == 'D' or line[0] == 'C':
                print(read_cd_record(line))
        print(read_z_record(line[-1]))


if __name__ == '__main__':
    parse_file(sys.argv[1])
