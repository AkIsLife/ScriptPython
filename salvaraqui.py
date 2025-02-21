import json

CAMINHO_ARQUIVO = "C:/Users/Aluno/Desktop/Trabalho/tarefas.json"

def carregar_tarefas():
    try:
        with open(CAMINHO_ARQUIVO, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def salvar_tarefas(tarefas):
    with open(CAMINHO_ARQUIVO, 'w') as file:
        json.dump(tarefas, file, indent=4)

def adicionar_tarefa():
    tarefa = input("Digite a descrição da tarefa: ")
    tarefas = carregar_tarefas()
    tarefas.append({"id": len(tarefas) + 1, "tarefa": tarefa})
    salvar_tarefas(tarefas)
    print(f"Tarefa '{tarefa}' adicionada.")

def listar_tarefas():
    tarefas = carregar_tarefas()
    if tarefas:
        for t in tarefas:
            print(f"{t['id']}. {t['tarefa']}")
    else:
        print("Nenhuma tarefa encontrada.")

def atualizar_tarefa():
    id_tarefa = int(input("Digite o ID da tarefa a ser atualizada: "))
    tarefas = carregar_tarefas()
    tarefa = next((t for t in tarefas if t["id"] == id_tarefa), None)
    
    if tarefa:
        tarefa["tarefa"] = input(f"Nova descrição para '{tarefa['tarefa']}': ")
        salvar_tarefas(tarefas)
        print(f"Tarefa {id_tarefa} atualizada.")
    else:
        print("Tarefa não encontrada.")

def deletar_tarefa():
    id_tarefa = int(input("Digite o ID da tarefa a ser deletada: "))
    tarefas = carregar_tarefas()
    tarefas = [t for t in tarefas if t["id"] != id_tarefa]
    salvar_tarefas(tarefas)
    print(f"Tarefa {id_tarefa} deletada.") if len(tarefas) < len(carregar_tarefas()) else print("Tarefa não encontrada.")

def menu():
    opcoes = {
        "1": adicionar_tarefa,
        "2": listar_tarefas,
        "3": listar_tarefas,
        "4": atualizar_tarefa,
        "5": deletar_tarefa,
        "6": exit
    }

    while True:
        print("\n1. Adicionar Tarefa\n2. Listar Tarefas\n3. Listar Tarefa Específica\n4. Atualizar Tarefa\n5. Deletar Tarefa\n6. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "3":
            id_tarefa = int(input("Digite o ID da tarefa para visualizar: "))
            tarefas = carregar_tarefas()
            tarefa = next((t for t in tarefas if t["id"] == id_tarefa), None)
            print(f"Tarefa {id_tarefa}: {tarefa['tarefa']}" if tarefa else "Tarefa não encontrada.")
        elif opcao in opcoes:
            opcoes[opcao]()  # Executa a função correspondente
        else:
            print("Opção inválida.")

menu()