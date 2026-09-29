# ============================================================
# SISTEMA DE GESTÃO DE NOTAS DE ALUNOS
# Linguagem: Python 3
# Autora: Patricia Gomes Dias
# ============================================================

def cadastrar_notas():
    notas = []
    while True:
        entrada = input("Digite a nota do aluno (ou 'fim' para encerrar): ")
        if entrada.lower() == 'fim':
            break
        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Por favor, insira uma nota válida entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Digite um número ou 'fim'.")
    return notas

def calcular_media(notas):
    if len(notas) == 0:
        return 0.0
    return sum(notas) / len(notas)

def verificar_situacao(media):
    if media >= 7.0:
        return "Aprovado"
    else:
        return "Reprovado"

def exibir_relatorio(notas, media, situacao):
    print("\n--- RELATÓRIO FINAL ---")
    print(f"Notas inseridas: {notas}")
    print(f"Média do aluno: {media:.2f}")
    print(f"Situação do aluno: {situacao}")
    print("------------------------")

def main():
    print("=== Sistema de Gestão de Notas ===")
    notas = cadastrar_notas()
    if not notas:
        print("Nenhuma nota foi informada.")
        return
    media = calcular_media(notas)
    situacao = verificar_situacao(media)
    exibir_relatorio(notas, media, situacao)

if _name_ == "_main_":
    main()
