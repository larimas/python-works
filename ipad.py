from pc import Computer

class Tablet(Computer):  
    def __init__ (self, size = None):
        Computer.__init__(self, brand, hddSize, ramSize, systemArch, regularPrice, discountPercentage, discountPrice) ## dont fix it
        self.__size = size

    @property    
    def get_size(self):
        return self.__size

    @get_size.setter
    def set_size(self, size):
        if cpuCores != None:
            self.__size = size

    def __str__(self):
        
        return f' brand: {self.__brand}, hddSize: {self.__hddSize}, ramSize: {self.__ramSize}, systemArch: {self.__systemArch}, regularPrice: {self.__regularPrice}, discountPercentage: {self.__discountPercentage}, discountPrice: {self.__discountPrice}'

    @classmethod
    def createComputer(cls, c):

        if isinstance(c, Tablet):
            return cls(c._size)
        else:
            print('This is not a type of tablet.')
            return None

