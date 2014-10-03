#!/usr/bin/env python
#imports go here

#
# Free Coding session for 2014-10-02
# Written by Matt Warren
#

# example of 3-tier pattern

class Data:
    data = [{"account": 234, "name":"bob"},
        {"account": 643, "name":"joan"}]

    def __iter__(self):
        for d in self.data:
            yield d

    def find(self, account_number):
        for d in self.data:
            if d['account'] == account_number:
                return d

class Controller:
    def __init__(self):
        self.data = Data()

    def get_data(self):
        return self.data

    def get_name(self, account_number):
        return self.data.find(account_number).get("name", None)

    def get_accounts(self):
        return [f['account'] for f in self.data]

class UI:
    def __init__(self):
        self.controller = Controller()

    def print_names(self):
        accounts = self.controller.get_accounts()
        for acct in accounts:
            print acct
            print self.controller.get_name(acct)

if __name__=='__main__':
    ui = UI()
    ui.print_names()
