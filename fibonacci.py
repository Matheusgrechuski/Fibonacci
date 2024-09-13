# 1) Verificar se um número pertence à sequência de Fibonacci
def is_fibonacci(n):
    a, b = 0, 1
    while b <= n:
        if b == n:
            return True
        a, b = b, a + b
    return False

# 2) Contar ocorrências da letra 'a' (maiúscula ou minúscula) em uma string
def contar_a(string):
    return string.lower().count('a')

# 3) Cálculo do valor da variável SOMA no código dado
def calcular_soma():
    INDICE = 12
    SOMA = 0
    K = 1
    while K < INDICE:
        K = K + 1
        SOMA = SOMA + K
    return SOMA

# 4) Completar o próximo elemento da sequência
def completar_sequencias():
    sequencias = {
        'a': [1, 3, 5, 7, 9],            # Soma de 2 em 2
        'b': [2, 4, 8, 16, 32, 64, 128], # Multiplica por 2
        'c': [0, 1, 4, 9, 16, 25, 36, 49],  # Quadrados perfeitos
        'd': [4, 16, 36, 64, 100],       # Quadrados de números pares
        'e': [1, 1, 2, 3, 5, 8, 13],     # Fibonacci
        'f': [2, 10, 12, 16, 17, 18, 19, 200]  # Mistura com salto
    }
    return sequencias

# Função principal para executar o código
def main():
    # 1) Verificação de número na sequência de Fibonacci
    numero = int(input("Informe um número para verificar se está na sequência de Fibonacci: "))
    if is_fibonacci(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci.")
    
    # 2) Contagem da letra 'a' na string
    texto = input("Informe uma string para contar a letra 'a': ")
    quantidade_a = contar_a(texto)
    print(f"A letra 'a' aparece {quantidade_a} vezes na string.")

    # 3) Cálculo do valor da variável SOMA
    soma = calcular_soma()
    print(f"O valor final da variável SOMA é: {soma}")

    # 4) Completar as sequências
    sequencias = completar_sequencias()
    print("\nPróximos elementos das sequências:")
    print(f"a) {sequencias['a']}")
    print(f"b) {sequencias['b']}")
    print(f"c) {sequencias['c']}")
    print(f"d) {sequencias['d']}")
    print(f"e) {sequencias['e']}")
    print(f"f) {sequencias['f']}")

# Executar o programa
if __name__ == "__main__":
    main()
