class Computer:

    __monitor = 1


    def __init__ (self, brand = None, hddSize = 0, ramSize = 0, systemArch = 0, regularPrice = 0.0, discountPercentage = 0.0, discountPrice = 0.0):

        self._cpuCores = 5
        self._brand = brand
        self._hddSize = hddSize
        self._ramSize = ramSize
        self._systemArch = systemArch
        self._regularPrice = regularPrice
        self._discountPercentage = discountPercentage
        self._discountPrice = discountPrice

    @property    
    def current_CPU_cores(self):
        return self._cpuCores

    @current_CPU_cores.setter
    def set_Cores(self, cpuCores):
        if cpuCores > 0:
            self._cpuCores = cpuCores

    @property
    def get_discountPercentage(self):
        return self._discountPercentage

    @get_discountPercentage.setter
    def set_discountPercentage(self, discountPercentage):
        if discountPercentage > 0:
            self._discountPercentage = discountPercentage

  
    @classmethod
    def createComputerOne(cls,brand = None,hddSize = 0,ramSize = 0,systemArch = 0, regularPrice = 0.0, discountPercentage = 0.0):
        return cls(brand,hddSize,ramSize,systemArch, regularPrice, discountPercentage)
    
    @classmethod
    def createComputerTwo(cls,brand = None,hddSize = 0,ramSize = 0,systemArch = 0, regularPrice = 0.0, discountPrice = 0.0):
        return cls(brand,hddSize,ramSize,systemArch, regularPrice, 0, discountPrice)
            
    @classmethod
    def totalNumberOfMonitor(cls):
        print(f'Total nº of monitors are {cls.__monitor}.')

    

    def __str__(self):
        
        return f'brand: {self._brand}, hddSize: {self._hddSize}, ramSize: {self._ramSize}, systemArch: {self._systemArch}, regularPrice: {self._regularPrice}, discountPercentage: {self._discountPercentage}, discountPrice: {self._discountPrice}'



    @classmethod
    def createComputer(cls, c):

        if isinstance(c, Computer):
            return cls(c._bran, c._hddSize, c._ramSize, c._systemArch, c._regularPrice, c._discountPercentage, c._discountPrice )
        else:
            print('This is not a type of computer.')
            return None