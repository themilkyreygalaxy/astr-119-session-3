import numpy as np		#import numpy library

#integers

i = 10				#integer
print(type(i))		#print out the data type of i

a_i = np.zeros(i, dtype=int)	#declare an array of ints
print(type(a_i))				#will return ndarray
print(type(a_i[0]))				#will return int64

#floats

x = 119.0		#floating point number
print(type(x)) 	#print out the data type of x

y = 1.19e2		#float 119 in scientific notation
print(type(y)) 	#print out the data type of y

z = np.zeros(i,dtype=float)	#declare array of floats
print(type(z))				#will return nd array
print(type(z[0])) 			#will return float 64