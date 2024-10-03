# Harga dasar pizza
Harga_pizza = 55000

# Pilih topping
print("Pilih topping Pizza")
print("1. Frankfurter BBQ")
print("2. Meast monsta")
print("3. Super supreme")
print("4. Super supreme chiken")
print("5. Meat lovers")
print("6. Chiken lovers")
print("7. Cheese lovers")
print("8. American fauvorite")

pilihan_topping = int(input("Masukkan pilihan topping : "))

# Cek pilihan topping
if pilihan_topping == 1:
    topping = "Frankfurter BBQ"
    Harga_topping = 15000
elif pilihan_topping == 2:
    topping = "Meast monsta"
    Harga_topping = 11000
elif pilihan_topping == 3:
    topping = "Super supreme"
    Harga_topping = 12000
elif pilihan_topping == 4:
    topping = "Super supreme chiken"
    Harga_topping = 13000
elif pilihan_topping == 5:
    topping = "Meat lovers"
    Harga_topping = 12000
elif pilihan_topping == 6:
    topping = "Chiken lovers"
    Harga_topping = 17000
elif pilihan_topping == 7:
    topping = "Cheese lovers"
    Harga_topping = 16000
elif pilihan_topping == 8:
    topping = "American fauvorite"
    Harga_topping = 14000
else:
    print("Topping tidak valid.")
    topping = None
    Harga_topping = 0

# Pilih jenis crust
print("\nPilih jenis crust:")
print("1. Thin Crust - Rp5000")
print("2. Thick Crust - Rp7000")
crust_pilihan = input("Masukkan nomor crust yang diinginkan (1/2): ")

# Cek pilihan crust
if crust_pilihan == "1":
    crust = "Thin Crust"
    harga_crust = 5000
elif crust_pilihan == "2":
    crust = "Thick Crust"
    harga_crust = 7000
else:
    print("Crust tidak valid.")
    crust = None
    harga_crust = 0

# Pilih ukuran pizza
print("\nPilih ukuran pizza:")
print("1. Kecil - Rp7000")
print("2. Sedang - Rp12000")
print("3. Besar - Rp18000")
ukuran_pilihan = input("Masukkan nomor ukuran yang diinginkan (1/2/3): ")

# Cek pilihan ukuran
if ukuran_pilihan == "1":
    ukuran = "Kecil"
    harga_ukuran = 7000
elif ukuran_pilihan == "2":
    ukuran = "Sedang"
    harga_ukuran = 12000
elif ukuran_pilihan == "3":
    ukuran = "Besar"
    harga_ukuran = 18000
else:
    print("Ukuran tidak valid.")
    ukuran = None
    harga_ukuran = 0

# Tambahan keju
print("\nApakah Anda ingin menambahkan keju ekstra?")
keju_pilihan = input("Tambahkan keju ekstra (ya/tidak): ").lower()

# Cek tambahan keju
if keju_pilihan == "ya":
    harga_keju = 5000
    keju = "Tambahan keju"
else:
    harga_keju = 0
    keju = "Tidak ada tambahan keju"

# Hitung total harga
total_harga = Harga_pizza + Harga_topping + harga_crust + harga_ukuran + harga_keju

# Tampilkan ringkasan pesanan
print(f"\nRingkasan Pesanan Anda:")
print(f"Topping: {topping}")
print(f"Crust: {crust}")
print(f"Ukuran: {ukuran}")
print(f"Keju: {keju}")
print(f"Total harga: Rp{total_harga}")

# Konfirmasi pesanan-
konfirmasi = input("\nKonfirmasi pesanan (ya/tidak)? ").lower()

# Percabangan untuk konfirmasi pesanan
if konfirmasi == "ya":
    print("Pesanan dikonfirmasi. Terima kasih!, Silahkan tunggu di meja")
else:
    print("Pesanan dibatalkan.")
