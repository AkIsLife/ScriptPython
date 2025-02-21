import json
import tkinter as tk
from tkinter import messagebox

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
    tarefa = entrada_tarefa.get()
    if tarefa:
        tarefas = carregar_tarefas()
        tarefas.append({"id": len(tarefas) + 1, "tarefa": tarefa})
        salvar_tarefas(tarefas)
        messagebox.showinfo("Sucesso", f"Tarefa '{tarefa}' adicionada.")
        listar_tarefas()
        entrada_tarefa.delete(0, tk.END)
    else:
        messagebox.showwarning("Atenção", "Por favor, insira uma tarefa.")

def listar_tarefas():
    tarefas = carregar_tarefas()
    lista_tarefas.delete(0, tk.END) 
    if tarefas:
        for t in tarefas:
            lista_tarefas.insert(tk.END, f"{t['id']}. {t['tarefa']}")
    else:
        lista_tarefas.insert(tk.END, "Nenhuma tarefa encontrada.")

def atualizar_tarefa():
    try:
        id_tarefa = int(entrada_id.get())
        tarefas = carregar_tarefas()
        tarefa = next((t for t in tarefas if t["id"] == id_tarefa), None)
        if tarefa:
            nova_tarefa = entrada_tarefa.get()
            if nova_tarefa:
                tarefa["tarefa"] = nova_tarefa
                salvar_tarefas(tarefas)
                messagebox.showinfo("Sucesso", f"Tarefa {id_tarefa} atualizada.")
                listar_tarefas() 
                entrada_tarefa.delete(0, tk.END) 
            else:
                messagebox.showwarning("Atenção", "Por favor, insira uma nova descrição para a tarefa.")
        else:
            messagebox.showwarning("Erro", "Tarefa não encontrada.")
    except ValueError:
        messagebox.showwarning("Erro", "Por favor, insira um ID válido.")

def deletar_tarefa():
    try:
        id_tarefa = int(entrada_id.get())
        tarefas = carregar_tarefas()
        tarefas = [t for t in tarefas if t["id"] != id_tarefa]
        salvar_tarefas(tarefas)
        messagebox.showinfo("Sucesso", f"Tarefa {id_tarefa} deletada.") if len(tarefas) < len(carregar_tarefas()) else messagebox.showwarning("Erro", "Tarefa não encontrada.")
        listar_tarefas() 
        entrada_id.delete(0, tk.END) 
    except ValueError:
        messagebox.showwarning("Erro", "Por favor, insira um ID válido.")

def exibir_tarefa_especifica():
    try:
        id_tarefa = int(entrada_id.get())
        tarefas = carregar_tarefas()
        tarefa = next((t for t in tarefas if t["id"] == id_tarefa), None)
        if tarefa:
            messagebox.showinfo("Tarefa", f"Tarefa {id_tarefa}: {tarefa['tarefa']}")
        else:
            messagebox.showwarning("Erro", "Tarefa não encontrada.")
    except ValueError:
        messagebox.showwarning("Erro", "Por favor, insira um ID válido.")

root = tk.Tk()
root.title("Gerenciador de Tarefas")

tk.Label(root, text="Tarefa:").grid(row=0, column=0)
entrada_tarefa = tk.Entry(root, width=40)
entrada_tarefa.grid(row=0, column=1)

tk.Label(root, text="ID da Tarefa:").grid(row=1, column=0)
entrada_id = tk.Entry(root, width=40)
entrada_id.grid(row=1, column=1)

lista_tarefas = tk.Listbox(root, height=10, width=50)
lista_tarefas.grid(row=2, column=0, columnspan=2)

tk.Button(root, text="Adicionar Tarefa", command=adicionar_tarefa).grid(row=3, column=0, pady=10)
tk.Button(root, text="Listar Tarefas", command=listar_tarefas).grid(row=3, column=1)
tk.Button(root, text="Atualizar Tarefa", command=atualizar_tarefa).grid(row=4, column=0)
tk.Button(root, text="Deletar Tarefa", command=deletar_tarefa).grid(row=4, column=1)
tk.Button(root, text="Exibir Tarefa Específica", command=exibir_tarefa_especifica).grid(row=5, column=0, columnspan=2, pady=10)

listar_tarefas()  
root.mainloop()
1
