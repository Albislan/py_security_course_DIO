import random, string

tamanho = 16

chars = string.ascii_letters + string.digits + '!@ç§}¨¬¢£ª[]{#$%&*()-=+,.;:/\|?'
rnd = random.SystemRandom()
print("*" * 60)
print(''.join(rnd.choice(chars) for i in range(tamanho)))
print("*" * 60)