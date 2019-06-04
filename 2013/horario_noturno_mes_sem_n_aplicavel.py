with open ('without_asthma.txt', 'rt') as myfile:  # Open file lorem.txt for reading text
    cat1 = 0
    cat2 = 0
    cat3 = 0 
    cat4 = 0
    cat5 = 0
    cat6 = 0
    contador = 0

    for index, myline in enumerate(myfile):                 # For each line, read it to a string 
        faixa = myline[456]
        if faixa == ' ':
            continue 
        contador += 1
        if faixa == '1':
            cat1 += 1
        elif faixa == '2':
            cat2 += 1
        elif faixa == '3':
            cat3 += 1
        elif faixa == '4':
            cat4 += 1
        elif faixa == '5':
            cat5 += 1
        elif faixa == '6':
            cat6 += 1

    print(contador)
    print(cat1)
    print(cat2)
    print(cat3)
    print(cat4)
    print(cat5)
    print(cat6)

    print(cat1/contador*100)
    print(cat2/contador*100)
    print(cat3/contador*100)
    print(cat4/contador*100)
    print(cat5/contador*100)
    print(cat6/contador*100)

    print('--------------------------')

with open ('with_asthma.txt', 'rt') as myfile:  # Open file lorem.txt for reading text
    cat1 = 0
    cat2 = 0
    cat3 = 0 
    cat4 = 0
    cat5 = 0
    cat6 = 0
    contador = 0    

    for index, myline in enumerate(myfile):                 # For each line, read it to a string 
        faixa = myline[456]
        if faixa == ' ':
            continue 
        contador += 1        
        if faixa == '1':
            cat1 += 1
        elif faixa == '2':
            cat2 += 1
        elif faixa == '3':
            cat3 += 1
        elif faixa == '4':
            cat4 += 1
        elif faixa == '5':
            cat5 += 1
        elif faixa == '6':
            cat6 += 1

    print(contador)
    print(cat1)
    print(cat2)
    print(cat3)
    print(cat4)
    print(cat5)
    print(cat6)
    print(cat1/contador*100)
    print(cat2/contador*100)
    print(cat3/contador*100)
    print(cat4/contador*100)
    print(cat5/contador*100)
    print(cat6/contador*100)

