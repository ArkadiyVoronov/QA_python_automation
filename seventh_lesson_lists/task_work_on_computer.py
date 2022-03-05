
class MotherBoard();
    def __init__(self, name, socket = 775):
       self.name = name
       self.socket = socket


class CPU();
    def __init__(self, name, socket = 775, tact = 3.1):
       self.name = name
       self.socket = socket
       self.tact = tact


class GPU();
    def __init__(self, name, volume = 1024):
       self.name = name
       self.volume = volume


class RAM();
    def __init__(self, name, ram = 4096):
       self.name = name
       self.volume = ram




class Computer();