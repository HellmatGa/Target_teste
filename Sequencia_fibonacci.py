# Função para verificar se um número pertence à sequência de Fibonacci
def is_fibonacci(n):
    # Iniciando a sequência de Fibonacci
    fib_sequence = [0, 1]

    # Gerar a sequência de Fibonacci até um valor maior ou igual ao número informado
    while fib_sequence[-1] < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    # Verifica se o número pertence à sequência
    if n in fib_sequence:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} NÃO pertence à sequência de Fibonacci."


# Definindo o número para verificar
num_to_check = 21

# Executando a verificação
resultado = is_fibonacci(num_to_check)
resultado