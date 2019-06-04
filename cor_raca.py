with open ('without_asthma.txt', 'rt') as myfile:  # Open file lorem.txt for reading text
    branca = 0
    preta = 0
    amarela = 0 
    parda = 0
    indígena = 0
    ignorado = 0

    for index, myline in enumerate(myfile):                 # For each line, read it to a string 
        if myline[49] == '1':
            branca += 1
        elif myline[49] == '2':
            preta += 1
        elif myline[49] == '3':
            amarela += 1
        elif myline[49] == '4':
            parda += 1
        elif myline[49] == '5':
            indígena += 1
        elif myline[49] == '9':
            ignorado += 1

    print(branca/202926*100)
    print(preta/202926*100)
    print(amarela/202926*100)
    print(parda/202926*100)
    print(indígena/202926*100)
    print(ignorado/202926*100)

    print('--------------------------')

    
with open ('with_asthma.txt', 'rt') as myfile:  # Open file lorem.txt for reading text
    branca = 0
    preta = 0
    amarela = 0 
    parda = 0
    indígena = 0
    ignorado = 0

    for index, myline in enumerate(myfile):                 # For each line, read it to a string 
        if myline[49] == '1':
            branca += 1
        elif myline[49] == '2':
            preta += 1
        elif myline[49] == '3':
            amarela += 1
        elif myline[49] == '4':
            parda += 1
        elif myline[49] == '5':
            indígena += 1
        elif myline[49] == '9':
            ignorado += 1

    print(branca/2620*100)
    print(preta/2620*100)
    print(amarela/2620*100)
    print(parda/2620*100)
    print(indígena/2620*100)
    print(ignorado/2620*100)
    



       


