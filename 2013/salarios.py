with open ('without_asthma.txt', 'rt') as myfile:  # Open file lorem.txt for reading text
    faixa1 = 0
    faixa2 = 0
    faixa3 = 0 
    faixa4 = 0
    faixa5 = 0
    faixa6 = 0
    faixa7 = 0
    naoConsta = 0


    for index, myline in enumerate(myfile):                 # For each line, read it to a string 
        salario = myline[95:104]
        if(salario[0] == ' '):
            naoConsta += 1
            continue
        salario = int(salario)
        if salario <= 678:
            faixa1 += 1
        elif salario <= 1356:
            faixa2 += 1
        elif salario <= 3390:
            faixa3 += 1
        elif salario <= 6780:
            faixa4 += 1
        elif salario <= 10170:
            faixa5 += 1
        elif salario <= 13560:
            faixa6 += 1
        else:
            faixa7 += 1

    print(faixa1/202926*100)
    print(faixa2/202926*100)
    print(faixa3/202926*100)
    print(faixa4/202926*100)
    print(faixa5/202926*100)
    print(faixa6/202926*100)
    print(faixa7/202926*100)
    print(naoConsta/202926*100)

    print('--------------------------')

    
with open ('with_asthma.txt', 'rt') as myfile:  # Open file lorem.txt for reading text
    faixa1 = 0
    faixa2 = 0
    faixa3 = 0 
    faixa4 = 0
    faixa5 = 0
    faixa6 = 0
    faixa7 = 0
    naoConsta = 0


    for index, myline in enumerate(myfile):                 # For each line, read it to a string 
        salario = myline[95:104]
        if(salario[0] == ' '):
            naoConsta += 1
            continue
        salario = int(salario)
        if salario <= 678:
            faixa1 += 1
        elif salario <= 1356:
            faixa2 += 1
        elif salario <= 3390:
            faixa3 += 1
        elif salario <= 6780:
            faixa4 += 1
        elif salario <= 10170:
            faixa5 += 1
        elif salario <= 13560:
            faixa6 += 1
        else:
            faixa7 += 1

    print(faixa1/2620*100)
    print(faixa2/2620*100)
    print(faixa3/2620*100)
    print(faixa4/2620*100)
    print(faixa5/2620*100)
    print(faixa6/2620*100)
    print(faixa7/2620*100)
    print(naoConsta/2620*100)
    



       


