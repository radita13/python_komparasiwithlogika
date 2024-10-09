# Program with python komparasi with logika and penggabungan
# Description program :
""" 
    Program ini dirancang untuk menentukan nilai True atau False berdasarkan kondisi dari angka-angka antara 0 hingga 11.
    Aturan yang digunakan dalam logika program ini adalah sebagai berikut:
    jika angka kurang dari atau sama dengan 0, maka hasil yang diberikan adalah False. Kemudian,
    jika angka tersebut lebih dari 0 dan kurang dari atau sama dengan 5, maka program akan mengembalikan nilai True.
    Selanjutnya, untuk angka yang lebih besar dari 5 namun kurang dari atau sama dengan 8, hasil yang dikembalikan adalah False.
    Jika angka lebih besar dari 8 dan kurang dari atau sama dengan 11, maka nilai yang diberikan adalah True.
    Terakhir, apabila angka tersebut lebih besar dari 11, maka program akan memberikan hasil False.
    Dengan menggunakan logika ini, program dapat memeriksa setiap angka dalam rentang yang telah ditentukan dan menentukan
    apakah hasilnya True atau False sesuai dengan kondisi yang berlaku.
"""

print("\n+=========================== Reading Rule Program ===========================+")
print("=> 1.Masukan angka <-----0 Output Flase")
print("=> 2.Masukan angka 0<+++>5 Output True")
print("=> 3.Masukan angka 5<--->8 Output False")
print("=> 4.Masukan angka 8<+++>11 Output True")
print("=> 5.Masukan angka 11----> Output True")
print("=> 6.Pengabungkan angka 0<+++>5 dan 8<+++>11 Output True")
print("=> 7.Pengabungkan angka <-----0, 5<---->8, dan 11-----> Output False")
print("+============================ End of Rule Program ===========================+\n")

inputUser = int(input("Masukkan angka : "))
print("+======================================================+")
print("|======= Hasil Program Komparisasi with Logika ========|")
print("+======================================================+")
isangka0 = inputUser >= 0
print("|Angka kurang dari = 0, maka", isangka0)

isangka1 = inputUser <= 5
print("|Angka lebih besar = 5, maka", isangka1)

isangka2 = inputUser >= 8
print("|Angka lebih kecil = 8, maka", isangka2)

isangka3 = inputUser <= 11
print("|Angka lebih besar = 11, maka", isangka3)
print("========================================================")
print("|  Hasil Program penggabungan Komparisasi with Logika  |")
print("========================================================")
isCorrect = isangka0 and isangka1 or isangka2 and isangka3
print("|Nilai angka digabungan :", isCorrect)
print("========================================================")