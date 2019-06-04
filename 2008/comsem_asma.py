with open ('PES2008.TXT', 'rt') as myfile:  # Open file lorem.txt for reading text
    yes_asthma = 0
    not_asthma = 0
    posicao = (1225 - 1)                                    # Contagem começa no zero (valor_tab-1)
    for index, myline in enumerate(myfile):                 # For each line, read it to a string 
        if myline[posicao] == '1':
            yes_asthma += 1
        if myline[posicao] == '3':
            not_asthma += 1

    print('Com Asma')
    print(yes_asthma)
    print('---------')
    print('Sem Asma')
    print(not_asthma)
    print('---------')
    print('SOMA')
    print(not_asthma+yes_asthma)
    print('---------')
    print('INDEX')
    print(index+1)


       


