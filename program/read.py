# Mendefinisikan sebuah fungsi untuk membaca data dari sebuah file
def read_file():
    # Membuka file "products.txt" dalam mode baca (read)
    file = open("products.txt", "r")
    # Membaca semua baris dari file dan menyimpannya dalam sebuah daftar
    lines = file.readlines()
    # Membuat sebuah daftar kosong untuk menyimpan data yang telah diuraikan
    L = []

    # Melakukan iterasi melalui setiap baris dalam file
    for line in lines:
        # Menghapus karakter newline dan memisahkan baris dengan tanda koma untuk memisahkan nilainya
        L.append(line.replace("\n", "").split(","))

    # Menutup file
    file.close()

    # Mencetak pesan selamat datang
    print("Halo! Selamat Datang di Toko Tama Dharma!")
    # Mencetak header untuk daftar produk
    print("Produk yang terdapat dalam toko kami adalah sebagai berikut")
    print("--------------------------------------------")
    print("PRODUK\t\tHARGA\t\tJUMLAH")
    print("--------------------------------------------")

    # Melakukan iterasi melalui data yang telah diuraikan dan mencetak informasi setiap produk
    for i in range(len(L)):
        print(L[i][0], "\t\t", L[i][1], "\t\t", L[i][2])

    # Mencetak garis pemisah
    print("--------------------------------------------")

    # Mengembalikan daftar data yang telah diuraikan
    return L