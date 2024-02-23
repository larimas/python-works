from pc import Computer


class Laptop(Computer):

    
    def __init__ (self, size = None):

        Computer.__init__(self, brand, hddSize, ramSize, systemArch, regularPrice, discountPercentage, discountPrice)
        self.__size = size


    @property    
    def get_size(self):
        return self.__size

    @get_size.setter
    def set_size(self, size):
        if cpuCores != None:
            self.__size = size

    def __str__(self):
        return f'brand: {self._brand}, hddSize: {self._hddSize}, ramSize: {self._ramSize}, systemArch: {self._systemArch}, regularPrice: {self._regularPrice}, discountPercentage: {self._discountPercentage}, discountPrice: {self._discountPrice}, size: {self.__size}'


    @classmethod
    def createComputer(cls, c):

        if isinstance(c, Laptop):
            return cls(c._size)
        else:
            print('This is not a type of notebook.')
            return None