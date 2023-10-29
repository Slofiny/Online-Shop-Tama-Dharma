def over_write(List, Dictionary):
    L = List
    d = Dictionary 
    
    for keys in d.keys():
        if keys == "PHONE":
            L[0][2] = str(int(L[0][2])-d['PHONE'])
        elif keys == "LAPTOP":
            L[1][2] = str(int(L[1][2])-d['LAPTOP'])
        elif keys == "HDD":
            L[2][2] = str(int(L[2][2])-d['HDD'])
        elif keys == "SSD":
            L[3][2] = str(int(L[3][2])-d['SSD'])
        elif keys == "DVD":
            L[4][2] = str(int(L[4][2])-d['DVD'])
        else:
            L[5][2] = str(int(L[5][2])-d['PS5'])
    #print("\nRemaining Stock Products:\n",L)
        
    files = open("products.txt", "w")
    for each in L:
        files.write(str(",".join(each)))
        files.write("\n")         
    files.close()
    return
