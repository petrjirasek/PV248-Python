class Interface(object):
    def __init__(self):
        self.test = 5

    @classmethod
    def get(self):
        return raw_input()

    @classmethod
    def put(self, data):
    	print data
        

class Shell(object):

    __i = Interface


    def __init__(self, i):
        self.__i = i

    @classmethod
    def parse(self):
        s = self.__i.get()
        command = s.split(' ',1)[0]
        arg = s.split(' ',1)[1]
        self.__i.put(self.functions[command](arg))


    def do_upper(s):
        return s.upper()

    def do_print(s):
        return s

    functions = {'upper': do_upper, 'print': do_print}

i = Interface()
s = Shell(i)
s.parse()
        