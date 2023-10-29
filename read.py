def read_file():
    file = open("products.txt", "r")
    lines = file.readlines()
    L = []
    for line in lines:
        L.append(line.replace("\n", "").split(","))
    file.close()
    print("Halo! Selamat Datang di Toko Tama Dharma!")
    print("Produk yang terdapat dalam toko kami adalah sebagai berikut")
    print("--------------------------------------------")
    print("PRODUK\t\tHARGA\t\tJUMLAH")
    print("--------------------------------------------")
    for i in range(len(L)):
        print(L[i][0], "\t\t", L[i][1], "\t\t", L[i][2])
    print("--------------------------------------------")
    return L
