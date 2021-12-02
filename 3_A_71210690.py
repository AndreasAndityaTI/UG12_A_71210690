kata = input("Input: ")
a = 0
b = 0
print("Output:")
while b < len(kata):
	print(kata[0:b])
	b += 1
while a < len(kata):
	print(kata[0:len(kata)-a])
	a += 1