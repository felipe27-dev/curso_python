from tkinter import *

# Dicionário para armazenar as notas cadastradas
notas_cadastradas = {
    'Linguagens': [],
    'Matemática': [],
    'Ciências Humanas': [],
    'Ciências da Natureza': []
}

def cadastrar_notas():
    janela_cadastrar = Tk()
    janela_cadastrar.title("Cadastrar Notas")

    # Função para cadastrar as notas
    def cadastrar():
        materia = str(materia_entry.get())
        n1 = float(n1_entry.get())
        n2 = float(n2_entry.get())
        n3 = float(n3_entry.get())
        media = (n1+n2+n3)
        nota_necessaria = 240 - media 
        nota_necessaria = round(nota_necessaria)
        print(nota_necessaria)
        if nota_necessaria < 0:
            nota_necessaria = "Você já passou"
        print(nota_necessaria)
        resultado_label.configure(text=f"Nota necessária para passar: {nota_necessaria}")

        # Adiciona as notas cadastradas ao dicionário
        notas_cadastradas[materia].append((n1, n2, n3))

    # Componentes da janela
    materia_label = Label(janela_cadastrar, text="Matéria:")
    materia_label.pack()
    materia_entry = Entry(janela_cadastrar)
    materia_entry.pack()

    n1_label = Label(janela_cadastrar, text="Primeira Nota:")
    n1_label.pack()
    n1_entry = Entry(janela_cadastrar)
    n1_entry.pack()

    n2_label = Label(janela_cadastrar, text="Segunda Nota:")
    n2_label.pack()
    n2_entry = Entry(janela_cadastrar)
    n2_entry.pack()

    n3_label = Label(janela_cadastrar, text="Terceira Nota:")
    n3_label.pack()
    n3_entry = Entry(janela_cadastrar)
    n3_entry.pack()

    cadastrar_btn = Button(janela_cadastrar, text="Cadastrar", command=cadastrar)
    cadastrar_btn.pack()

    resultado_label = Label(janela_cadastrar, text="")
    resultado_label.pack()

    janela_cadastrar.mainloop()

def ver_notas_cadastradas():
    janela_ver = Tk()
    janela_ver.title("Ver Notas Cadastradas")

    # Função para visualizar as notas cadastradas
    def ver():
        notas_text.delete(1.0, END)
        for materia, notas in notas_cadastradas.items():
            notas_text.insert(END, f"Notas cadastradas para {materia}:\n")
            for i, nota in enumerate(notas):
                notas_text.insert(END, f"Nota {i+1}: {nota[0]}, {nota[1]}, {nota[2]}\n")
            notas_text.insert(END, "\n")

    # Componentes da janela
    notas_label = Label(janela_ver, text="Notas Cadastradas:")
    notas_label.pack()
    notas_text = Text(janela_ver, width=50, height=10)
    notas_text.pack()

    ver_btn = Button(janela_ver, text="Ver", command=ver)
    ver_btn.pack()

    janela_ver.mainloop()

def finalizar_programa():
    print("Opção: Finalizar Programa")
    exit()
def criar_janela():
    janela = Tk()
    janela.title("Programa de Notas")
    cadastrar_btn = Button(janela, text="Cadastrar Notas", command=cadastrar_notas, font=("Arial", 14), padx=10, pady=5)
    cadastrar_btn.pack(pady=5)

    ver_btn = Button(janela, text="Ver Notas Cadastradas", command=ver_notas_cadastradas, font=("Arial", 14), padx=5)
    ver_btn.pack(pady=5)

    ver_btn = Button(janela, text="Finalizar Programa", command=finalizar_programa, font=("Arial", 14), padx=5)
    ver_btn.pack(pady=5)
    janela.mainloop()
criar_janela()