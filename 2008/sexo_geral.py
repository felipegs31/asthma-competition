with open ('PES2008.TXT', 'rt') as myfile:  # Open file lorem.txt for reading text
    masculino = 0
    feminino = 0
    posicao = (18 - 1)                                            # Contagem começa no zero (valor_tab-1)
    for index, myline in enumerate(myfile):                 # For each line, read it to a string 
        if myline[posicao] == '2':
            masculino += 1
        if myline[posicao] == '4':
            feminino += 1

    print('Masculino 2008')
    print(masculino)
    print('----------')
    print('Feminino')
    print(feminino)


       


