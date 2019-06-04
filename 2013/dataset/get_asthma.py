with open ('PESPNS2013.txt', 'rt') as myfile:  # Open file lorem.txt for reading text
    for index, myline in enumerate(myfile):                 # For each line, read it to a string 
        if myline[869] == '2' or myline[869] == ' ':
            with open('without_asthma.txt', 'a') as out:
                out.write(myline)                     
