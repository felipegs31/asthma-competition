with open ('without_asthma.txt', 'rt') as myfile:  # Open file lorem.txt for reading text
    muitoBom = 0
    bom = 0
    regular = 0 
    ruim = 0
    muitoRuim = 0
    nuncaUsou = 0
    naoConsta = 0
    contador_geral = 0


    for index, myline in enumerate(myfile):                 # For each line, read it to a string 
        if(myline[222] == '2'):
            continue
        contador_geral += 1
        planoSaude = myline[228]
        if planoSaude == '1':
            muitoBom += 1
        elif planoSaude == '2':
            bom += 1
        elif planoSaude == '3':
            regular += 1
        elif planoSaude == '4':
            ruim += 1
        elif planoSaude == '5':
            muitoRuim += 1
        elif planoSaude == '6':
            nuncaUsou += 1

    print('contador_geral: ', contador_geral)
    print(muitoBom/contador_geral*100)
    print(bom/contador_geral*100)
    print(regular/contador_geral*100)
    print(ruim/contador_geral*100)
    print(muitoRuim/contador_geral*100)
    print(nuncaUsou/contador_geral*100)

    print('--------------------------')

with open ('with_asthma.txt', 'rt') as myfile:  # Open file lorem.txt for reading text
    muitoBom = 0
    bom = 0
    regular = 0 
    ruim = 0
    muitoRuim = 0
    nuncaUsou = 0
    naoConsta = 0
    contador_geral = 0


    for index, myline in enumerate(myfile):                 # For each line, read it to a string 
        if(myline[222] == '2'):
            continue
        contador_geral += 1
        planoSaude = myline[228]
        if planoSaude == '1':
            muitoBom += 1
        elif planoSaude == '2':
            bom += 1
        elif planoSaude == '3':
            regular += 1
        elif planoSaude == '4':
            ruim += 1
        elif planoSaude == '5':
            muitoRuim += 1
        elif planoSaude == '6':
            nuncaUsou += 1

    print('contador_geral: ', contador_geral)
    print(muitoBom/contador_geral*100)
    print(bom/contador_geral*100)
    print(regular/contador_geral*100)
    print(ruim/contador_geral*100)
    print(muitoRuim/contador_geral*100)
    print(nuncaUsou/contador_geral*100)