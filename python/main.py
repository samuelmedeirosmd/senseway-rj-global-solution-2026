# ============================================================
#  GS CitizenTech · Computational Thinking with Python
#  Atividade: O Cérebro da CitizenTech
#
#  Equipe: Samuel Dantas Silva de Medeiros - RM 576922
#          Felipe de Oliveira Corrêa - RM 574803
#  Turma: 1ESSRQ-2026
#  CitizenTech: SenseWay RJ
#  Problema: obstáculos urbanos dificultam a mobilidade de
#  pessoas com deficiência visual em Madureira, no Rio.
# ============================================================
#
#  Partes do programa:
#    PARTE 1 - Dados       (lista com 10+ registros)
#    PARTE 2 - Faixas      (limites do protótipo SenseWay RJ)
#    PARTE 3 - Menu        (loop que só termina no Sair)
#    PARTE 4 - Opções      (classificar, resumir, avisar)
# ============================================================


# ------------------------------------------------------------
# PARTE 1 - DADOS
# Cada valor simula uma leitura de distância do sensor.
# Não são medições reais de Madureira.
# ------------------------------------------------------------

nome_local = "Madureira - Rio de Janeiro"
grandeza = "Distância até o obstáculo"
unidade = "cm"

# 12 distâncias válidas e uma leitura inválida (0 = falha)
leituras = [220, 180, 150, 121, 120, 95, 72, 50, 38, 25, 65, 145, 0]


# ------------------------------------------------------------
# PARTE 2 - FAIXAS DE DECISÃO
# Os mesmos limites devem aparecer no Edge e no site.
# Faixas ilustrativas, não validadas para uso em deslocamento.
# ------------------------------------------------------------

minimo_sensor = 2
maximo_sensor = 400
limite_proximo = 50       # de 2 a 50 cm: PRÓXIMO
limite_atencao = 120     # acima de 50 até 120 cm: ATENÇÃO

aviso_livre = "Nenhum obstáculo próximo detectado pelo sensor."
aviso_atencao = "Atenção: obstáculo na faixa de alerta."
aviso_proximo = "Obstáculo muito próximo! Tenha cuidado."
aviso_falha = "Falha na leitura. Não considerar o caminho livre."


# ------------------------------------------------------------
# PARTE 3 - MENU
# O menu repete até o usuário escolher 0.
# Entrada inválida NÃO pode derrubar o programa.
# ------------------------------------------------------------

print("=" * 48)
print(f"  SenseWay RJ · {nome_local}")
print("=" * 48)

opcao = ""
while opcao != "0":
    print()
    print("1 - Ver todas as leituras classificadas")
    print("2 - Resumo das leituras")
    print("3 - Consultar uma leitura")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ").strip()

    # --------------------------------------------------------
    # PARTE 4 - OPÇÕES
    # --------------------------------------------------------

    if opcao == "1":
        # Percorre a lista e classifica cada registro.
        print()
        print(f"{grandeza} em {nome_local}:")
        for posicao in range(len(leituras)):
            valor = leituras[posicao]

            if valor < minimo_sensor or valor > maximo_sensor:
                faixa = "FALHA"
            elif valor <= limite_proximo:
                faixa = "PRÓXIMO"
            elif valor <= limite_atencao:
                faixa = "ATENÇÃO"
            else:
                faixa = "LIVRE"

            print(f"  Leitura {posicao + 1:02d}: {valor} {unidade} -> {faixa}")

    elif opcao == "2":
        # Resumo: média, maior valor e % das leituras válidas em alerta.
        soma = 0
        maior = 0
        quantidade_validas = 0
        quantidade_alerta = 0
        quantidade_proximo = 0
        quantidade_falhas = 0

        for valor in leituras:
            if valor < minimo_sensor or valor > maximo_sensor:
                quantidade_falhas += 1
            else:
                soma = soma + valor
                quantidade_validas += 1
                if valor > maior:
                    maior = valor
                if valor <= limite_proximo:
                    quantidade_proximo += 1
                    quantidade_alerta += 1
                elif valor <= limite_atencao:
                    quantidade_alerta += 1

        print()
        if quantidade_validas > 0:
            media = soma / quantidade_validas
            percentual_alerta = quantidade_alerta / quantidade_validas * 100
            print(f"Média das distâncias: {media:.2f} {unidade}")
            print(f"Maior distância: {maior} {unidade}")
            print(f"Leituras em alerta: {quantidade_alerta} de {quantidade_validas} ({percentual_alerta:.1f}%)")
            print(f"Leituras inválidas: {quantidade_falhas}")

            if quantidade_proximo > 0:
                print(f"AVISO: {aviso_proximo}")
            elif quantidade_alerta > 0:
                print(f"AVISO: {aviso_atencao}")
            else:
                print(f"AVISO: {aviso_livre}")
        else:
            print("Nenhuma leitura válida para calcular o resumo.")
            print(f"AVISO: {aviso_falha}")

    elif opcao == "3":
        # Consulta com validação: insiste até receber um número válido.
        numero = input(f"Número da leitura (1 a {len(leituras)}): ").strip()
        while not numero.isdigit() or int(numero) < 1 or int(numero) > len(leituras):
            print("Valor inválido. Digite apenas o número da leitura.")
            numero = input(f"Número da leitura (1 a {len(leituras)}): ").strip()

        valor = leituras[int(numero) - 1]
        if valor < minimo_sensor or valor > maximo_sensor:
            faixa = "FALHA"
            aviso = aviso_falha
        elif valor <= limite_proximo:
            faixa = "PRÓXIMO"
            aviso = aviso_proximo
        elif valor <= limite_atencao:
            faixa = "ATENÇÃO"
            aviso = aviso_atencao
        else:
            faixa = "LIVRE"
            aviso = aviso_livre

        print(f"Leitura {numero}: {valor} {unidade} -> {faixa}")
        print(f"AVISO: {aviso}")

    elif opcao == "0":
        print("Encerrando o SenseWay RJ. Até logo!")

    else:
        print("Opção inválida. Escolha um número do menu.")
