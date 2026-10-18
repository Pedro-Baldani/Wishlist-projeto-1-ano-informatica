nomes = []
precos = []
prioridades = []
comprados = []
numeracoes = []

def adicionar():
    while True:
        try:
            nome = input("Digite o nome do jogo: ").title().strip()
            if not nome:
                print("Digite um nome.")
                print()
                return adicionar()                
            preco = float(input("Digite o preço do jogo: "))
            prioridade = int(input("Qual a prioridade da compra? [1: Baixa / 2: Média / 3: Alta]: "))
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
            print(f"{numeracoes[i]} - Nome: {nomes[i]}" + f" | Preço:  R${precos[i]}" + f" | Prioridade:  {prioridades[i]}" + f" | Já foi comprado? {sim_ou_nao_comprados}")
    else:
        print("Lista vazia. Tente adicionar um jogo primeiro!")

def atualizar():
    if nomes:
        while True:
            try:
                numeracao = int(input("Qual o item que deseja atualizar? "))
                if numeracao not in numeracoes:
                    print("Opção inválida. Por favor, digite o número de um item que esteja na lista.")
                    print()
                    return atualizar()
                nome2 = input("Digite o nome do jogo: ").title().strip()
                if not nome2:
                    print("Digite um nome.")
                    print()
                    return adicionar()
                preco2 = float(input("Digite o preço do jogo: "))
                prioridade2 = int(input("Qual a prioridade da compra? [1: Baixa / 2: Média / 3: Alta]: "))
                if prioridade2 < 1 or prioridade2 > 3:
                    print("Opção inválida. Por favor, digite um número de 1 a 3.")
                    print()
                    return adicionar()
                comprados2 = input("O item já foi comprado? [s/n]: ").strip().lower()
            except ValueError:
                print("Opção inválida. por favor, tente novamente.")
                print()
                continue
            break
            
        match prioridade2:
            case 1:
                prioridade2 = "Baixa"
            case 2:
                prioridade2 = "Média"
            case 3:
                prioridade2 = "Alta"
        if comprados2 not in ["s", "n"]:
            print("Opção inválida. por favor, digite 's' para sim ou 'n' para não.")
            print()
            return atualizar()

        for i in range(len(numeracoes)):
            if numeracoes[i] == numeracao:
                nomes[i] = nome2
                precos[i] = preco2
                prioridades[i] = prioridade2
                comprados[i] = comprados2 == "s"
                break
    else:
        print("Lista vazia. Tente adicionar um jogo primeiro!")

def remover():
    if nomes:
        while True:
            try:
                numeracao = int(input("Qual o item que deseja remover? "))
            except ValueError:
                print("Opção inválida. Por favor, digite o número de um item que esteja na lista.")
                print()
                continue
            break
        if numeracao not in numeracoes:
            print("Opção inválida. Por favor, digite o número de um item que esteja na lista.")
            return remover()
        confirmacao_remover = input(f"Tem certeza que deseja remover o item {numeracao}? [s/n]: ").strip().lower()
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
    print("5. Limpar lista (Em construção)")
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
