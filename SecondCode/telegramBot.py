import telebot
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '\
       'AppleWebKit/537.36 (KHTML, like Gecko) '\
           'Chrome/75.0.3770.80 Safari/537.36'}


def cotacao(item):
  if item == "/milho":
    pagina = requests.get('https://www.cepea.esalq.usp.br/br/indicador/milho.aspx', headers=headers)

    tipo = "DO MILHO"
  
  elif item == "/soja":
    pagina = requests.get('https://www.cepea.esalq.usp.br/br/indicador/soja.aspx', headers = headers)

    tipo = "DA SOJA"

  else:
    pagina = requests.get('https://www.cepea.esalq.usp.br/br/indicador/cafe.aspx', headers = headers)

    tipo = "DO CAFÉ"


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

  mensagem = (f'''COTAÇÃO {tipo} (SACA DE 60Kg)↓↓↓	
  {cot2} = R${cot3.text}
  {cot4.text} = R${cot5.text}
  {cot6.text} = R${cot7.text}
  {cot8.text} = R${cot9.text}
  {cot10.text} = R${cot11.text}''')
  
  return mensagem

api = '5292833591:AAFs1BgWkcPHl4g0ozllgkq9djipeBpbZBU'

bot = telebot.TeleBot(api)


@bot.message_handler(commands=['milho', 'soja', 'cafe'])
def opcao1(a):
  bot.reply_to(a, f"{cotacao(a.text)}")
  

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