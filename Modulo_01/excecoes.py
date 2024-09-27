#Excecoes podem interromper o programa, funcionam como tratamento de erros e excecoes não tratadas podem vir a se tornar bugs
print("Exemplo de captura de exeções")
try:
    numero = int(input("Digite um número inteiro: "))
    resultado = 10/ numero
except ValueError as e:
    print(f"ERRO DE VALOR PORRAAAAA: {e}")
    raise ValueError("Tipo de variaveis incompativeis")

except Exception as e:
    print(f"ERRO AQUIII: {e}")

else:       #usado só se o try der certo
    print(resultado)

finally:    #vai funcionar se der certo ou se der erro
    print("Operação finalizada")