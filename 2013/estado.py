# WITH ASTHMA
with open ('with_asthma.txt', 'rt') as myfile:  # Open file lorem.txt for reading text
    withAsthma = 2620

    rondonia = 0
    acre = 0
    amazonas = 0
    roraima = 0
    para = 0
    amapa = 0
    tocantins = 0
    maranhao = 0
    piaui = 0
    ceara = 0
    rioGrandeNorte = 0
    paraiba = 0
    pernambuco = 0
    alagoas = 0
    sergipe = 0
    bahia = 0
    minasGerais = 0
    espíritoSanto = 0
    rioJaneiro = 0
    saoPaulo = 0
    parana = 0
    santaCatarina = 0
    rioGrandeSul = 0
    matoGrossoSul = 0
    matoGrosso = 0
    goias = 0
    distritoFederal = 0

    for index, myline in enumerate(myfile):                 # For each line, read it to a string 
        if myline[0] == '1' and myline[1] == '1':
            rondonia += 1
        elif myline[0] == '1' and myline[1] == '2':
            acre += 1
        elif myline[0] == '1' and myline[1] == '3':
            amazonas += 1
        elif myline[0] == '1' and myline[1] == '4':
            roraima += 1
        elif myline[0] == '1' and myline[1] == '5':
            para += 1
        elif myline[0] == '1' and myline[1] == '6':
            amapa += 1
        elif myline[0] == '1' and myline[1] == '7':
            tocantins += 1
        elif myline[0] == '2' and myline[1] == '1':
            maranhao += 1
        elif myline[0] == '2' and myline[1] == '2':
            piaui += 1
        elif myline[0] == '2' and myline[1] == '3':
            ceara += 1
        elif myline[0] == '2' and myline[1] == '4':
            rioGrandeNorte += 1
        elif myline[0] == '2' and myline[1] == '5':
            paraiba += 1
        elif myline[0] == '2' and myline[1] == '6':
            pernambuco += 1
        elif myline[0] == '2' and myline[1] == '7':
            alagoas += 1
        elif myline[0] == '2' and myline[1] == '8':
            sergipe += 1
        elif myline[0] == '2' and myline[1] == '9':
            bahia += 1
        elif myline[0] == '3' and myline[1] == '1':
            minasGerais += 1
        elif myline[0] == '3' and myline[1] == '2':
            espíritoSanto += 1
        elif myline[0] == '3' and myline[1] == '3':
            rioJaneiro += 1
        elif myline[0] == '3' and myline[1] == '5':
            saoPaulo += 1
        elif myline[0] == '4' and myline[1] == '1':
            parana += 1
        elif myline[0] == '4' and myline[1] == '2':
            santaCatarina += 1
        elif myline[0] == '4' and myline[1] == '3':
            rioGrandeSul += 1
        elif myline[0] == '5' and myline[1] == '0':
            matoGrossoSul += 1
        elif myline[0] == '5' and myline[1] == '1':
            matoGrosso += 1
        elif myline[0] == '5' and myline[1] == '2':
            goias += 1
        elif myline[0] == '5' and myline[1] == '3':
            distritoFederal += 1


    print(rondonia)
    print(acre)
    print(amazonas)
    print(roraima)
    print(para)
    print(amapa)
    print(tocantins)
    print(maranhao)
    print(piaui)
    print(ceara)
    print(rioGrandeNorte)
    print(paraiba)
    print(pernambuco)
    print(alagoas)
    print(sergipe)
    print(bahia)
    print(minasGerais)
    print(espíritoSanto)
    print(rioJaneiro)
    print(saoPaulo)
    print(parana)
    print(santaCatarina)
    print(rioGrandeSul)
    print(matoGrossoSul)
    print(matoGrosso)
    print(goias)
    print(distritoFederal)
    print('------------------------------')

# WITHOUT ASTHMA
with open ('without_asthma.txt', 'rt') as myfile:  # Open file lorem.txt for reading text
    withoutAsthma = 202926

    rondonia = 0
    acre = 0
    amazonas = 0
    roraima = 0
    para = 0
    amapa = 0
    tocantins = 0
    maranhao = 0
    piaui = 0
    ceara = 0
    rioGrandeNorte = 0
    paraiba = 0
    pernambuco = 0
    alagoas = 0
    sergipe = 0
    bahia = 0
    minasGerais = 0
    espíritoSanto = 0
    rioJaneiro = 0
    saoPaulo = 0
    parana = 0
    santaCatarina = 0
    rioGrandeSul = 0
    matoGrossoSul = 0
    matoGrosso = 0
    goias = 0
    distritoFederal = 0

    for index, myline in enumerate(myfile):                 # For each line, read it to a string 
        if myline[0] == '1' and myline[1] == '1':
            rondonia += 1
        elif myline[0] == '1' and myline[1] == '2':
            acre += 1
        elif myline[0] == '1' and myline[1] == '3':
            amazonas += 1
        elif myline[0] == '1' and myline[1] == '4':
            roraima += 1
        elif myline[0] == '1' and myline[1] == '5':
            para += 1
        elif myline[0] == '1' and myline[1] == '6':
            amapa += 1
        elif myline[0] == '1' and myline[1] == '7':
            tocantins += 1
        elif myline[0] == '2' and myline[1] == '1':
            maranhao += 1
        elif myline[0] == '2' and myline[1] == '2':
            piaui += 1
        elif myline[0] == '2' and myline[1] == '3':
            ceara += 1
        elif myline[0] == '2' and myline[1] == '4':
            rioGrandeNorte += 1
        elif myline[0] == '2' and myline[1] == '5':
            paraiba += 1
        elif myline[0] == '2' and myline[1] == '6':
            pernambuco += 1
        elif myline[0] == '2' and myline[1] == '7':
            alagoas += 1
        elif myline[0] == '2' and myline[1] == '8':
            sergipe += 1
        elif myline[0] == '2' and myline[1] == '9':
            bahia += 1
        elif myline[0] == '3' and myline[1] == '1':
            minasGerais += 1
        elif myline[0] == '3' and myline[1] == '2':
            espíritoSanto += 1
        elif myline[0] == '3' and myline[1] == '3':
            rioJaneiro += 1
        elif myline[0] == '3' and myline[1] == '5':
            saoPaulo += 1
        elif myline[0] == '4' and myline[1] == '1':
            parana += 1
        elif myline[0] == '4' and myline[1] == '2':
            santaCatarina += 1
        elif myline[0] == '4' and myline[1] == '3':
            rioGrandeSul += 1
        elif myline[0] == '5' and myline[1] == '0':
            matoGrossoSul += 1
        elif myline[0] == '5' and myline[1] == '1':
            matoGrosso += 1
        elif myline[0] == '5' and myline[1] == '2':
            goias += 1
        elif myline[0] == '5' and myline[1] == '3':
            distritoFederal += 1


    print(rondonia)
    print(acre)
    print(amazonas)
    print(roraima)
    print(para)
    print(amapa)
    print(tocantins)
    print(maranhao)
    print(piaui)
    print(ceara)
    print(rioGrandeNorte)
    print(paraiba)
    print(pernambuco)
    print(alagoas)
    print(sergipe)
    print(bahia)
    print(minasGerais)
    print(espíritoSanto)
    print(rioJaneiro)
    print(saoPaulo)
    print(parana)
    print(santaCatarina)
    print(rioGrandeSul)
    print(matoGrossoSul)
    print(matoGrosso)
    print(goias)
    print(distritoFederal)



def checkStates(data):
    rondonia = 0
    acre = 0
    amazonas = 0
    roraima = 0
    para = 0
    amapa = 0
    tocantins = 0
    maranhao = 0
    piaui = 0
    ceara = 0
    rioGrandeNorte = 0
    paraiba = 0
    pernambuco = 0
    alagoas = 0
    sergipe = 0
    bahia = 0
    minasGerais = 0
    espíritoSanto = 0
    rioJaneiro = 0
    saoPaulo = 0
    parana = 0
    santaCatarina = 0
    rioGrandeSul = 0
    matoGrossoSul = 0
    matoGrosso = 0
    goias = 0
    distritoFederal = 0

    if data[0] == 1 and data[1] == 1:
        rondonia += 1
    elif data[0] == 1 and data[1] == 2:
        acre += 1
    elif data[0] == 1 and data[1] == 3:
        amazonas += 1
    elif data[0] == 1 and data[1] == 4:
        roraima += 1
    elif data[0] == 1 and data[1] == 5:
        para += 1
    elif data[0] == 1 and data[1] == 6:
        amapa += 1
    elif data[0] == 1 and data[1] == 7:
        tocantins += 1
    elif data[0] == 2 and data[1] == 1:
        maranhao += 1
    elif data[0] == 2 and data[1] == 2:
        piaui += 1
    elif data[0] == 2 and data[1] == 3:
        ceara += 1
    elif data[0] == 2 and data[1] == 4:
        rioGrandeNorte += 1
    elif data[0] == 2 and data[1] == 5:
        paraiba += 1
    elif data[0] == 2 and data[1] == 6:
        pernambuco += 1
    elif data[0] == 2 and data[1] == 7:
        alagoas += 1
    elif data[0] == 2 and data[1] == 8:
        sergipe += 1
    elif data[0] == 2 and data[1] == 9:
        bahia += 1
    elif data[0] == 3 and data[1] == 1:
        minasGerais += 1
    elif data[0] == 3 and data[1] == 2:
        espíritoSanto += 1
    elif data[0] == 3 and data[1] == 3:
        rioJaneiro += 1
    elif data[0] == 3 and data[1] == 5:
        saoPaulo += 1
    elif data[0] == 4 and data[1] == 1:
        parana += 1
    elif data[0] == 4 and data[1] == 2:
        santaCatarina += 1
    elif data[0] == 4 and data[1] == 3:
        rioGrandeSul += 1
    elif data[0] == 3 and data[1] == 1:
        matoGrossoSul += 1
    elif data[0] == 3 and data[1] == 2:
        matoGrosso += 1
    elif data[0] == 3 and data[1] == 3:
        goias += 1
    elif data[0] == 3 and data[1] == 5:
        distritoFederal += 1

    d = dict();  

    d['rondonia'] = rondonia
    d['acre'] = acre
    d['amazonas'] = amazonas
    d['roraima'] = roraima
    d['para'] = para
    d['amapa'] = amapa
    d['tocantins'] = tocantins
    d['maranhao'] = maranhao
    d['piaui'] = piaui
    d['ceara'] = ceara
    d['rioGrandeNorte'] = rioGrandeNorte
    d['paraiba'] = paraiba
    d['pernambuco'] = pernambuco
    d['alagoas'] = alagoas
    d['sergipe'] = sergipe
    d['bahia'] = bahia
    d['minasGerais'] = minasGerais
    d['espíritoSanto'] = espíritoSanto
    d['rioJaneiro'] = rioJaneiro
    d['saoPaulo'] = saoPaulo
    d['parana'] = parana
    d['santaCatarina'] = santaCatarina
    d['rioGrandeSul'] = rioGrandeSul
    d['matoGrossoSul'] = matoGrossoSul
    d['matoGrosso'] = matoGrosso
    d['goias'] = goias
    d['distritoFederal'] = distritoFederal

    return d

      