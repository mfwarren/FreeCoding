#!/usr/bin/env python
# imports go here
from datetime import date

#
# Free Coding session for 2014-11-30
# Written by Matt Warren
#


class CPAFile():

    CLIENT_NUMBER = '0000000000'
    PROCESSING_CENTRE = '00000'
    # file_number = ''
    record_count = 0

    total_debit_amount = 0
    total_debit_count = 0
    total_credit_amount = 0
    total_credit_count = 0

    def __init__(self, **kwargs):
        # global file_number
        self.file_number = kwargs['file_number']
        self.today = self.format_date(date.today())
        self.record_count = 0
        self.transactions = kwargs['transactions']
        pass

    def format_date(self, d):
        return d.strfprint("0%y%j")

    def format_number(self, n, width):
        return "{0:>{1}}".format(n, width)

    def format_alpha(self, s, width):
        return "{0:<{1}}".format(s, width)

    def header_record(self):
        self.record_count += 1
        return "A%s%s%s%s%sCAD%s" % (self.format_number(self.record_count, 9),
                                     self.CLIENT_NUMBER,
                                     self.file_number,
                                     self.today,
                                     " " * 20,
                                     self.PROCESSING_CENTRE,
                                     " " * 1406)

    def footer_record(self):
        self.record_count += 1
        return "Z%s%s%s%s%sCAD%s" % (self.format_number(self.record_count, 9),
                                     self.CLIENT_NUMBER,
                                     self.file_number,
                                     self.format_number(self.total_debit_amount, 14),
                                     self.format_number(self.total_debit_count, 8),
                                     self.format_number(self.total_credit_amount, 14),
                                     self.format_number(self.total_credit_count, 8),
                                     "0" * 1396)

    def debit_records(self):
        all_records = []
        lr = ""
        for transaction in [t for t in self.transactions if t.is_debit]:
            assert(len(lr) <= 1464)
            if len(lr) == 1464:
                all_records.append(lr)
                lr = ''
            if len(lr) == 0:
                self.record_count += 1
                lr = 'D%s%s%s' % (self.format_number(self.record_count, 9),
                                  self.CLIENT_NUMBER,
                                  self.file_number)
            segment = '%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % (self.format_alpha(self.debit_transaction_code, 3),
                                                          self.format_number(transaction.amount, 10),
                                                          self.format_date(transaction.date),
                                                          self.format_number(transaction.routing_number, 9),
                                                          self.format_alpha(transaction.account_number, 12),
                                                          "0" * 25,
                                                          self.format_alpha(self.SHORT_NAME, 15),
                                                          self.format_alpha(transaction.customer_name, 30),
                                                          self.format_alpha(self.LONG_NAME, 30),
                                                          self.format_alpha(self.CLIENT_NUBMER, 10),
                                                          self.format_alpha(transaction.customer_number, 19),
                                                          "0" * 9,
                                                          " " * 12,
                                                          self.format_alpha(self.CLIENT_SUNDRY, 15),
                                                          " " * 35)
            self.total_debit_amount += transaction.amount
            self.total_debit_count += 1
            lr = lr + segment

        while len(lr) < 1464:
            lr = lr + self.blank_segment
        all_records.append(lr)

        return ''.join(all_records)

    def generate_file(self, filename):
        with open(filename, 'w') as f:
            f.write(self.header_record())
            f.write(self.debit_records())
            f.write(self.footer_record())
