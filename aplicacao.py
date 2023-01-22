from tkinter import *

class funcs():
    def criando_perguntas(self):
        self.n_perguntas = self.input_nP.get()
        print(self.n_perguntas)

class Aplication(funcs):
    def __init__(self, root):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        root.mainloop()

    def tela(self):
        self.root.title("Hanna")
        self.root.configure(background = '#1e3743')
        self.root.geometry("400x700")
        self.root.resizable(False, False)
        self.root.maxsize(width=800, height=700)
        self.root.minsize(width=500, height=300)

    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, border=4, bg = 'white', highlightbackground= 'black', highlightthickness=1.2)
        self.frame_1.place(relx=0.08 ,rely=0.04, relheight=0.4, relwidth=.84)


    def widgets_frame1(self):
        self.lb_nP = Label(self.frame_1, text='Digite o numero de perguntas necessárias: ',bg='white',font=('Verdana', '8', 'bold'))
        self.lb_nP.place(relx=0.01, rely=0.02, relwidth=0.7, relheight=0.1)

        self.input_nP = Entry(self.frame_1)
        self.input_nP.place(relx=0.01, rely=0.1, relwidth=0.1, relheight=0.05)

        # self.lb_p1 = Label(self.frame_1, text='Digite a pergunta numero 1: ',bg='white',font=('Verdana', '8', 'bold'))
        # self.lb_p1.place(relx=0.01, rely=0.03, relwidth=0.7, relheight=0.1)

        # self.input_p1 = Entry(self.frame_1)
        # self.input_p1.place(relx=0.01, rely=0.1, relwidth=0.1, relheight=0.05)

        # self.lb_p2 = Label(self.frame_1, text='Digite a pergunta numero 2: ',bg='white',font=('Verdana', '8', 'bold'))
        # self.lb_p2.place(relx=0.01, rely=0.03, relwidth=0.7, relheight=0.1)

        # self.input_p2 = Entry(self.frame_1)
        # self.input_p2.place(relx=0.01, rely=0.1, relwidth=0.1, relheight=0.05)

        # self.bt_cadastrar = Button(self.frame_1, text='Enter' , bg = '#107db2',
        #                          fg = 'white', command=self.criando_perguntas)
        # self.bt_cadastrar.place(relx=0.14, rely=0.1, relwidth=0.2, relheight=0.05)



root = Tk()
Aplication(root)