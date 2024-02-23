"""
student: larissa (2234567)
Question 1 = random len by adding a number from a repitition chara; string
"""
def printRepe(s) :
	i = 0
	while( i < len(s) - 1) :
		count = 1

		while s[i] == s[i + 1] :

			i += 1
			count += 1
			
			if i + 1 == len(s):
				break
		
		print(str(s[i]) + str(count), 
						end = " ")
		i += 1	
	print()
## given example with the function
if __name__ == "__main__" :
	printRepe("gggN@@@@@KKeeeejjdsmmu")
	## try with others
	printRepe("pipipipopopopapapa")
	printRepe("lalalaaaaaaa")
