import requests
from requests.api import request

def escolha_exercicio():
    escolha = input('Digite qual exericio voce deseja testar: ')
    if(escolha=='1'):

        formato_xml = 'xml'
        url = 'https://viacep.com.br/ws/'
        cep = ['30140071']
        
        response(url, cep, formato_xml)
    
    elif(escolha=='2'):
        formato_json= 'json'
        url = 'https://viacep.com.br/ws/'
        cep = ['30140071','30140072','30140073','30140074','30140075']
        response(url, cep, formato_json)

    elif(escolha=='3'):
        formato_json= 'json'
        url = 'https://viacep.com.br/ws/'
        estado='MG'
        cidade='Belo Horizonte'
        rua='Rua dos Aimores'
        endereco_completo= [estado+'/'+cidade+'/'+rua+'/']
        response(url, endereco_completo, formato_json)
    
    elif(escolha=='4'):
        formato_xml = 'xml'
        url = 'https://viacep.com.br/abc/'
        cep = ['30140071']
        response(url, cep, formato_xml)
    elif(escolha=='5'):
        formato_google = 'google'
        url = 'https://www.google.com/search'
        assunto= 'elson abreu'

        r = requests.get(url,params={'q':assunto})
        
        
        with open('response.txt','w') as file:
            file.write(r.text)
def response(url, localizacao, formato):
    
    for local in localizacao:

        r = requests.get(url +'/' + local + '/'+ formato)

        if (r.status_code == 200 and formato=='xml'):

            print(f'codigo_retorno: {r}')
            print(f'{formato}: ', r.text)
            print()
            
            
            
        elif (r.status_code == 200 and formato =='json'):
            
            print(f'{formato}: ', r.json())
            print()
            
        

        else:
            print('Nao houve sucesso na requisicao.')
            print(f'codigo_retorno: {r}')
            print(f'{formato}: ', r.text)


if __name__ == '__main__':
    escolha_exercicio()

    
 