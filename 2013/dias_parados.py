with open ('with_asthma.txt', 'rt') as myfile:  # Open file lorem.txt for reading text
    sim = 0
    soma_dias = 0
    pessoas_com_dado_dias = 0
    for index, myline in enumerate(myfile):                 # For each line, read it to a string 
        if myline[241] == '1' and myline[242] == '1':
            sim += 1
            dias = myline[239:241]
            if(dias[1] == ' '):
                continue
            dias = int(dias)
            if(dias == 0):
                continue
            pessoas_com_dado_dias += 1
            soma_dias += dias


    print('COM ASMA')
    print(sim/2620*100)
    print('pessoas_com_dado_dias', pessoas_com_dado_dias)
    print('soma_dias', soma_dias)
    print(soma_dias / pessoas_com_dado_dias)




       


