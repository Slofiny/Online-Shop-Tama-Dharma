def purchase(List):
    L = List 
    a_name = input("Halo, siapa nama Anda? ")
    print("\nHalo " + a_name + "! Selamat datang di Toko Tama Dharma.\nSilakan pilih produk yang Anda inginkan.")
    q = {} 
    flag = "Y"
    while flag.upper() == "Y": 
        product = input("\nProduk apa yang ingin Anda beli? ")
        product_name = product.upper()

        if product_name == L[0][0].upper() or product_name == L[1][0].upper() or product_name == L[2][0].upper() or product_name == L[3][0].upper() or product_name == L[4][0].upper() or product_name == L[5][0].upper():
            p_quantity = int(input(f"Berapa {product} yang ingin Anda beli? "))
            if product_name == L[0][0].upper() and p_quantity <= int(L[0][2]):
                q[product_name] = p_quantity
            elif product_name == L[1][0].upper() and p_quantity <= int(L[1][2]):
                q[product_name] = p_quantity
            elif product_name == L[2][0].upper() and p_quantity <= int(L[2][2]):
                q[product_name] = p_quantity
            elif product_name == L[3][0].upper() and p_quantity <= int(L[3][2]):
                q[product_name] = p_quantity
            elif product_name == L[4][0].upper() and p_quantity <= int(L[4][2]):
                q[product_name] = p_quantity
            elif product_name == L[5][0].upper() and p_quantity <= int(L[5][2]):
                q[product_name] = p_quantity
            else:
                print(
                    f"\nMaaf {a_name}! {product} sedang kurang stocknya. \nKami akan segera menambah stock {product}. ")

            flag = (input("Apakah Anda ingin membeli produk lain?"))
        else:
            print(f"Maaf!! {product} tidak tersedia dalam toko kami. \nMohon pilih dari daftar barang dibawah ini")
            print("--------------------------------------------")
            print("PRODUK\t\tHARGA\t\tJUMLAH")
            print("--------------------------------------------")
            for i in range(len(L)):
                print(L[i][0], "\t\t", L[i][1], "\t\t",
                      L[i][2])
            print("--------------------------------------------")

    print("\nBarang yang Anda pilih beserta Jumlahnya:\n", q, "\n")

    f_amount = 0 
    for keys in q.keys():
        if keys == L[0][0].upper(): 
            p_price = int(L[0][1])
            p_num = int(q[keys])
            p_amount = (p_price * p_num)
            f_amount += (p_price * p_num)
            print("\nTotal harga untuk phone: ", p_amount)
        elif keys == L[1][0].upper(): 
            l_price = int(L[1][1])
            l_num = int(q[keys])
            l_amount = (l_price * l_num)
            f_amount += (l_price * l_num)
            print("Total harga untuk laptop: ", l_amount)
        elif keys == L[2][0].upper(): 
            h_price = int(L[2][1])
            h_num = int(q[keys])
            h_amount = (h_price * h_num)
            f_amount += (h_price * h_num)
            print("\nTotal harga untuk HDD: ", h_amount)
        elif keys == L[3][0].upper(): 
            s_price = int(L[3][1])
            s_num = int(q[keys])
            s_amount = (s_price * s_num)
            f_amount += (s_price * s_num)
            print("\nTotal harga untuk SSD: ", s_amount)
        elif keys == L[4][0].upper(): 
            dv_price = int(L[4][1])
            dv_num = int(q[keys])
            dv_amount = (dv_price * dv_num)
            f_amount += (dv_price * dv_num)
            print("\nTotal harga untuk DVD: ", dv_amount)

        else:
            ps_price = int(L[5][1])
            ps_num = int(q[keys])
            ps_amount = (ps_price * ps_num)
            f_amount += (ps_price * ps_num)
            print("Total harga untuk PS5: ", ps_amount)
    print(f"\nTotal Anda sebelum diskon adalah: {f_amount} ")

    dis = 0.0
    total = f_amount
    if (f_amount >= 5000) and (f_amount < 10000):
        discount = 5.0
        dis = (discount * f_amount) / 100
        total = float(f_amount - dis)
        print(f"Anda mendapatkan diskon {str(discount)}% senilai: {dis} ")
    elif f_amount >= 10000:
        discount = 10
        dis = (discount * f_amount) / 100
        total = float(f_amount - dis)
        print(f"Anda mendapatkan diskon {str(discount)}% senilai: {dis} ")
    print(f"Total Anda adalah: {total} ")

    import datetime 
    dt = str(datetime.datetime.now().year) + "-" + str(datetime.datetime.now().month) + "-" + str(
        datetime.datetime.now().day) + "-" + str(datetime.datetime.now().hour) + "-" + str(
        datetime.datetime.now().minute) + "-" + str(datetime.datetime.now().second)
    invoice = str(dt) 
    t = str(datetime.datetime.now().year) + "-" + str(datetime.datetime.now().month) + "-" + str(
        datetime.datetime.now().day) 
    d = str(t) 
    u = str(datetime.datetime.now().hour) + ":" + str(datetime.datetime.now().minute) + ":" + str(
        datetime.datetime.now().second) 
    e = str(u) 

    file = open(invoice + " (" + a_name + ").txt", "w") 
    file.write("=============================================================")
    file.write("\nTOKO TAMA DHARMA                   INVOICE")
    file.write(f"\n\nInvoice: {invoice}                  Date: {d}")
    file.write(f"\n                                    Time: {e}")
    file.write("\nName Pembeli: " + str(a_name) + "")
    file.write("\n=============================================================")
    file.write("\nPARTICULAR\tQUANTITY\tUNIT PRICE\tTOTAL")
    file.write("\n-------------------------------------------------------------")

    for keys in q.keys(): 
        if keys == "PHONE":
            file.write(
                str("\n" + str(keys) + " \t\t " + str(q['PHONE']) + " \t\t " + str(L[0][1]) + " \t\t " + str(p_amount)))
        elif keys == "LAPTOP":
            file.write(str(
                "\n" + str(keys) + " \t\t " + str(q['LAPTOP']) + " \t\t " + str(L[1][1]) + " \t\t " + str(l_amount)))
        elif keys == "HDD":
            file.write(str(
                "\n" + str(keys) + " \t\t " + str(q['HDD']) + " \t\t " + str(L[2][1]) + " \t\t " + str(h_amount)))
        elif keys == "SSD":
            file.write(str(
                "\n" + str(keys) + " \t\t " + str(q['SSD']) + " \t\t " + str(L[3][1]) + " \t\t " + str(s_amount)))
        elif keys == "DVD":
            file.write(str(
                "\n" + str(keys) + " \t\t " + str(q['DVD']) + " \t\t " + str(L[4][1]) + " \t\t " + str(dv_amount)))
        else:
            file.write(
                str("\n" + str(keys) + " \t\t " + str(q['PS5']) + " \t\t " + str(L[5][1]) + " \t\t " + str(ps_amount)))

    file.write("\n\n-------------------------------------------------------------")
    file.write("\n\t\t\tTotal sebelum diskon: " + str(f_amount))
    file.write("\n-------------------------------------------------------------")
    file.write(f"\n\t\t    Total harga yang didiskon: {str(dis)}")
    file.write("\n-------------------------------------------------------------")
    file.write("\n\t\t\t Total setelah diskon: " + str(total))
    file.write("\n-------------------------------------------------------------")
    file.write("\n\n\tTerima kasih " + a_name + " atas transaksi Anda!.\n\t\tSee you again!")
    file.write("\n=============================================================")
    file.close()
    return q
