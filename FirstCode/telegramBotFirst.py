import telebot
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '\
       'AppleWebKit/537.36 (KHTML, like Gecko) '\
           'Chrome/75.0.3770.80 Safari/537.36'}


# ↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	 COTAÇÃO DO MILHO  ↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓



pagina = requests.get('https://www.cepea.esalq.usp.br/br/indicador/milho.aspx', headers=headers)

conteudo = pagina.content

site = BeautifulSoup(conteudo, 'html.parser')

tabela = site.find('div', attrs={'class':'imagenet-table-responsiva'})

cot1 = tabela.find('tbody')

cot2 = cot1.find_all('td')[0].get_text()

cot3 = cot1.find_all('td')[1]

cot4 = cot1.find_all('td')[5]

cot5 = cot1.find_all('td')[6]

cot6 = cot1.find_all('td')[10]

cot7 = cot1.find_all('td')[11]

cot8 = cot1.find_all('td')[15]

cot9 = cot1.find_all('td')[16]

cot10 = cot1.find_all('td')[20]

cot11 = cot1.find_all('td')[21]

# ↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	COTAÇÃO DA SOJA ↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	#

pagina2 = requests.get('https://www.cepea.esalq.usp.br/br/indicador/soja.aspx', headers = headers)

conteudo2 = pagina2.content

site2 = BeautifulSoup(conteudo2, 'html.parser')

tabela2 = site2.find('div', attrs ={'class' : 'imagenet-table-responsiva'})

cota1 = tabela2.find('tbody')

cot12 = cota1.find_all('td')[0]

cot13 = cota1.find_all('td')[1]

cot14 = cota1.find_all('td')[5]

cot15 = cota1.find_all('td')[6]

cot16 = cota1.find_all('td')[10]

cot17 = cota1.find_all('td')[11]

cot18 = cota1.find_all('td')[15]

cot19 = cota1.find_all('td')[16]

cot20 = cota1.find_all('td')[20]

cot21 = cota1.find_all('td')[21]

#	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓ COTAÇÃO DO CAFÉ	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓

pagina3 = requests.get('https://www.cepea.esalq.usp.br/br/indicador/cafe.aspx', headers = headers)

conteudo3 = pagina3.content

site3 = BeautifulSoup(conteudo3, 'html.parser')

tabela3 = site3.find('div', attrs ={'class' : 'imagenet-table-responsiva'})

cota2 = tabela3.find('tbody')

cot22 = cota2.find_all('td')[0]

cot23 = cota2.find_all('td')[1]

cot24 = cota2.find_all('td')[5]

cot25 = cota2.find_all('td')[6]

cot26 = cota2.find_all('td')[10]

cot27 = cota2.find_all('td')[11]

cot28 = cota2.find_all('td')[15]

cot29 = cota2.find_all('td')[16]

cot30 = cota2.find_all('td')[20]

cot31 = cota2.find_all('td')[21]

# ↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	BOT TELEGRAM ↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	↓	#

api = '5292833591:AAFs1BgWkcPHl4g0ozllgkq9djipeBpbZBU'

bot = telebot.TeleBot(api)


@bot.message_handler(commands=['milho'])
def opcao1(a):
  bot.reply_to(a, (f'''COTAÇÃO DO MILHO (SACA DE 60Kg)↓↓↓	
{cot2} = R${cot3.text}
{cot4.text} = R${cot5.text}
{cot6.text} = R${cot7.text}
{cot8.text} = R${cot9.text}
{cot10.text} = R${cot11.text}'''))
  

@bot.message_handler(commands=['soja'])
def opcao2(a):
  bot.reply_to(a, (f'''COTAÇÃO DA SOJA (SACA DE 60Kg)↓↓↓
{cot12.text} = R${cot13.text}
{cot14.text} = R${cot15.text}
{cot16.text} = R${cot17.text}
{cot18.text} = R${cot19.text}
{cot20.text} = R${cot21.text}''')) 


@bot.message_handler(commands=['cafe'])
def opcao3(a):
  bot.reply_to(a, (f'''COTAÇÃO DO CAFÉ (SACA DE 60Kg)↓↓↓
{cot22.text} = R${cot23.text}
{cot24.text} = R${cot25.text}
{cot26.text} = R${cot27.text}
{cot28.text} = R${cot29.text}
{cot30.text} = R${cot31.text}'''))

def verificar(a):
  return True

@bot.message_handler(func=verificar)
def responder(a): 
  bot.reply_to(a, '''Olá, sou o Cotador, seu robô que traz cotações atualizadas do Milho, Soja e Café
/milho para consultar o preço do Milho
/soja para consultar o preço da Soja
/cafe para consultar o preço do Café

Clique em uma das opções acima
''')












bot.polling()