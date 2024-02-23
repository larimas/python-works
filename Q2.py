"""
student: larissa (2234567)
Question 2 - python program to find the binary equivalent of a number
without using bin() function

### with the example from the question
def binaryNumber(num):
	
	if num >= 1:
		binaryNumber(num // 2)
	print(num % 2, end = '') ## modulo to find the equivalent nº
## return the binary number of 10
if __name__ == '__main__':
	dec_val = 10
	binaryNumber(dec_val)
## return the binary number of 30
if __name__ == '__main__':
	dec_val = 30
	binaryNumber(dec_val)
    
"""
## user input
n = int(input("Enter a number : "))
modulo = n % 2
div = int(n/2)
result = str(modulo)
## return
while div != 0:
	modulo = int(div % 2)
	div = int(div/2)
	result = str(modulo) + result
print(f"Binary equivalent of {n} is {result}")
