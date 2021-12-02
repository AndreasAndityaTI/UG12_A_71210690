x=input("Masukkan deret angka : ")
y=x.split(",")
total=0
bilangan=''
for o in y:
    if int(o)%2==0:
        nomer=0+int(o)
    else:
        nomer=0-int(o)
    total=total+nomer
print("Total: ",end='')
for o in y:
    if int(o)%2==0:
        operator=("+ "+str(o)+" ")
    else:
        operator=("- "+str(o)+" ")
    bilangan+=operator
if bilangan[0]=="+":
    print(bilangan[2:len(bilangan)])
else:
    print(bilangan)
print("Hasil perhitungan di atas ialah: ",total)