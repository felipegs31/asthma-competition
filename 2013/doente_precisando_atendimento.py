with open ('without_asthma.txt', 'rt') as myfile:  # Open file lorem.txt for reading text
    cat1 = 0
    cat2 = 0
    cat3 = 0 
    cat4 = 0
    cat5 = 0
    cat6 = 0
    cat7 = 0
    cat8 = 0
    cat9 = 0
    cat10 = 0
    cat11 = 0
    cat12 = 0
    cat13 = 0


    for index, myline in enumerate(myfile):                 # For each line, read it to a string 
        planoSaudePrecoAtendimento = myline[249:251]
        if(planoSaudePrecoAtendimento[0] == " "):
            continue
        planoSaudePrecoAtendimento = int(planoSaudePrecoAtendimento)
        if planoSaudePrecoAtendimento == 1:
            cat1 += 1
        elif planoSaudePrecoAtendimento == 2:
            cat2 += 1
        elif planoSaudePrecoAtendimento == 3:
            cat3 += 1
        elif planoSaudePrecoAtendimento == 4:
            cat4 += 1
        elif planoSaudePrecoAtendimento == 5:
            cat5 += 1
        elif planoSaudePrecoAtendimento == 6:
            cat6 += 1
        elif planoSaudePrecoAtendimento == 7:
            cat7 += 1
        elif planoSaudePrecoAtendimento == 8:
            cat8 += 1
        elif planoSaudePrecoAtendimento == 9:
            cat9 += 1
        elif planoSaudePrecoAtendimento == 10:
            cat10 += 1
        elif planoSaudePrecoAtendimento == 11:
            cat11 += 1
        elif planoSaudePrecoAtendimento == 12:
            cat12 += 1
        elif planoSaudePrecoAtendimento == 13:
            cat13 += 1


    print(cat1/202926*100)
    print(cat2/202926*100)
    print(cat3/202926*100)
    print(cat4/202926*100)
    print(cat5/202926*100)
    print(cat6/202926*100)
    print(cat7/202926*100)
    print(cat8/202926*100)
    print(cat9/202926*100)
    print(cat10/202926*100)
    print(cat11/202926*100)
    print(cat12/202926*100)
    print(cat13/202926*100)


    print('--------------------------')

with open ('with_asthma.txt', 'rt') as myfile:  # Open file lorem.txt for reading text
    cat1 = 0
    cat2 = 0
    cat3 = 0 
    cat4 = 0
    cat5 = 0
    cat6 = 0
    cat7 = 0
    cat8 = 0
    cat9 = 0
    cat10 = 0
    cat11 = 0
    cat12 = 0
    cat13 = 0


    for index, myline in enumerate(myfile):                 # For each line, read it to a string 
        planoSaudePrecoAtendimento = myline[249:251]
        if(planoSaudePrecoAtendimento[0] == " "):
            continue
        planoSaudePrecoAtendimento = int(planoSaudePrecoAtendimento)
        if planoSaudePrecoAtendimento == 1:
            cat1 += 1
        elif planoSaudePrecoAtendimento == 2:
            cat2 += 1
        elif planoSaudePrecoAtendimento == 3:
            cat3 += 1
        elif planoSaudePrecoAtendimento == 4:
            cat4 += 1
        elif planoSaudePrecoAtendimento == 5:
            cat5 += 1
        elif planoSaudePrecoAtendimento == 6:
            cat6 += 1
        elif planoSaudePrecoAtendimento == 7:
            cat7 += 1
        elif planoSaudePrecoAtendimento == 8:
            cat8 += 1
        elif planoSaudePrecoAtendimento == 9:
            cat9 += 1
        elif planoSaudePrecoAtendimento == 10:
            cat10 += 1
        elif planoSaudePrecoAtendimento == 11:
            cat11 += 1
        elif planoSaudePrecoAtendimento == 12:
            cat12 += 1
        elif planoSaudePrecoAtendimento == 13:
            cat13 += 1


    print(cat1/2620*100)
    print(cat2/2620*100)
    print(cat3/2620*100)
    print(cat4/2620*100)
    print(cat5/2620*100)
    print(cat6/2620*100)
    print(cat7/2620*100)
    print(cat8/2620*100)
    print(cat9/2620*100)
    print(cat10/2620*100)
    print(cat11/2620*100)
    print(cat12/2620*100)
    print(cat13/2620*100)

