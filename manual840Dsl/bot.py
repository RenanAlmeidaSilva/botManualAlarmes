import logging
import json
from aiogram import Bot, Dispatcher, executor, types



API_TOKEN = 'API TOKEN'     # Chave bot Telegram

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
with open('alarmes.json', 'r') as f:
    alarmes = json.load(f)



@dp.message_handler(commands=['info'])
async def send_welcome(message: types.Message):
    await message.reply("Hi! I'm Alarmes828DBot!\nPowered by: \nDev. Laura Sorato. (Estagiário Developer) \nDev. Renan Almeida. (Estagiário Developer)\n")



@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    with open('user.txt') as file:
        userList = file.read()
    user = userList.split('\n')

    # Confere se usuário tem permissão para acessar o bot
    textomsg1 = ''
    if message['chat']['username']:
        textomsg1 += message["chat"]["username"]
        with open('logs.log', 'a') as arquivo:
            arquivo.write('\n' + message["chat"]["username"] + '\n\n')

        if textomsg1 in user:
            await message.answer('Olá ' + message['chat'][
                'first_name'] + ', eu sou o Bot para o alarme 840Dsl, criado para encontrar as informações do seu erro.\n'
                                'Você deve me fornecer um valor para pesquisa.')

        else:
            await message.answer("Olá, eu sou o Bot para o alarme 840Dsl, criado para encontrar as informações do seu erro.\n"
                                 "No momento você não possui permissão para acessar as informações internas.\n"
                                 "Entre em contato com os desenvolvedores.\n"
                                 "Para mais informações dos meu criadores digite '/info'")

    else:
        await message.answer('Olá ' + message['chat'][
            'first_name'] + ', no momento não encontrei seu username. Você deve verifica-lo nas configurações do Telegram.')



@dp.message_handler()
async def echo(message: types.Message):
    segundos = message['date']
    with open('logs.log', 'a') as arquivo:
        arquivo.write(segundos.__str__())

    with open('user.txt') as file:
        userList = file.read()
    #print(userList)
    user = userList.split('\n')
    #print(user)

    textomsg = ''
    if message["chat"]["username"]:
        textomsg += message["chat"]["username"]

        # Cria log
        with open('logs.log', 'a') as arquivo:
            arquivo.write('\n'+message["chat"]["username"]+'\n\n')

    else:
        await message.answer("Você não possui um Username. Logo, deverá ir em suas configurações e nomea-lo.")

    if message.text == '27001':
        await message.answer('Mensagem muito longa, por favor verifique o manual:\n'
                             'https://www.autservice.com.br/admin/assets/repositorio/292d4f09b8fe329bf5c7bbb922b6d3bc.pdf#page=481')

    if message.text == '27033':
        await message.answer('Mensagem muito longa, por favor verifique o manual:\n'
                             'https://www.autservice.com.br/admin/assets/repositorio/292d4f09b8fe329bf5c7bbb922b6d3bc.pdf#page=496')

    elif textomsg in user:
        entradas = ['oi', 'olá', 'ola', 'oie', 'roi']
        alarmes
        txt = ''

        # Pesquisa no dicionário
        for alarme in alarmes:
            if alarme['numero'] == message.text:
                if alarme['titulo']:
                    txt += f'TÍTULO: {alarme["titulo"]}\n'
                if alarme['Explanation']:
                    txt += f'\nEXPLANATION:\n{alarme["Explanation"]}\n'
                if alarme['reaction']:
                    txt += f'\nREACTION:\n{alarme["reaction"]}\n'
                if alarme['Programm']:
                    txt += f'PROGRAMM CONTINUATION:{alarme["Programm"]}\n'
                if alarme['parameters']:
                    txt += f'PARAMETERS:\n{alarme["parameters"]}\n'
                if alarme['Remedy']:
                    txt += f'REMEDY:\n{alarme["Remedy"]}\n'
                if alarme['messagevalue']:
                    txt += f'MESSAGE VALUE:\n{alarme["messagevalue"]}\n'
                if alarme['cause']:
                    txt += f'CAUSE:\n{alarme["cause"]}\n'
                if alarme['driveobject']:
                    txt += f'DRIVE OBJECT:\n{alarme["driveobject"]}\n'
                if alarme['Acknowledge']:
                    txt += f'ACKNOWLEDGE:\n{alarme["Acknowledge"]}\n'

        if txt != '':
            await message.answer(txt)

        elif message.text.lower() in (entradas):
            await message.answer('Olá ' + message['chat'][
                'first_name'] + ', eu sou o Bot para o alarme 840Dsl, criado para encontrar as informações do seu erro.\n'
                                'Você deve me fornecer um valor para pesquisa.')

        else:
            erro = "Você deve fornecer um valor válido."
            await message.answer(erro)

        '''
        if message.text == '27001':
            Explanation = [x for x in alarmes if x['numero'] == '27001'][0]['Explanation']
            await message.answer(Explanation)
        
            for cont in range(1):
                divisor = []
                if txt.find('Divisor..//') >= 0:
                    divisor(cont) += x.split('Divisor..//')[1].split('Divisor..//')[0]
                    await message.answer(divisor)
        '''

    else:
        await message.answer("Olá, eu sou o Bot para o alarme 828D, criado para encontrar as informações do seu erro.\n"
                             "No momento você não possui permissão para acessar as informações internas.\n"
                             "Entre em contato com os desenvolvedores.\n"
                             "Para mais informações dos meu criadores digite '/info'")



# Final (não retirar)
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
