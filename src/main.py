def exibir_menu():
    print("\n" + "="*40)
    print("         TASKTRACKER - MENU")
    print("="*40)
    print("1. Cadastrar nova tarefa")
    print("2. Visualizar tarefas cadastradas")
    print("3. Sair da aplicacao")
    print("="*40)


def cadastrar_tarefa(tarefas):
    print("\n--- CADASTRO DE NOVA TAREFA ---\n")

    while True:
        titulo = input("Titulo da tarefa: ").strip()
        if titulo == "":
            print("ERRO: O titulo nao pode ser vazio. Tente novamente.")
        else:
            break

    descricao = input("Descricao da tarefa: ").strip()

    prioridades_validas = ["alta", "media", "média", "baixa"]
    while True:
        prioridade = input("Prioridade (Alta / Media / Baixa): ").strip()
        if prioridade.lower() not in prioridades_validas:
            print("ERRO: Prioridade invalida! Digite Alta, Media ou Baixa.")
        else:
            if prioridade.lower() in ["media", "média"]:
                prioridade = "Media"
            else:
                prioridade = prioridade.capitalize()
            break

    data_limite = input("Data limite (DD/MM/AAAA): ").strip()

    status = "Pendente"

    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": status
    }

    tarefas.append(tarefa)
    print("\nTarefa cadastrada com sucesso!")


def visualizar_tarefas(tarefas):
    print("\n--- LISTA DE TAREFAS ---\n")

    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada ainda.")
        return

    for i, tarefa in enumerate(tarefas, 1):
        print(f"Tarefa {i}:")
        print(f"  Titulo:      {tarefa['titulo']}")
        print(f"  Descricao:   {tarefa['descricao']}")
        print(f"  Prioridade:  {tarefa['prioridade']}")
        print(f"  Data Limite: {tarefa['data_limite']}")
        print(f"  Status:      {tarefa['status']}")
        print("-" * 30)


def main():
    tarefas = []

    while True:
        exibir_menu()
        opcao = input("Escolha uma opcao (1-3): ").strip()

        if opcao == "1":
            cadastrar_tarefa(tarefas)
        elif opcao == "2":
            visualizar_tarefas(tarefas)
        elif opcao == "3":
            print("\nSaindo da aplicacao... Ate logo!")
            break
        else:
            print("\nOpcao invalida! Digite 1, 2 ou 3.")


main()