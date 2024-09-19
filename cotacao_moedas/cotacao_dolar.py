import requests
import json

api_server = 'https://api.logv.xyz/'

# Buscar moedas disponíveis na Open Finance da Logic Vision
def buscarMoedas():
    resp = requests.get('{}api/v1/moeda/all'.format(api_server))
    moedas = resp.json()
    print(json.dumps(moedas, indent=2))

    for moeda in moedas:
        id = moeda['id']
        simbolo = moeda['simbolo']
        nome_formatado = moeda['nome_formatado']
        tipo_moeda = moeda['tipo_moeda']

    return moedas

# Buscar cotação do dólar na Open Finance da Logic Vision
def buscarCotacaoDolar():
    moedas = buscarMoedas()
    for moeda in moedas:
        if moeda['simbolo'] == 'USD':
            moeda_id = moeda['id']
    resp = requests.get('{}/api/v1/cotacao-dia/fechamento/{}'.format(api_server, moeda_id))
    cotacao = resp.json()
    
    paridade_compra = cotacao['paridade_compra']
    paridade_venda = cotacao['paridade_venda']
    cotacao_compra = cotacao['cotacao_compra']
    cotacao_venda = cotacao['cotacao_venda']
    data_hora_cotacao = cotacao['data_hora_cotacao']
    tipo_boletim = cotacao['tipo_boletim']

    print(json.dumps(cotacao, indent=2))

buscarCotacaoDolar()