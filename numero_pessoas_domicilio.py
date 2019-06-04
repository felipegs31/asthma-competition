with open ('without_asthma.txt', 'rt') as myfile:  # Open file lorem.txt for reading text
    contador = 0
    for index, myline in enumerate(myfile):                 # For each line, read it to a string 
       myStringNumber = myline[31] + myline[32]
       print(myStringNumber)
       contador += int(myStringNumber)
    print('contador')
    print(contador)





