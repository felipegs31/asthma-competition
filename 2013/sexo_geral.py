with open ('PESPNS2013.txt', 'rt') as myfile:  # Open file lorem.txt for reading text
    masculino = 0
    feminino = 0
    for index, myline in enumerate(myfile):                 # For each line, read it to a string 
        if myline[37] == '1':
            masculino += 1
        if myline[37] == '2':
            feminino += 1

    print('masculino')
    print(masculino)
    print('feminino')
    print(feminino)


       


