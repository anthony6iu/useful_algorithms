import math
"""
This script is to solve RSA encryption and decryption.
Created by Hongchi Liu on 3/30/18.
Copyright © 2018 hongchi liu. All rights reserved.
"""
# Functions
"""
Calculate n, by using p and q.
Input: p, q(two large enough prime numbers).
Output: product of p*q.
"""
def calc_n(p,q):
	return p*q

"""
Calculate Φ(p*q)
Input: p, q(two large enough prime numbers).
Output: Φ(n)
"""
def calc_phi_n(p,q):
	return (p-1)*(q-1)

"""
BF algorithm.
Input: two large enough prime numbers: p,q and e: GCD(e,Φ(n)) = 1
Output: return d if d is between 1 and n-1 and (d*e) mod Φ(n) = 1
"""
def calc_d(e,p,q):
	n  = calc_n(p,q)
	Pn = calc_phi_n(p,q)
	for d in range(1,n):
		if (e*d-1)%Pn == 0:
			return True,d
	return False,0

"""
BB() faster modular exponentiation.
Input: a,b,n : (a^b) mod n
Ouput: result of (a^b) mod n
"""
def exp(a,b,n):
	i = b
	prod = 1
	x = a%n
	while i > 0 :
		if i%2 == 1 :
			prod = (prod*x)%n
		x = (x*x) % n
		i = math.floor(i/2)
	return prod

"""
run() to solve this question.
Input: two large enough prime numbers: p,q and e: GCD(e,Φ(n)) = 1 and message: M
Output: print details.
"""
def run(p,q,e,M1):
	n = calc_n(p,q)
	phi_n = calc_phi_n(p,q)
	print("p : "+str(p)+" q : "+str(q))
	print("n : "+str(n))
	print("e : "+str(e))
	print("Φ(n) : "+str(phi_n))
	# calc d value.
	d = 0
	flag,d = calc_d(e,p,q)
	if flag == True:
		print("d : "+str(d))
		C = exp(M1,e,n)
		M2 = exp(C,d,n)
		print("M : "+str(M1))
		print("C : "+str(C))
		print("M': "+str(M2))
	else:
		print("d didn't exist.")
		
# Run this script with Q5's parameters
run(29,17,15,28)
