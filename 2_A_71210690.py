peserta = []
kursi_urut = []
while True:
	nama_peserta = (input("Masukkan peserta: "))
	if nama_peserta == "STOP":
		break
	else:
		kursi = (input("Masukkan nomor kursi "+nama_peserta+": "))
	
	if kursi in kursi_urut:
		print("Mohon maaf, kursi tersebut telah terisi")
	else:
		peserta.append(nama_peserta)
		kursi_urut.append(kursi)
		
print("\nLihat kursi yang telah terisi: ")

for i in range(len(kursi_urut)):
	print("Nomor",kursi_urut[i],"telah diisi oleh", peserta[i])