with open ('first_rows_person.txt', 'rt') as myfile:  # Open file lorem.txt for reading text
    for index, myline in enumerate(myfile):                 # For each line, read it to a string 
        if myline[0] == '1' and myline[1] == '1':
            with open('treated_file.txt', 'a') as out:
                out.write(myline)                     




