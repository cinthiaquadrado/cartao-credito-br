# Documentação: https://dadosabertos.bcb.gov.br/dataset/20542-saldo-da-carteira-de-credito-com-recursos-livres---total/resource/6e2b0c97-afab-4790-b8aa-b9542923cf88

# Banco de Dados: https://www3.bcb.gov.br/sgspub/localizarseries/localizarSeries.do?method=prepararTelaLocalizarSeries

# Link de referência para criar o código: https://youtu.be/pZlsfaVk7c0

0. Importar as bibliotecas

import pandas as pd
import matplotlib.pyplot as plt

1.Extração dos dados

url = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.1178/dados?formato=json&dataInicial=01/01/2010&dataFinal=31/12/2016'

df = pd.read_json(url)

df.set_index('data', inplace = True)

df.head()

Passos seguintes:

df.index = pd.to_datetime(df.index, dayfirst= True)

df.plot()

2. Generalização da extração

def extracao_bcb(codigo, data_inicio, data_fim):
  url = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.{}/dados?formato=json&dataInicial={}&dataFinal={}'.format(codigo, data_inicio, data_fim)
  df = pd.read_json(url)
  df.set_index('data', inplace = True)
  df.index = pd.to_datetime(df.index, dayfirst= True)
  return df

# Saldo da carteira de crédito com recursos livres - Pessoas físicas - Cartão de crédito rotativo
pf_cartao_credito_rotativo = extracao_bcb(20587,'01/03/2007', '31/10/2024')

_df_0['valor'].plot(kind='hist', bins=20, title='Saldo da carteira de crédito com recursos livres - PF - Cartão de crédito rotativo')
plt.gca().spines[['top', 'right',]].set_visible(False)

plt.figure(figsize=(10, 6))
pf_cartao_credito_rotativo.plot(title='Saldo da carteira de crédito com recursos livres - PF - Cartão de crédito rotativo')
plt.xlabel('Data')
plt.ylabel('Valor')
plt.grid(True)

plt.show()

