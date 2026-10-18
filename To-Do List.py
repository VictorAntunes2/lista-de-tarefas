tarefas = []

def adicionar_tarefa():
    tarefa = input("Digite a tarefa: ")
    tarefas.append({"nome": tarefa, "concluida": False})
    print("Tarefa adicionada!")

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    for i, tarefa in enumerate(tarefas, start=1):
        status = "✅" if tarefa["concluida"] else "❌"
        print(f"{i}. {tarefa['nome']} - {status}")

def concluir_tarefa():
    listar_tarefas()

    try:
        indice = int(input("Número da tarefa: ")) - 1
        tarefas[indice]["concluida"] = True
        print("Tarefa concluída!")
    except:
        print("Opção inválida!")

while True:
    print("\n=== TO-DO LIST ===")
    print("1 - Adicionar")
    print("2 - Listar")
    print("3 - Concluir")
    print("4 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        listar_tarefas()
    elif opcao == "3":
        concluir_tarefa()
    elif opcao == "4":
        break

import json

with open("tarefas.json", "w") as arquivo:
    json.dump(tarefas, arquivo)
try:
    with open("tarefas.json", "r") as arquivo:
        tarefas = json.load(arquivo)
except FileNotFoundError:
    tarefas = []

import tkinter as tk

janela = tk.Tk()
janela.title("To-Do List")

entrada = tk.Entry(janela, width=30)
entrada.pack()

lista = tk.Listbox(janela)
lista.pack()

def adicionar():
    lista.insert(tk.END, entrada.get())
    entrada.delete(0, tk.END)

botao = tk.Button(janela, text="Adicionar", command=adicionar)
botao.pack()

janela.mainloop()

