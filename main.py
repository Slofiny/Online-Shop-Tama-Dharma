import read
import purchase
import write

again = "Y"
while again.upper() == "Y":
    a = read.read_file()
    b = purchase.purchase(a)
    write.over_write(a, b)
    again = input("\nApakah Anda ingin melakukan transaksi lagi? ")
print("\nTerima kasih telah berbelanja di toko kami!!")
print("Silakan periksa struk Anda untuk detail belanja Anda, \nKami tidak menerima komplain setelah Anda keluar dari toko kami.")
