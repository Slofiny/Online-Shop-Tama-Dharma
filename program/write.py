# Mendefinisikan fungsi "over_write" yang menerima dua argumen: "List" dan "Dictionary"
def over_write(List, Dictionary):
    # Menyalin daftar "List" ke variabel "L"
    L = List
    # Menyalin kamus "Dictionary" ke variabel "d"
    d = Dictionary

    # Melakukan iterasi melalui kunci-kunci dalam kamus "d" (produk yang dibeli)
    for keys in d.keys():
        # Memeriksa produk yang dibeli, mengurangkan jumlah stok yang tersedia sesuai dengan jumlah pembelian
        if keys == "PHONE":
            L[0][2] = str(int(L[0][2]) - d['PHONE'])
        elif keys == "LAPTOP":
            L[1][2] = str(int(L[1][2]) - d['LAPTOP'])
        elif keys == "HDD":
            L[2][2] = str(int(L[2][2]) - d['HDD'])
        elif keys == "SSD":
            L[3][2] = str(int(L[3][2]) - d['SSD'])
        elif keys == "DVD":
            L[4][2] = str(int(L[4][2]) - d['DVD'])
        else:
            L[5][2] = str(int(L[5][2]) - d['PS5'])

    # Membuka file "products.txt" dalam mode penulisan (write)
    files = open("products.txt", "w")

    # Menulis data produk yang telah diperbarui ke dalam file "products.txt"
    for each in L:
        files.write(str(",".join(each)))
        files.write("\n")

    # Menutup file
    files.close()
