
    # função para validar a opção escolhida pelo usuário:
def validar_opcao(opcao):
        if opcao not in ["1", "2", "3", "4"]:
            print("\033[31mOpção inválida. Por favor, escolha uma opção válida.\033[0m")
            return False
        return True

    # função para ler a tarefa com validação de entrada:
def ler_tarefa():
        while True:
            nome = input("Digite o nome da tarefa: ")
            if nome.strip() == "":
                print("\033[31mO nome da tarefa não pode estar vazio. Tente novamente.\033[0m")
            else:
                break
        while True:
            descricao = input("Digite a descrição da tarefa: ")
            if descricao.strip() == "":
                print("\033[31mA descrição da tarefa não pode estar vazia. Tente novamente.\033[0m")
            else:
                break
        while True:
            prioridade = input("Digite a prioridade da tarefa (1-3): ")
            if prioridade not in ["1", "2", "3"]:
                print("\033[31mA prioridade deve ser um número entre 1 e 3. Tente novamente.\033[0m")
            else:
                break
        return {"nome": nome, "descricao": descricao, "prioridade": prioridade}

#criação da lista para armazenar as tarefas:
listas_tarefas = []

#iniciando o loop principal do programa, exibe o menu e processa as opções escolhidas pelo usuário:
while True:
        print(f"\033[34m" + " MENU ".center(35, "=") + "\033[0m")
        opcao = input("Escolha uma opção (1, 2, 3 ou 4): \n 1 - Criar \n 2 - Listar \n 3 - Concluir \n 4 - Sair \n Digite sua opção: ")
        print("\033[34m===================================\033[0m")

        #processa a opção escolhida pelo usuário
        if validar_opcao(opcao):
            #se a opção for criar a tarefa, chama a função ler_tarefa:
                #adiciona a tarefa à lista de tarefas
            if opcao == "1":
                print("\033[34m" + " Criar Tarefa ".center(35, "=") + "\033[0m")
                #chama a função para ler a tarefa e armazena a resposta em uma variável
                resposta = ler_tarefa()
                #adiciona a tarefa criada à lista de tarefas
                listas_tarefas.append(resposta)
                print("\033[32mTarefa criada com sucesso!\033[0m")

            elif opcao == "2":
                print(f"\033[34m" + " LISTAR TAREFAS ".center(35, "=") + "\033[0m")
                if not listas_tarefas:
                    print(f"\033[31m" + "Nenhuma tarefa cadastrada.".center(35, " ") + "\033[0m")

                else:
                    for resposta in listas_tarefas:
                        print(f"Nome: {resposta['nome']}")
                        print(f"Descrição: {resposta['descricao']}")
                        print(f"Prioridade: {resposta['prioridade']}")
                        print("\033[34m===================================\033[0m")

            elif opcao == "3":
                print(f"\033[34m" + " CONCLUIR TAREFAS ".center(35, "=") + "\033[0m")
                if not listas_tarefas:
                    print(f"\033[31m" + "Nenhuma tarefa cadastrada.".center(35, " ") + "\033[0m")
                else:
                    for i, resposta in enumerate(listas_tarefas):
                        print(f"{i + 1} - {resposta['nome']} (Prioridade: {resposta['prioridade']})")
                    while True:
                        try:
                            escolha = int(input("Digite o número da tarefa que deseja concluir: "))
                            if 1 <= escolha <= len(listas_tarefas):
                                tarefa_concluida = listas_tarefas.pop(escolha - 1)
                                print(f"\033[32mTarefa '{tarefa_concluida['nome']}' concluída com sucesso!\033[0m")
                                break
                            else:
                                print("\033[31mNúmero inválido. Tente novamente.\033[0m")
                        except ValueError:
                            print("\033[31mEntrada inválida. Por favor, digite um número.\033[0m")
                            

            elif opcao == "4":
                print("\033[34mEncerrando o programa...\033[0m")
                break