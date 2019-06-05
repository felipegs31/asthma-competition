with open ('with_asthma.txt', 'rt') as myfile:  # Open file lorem.txt for reading text
    diariamente = 0
    menosdia = 0
    naofuma = 0
    naosabe = 0
    naoaplica = 0
    posicao = (1358 - 1)                                      # Contagem começa no zero (valor_tab-1)
    
    for index, myline in enumerate(myfile):                 # For each line, read it to a string 
        if myline[posicao] == '1':
            diariamente += 1
        if myline[posicao] == '3':
            menosdia += 1
        if myline[posicao] == '5':
            naofuma += 1
        if myline[posicao] == '7':
            naosabe += 1
        if myline[posicao] == ' ':
            naoaplica += 1

    print('Fuma diariamente ', diariamente/(index+1))
    print('Fuma menos de 1x/dia ', menosdia/(index+1))
    print('Não fuma ', naofuma/(index+1))
    print('Não sabe ', naosabe/(index+1))
    print('Não aplica ', naoaplica/(index+1))

    
   