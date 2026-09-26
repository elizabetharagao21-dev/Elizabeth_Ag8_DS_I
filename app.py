# Contadores
excelente = 0
ruim = 0

# Repetição para 50 entrevistados
for i in range(50):
    print(f"\n--- Entrevistado {i + 1} ---")

    nome = input("Digite aqui o seu nome: ")
    idade = int(input("Qual a sua idade? "))

    print("Opções de atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    opiniao = int(input("Digite o número correspondente à sua opinião: "))

    if opiniao == 1:
        excelente += 1
        print("Opinião registrada: EXCELENTE")
    elif opiniao == 2:
        print("Opinião registrada: BOM")
    elif opiniao == 3:
        ruim += 1
        print("Opinião registrada: RUIM")
    else:
        print("Opção inválida!")

# Resultado final
print("\n========== RESULTADO DA PESQUISA ==========")
print("Quantidade de respostas EXCELENTE:", excelente)
print("Quantidade de respostas RUIM:", ruim)
