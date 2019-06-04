with open ('without_asthma.txt', 'rt') as myfile:  # Open file lorem.txt for reading text
    branca = 0
    preta = 0
    amarela = 0 
    parda = 0
    indígena = 0
    ignorado = 0
    
    posicao = (33 - 1)
    withoutAsthma = 391868

    for index, myline in enumerate(myfile):                 # For each line, read it to a string 
        if myline[posicao] == '2':
            branca += 1
        elif myline[posicao] == '4':
            preta += 1
        elif myline[posicao] == '6':
            amarela += 1
        elif myline[posicao] == '8':
            parda += 1
        elif myline[posicao] == '0':
            indígena += 1
        elif myline[posicao] == '9':
            ignorado += 1

    print(branca/withoutAsthma*100)
    print(preta/withoutAsthma*100)
    print(amarela/withoutAsthma*100)
    print(parda/withoutAsthma*100)
    print(indígena/withoutAsthma*100)
    print(ignorado/withoutAsthma*100)

    print('--------------------------')

    
with open ('with_asthma.txt', 'rt') as myfile:  # Open file lorem.txt for reading text
    branca = 0
    preta = 0
    amarela = 0 
    parda = 0
    indígena = 0
    ignorado = 0
    
    posicao = (33 - 1)
    withAsthma = 19160

    for index, myline in enumerate(myfile):                 # For each line, read it to a string 
        if myline[posicao] == '2':
            branca += 1
        elif myline[posicao] == '4':
            preta += 1
        elif myline[posicao] == '6':
            amarela += 1
        elif myline[posicao] == '8':
            parda += 1
        elif myline[posicao] == '0':
            indígena += 1
        elif myline[posicao] == '9':
            ignorado += 1

    print(branca/withAsthma*100)
    print(preta/withAsthma*100)
    print(amarela/withAsthma*100)
    print(parda/withAsthma*100)
    print(indígena/withAsthma*100)
    print(ignorado/withAsthma*100)
    



       


