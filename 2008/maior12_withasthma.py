with open ('with_asthma.txt', 'rt') as myfile:  # Open file lorem.txt for reading text
    maiores15 = 0
    posicao = (27 - 1)                                      # Contagem começa no zero (valor_tab-1)
    for index, myline in enumerate(myfile):                 # For each line, read it to a string 
        idade = (myline[posicao:posicao+3])
        if idade[0] == " ":
            continue
        idade = int(idade)
        if  idade > 15:
            maiores15 += 1


    print('Maiores de 15 anos c/ asma')
    print(maiores15)
    