# class Borg(object):
#     _shared_state = {}
#     def __new__(cls, *a, **k):
#         obj = super(Borg, cls).__new__(cls, *a, **k)
#         obj.__dict__ = cls._shared_state
#         return obj

class Borg(object):
    _shared_state = {}
    def __init__(self):
        self.__dict__ = self._shared_state

class SubBorg(Borg):
    def __init__(self):
        super(SubBorg, self).__init__()
        self.state = "sub"

b = Borg()
b.a = 'hi'

c = SubBorg()
print c.a  # prints 'hi'


import os

if __name__=='__main__':
    for filename in os.listdir('.'):
        if filename.find('-') >=0:
            new_filename = filename.replace('-', '_')
            os.rename(filename, new_filename)
    for filename in os.listdir('.'):
        if filename.startswith("2014"):
            new_filename = 'fc_' + filename
            os.rename(filename, new_filename)
