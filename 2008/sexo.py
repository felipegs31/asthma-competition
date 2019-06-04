with open ('without_asthma.txt', 'rt') as myfile:  # Open file lorem.txt for reading text
    masculino = 0
    feminino = 0
    posicao = (18 - 1)
    withoutAsthma = 391868

    for index, myline in enumerate(myfile):                 # For each line, read it to a string 
        if myline[posicao] == '2':
            masculino += 1
        if myline[posicao] == '4':
            feminino += 1

    print('masculino SEM ASMA')
    print(masculino/withoutAsthma*100)
    print('feminino SEM ASMA')
    print(feminino/withoutAsthma*100)

with open ('with_asthma.txt', 'rt') as myfile:  # Open file lorem.txt for reading text
    masculino = 0
    feminino = 0
    posicao = (18 - 1)
    withAsthma = 19160
    
    for index, myline in enumerate(myfile):                 # For each line, read it to a string 
        if myline[posicao] == '2':
            masculino += 1
        if myline[posicao] == '4':
            feminino += 1

    print('masculino COM ASMA')
    print(masculino/withAsthma*100)
    print('feminino COM ASMA')
    print(feminino/withAsthma*100)


       


