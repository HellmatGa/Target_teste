# Função para verificar a existência da letra 'a' (maiúscula ou minúscula) em uma string
def count_letter_a(s):
    # Conta as ocorrências de 'a' e 'A'
    count = s.lower().count('a')

    if count > 0:
        return f"A letra 'a' aparece {count} vez(es) na string."
    else:
        return "A letra 'a' não aparece na string."


# Definindo a string para verificar
string_to_check = "A rápida raposa marrom salta sobre o cão preguiçoso."

# Executando a verificação
resultado = count_letter_a(string_to_check)
resultado