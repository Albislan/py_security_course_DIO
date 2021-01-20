import hashlib
#import os
#print(os.getcwd()) #Como Saber em qual pasta principal o sistema ira buscar os arquivos#

arquivo1 = './security/comparador_de_hashes/a.txt'

arquivo2 = './security/comparador_de_hashes/b.txt'

hash1 = hashlib.new('ripemd160')

hash1.update(open(arquivo1, 'rb').read())

hash2 = hashlib.new('ripemd160')

hash2.update(open(arquivo2, 'rb').read())

if hash1.digest() != hash2.digest():
    print("*" * 60)
    print(f'O hash do Arquivo: {arquivo1} é diferente do  hash do Arquivo {arquivo2}')
    print('\n O hash do arquivo a.txt é ', hash1.hexdigest())
    print('\n O hash do arquivo b.txt é ', hash2.hexdigest())
    print("*" * 60)
else:
    print("*" * 60)
    print(f'O hash do Arquivo: {arquivo1} é identico ao hash do Arquivo: {arquivo2}')
    print('\n O hash do arquivo a.txt é ', hash1.hexdigest())
    print('\n O hash do arquivo b.txt é ', hash2.hexdigest())
    print("*" * 60)    