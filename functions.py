import numpy as np
import sys

#define a function that returns a value
def expo(x):
	return np.exp(x)	#returns the np e^x function
	
#define a subroutine that does not return a value
def show_expo(n):
	for i in range(n):
		print (expo(float(i)))	#call the expo function
	
#define amain function
def main():
	n = 10	#provide a default function for n
	
	#check if there is a command line argument provided
	if(len(sys.argv)>1):		#argv variable arguments, nod to C
		n = int(sys.argv[1])	#if an argument was provided, use it for n
		
	show_expo(n)
	
#run the main function
if __name__ == "__main__":
	main()
	
	
# if you do python3 functions.py 6 -- it will loop from 0-5 and end up giving you up until e^6