
import tiktoken

modelo = "gpt-4"
codificador = tiktoken.encoding_for_model(modelo)

# Texto processado (tokenizado) via encode
lista_tokens = codificador.encode("O gato correu.")

print("gpt-4 Lista de Tokens: ", lista_tokens) # Lista de Tokens:  [46, 342, 4428, 12603, 84, 13]
print("gpt-4 Quantos tokens temos: ", len(lista_tokens))
print(f"gpt-4 Custo para o modelo {modelo} é de ${((len(lista_tokens)/1000)*0.03):.5f}")


modelo = "gpt-3.5-turbo-1106"
codificador = tiktoken.encoding_for_model(modelo)
lista_tokens = codificador.encode("O gato pulou.")

print("gpt-3.5 Lista de Tokens: ", lista_tokens) #  Lista de Tokens:  [46, 342, 4428, 7893, 283, 13] -> tokens semelhantes porque as frases são parecidas
print("gpt-3.5 Quantos tokens temos: ", len(lista_tokens))
print(f"gpt-3.5 Custo para o modelo {modelo} é de ${((len(lista_tokens)/1000)*0.002):.5f}")
