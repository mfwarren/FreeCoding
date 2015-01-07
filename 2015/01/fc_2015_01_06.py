#!/usr/bin/env python
# imports go here
import rumps
import os
import datetime

#
# Free Coding session for 2015-01-06
# Written by Matt Warren
#

file_template = """#!/usr/bin/env python3
# imports go here

#
# Free Coding session for %s
# Written by Matt Warren
#
"""


class MyStatusBarHelper(rumps.App):
    @rumps.clicked("New File")
    def start_new_file(self, _):
        today = datetime.date.today()
        path = today.strftime(os.envget("FREECODE_DIR") + "/%Y/%m/")
        if not os.path.exists(path):
            os.makedirs(path)
        filename = today.strftime('fc_%Y_%m_%d.py')
        full_path = os.path.join(path, filename)
        if os.path.isfile(full_path):
            rumps.alert("Today's file is already created")
        else:
            with open(full_path, 'w') as file:
                file.write(file_template % today.isoformat())
        rumps.notification("Halotis", "started a new file", "good to go")

if __name__ == "__main__":
    MyStatusBarHelper("Halotis").run()
