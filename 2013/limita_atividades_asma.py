with open ('with_asthma.txt', 'rt') as myfile:  # Open file lorem.txt for reading text
    cat1 = 0
    cat2 = 0
    cat3 = 0 
    cat4 = 0
    cat5 = 0
    naoAplica = 0
    contador_geral = 0


    for index, myline in enumerate(myfile):                 # For each line, read it to a string 
        contador_geral += 1
        atrapalhaNasAtividades = myline[875]
        if atrapalhaNasAtividades == '1':
            cat1 += 1
        elif atrapalhaNasAtividades == '2':
            cat2 += 1
        elif atrapalhaNasAtividades == '3':
            cat3 += 1
        elif atrapalhaNasAtividades == '4':
            cat4 += 1
        elif atrapalhaNasAtividades == '5':
            cat5 += 1
        elif atrapalhaNasAtividades == ' ':
            naoAplica += 1

    print('contador_geral: ', contador_geral)
    print(cat1/contador_geral*100)
    print(cat2/contador_geral*100)
    print(cat3/contador_geral*100)
    print(cat4/contador_geral*100)
    print(cat5/contador_geral*100)
    print(naoAplica/contador_geral*100)

