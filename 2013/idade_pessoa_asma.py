with open ('without_asthma.txt', 'rt') as myfile:  # Open file lorem.txt for reading text
    cat1 = 0
    cat2 = 0
    cat3 = 0 
    cat4 = 0
    cat5 = 0
    cat6 = 0
    cat7 = 0
    cat8 = 0
    cat9 = 0
    cat10 = 0
    cat11 = 0

    contador_geral = 0

    for index, myline in enumerate(myfile):                 # For each line, read it to a string 
        idade = myline[46:49]
        if idade[0] == " ":
            continue
        idade = int(idade)
        contador_geral += 1
        if idade <= 2:
            cat1 += 1
        elif idade <= 5:
            cat2 += 1
        elif idade <= 10:
            cat3 += 1
        elif idade <= 15:
            cat4 += 1
        elif idade <= 20:
            cat5 += 1
        elif idade <= 30:
            cat6 += 1
        elif idade <= 40:
            cat7 += 1
        elif idade <= 50:
            cat8 += 1
        elif idade <= 60:
            cat9 += 1
        elif idade <= 70:
            cat10 += 1
        else:
            cat11 += 1

    print('contador_geral: ', contador_geral)
    print(cat1/contador_geral*100)
    print(cat2/contador_geral*100)
    print(cat3/contador_geral*100)
    print(cat4/contador_geral*100)
    print(cat5/contador_geral*100)
    print(cat6/contador_geral*100)
    print(cat7/contador_geral*100)
    print(cat8/contador_geral*100)
    print(cat9/contador_geral*100)
    print(cat10/contador_geral*100)

with open ('with_asthma.txt', 'rt') as myfile:  # Open file lorem.txt for reading text
    cat1 = 0
    cat2 = 0
    cat3 = 0 
    cat4 = 0
    cat5 = 0
    cat6 = 0
    cat7 = 0
    cat8 = 0
    cat9 = 0
    cat10 = 0
    cat11 = 0

    contador_geral = 0

    for index, myline in enumerate(myfile):                 # For each line, read it to a string 
        idade = myline[46:49]
        if idade[0] == " ":
            continue
        idade = int(idade)
        contador_geral += 1
        if idade <= 2:
            cat1 += 1
        elif idade <= 5:
            cat2 += 1
        elif idade <= 10:
            cat3 += 1
        elif idade <= 15:
            cat4 += 1
        elif idade <= 20:
            cat5 += 1
        elif idade <= 30:
            cat6 += 1
        elif idade <= 40:
            cat7 += 1
        elif idade <= 50:
            cat8 += 1
        elif idade <= 60:
            cat9 += 1
        elif idade <= 70:
            cat10 += 1
        else:
            cat11 += 1

    print('contador_geral: ', contador_geral)
    print(cat1/contador_geral*100)
    print(cat2/contador_geral*100)
    print(cat3/contador_geral*100)
    print(cat4/contador_geral*100)
    print(cat5/contador_geral*100)
    print(cat6/contador_geral*100)
    print(cat7/contador_geral*100)
    print(cat8/contador_geral*100)
    print(cat9/contador_geral*100)
    print(cat10/contador_geral*100)

