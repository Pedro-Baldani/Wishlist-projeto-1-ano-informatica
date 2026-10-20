nomes = []
precos = []
prioridades = []
comprados = []
numeracoes = []


def adicionar():
    while True:
        try:
            nome = input("Digite o nome do jogo: ").title().strip()
            if len(nome) > 150:
                print("Nome muito grande. Tente novamente.")
                return adicionar()
            if not nome:
                print("Digite um nome.")
                print()
                return adicionar()
            preco = float(input("Digite o preço do jogo: "))
            if preco < 0:
                print("Opção inválida. Por favor, digite um número maior do que 0.")
                print()
                return adicionar()
            prioridade = int(
                input("Qual a prioridade da compra? [1: Baixa / 2: Média / 3: Alta]: "))
        except ValueError:
            print("Opção inválida. Por favor, tente novamente.")
            print()
            continue
        break

    if prioridade < 1 or prioridade > 3:
        print("Opção inválida. por favor, digite um número de 1 a 3.")
        print()
        return adicionar()
    match prioridade:
        case 1:
            prioridade = "Baixa"
        case 2:
            prioridade = "Média"
        case 3:
            prioridade = "Alta"

    nomes.append(nome)
    precos.append(preco)
    prioridades.append(prioridade)
    comprados.append(False)
    numeracoes.append(len(nomes))
    print("Jogo adicionado com sucesso!")


def listar():
    if nomes:
        for i in range(len(nomes)):
            if comprados[i] == True:
                sim_ou_nao_comprados = "Sim"
            else:
                sim_ou_nao_comprados = "Não"
            print(f"{numeracoes[i]} - Nome: {nomes[i]}" + f" | Preço:  R${precos[i]}" +
                  f" | Prioridade:  {prioridades[i]}" + f" | Já foi comprado? {sim_ou_nao_comprados}")
    else:
        print("Lista vazia. Tente adicionar um jogo primeiro!")


def atualizar():
    if nomes:
        while True:
            try:
                comprou_ou_atualizar = int(input(
                    "Deseja atualizar um item ou marcar um como comprado? [1: Atualizar / 2: Marcar como comprado] "))
                match comprou_ou_atualizar:
                    case 1:
                        numeracao = int(
                            input("Qual o item que deseja atualizar? "))
                        if numeracao not in numeracoes:
                            print(
                                "Opção inválida. Por favor, digite o número de um item que esteja na lista.")
                            print()
                            return atualizar()
                        o_que_atualizar = int(
                            input("Qual campo deseja atualizar? [1: Nome / 2: Preço / 3: Prioridade]: "))
                        if o_que_atualizar < 1 or o_que_atualizar > 3:
                            print(
                                "Opção inválida. Por favor, digite um número de 1 a 3.")
                            return atualizar()
                        else:
                            match o_que_atualizar:
                                case 1:
                                    for i in range(len(numeracoes)):
                                        if numeracoes[i] == numeracao:
                                            nome2 = input(
                                                "Digite o nome do jogo: ").title().strip()
                                            nomes[i] = nome2
                                            if not nome2:
                                                print("Digite um nome.")
                                                print()
                                                return atualizar()
                                            return main()
                                case 2:
                                    for i in range(len(numeracoes)):
                                        if numeracoes[i] == numeracao:
                                            preco2 = float(
                                                input("Digite o preço do jogo: "))
                                            precos[i] = preco2
                                            return main()
                                case 3:
                                    for i in range(len(numeracoes)):
                                        if numeracoes[i] == numeracao:
                                            prioridade2 = int(
                                                input("Qual a prioridade da compra? [1: Baixa / 2: Média / 3: Alta]: "))
                                            if prioridade2 < 1 or prioridade2 > 3:
                                                print(
                                                    "Opção inválida. Por favor, digite um número de 1 a 3.")
                                                print()
                                                return atualizar()
                                            match prioridade2:
                                                case 1:
                                                    prioridade2 = "Baixa"
                                                case 2:
                                                    prioridade2 = "Média"
                                                case 3:
                                                    prioridade2 = "Alta"
                                            prioridades[i] = prioridade2
                                            return main()
                    case 2:
                        for i in range(len(numeracoes)):
                            # alterei uma variavel de comprados2 pra comprados[i] e funcionou PARCIALMENTE, o treco ta marcando apenas o primeiro item da lista como comprado ou não
                            # ja que também não tem nada pra selecionar qual item da lista marcar, porém ao menos tá marcando o primeiro item :/
                            comprados[i] == False
                            confirmacao_ja_comprou = input(
                                "Deseja marcar o item como comprado? [s/n] ").strip().lower()
                            if confirmacao_ja_comprou == "s":
                                comprados[i] = True
                                return main()
                            elif confirmacao_ja_comprou == "n":
                                print("Operação cancelada.")
                                return main()
                            else:
                                print(
                                    "Opção inválida. Por favor, digite 's' para sim e 'n' para não.")
                                return atualizar()
            except ValueError:
                print("Opção inválida. Por favor, tente novamente.")
                print()
                continue
            break
    else:
        print("Lista vazia. Tente adicionar um jogo primeiro!")


def remover():
    if nomes:
        while True:
            try:
                numeracao = int(input("Qual o item que deseja remover? "))
            except ValueError:
                print(
                    "Opção inválida. Por favor, digite o número de um item que esteja na lista.")
                print()
                continue
            break
        if numeracao not in numeracoes:
            print(
                "Opção inválida. Por favor, digite o número de um item que esteja na lista.")
            return remover()
        confirmacao_remover = input(
            f"Tem certeza que deseja remover o item {numeracao}? [s/n]: ").strip().lower()
        if confirmacao_remover == "s":
            for i in range(len(numeracoes)):
                if numeracoes[i] == numeracao:
                    nomes.remove(nomes[i])
                    precos.remove(precos[i])
                    prioridades.remove(prioridades[i])
                    comprados.remove(comprados[i])
                    numeracoes.remove(numeracoes[i])
                    break
            print("Item removido com sucesso!")
        elif confirmacao_remover == "n":
            print("Ação cancelada.")
            return main()
        else:
            print("Opção inválida. Por favor, digite 's' para sim ou 'n' para não.")
            print()
            return remover()
    else:
        print("Lista vazia. Tente adicionar um jogo primeiro!")


def limpar():
    if nomes:
        limparlista = input("Tem certeza que deseja limpar a lista? [s/n]: ")
        if limparlista == "s":
            for i in range(len(numeracoes)):
                nomes.pop()
                precos.pop()
                prioridades.pop()
                comprados.pop()
                numeracoes.pop()
            print("Lista limpa com sucesso!")
            return main()
        elif limparlista == "n":
            print("Ação cancelada.")
            return main()
        else:
            print("Opção inválida. Por favor, digite 's' para sim ou 'n' para não.")
            print()
            return limpar()
    else:
        print("Lista vazia. Tente adicionar um jogo primeiro!")


def menu():
    print("=" * 20)
    print("Lista de desejos")
    print()
    print("1. Adicionar item")
    print("2. Ver lista")
    print("3. Atualizar lista")
    print("4. Remover item")
    print("5. Limpar lista")
    print("0. Sair (Em construção)")
    print("=" * 20)


def main():
    while True:
        menu()
        try:
            op = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida. Por favor, digite um número de 0 a 5.")
            return main()
        if op < 0 or op > 5:
            print("Opção inválida. Por favor, digite um número de 0 a 5.")

        match op:
            case 1:
                adicionar()

            case 2:
                listar()

            case 3:
                atualizar()

            case 4:
                remover()

            case 5:
                limpar()

            case 0:
                pass


if __name__ == "__main__":
    main()
