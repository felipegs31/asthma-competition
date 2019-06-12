with open ('with_asthma.txt', 'rt') as myfile:  # Open file lorem.txt for reading text
    cat1 = 0
    cat2 = 0
    cat3 = 0 
    naoAplica = 0
    contador_geral = 0

    for index, myline in enumerate(myfile):                 # For each line, read it to a string 
        idade = myline[46:49]
        if idade[0] == " ":
            continue
        idade = int(idade)
        if(idade < 15):
            continue
        contador_geral += 1
        fumante = myline[645]
        if fumante == '1':
            cat1 += 1
        elif fumante == '2':
            cat2 += 1
        elif fumante == '3':
            cat3 += 1
        elif fumante == ' ':
            naoAplica += 1
      

    print('contador_geral: ', contador_geral)
    print(cat1/contador_geral*100)
    print(cat2/contador_geral*100)
    print(cat3/contador_geral*100)
    print(naoAplica/contador_geral*100)


with open ('without_asthma.txt', 'rt') as myfile:  # Open file lorem.txt for reading text
    cat1 = 0
    cat2 = 0
    cat3 = 0 
    naoAplica = 0
    contador_geral = 0

    for index, myline in enumerate(myfile):                 # For each line, read it to a string 
        idade = myline[46:49]
        if idade[0] == " ":
            continue
        idade = int(idade)
        if(idade < 15):
            continue
      
        fumante = myline[645]
        if(fumante == ' '):
            continue
        contador_geral += 1
        if fumante == '1':
            cat1 += 1
        elif fumante == '2':
            cat2 += 1
        elif fumante == '3':
            cat3 += 1
      

    print('contador_geral: ', contador_geral)
    print(cat1/contador_geral*100)
    print(cat2/contador_geral*100)
    print(cat3/contador_geral*100)