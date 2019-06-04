with open ('without_asthma.txt', 'rt') as myfile:  # Open file lorem.txt for reading text
    cat1 = 0
    cat2 = 0
    cat3 = 0 
    cat4 = 0
    cat5 = 0
    cat6 = 0
    cat7 = 0
    contador_geral = 0


    for index, myline in enumerate(myfile):                 # For each line, read it to a string 
        if(myline[222] == '2'):
            continue
        contador_geral += 1
        planoSaudePreco = myline[236]
        if planoSaudePreco == '1':
            cat1 += 1
        elif planoSaudePreco == '2':
            cat2 += 1
        elif planoSaudePreco == '3':
            cat3 += 1
        elif planoSaudePreco == '4':
            cat4 += 1
        elif planoSaudePreco == '5':
            cat5 += 1
        elif planoSaudePreco == '6':
            cat6 += 1
        elif planoSaudePreco == '7':
            cat7 += 1

    print('contador_geral: ', contador_geral)
    print(cat1/contador_geral*100)
    print(cat2/contador_geral*100)
    print(cat3/contador_geral*100)
    print(cat4/contador_geral*100)
    print(cat5/contador_geral*100)
    print(cat6/contador_geral*100)
    print(cat7/contador_geral*100)


    print('--------------------------')

with open ('with_asthma.txt', 'rt') as myfile:  # Open file lorem.txt for reading text
    cat1 = 0
    cat2 = 0
    cat3 = 0 
    cat4 = 0
    cat5 = 0
    cat6 = 0
    cat7 = 0
    contador_geral = 0


    for index, myline in enumerate(myfile):                 # For each line, read it to a string 
        if(myline[222] == '2'):
            continue
        contador_geral += 1
        planoSaudePreco = myline[236]
        if planoSaudePreco == '1':
            cat1 += 1
        elif planoSaudePreco == '2':
            cat2 += 1
        elif planoSaudePreco == '3':
            cat3 += 1
        elif planoSaudePreco == '4':
            cat4 += 1
        elif planoSaudePreco == '5':
            cat5 += 1
        elif planoSaudePreco == '6':
            cat6 += 1
        elif planoSaudePreco == '7':
            cat7 += 1

    print('contador_geral: ', contador_geral)
    print(cat1/contador_geral*100)
    print(cat2/contador_geral*100)
    print(cat3/contador_geral*100)
    print(cat4/contador_geral*100)
    print(cat5/contador_geral*100)
    print(cat6/contador_geral*100)
    print(cat7/contador_geral*100)
