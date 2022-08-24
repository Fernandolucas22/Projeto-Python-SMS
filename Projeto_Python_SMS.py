from email import message
import pandas as pd
from twilio.rest import Client

account_sid = "ACc652dbb5b52382407ba5324287bb1f9d"
auth_token = "4460fce72057ce48a6936a86665584c3"
client = Client(account_sid, auth_token)

#Passo a passo de solução

#Abrir os Arquivos em excel
lista_meses = ['Agosto', 'Julho', 'Junho']

for mes in lista_meses:
    tabela_Vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_Vendas['DEBITO'] > 0).any():
        ALUNOS = tabela_Vendas.loc[tabela_Vendas['DEBITO'] > 0, 'ALUNOS'].values[0]
        DEBITO = tabela_Vendas.loc[tabela_Vendas['DEBITO'] > 0, 'DEBITO'].values[0]
        print(f'No Mês {mes} Encontramos alguem com Debito A PAGAR. ALUNOS: {ALUNOS}')
        message = client.messages.create(
            to="+5586994151242",
            from_="+19206969535",
            body=f'No Mês {mes} Encontramos alguem com Debito A PAGAR. ALUNOS: {ALUNOS}')
        print(message.sid)

    


#Para cada arquivo:

#Verificar se algum aluno esta em debito apagar

#Se tiver debito mandar um SMS com a data de vencimento e o mes devedor 