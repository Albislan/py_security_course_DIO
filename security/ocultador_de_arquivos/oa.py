import ctypes

atributo_ocultar = 0x02

retorno = ctypes.windll.kernel32.SetFileAttributesW('./security/ocultador_de_arquivos/ocultar.txt', atributo_ocultar)

if retorno:
    print('O Arquivo foi ocultado')
else:
    print('O Aqruivo não foi ocultado')    
