from tkinter import *
 
class MenuCadastro(Toplevel):
    def __init__(self, master = None):
        # Toplevel.__init__(self, master=master)
        self.MenuCadastro = Toplevel()

        # Configuração da janela principal
        self.MenuCadastro.title('Menu Cadastro')
        self.MenuCadastro.geometry('500x200')
        self.MenuCadastro.configure(borderwidth=8)
        self.MenuCadastro.configure(background = '#1e3743')

        for name in ("Cabeçalho", "Documentos", "Conclusão"):
            self.button = Button(self.MenuCadastro, text=name, height=5, width=15, font=('arial', '9', 'bold'))
            self.button.bind("<Button-1>", self.handle_event)
            self.button.pack(side='left', fill='x', expand=True)

        self.button = Button(self.MenuCadastro, text='Voltar', height=5, width=15, font=('arial', '9', 'bold'))
        self.button.bind("<Button-1>", self.MenuCadastro.destroy)
        self.button.place(relx=0.01, rely=0.9, relwidth=0.2, relheight=0.1)


        # Empacotamos o frame principal
        # self.pack(fill='both', expand=True)

    def handle_event(self, event):
        btn_name = event.widget.cget('text')
        if btn_name == "Conclusão":
            pass
            # window = MenuCadastro()
        if btn_name == "Documentos":
            pass
            # window = MenuCadastro()
        if btn_name == "Cabeçalho":
            window = CadastroCabecalho()
        
        window.mainloop()

    # def destroy(self):
    #     self.master.destroy()


class MenuDocumentos(Toplevel):
    def __init__(self, master = None):
        # Toplevel.__init__(self, master=master)
        Toplevel.__init__(self, master = master)

        # Configuração da janela principal
        self.title('Cadastro Documentos')
        self.geometry('500x200')
        self.configure(borderwidth=8)
        self.configure(background = '#1e3743')

        for name in ("Cabeçalho", "Documentos", "Conclusão"):
            self.button = Button(self, text=name, height=5, width=15, font=('arial', '9', 'bold'))
            self.button.bind("<Button-1>", self.handle_event)
            self.button.pack(side='left', fill='x', expand=True)

        # Empacotamos o frame principal
        # self.pack(fill='both', expand=True)

    def handle_event(self, event):
        btn_name = event.widget.cget('text')
        if btn_name == "Conclusão":
            pass
            # window = MenuCadastro()
        if btn_name == "Documentos":
            pass
            # window = MenuCadastro()
        if btn_name == "Cabeçalho":
            pass

class CadastroCabecalho(Toplevel):
    def __init__(self):
        Toplevel.__init__(self, master=None)

        # Configuração da janela principal
        self.title('Cadastro Cabeçalho')
        self.geometry('500x200')
        self.configure(borderwidth=8)
        self.configure(background = '#1e3743')

        for name in ("Voltar", "Salvar"):
            self.button = Button(self, text=name, height=5, width=15, font=('arial', '9', 'bold'))
            self.button.bind("<Button-1>", self.master.destroy())
            self.button.place(relx=0.01, rely=0.02, relwidth=0.7, relheight=0.1)

        # Empacotamos o frame principal
        self.pack(fill='both', expand=True)

    def handle_event(self, event):
        btn_name = event.widget.cget('text')
        if btn_name == "Conclusão":
            pass
            # window = MenuCadastro()
        if btn_name == "Documentos":
            pass
            # window = MenuCadastro()
        if btn_name == "Cabeçalho":
            window = CadastroCabecalho()

        window.mainloop()

class MainWindow(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, master=None)

        # Configuração da janela principal
        self.master.title('Hanna')
        self.master.geometry('300x200')
        self.configure(borderwidth=8)
        self.configure(background = '#1e3743')

        for name in ("Hanna Cadastro", "Hanna Análise"):
            self.button = Button(self, text=name, height=5, width=15, font=('arial', '9', 'bold'))
            self.button.bind("<Button-1>", self.handle_event)
            self.button.pack(side='left', fill='x', expand=True)

        # Empacotamos o frame principal
        self.pack(fill='both', expand=True)

    def handle_event(self, event):
        btn_name = event.widget.cget('text')
        if btn_name.endswith('o'):
            window = MenuCadastro()
        # if btn_name.endswith('e'):
        #     window = SecondWindow()

        window.mainloop()


if __name__ == '__main__':
    mainWindow = MainWindow()
    mainWindow.mainloop() 
    