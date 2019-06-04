with open ('without_asthma.txt', 'rt') as myfile:  # Open file lorem.txt for reading text
    sim = 0
    nao = 0
    contador = 0
    
    for index, myline in enumerate(myfile):                 # For each line, read it to a string 
        if myline[457] == '1':
            sim += 1
            contador += 1
        if myline[457] == '2':
            nao += 1
            contador += 1

    print('SEM ASMA')
    print(sim/contador*100)
    print(nao/contador*100)

with open ('with_asthma.txt', 'rt') as myfile:  # Open file lorem.txt for reading text
    sim = 0
    nao = 0
    contador = 0

    for index, myline in enumerate(myfile):                 # For each line, read it to a string 
        if myline[457] == '1':
            sim += 1
            contador += 1
        if myline[457] == '2':
            nao += 1
            contador += 1

    print('COM ASMA')
    print(sim/contador*100)
    print(nao/contador*100)



       


