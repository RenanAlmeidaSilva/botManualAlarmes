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
    if linha not in ['Alarmes\r', 'NCK-Alarme\r', 'Alarmes de ciclos\r', 'HMI-Alarmes\r', 'SINAMICS-Alarmes\r',
                     'Alarmes de acionamento e periféricos\r', 'PLC-Alarmes\r', ]:
        if not linha.startswith('Manual de diagnóstico, 03/2013, 6FC5398-8BP40-3KA1') and not linha.startswith('1000 * first identical encoder') and not linha.startswith('0000yyxx'):
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
        if x.find('Definições:') >= 0:
            definicoes = x.split('Definições:')[1].split('Reação:')[0]
        else:
            definicoes = ''
        if x.find('Reação:') >= 0:
            if x.find('Correção') >= 0:
                reacoes = x.split('Reação:')[1].split('Correção:')[0]
            if x.find('Reconhecimento:') >= 0:
                reacoes = x.split('Reação:')[1].split('Reconhecimento:')[0]
        else:
            reacoes = ''
        if x.find('Correção:') >= 0:
            if x.find('Continuação do') >= 0:
                correcoes = x.split('Correção:')[1].split('Continuação do')[0]
            else:
                correcoes = x.split('Correção:')[1]
        else:
            correcoes = ''
        if x.find('programa:') >= 0:
            if x.find('Recomece') >= 0:
                programa = x.split('Continuação do')[1].split("programa.")[0]
            else:
                programa = x.split('programa:')[1]
        else:
            programa = ''
        if x.find('Parâmetros:') >= 0:
            parametro = x.split('Parâmetros:')[1].split('Definições:')[0]
        else:
            parametro = ''
        if x.find('Valor de mensagem:') >= 0:
            valormsg = x.split('Valor de mensagem:')[1].split('Objeto drive:')[0]
        else:
            valormsg = ''
        if x.find('Objeto drive:') >= 0:
            objeto = x.split('Objeto drive:')[1].split('Reação')[0]
        else:
            objeto = ''
        if x.find('Reconhecimento:') >= 0:
            reconhecimento = x.split('Reconhecimento:')[1].split('Causa:')[0]
        else:
            reconhecimento = ''
        if x.find('Causa:') >= 0:
            causa = x.split('Causa:')[1].split('Correção:')[0]
        else:
            causa = ''

    # print(numero, titulo)

    # Escreve dicionário
    alarmes.append(dict(
        numero=numero,
        titulo=titulo,
        definicoes=definicoes,
        reacoes=reacoes,
        correcoes=correcoes,
        programa=programa,
        parametro=parametro,
        valormsg=valormsg,
        objeto=objeto,
        reconhecimento=reconhecimento,
        causa=causa
    ))

'''
txt = ''
for alarme in alarmes:
    if alarme['numero'] == message.text:
        if alarme['titulo']:
            txt += f'TÍTULO: {alarme["titulo"]}\n'
        if alarme['definicoes']:
            txt += f'\nDEFINIÇÕES:\n{alarme["definicoes"]}\n'
        if alarme['reacoes']:
            txt += f'\nREAÇÕES:\n{alarme["reacoes"]}\n'
        if alarme['correcoes']:
            txt += f'CORREÇÕES:\n{alarme["correcoes"]}\n'
        if alarme['programa']:
            txt += f'CONTINUAÇÃO DO PROGRAMA:{alarme["programa"]}\n'
        if alarme['parametro']:
            txt += f'PARÂMETRO:\n{alarme["parametro"]}\n'
        if alarme['valormsg']:
            txt += f'VALOR DE MENSAGEM:\n{alarme["valormsg"]}\n'
        if alarme['objeto']:
            txt += f'OBJETO:\n{alarme["objeto"]}\n'
        if alarme['reconhecimento']:
            txt += f'RECONHECIMENTO:\n{alarme["reconhecimento"]}\n'
        if alarme['causa']:
            txt += f'CAUSA:\n{alarme["causa"]}\n'

if txt != '':
    await message.answer(txt)
else:
    erro = "Você deve fornecer um valor válido."
    await message.answer(erro)
'''


# cria arquivo json dos erros
alarmejson = json.dumps(alarmes, sort_keys=True, indent=4, ensure_ascii=True)
with open('alarmes.json', 'w+') as file:
    file.write(alarmejson)
