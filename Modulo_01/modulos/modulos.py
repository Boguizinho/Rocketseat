#importação e utilização de um módulo padrão python

from math import sqrt

raiz_quadrada = sqrt(25)
print(raiz_quadrada)

print("\nExemplo de criação e utilização de um módulo personalizado")

import meu_modulo

mensagem = meu_modulo.saudacao("Gabriel")
resultado = meu_modulo.dobro(5)

print(mensagem, resultado)
