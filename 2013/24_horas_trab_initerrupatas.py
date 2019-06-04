with open ('without_asthma.txt', 'rt') as myfile:  # Open file lorem.txt for reading text
    sim = 0
    nao = 0
    nAplicavel = 0
    for index, myline in enumerate(myfile):                 # For each line, read it to a string 
        if myline[457] == '1':
            sim += 1
        if myline[457] == '2':
            nao += 1
        if myline[457] == ' ':
            nAplicavel += 1

    print('SEM ASMA')
    print(sim/202926*100)
    print(nao/202926*100)
    print(nAplicavel/202926*100)

with open ('with_asthma.txt', 'rt') as myfile:  # Open file lorem.txt for reading text
    sim = 0
    nao = 0
    nAplicavel = 0

    for index, myline in enumerate(myfile):                 # For each line, read it to a string 
        if myline[457] == '1':
            sim += 1
        if myline[457] == '2':
            nao += 1
        if myline[457] == ' ':
            nAplicavel += 1

    print('COM ASMA')
    print(sim/2620*100)
    print(nao/2620*100)
    print(nAplicavel/2620*100)



       


