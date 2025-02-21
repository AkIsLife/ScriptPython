import json
import tkinter as tk
from tkinter import messagebox

CAMINHO_ARQUIVO = "C:/Users/Aluno/Desktop/ScriptPython/tarefas.json"

def carregar_tarefas():
    try:
        with open(CAMINHO_ARQUIVO, 'r') as file:
            tarefas = json.load(file)
            for tarefa in tarefas:
                if 'status' not in tarefa:
                    tarefa['status'] = 'Pendente'
            return tarefas
    except FileNotFoundError:
        return []

def salvar_tarefas(tarefas):
    with open(CAMINHO_ARQUIVO, 'w') as file:
        json.dump(tarefas, file, indent=4)

def adicionar_tarefa():
    tarefa = entrada_tarefa.get()
    if tarefa:
        tarefas = carregar_tarefas()
        tarefas.append({"id": len(tarefas) + 1, "tarefa": tarefa, "status": "Pendente"})
        salvar_tarefas(tarefas)
        messagebox.showinfo("Sucesso", f"Tarefa '{tarefa}' adicionada.")
        listar_tarefas()
        entrada_tarefa.delete(0, tk.END)
    else:
        messagebox.showwarning("Atenção", "Por favor, insira uma tarefa.")

def listar_tarefas():
    tarefas = carregar_tarefas()
    lista_pendentes.delete(0, tk.END)
    lista_nao_concluidas.delete(0, tk.END)
    
    pendentes = [t for t in tarefas if t["status"] == "Pendente"]
    nao_concluidas = [t for t in tarefas if t["status"] == "Não Concluída"]
    
    if pendentes:
        for t in pendentes:
            lista_pendentes.insert(tk.END, f"{t['id']}. {t['tarefa']}")
    else:
        lista_pendentes.insert(tk.END, "Nenhuma tarefa pendente.")
    
    if nao_concluidas:
        for t in nao_concluidas:
            lista_nao_concluidas.insert(tk.END, f"{t['id']}. {t['tarefa']}")
    else:
        lista_nao_concluidas.insert(tk.END, "Nenhuma tarefa não concluída.")

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
            messagebox.showinfo("Tarefa", f"Tarefa {id_tarefa}: {tarefa['tarefa']} - {tarefa['status']}")
        else:
            messagebox.showwarning("Erro", "Tarefa não encontrada.")
    except ValueError:
        messagebox.showwarning("Erro", "Por favor, insira um ID válido.")

def atualizar_status():
    try:
        id_tarefa = int(entrada_id.get())
        tarefas = carregar_tarefas()
        tarefa = next((t for t in tarefas if t["id"] == id_tarefa), None)
        if tarefa:
            novo_status = status_var.get()
            tarefa["status"] = novo_status
            salvar_tarefas(tarefas)
            messagebox.showinfo("Sucesso", f"Status da tarefa {id_tarefa} atualizado para '{novo_status}'.")
            listar_tarefas()
        else:
            messagebox.showwarning("Erro", "Tarefa não encontrada.")
    except ValueError:
        messagebox.showwarning("Erro", "Por favor, insira um ID válido.")

root = tk.Tk()
root.title("Gerenciador de Tarefas")
root.geometry("800x400")

root.configure(bg="#f0f0f0")

tk.Label(root, text="Tarefa:", bg="#f0f0f0").grid(row=0, column=0, sticky="e", padx=10, pady=5)
entrada_tarefa = tk.Entry(root, width=40, relief="solid", bd=2)
entrada_tarefa.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="ID da Tarefa:", bg="#f0f0f0").grid(row=1, column=0, sticky="e", padx=10, pady=5)
entrada_id = tk.Entry(root, width=40, relief="solid", bd=2)
entrada_id.grid(row=1, column=1, padx=10, pady=5)

frame_left = tk.Frame(root, bg="#f0f0f0")
frame_left.grid(row=2, column=0, padx=10, pady=5)

frame_right = tk.Frame(root, bg="#f0f0f0")
frame_right.grid(row=2, column=2, padx=10, pady=5)

tk.Label(frame_left, text="Tarefas Pendentes", bg="#f0f0f0").pack()
lista_pendentes = tk.Listbox(frame_left, height=10, width=30, bd=2, relief="solid")
lista_pendentes.pack()

tk.Label(frame_right, text="Tarefas Não Concluídas", bg="#f0f0f0").pack()
lista_nao_concluidas = tk.Listbox(frame_right, height=10, width=30, bd=2, relief="solid")
lista_nao_concluidas.pack()

button_style = {"width": 20, "padx": 5, "pady": 5}

tk.Button(root, text="Adicionar Tarefa", command=adicionar_tarefa, **button_style).grid(row=3, column=0, pady=5)
tk.Button(root, text="Atualizar Tarefa", command=atualizar_tarefa, **button_style).grid(row=3, column=1, pady=5)
tk.Button(root, text="Deletar Tarefa", command=deletar_tarefa, **button_style).grid(row=3, column=2, pady=5)

tk.Label(root, text="Status da Tarefa:", bg="#f0f0f0").grid(row=4, column=0, sticky="e", padx=10, pady=5)
status_var = tk.StringVar(value="Pendente")
tk.OptionMenu(root, status_var, "Pendente", "Concluída", "Não Concluída").grid(row=4, column=1, padx=10, pady=5)

tk.Button(root, text="Atualizar Status", command=atualizar_status, **button_style).grid(row=4, column=2, columnspan=2, pady=10)

listar_tarefas()

root.mainloop()
