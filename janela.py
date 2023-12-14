from tkinter import *

class Gui():
    def __init__(self):
        self.window = Tk()
        self.window.wm_title('Cadastro de Clientes')

        # Variáveis de controle
        self.txtNome = StringVar()
        self.txtSobrenome = StringVar()
        self.txtEmail = StringVar()
        self.txtCPF = StringVar()

        # Criando os objetos que farão parte das janelas
        lblnome = Label(self.window, text='Nome')
        lblsobrenome = Label(self.window, text='Sobrenome')
        lblemail = Label(self.window, text='Email')
        lblcpf = Label(self.window, text='CPF')
        entNome = Entry(self.window, textvariable=self.txtNome, width=30)
        entSobrenome = Entry(self.window, textvariable=self.txtSobrenome, width=30)
        entEmail = Entry(self.window, textvariable=self.txtEmail, width=30)
        entCPF = Entry(self.window, textvariable=self.txtCPF, width=30)
        listClientes = Listbox(self.window, width=100)
        scrollClientes = Scrollbar(self.window)
        btnViewALL = Button(self.window, text='Ver todos')
        btnBuscar = Button(self.window, text='Buscar')
        btnInserir = Button(self.window, text='Inserir')
        btnUpdate = Button(self.window, text='Atualizar Selecionados')
        btnDel = Button(self.window, text='Deletar Selecionados')
        btnClose = Button(self.window, text='Fechar')

        # Associando objetos
        lblnome.grid(row=0, column=0)
        lblsobrenome.grid(row=1, column=0)
        lblemail.grid(row=2, column=0)
        lblcpf.grid(row=3, column=0)
        entNome.grid(row=0, column=1, padx=50, pady=50)
        entSobrenome.grid(row=1, column=1)
        entEmail.grid(row=2, column=1)
        entCPF.grid(row=3, column=1)
        listClientes.grid(row=0, column=2, rowspan=10)
        scrollClientes.grid(row=0, column=6, rowspan=10)
        btnViewALL.grid(row=4, column=0, columnspan=2)
        btnBuscar.grid(row=5, column=0, columnspan=2)
        btnInserir.grid(row=6, column=0, columnspan=2)
        btnUpdate.grid(row=7, column=0, columnspan=2)
        btnDel.grid(row=8, column=0, columnspan=2)
        btnClose.grid(row=9, column=0, columnspan=2)

        # União do Scrollbar com a Listbox
        listClientes.configure(yscrollcommand=scrollClientes.set)
        scrollClientes.configure(command=listClientes.yview)

        # Adicionar SWAG (aparência) à interface
        for child in self.window.winfo_children():
            Widget_class = child.__class__.__name__
            if Widget_class == 'Button':
                child.grid_configure(sticky='WE', padx=5, pady=3)
            elif Widget_class == 'Listbox':
                child.grid_configure(padx=0, pady=0, sticky='NS')
            elif Widget_class == 'Scrollbar':
                child.grid_configure(padx=0, pady=0, sticky='NS')
            else:
                child.grid_configure(padx=5, pady=3, sticky='N')

    def run(self):
        self.window.mainloop()

# Exemplo de uso
if __name__ == '__main__':
    app = Gui()
    app.run()



