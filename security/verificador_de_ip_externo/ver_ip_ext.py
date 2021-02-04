import re
import json
from urllib.request import urlopen

url = 'https://ipinfo.io/json'

resposta = urlopen(url)

dados = json.load(resposta)

ip = dados['ip']
hostname = dados['hostname']
city = dados['city']
estado = dados['region']
pais = dados['country']
local = dados['loc']
org = dados['org']
cep = dados['postal']
fuzo_horario = dados['timezone']
readme = dados['readme']

print('Detalhes do IP externo\n')
print('IP: {0}\nEstado: {1}\nPaís: {2}\nCidade: {3}\nOrg.: {4}\nCEP: {6}\nHost: {9}\nLocal: {5}\nFuzo: {7}\nReadme: {8}'.format(ip, estado, pais, city, org, local, cep, fuzo_horario, readme, hostname))