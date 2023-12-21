def check_flag(param_1):
    local_38 = 0xa3e3a19b93eaa493
    local_30 = 0xe3a4eacf
    uStack_2c = 0xa1e5c3cf
    uStack_28 = 0xcfe3a2a6
    local_24 = 0xb1efcfaa9e97e5a4
    local_9 = 1
    chaine =""
    sVar1 = len(param_1)
    print(0x21)
    if sVar1 == 33:
        print("dans if")
        for i in range(0, 28):
            print("param i+4 : ",param_1[i + 4])
            print("XOR = ",(int(param_1[i + 4]) ^ 227) + 19)
            print("elem to compare",chr((local_38 >> (8 * i)) & 0xFF))
            valueToCompare =((local_38 >> (8 * i)) & 0xFF)
            print("value to compare",valueToCompare)
            valeurRecherche = 227 ^ valueToCompare
            print('valeur recherchée',valeurRecherche)
            print('char recherche', chr(valeurRecherche))
            chaine += chr(valeurRecherche)
            if ((int(param_1[i + 4]) ^ 227) + 19 !=((local_38 >> (8 * i)) & 0xFF)):
                local_9 = 0
    else:
        local_9 = 0

    print(chaine)
    return local_9

check_flag = check_flag('pG pxB@ãããããããããããããããããããããããããã')
print("return méthode = ",check_flag)




