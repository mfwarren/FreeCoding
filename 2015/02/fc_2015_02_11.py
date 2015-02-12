#!/usr/bin/env python3
# imports go here
import datetime

#
# Free Coding session for 2015-02-11
# Written by Matt Warren
#


class NotificationSettings:

    def __init__(self, starting_on, every_x_minutes, block_out_times, methods, message):
        self.starting_on = starting_on
        self.every_x_minutes = every_x_minutes
        self.block_out_times = block_out_times
        self.methods = methods

    def in_block_out(self, now):
        # not sure what block out times would be encoded as
        return False

    def should_send(self, now, last_sent):
        if now > self.starting_on and (now - last_sent).minutes > self.every_x_minutes and not self.in_block_out(now):
            return True
        return False

    def try_sending(self):
        if self.should_send(datetime.datetime.now):
            if 'email' in self.methods:
                mail(self.message)
            if 'sms' in self.methods:
                sms(self.message)
            if 'push' in self.methods:
                push_notification(self.message)
