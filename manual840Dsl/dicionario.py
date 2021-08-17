import json


manual = ''
with open('manual.txt', 'rb') as m:
    manual = m.read().decode()

full = []
alarmes = []
txt = ''

manualList = manual.split('\n')

# Remove linhas desnecessárias
for linha in manualList:
    if linha not in ['Alarms\r', 'PLC alarms\r', 'NC alarms\r', 'Cycle alarms\r', 'HMI alarms\r',
                     'SINAMICS alarms\r', 'Drive and I/O alarms\r', 'Systems responses\r', 'Appendix A\r',
                     'Diagnostics Manual, 01/2015, 6FC5398-6BP40-5BA2 1407\r', '-\r']:
        if not linha.find('Diagnostics Manual, 01/2015, 6FC5398-6BP40-5BA2 1407') >= 0:
            if not linha.find('Diagnostics Manual, 01/2015, 6FC5398-6BP40-5BA2 713') >= 0:
                if not linha.find('Diagnostics Manual, 01/2015, 6FC5398-6BP40-5BA2') >= 0:
                    if not linha.find('(PLC sign-of-life) output.') >= 0:
                        if linha[:4].isdigit():
                            if txt:
                                full.append(txt)
                                txt = ''

                        txt += linha + '\n'



# Dicionário
for x in full:
    if x[:7].split()[0].isdigit():
        numero = x.split()[0]
        titulo = x.split('\n')[0][x.split('\n')[0].find(' '):]

        if x.find('Reaction:') >= 0:
            if x.find('Remedy:') >= 0:
                reaction = x.split('Reaction:')[1].split('Remedy:')[0]
            if x.find('Acknowledge:') >= 0:
                reaction = x.split('Reaction:')[1].split('Acknowledge:')[0]
        else:
            reaction = ''
        if x.find('continuation:') >= 0:
            Programm = x.split('continuation:')[1]
        else:
            Programm = ''
        if x.find('Parameters:') >= 0:
            parameters = x.split('Parameters:')[1].split('Explanation:')[0]
        else:
            parameters = ''
        if x.find('Explanation:') >= 0:
            if x.find('Reaction:') >= 0:
                Explanation = x.split('Explanation:')[1].split('Reaction:')[0]
            if x.find('Divisor..//'):
                Explanation = x.split('Explanation:')[1].split('Divisor..//')[0]
        else:
            Explanation = ''
        if x.find('Cause:') >= 0:
            if x.find('Remedy:') >= 0:
                cause = x.split('Cause:')[1].split('Remedy:')[0]
            if x.find(':') >= 0:
                cause = x.split('Cause:')[1].split('Remedy')[0]
            else:
                cause = x.split('Cause:')
        else:
            cause = ''
        if x.find('Remedy:') >= 0:
            if x.find('Programm') >= 0:
                Remedy = x.split('Remedy:')[1].split('Programm')[0]
            else:
                Remedy = x.split('Remedy:')[1]
        else:
            Remedy = ''
        if x.find('Message value:') >= 0:
            messagevalue = x.split('Message value:')[1].split('Drive')[0]
        else:
            messagevalue = ''
        if x.find('Drive object:') >= 0:
            driveobject = x.split('Drive object:')[1].split('Reaction:')[0]
        else:
            driveobject = ''
        if x.find('Acknowledge:') >= 0:
            Acknowledge = x.split('Acknowledge:')[1].split('Cause:')[0]
        else:
            Acknowledge = ''

    # print(numero, titulo)

    # Escreve dicionário
    alarmes.append(dict(
        numero=numero,
        titulo=titulo,
        reaction=reaction,
        Remedy=Remedy,
        Programm=Programm,
        parameters=parameters,
        Explanation=Explanation,
        messagevalue=messagevalue,
        driveobject=driveobject,
        Acknowledge=Acknowledge,
        cause=cause
    ))



# Cria arquivo json dos erros
alarmejson = json.dumps(alarmes, sort_keys=True, indent=4, ensure_ascii=True)
with open('alarmes.json', 'w+') as file:
    file.write(alarmejson)

'''
print([x for x in alarmes if x['numero'] == '230886'][0]['cause'])
'''
