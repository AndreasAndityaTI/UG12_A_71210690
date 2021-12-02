tinggi_segitiga = int(input("Input: "))

print("Output: ")
if tinggi_segitiga == 0:
	print(" ")
elif tinggi_segitiga < 0:
	print("maaf input salah ")
elif tinggi_segitiga == 2:
	print(" * ")
	print("* *")
elif tinggi_segitiga == 1:
	print("*")
else:
	print(" "*(tinggi_segitiga-1)+"*"+" "*(tinggi_segitiga-1))
	for x in range (1,tinggi_segitiga):
		print(" "*(tinggi_segitiga-1-x) + "*" + " "*(x*2-1) +"*"+ " "*(tinggi_segitiga-1-x))
		if x == tinggi_segitiga-2:
			break
	for y in range(tinggi_segitiga):
		print("*",end=' ' )