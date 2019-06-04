with open ('without_asthma.txt', 'rt') as myfile:  # Open file lorem.txt for reading text
    masculino = 0
    feminino = 0
    for index, myline in enumerate(myfile):                 # For each line, read it to a string 
        if myline[37] == '1':
            masculino += 1
        if myline[37] == '2':
            feminino += 1

    print('masculino SEM ASMA')
    print(masculino/202926*100)
    print('feminino SEM ASMA')
    print(feminino/202926*100)

with open ('with_asthma.txt', 'rt') as myfile:  # Open file lorem.txt for reading text
    masculino = 0
    feminino = 0
    for index, myline in enumerate(myfile):                 # For each line, read it to a string 
        if myline[37] == '1':
            masculino += 1
        if myline[37] == '2':
            feminino += 1

    print('masculino COM ASMA')
    print(masculino/2620*100)
    print('feminino COM ASMA')
    print(feminino/2620*100)


       


