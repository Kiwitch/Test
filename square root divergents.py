from fractions import Fraction

def digit_exceeds(nominator,denominator): #WORKS
	#returns True if the number of digits of the numerator exceeds the one of the denominator
	i = 0
	while True:
		if nominator//(10**i)>0 and not denominator//(10**i)>0:
			return True
		if denominator//(10**i)>0 and not nominator//(10**i)>0:
			return False
		if nominator//(10**i)==0 and denominator//(10**i)==0:
			return False
		i += 1

def generate_expansion(n):
	#generates the n first expansions of sqrt(2)
	expansions = []
	
	for c in  range(n-1):
		s = Fraction(2) + Fraction(1/2)
		for i in range(c):
			s = 2 + 1/s
		expansions.append(1 + 1/s)
		print(c)
	return expansions

a = generate_expansion(1000)
print(a)
input()
count = 0
coo = 0
for elt in a:

	coo += 1
	print(coo)
	if digit_exceeds(elt.numerator,elt.denominator):
		count += 1
		
print(count)
input()

#ANSWER IS 153 (I think)