with open ('without_asthma.txt', 'rt') as myfile:  # Open file lorem.txt for reading text
    sim = 0
    nao = 0
    for index, myline in enumerate(myfile):                 # For each line, read it to a string 
        if myline[222] == '1':
            sim += 1
        if myline[222] == '2':
            nao += 1

    print('SEM ASMA')
    print(sim/202926*100)
    print(nao/202926*100)

with open ('with_asthma.txt', 'rt') as myfile:  # Open file lorem.txt for reading text
    sim = 0
    nao = 0
    for index, myline in enumerate(myfile):                 # For each line, read it to a string 
        if myline[222] == '1':
            sim += 1
        if myline[222] == '2':
            nao += 1

    print('COM ASMA')
    print(sim/2620*100)
    print(nao/2620*100)


       


