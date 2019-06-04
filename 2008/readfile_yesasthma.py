with open ('PES2008.TXT', 'rt') as myfile:  # Open file lorem.txt for reading text
    posicao = (1225 - 1)
    open('with_asthma.txt', 'w+')
    open('without_asthma.txt', 'w+')
    for index, myline in enumerate(myfile):                 # For each line, read it to a string 
        if myline[posicao] == '1':
            with open('with_asthma.txt', 'a') as out:
                out.write(myline)
        if myline[posicao] == '3':
            with open('without_asthma.txt', 'a') as out:
                out.write(myline)                     
