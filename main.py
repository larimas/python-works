from pc import Computer
from portatil import Laptop
from ipad import Tablet

counter = 0
x = "-"

def findPC(variable):

    for i in range(len(variable)):
        if variable[i] == "-":
            
            if i == 5:
                C = Computer.createComputerTwo(variable[0], variable[1], variable[2], variable[3], variable[4], variable[6])

                return C

            elif i == 6:
                C = Computer.createComputerOne(variable[0], variable[1], variable[2], variable[3], variable[4], variable[5])

                return C

    C = Computer(variable[0], variable[1], variable[2], variable[3], variable[4], variable[5], variable[6])

    return C
if __name__ == '__main__':
    
    with open('./product.txt', 'r') as ReadFile:
         for read in ReadFile:
             if counter != 0:
                 if counter == 1:
                     c01 = read
                     
                     c01 = c01.split("\t")
                     
                     c01 = findPC(c01)
                     print(c01)
                     
                 elif counter == 2:
                    c02 = read
                    
                    c02 = c02.split("\t")
                    
                    c02 = findPC(c02)
                    print(c02)
                 elif counter == 3:
                    c03 = read
                    
                    c03 = c03.split("\t")

                    c03 = findPC(c03)
                    print(c03)

                 else:
                    c04 = read
                    
                    c04 = c04.split("\t")
                    

                    c04 = findPC(c04)
                    print(c04)
                    
             
             counter = counter + 1


### print CPU_cores
    print("\n")

    print(c01.current_CPU_cores)
    print(c03.current_CPU_cores)
    
    print("\n")

    c01.set_Cores = 7
    c02.set_Cores = 3

### set the cores
    print(c01.current_CPU_cores)
    print(c02.current_CPU_cores)
    print("\n")

    c04.totalNofMonitors()
    
    c03.totalNofMonitors()

    laptopOne = Laptop('Apple', 455, 14, 64, 1600.21, 5, 1520.20)