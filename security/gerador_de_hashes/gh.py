import hashlib
texto = input('Digite o texto  a ser gerado a hash: \n')
print('')
md5 = hashlib.md5(texto.encode('utf-8'))
sha1 = hashlib.sha1(texto.encode('utf-8'))
sha256 = hashlib.sha256(texto.encode('utf-8'))
sha512 = hashlib.sha512(texto.encode('utf-8'))

def codigo(menu):
    if menu == 1:
        return 'MD5'
    if menu == 2:
        return 'SHA1'
    if menu == 3:
        return 'SHA256'
    if menu == 4:
        return 'SHA512'                


def enfeite():
    print('')
    print('*' * 100)
    print('A hash {} da String: {} é: {}'.format(codigo(menu), texto, impressao(menu).hexdigest()))
    print('*' * 100)
    print('')

def impressao(menu):
    if menu == 1:
        resultado = md5
    if menu == 2:
        resultado = sha1
    if menu == 3:
        resultado = sha256
    if menu == 4:
        resultado = sha512    
    return resultado            



menu = int(input(''' #### MENU - ESCOLHA O TIPO DE HASH ####
                1) MD5
                2) SHA1
                3) SHA256
                4) SHA512 \n
                Escolha um número de 1 a 4 equivalente ao hash a ser gerado: \n'''))
enfeite()                
# if menu == 1:
#     resultado = hashlib.md5(texto.encode('utf-8'))
#     print('')
#     print('*' * 100)
#     print('A hash MD5 da String: {} é: {}'.format(texto, resultado.hexdigest()))
#     print('*' * 100)
#     print('')

# elif menu == 2:
#     resultado = hashlib.sha1(texto.encode('utf-8'))
#     print('')
#     print('*' * 100)
#     print('A hash SHA1 da String: {} é: {}'.format(texto, resultado.hexdigest()))
#     print('*' * 100)
#     print('')

# elif menu == 3:
#     resultado = hashlib.sha256(texto.encode('utf-8'))
#     print('')
#     print('*' * 100)
#     print('A hash SHA256 da String: {} é: {}'.format(texto, resultado.hexdigest()))
#     print('*' * 100)
#     print('')

# elif menu == 4:
#     resultado = hashlib.sha512(texto.encode('utf-8'))
#     print('')
#     print('*' * 100)
#     print('A hash SHA512 da String: {} é: {}'.format(texto, resultado.hexdigest()))
#     print('*' * 100)
#     print('')            