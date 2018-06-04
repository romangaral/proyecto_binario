
import time

print("Conversor binario a decimal, y decimal a binario.")
time.sleep(1)

print("Menu:")
time.sleep(1)

print("a -- Decimal a binario.")
print("b -- Binario a decimal.")
time.sleep(2)

opcion=input("Elige una opcion --- a o b --- ")

if opcion=="a":

	print("Inroduce un numero decimal: ")
	num_decimal=int(input(" "))
	print("El numero binario es: "  +  bin(num_decimal))

if opcion=="b":

	binario=input("intoduce numero binario: ")

	n=len(binario)
	res=0

	for i in range(1,n+1):
		res=res+ int(binario[i-1])*2**(n-i)

	print("el numero decimal es " +str(res))

