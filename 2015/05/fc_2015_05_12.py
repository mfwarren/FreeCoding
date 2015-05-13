#!/usr/bin/env python3
# imports go here
import json
import os
import datetime
import re

from refreshbooks import api
import requests

#
# Free Coding session for 2015-05-12
# Written by Matt Warren
#

SLACK_HOOK_URL = 'https://hooks.slack.com/services/Something'

freshbooks = api.TokenClient(
    os.environ['FRESHBOOKS_DOMAIN'],
    os.environ['FRESHBOOKS_API_TOKEN']
)


def post_to_slack(message):
    payload = {'channel': '#issues', 'text': message}
    requests.post(SLACK_HOOK_URL, data=json.dumps(payload))

def number_of_clients():
    try:
        return freshbooks.client.list().clients.attrib['total']
    except:
        return 0

def revenue_ytd():
    """
    Pull down all invoices and add up the totals
    """
    total_amount = 0
    total_amount_outstanding = 0
    year = str(datetime.date.today().year)

    invoices_response = freshbooks.invoice.list().invoices
    for invoice in invoices_response.invoice:
        if re.match(invoice.date, year):
            total_amount += invoice.amount
            total_amount_outstanding += invoice.amount_outstanding

    return total_amount, total_amount_outstanding

def main():
    clients = number_of_clients()
    amount, amount_outstanding = revenue_ytd()

    post_to_slack("[KPIs] total # of Clients: {0}, Revenue YTD: {1}, Outstanding: {3}".format(clients, amount, amount_outstanding))

if __name__ == '__main__':
    main()
