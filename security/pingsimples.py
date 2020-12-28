import os

print('#' * 60)
ip_ou_host = input("Digite o host a ser verificado:\n")
print('')
print("*" *60)
os.system('ping -n 6 {}'.format(ip_ou_host)) #Chamando o Ping pela biblioteca os.system#
print("*" *60)
