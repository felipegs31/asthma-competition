with open ('without_asthma.txt', 'rt') as myfile:  # Open file lorem.txt for reading text
    cat1 = 0
    cat2 = 0
    cat3 = 0 
    cat4 = 0
    cat5 = 0
    cat6 = 0
    cat7 = 0

    for index, myline in enumerate(myfile):                 # For each line, read it to a string 
        faixa = myline[456]
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
        elif faixa == ' ':
            cat7 += 1

    print(cat1/202926*100)
    print(cat2/202926*100)
    print(cat3/202926*100)
    print(cat4/202926*100)
    print(cat5/202926*100)
    print(cat6/202926*100)
    print(cat7/202926*100)


    print('--------------------------')

with open ('with_asthma.txt', 'rt') as myfile:  # Open file lorem.txt for reading text
    cat1 = 0
    cat2 = 0
    cat3 = 0 
    cat4 = 0
    cat5 = 0
    cat6 = 0
    cat7 = 0

    for index, myline in enumerate(myfile):                 # For each line, read it to a string 
        faixa = myline[456]
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
        elif faixa == ' ':
            cat7 += 1

    print(cat1/2620*100)
    print(cat2/2620*100)
    print(cat3/2620*100)
    print(cat4/2620*100)
    print(cat5/2620*100)
    print(cat6/2620*100)
    print(cat7/2620*100)


    print('--------------------------')
