from tkinter import *
from tkinter import scrolledtext

def MainMenu():
    root = Tk() 

    root.geometry("900x500")
    root.title('Hanna')
    root.configure(borderwidth=8)
    root.configure(background = '#1e3743')
    root.minsize(width=450, height=300)

    def handle_event(event):
        btn_name = event.widget.cget('text')
        if btn_name == "Hanna Cadastro":
            MenuCadastro(root)
        if btn_name.endswith('Hanna Análise'):
            AnaliseHanna(root)
 
    for name in ("Hanna Cadastro", "Hanna Análise"):
        root.button = Button(root, text=name, height=5, width=15, font=('arial', '9', 'bold'))
        root.button.bind("<Button-1>", handle_event)
        root.button.pack(side='left', fill='x', expand=True)

    root.button = Button(root, text='Sair', height=5, width=15, font=('arial', '9', 'bold'), command=root.destroy)
    root.button.place(relx=0.01, rely=0.9, relwidth=0.2, relheight=0.1)


    root.mainloop() 
    

def Cad_Cabecalho(MenuCadastro): 
     
    Cad_Cabecalho = Toplevel(MenuCadastro)
    Cad_Cabecalho.title("Cadastro Cabeçalho")
    Cad_Cabecalho.geometry("900x500")
    Cad_Cabecalho.configure(borderwidth=8)
    Cad_Cabecalho.configure(background = '#1e3743')
    Cad_Cabecalho.minsize(width=900, height=500)
    Cad_Cabecalho.focus_force()
    Cad_Cabecalho.grab_set()
     
    # Create label
    label = Label(Cad_Cabecalho, text = "CABEÇALHO ",font=('arial', '14'), background='#1e3743', foreground='white')
    label.place(relx=0.4, rely=0.01, relwidth=0.2, relheight=0.1)
     

    text_area = scrolledtext.ScrolledText(Cad_Cabecalho, wrap=WORD, width=40, height=8, font=("Times New Roman", 15))
    text_area.place(relx=0.01, rely=0.15, relwidth=0.99, relheight=0.7)
    text_area.focus()

    Cad_Cabecalho.button = Button(Cad_Cabecalho, text='Voltar', height=5, width=15, font=('arial', '9', 'bold'), command=Cad_Cabecalho.destroy)
    Cad_Cabecalho.button.place(relx=0.01, rely=0.9, relwidth=0.2, relheight=0.1)

    Cad_Cabecalho.button = Button(Cad_Cabecalho, text='Salvar', height=5, width=15, font=('arial', '9', 'bold'), command=Cad_Cabecalho.destroy)
    Cad_Cabecalho.button.place(relx=0.79, rely=0.9, relwidth=0.2, relheight=0.1)
     
    # Display until closed manually.
    Cad_Cabecalho.mainloop()
      

def MenuCadastro(root): 
    MenuCadastro = Toplevel(root)

    MenuCadastro.title('Menu Cadastro')
    MenuCadastro.geometry("900x500")
    MenuCadastro.configure(borderwidth=8)
    MenuCadastro.configure(background = '#1e3743')
    MenuCadastro.minsize(width=500, height=200)
    MenuCadastro.focus_force()
    MenuCadastro.grab_set()
     
    def handle_event(event):
        btn_name = event.widget.cget('text')
        if btn_name == 'Cabeçalho':
            Cad_Cabecalho(MenuCadastro)
        if btn_name == 'Documentos':
            Cad_Documentos(MenuCadastro)
        if btn_name == 'Conclusão':
            Cad_Conclusao(MenuCadastro)
 

    for name in ("Cabeçalho", "Documentos", "Conclusão"):
        MenuCadastro.button = Button(MenuCadastro, text=name, height=5, width=15, font=('arial', '9', 'bold'))
        MenuCadastro.button.bind("<Button-1>", handle_event)
        MenuCadastro.button.pack(side='left', fill='x', expand=True)

    MenuCadastro.button = Button(MenuCadastro, text='Voltar', height=5, width=15, font=('arial', '9', 'bold'), command=MenuCadastro.destroy)
    MenuCadastro.button.place(relx=0.01, rely=0.9, relwidth=0.2, relheight=0.1)

    MenuCadastro.mainloop()
 

def Cad_Documentos(MenuCadastro): 
     
    Cad_Documentos = Toplevel(MenuCadastro)
    Cad_Documentos.title("Cadastro de Documentos")
    Cad_Documentos.geometry("1100x700")
    Cad_Documentos.configure(borderwidth=8)
    Cad_Documentos.configure(background = '#1e3743')
    Cad_Documentos.minsize(width=1100, height=700)
    Cad_Documentos.focus_force()
    Cad_Documentos.grab_set()

    inputs = list()

    def Get_inputs():
        global inputs 
        return inputs

    def Save_inputs():
        documentos = list()
        documentos = [str(docs.get()) for docs in inputs]
        print(documentos)
        

    for i in range(5):
        for j in range(6):
            Cad_Documentos.Label = Label(Cad_Documentos, text = ("Documento " + str((j+1)+(6*i))),font=('arial', '14'), background='#1e3743', foreground='white')
            Cad_Documentos.Label.place(relx=(0.01 + (j*0.16)), rely=(0.13 + (i*0.15)), relwidth=0.15, relheight=0.03)

            inputs.append(Entry(Cad_Documentos))
            inputs[j + (6*i)].place(relx=(0.01 + (j*0.16)), rely=(0.16 + (i*0.15)), relwidth=0.15, relheight=0.03)


    # Create label
    label = Label(Cad_Documentos, text = "POSSIVEIS DOCUMENTOS",font=('arial', '14'), background='#1e3743', foreground='white')
    label.place(relx=0.35, rely=0, relwidth=0.3, relheight=0.05)


    Cad_Documentos.button = Button(Cad_Documentos, text='Voltar', height=5, width=15, font=('arial', '9', 'bold'), command=Cad_Documentos.destroy)
    Cad_Documentos.button.place(relx=0.01, rely=0.9, relwidth=0.2, relheight=0.1)

    Cad_Documentos.button = Button(Cad_Documentos, text='Salvar', height=5, width=15, font=('arial', '9', 'bold'), command=Save_inputs)
    Cad_Documentos.button.place(relx=0.79, rely=0.9, relwidth=0.2, relheight=0.1)

    # Display until closed manually.
    Cad_Documentos.mainloop()
      

def Cad_Conclusao(MenuCadastro):

         
    Cad_Conclusao = Toplevel(MenuCadastro)
    Cad_Conclusao.title("Cadastro Cabeçalho")
    Cad_Conclusao.geometry("900x500")
    Cad_Conclusao.configure(borderwidth=8)
    Cad_Conclusao.configure(background = '#1e3743')
    Cad_Conclusao.minsize(width=900, height=500)
    Cad_Conclusao.focus_force()
    Cad_Conclusao.grab_set()
     
    # Create label
    label = Label(Cad_Conclusao, text = "CONCLUSÃO ",font=('arial', '14'), background='#1e3743', foreground='white')
    label.place(relx=0.4, rely=0.01, relwidth=0.2, relheight=0.1)
     

    text_area = scrolledtext.ScrolledText(Cad_Conclusao, wrap=WORD, width=40, height=8, font=("Times New Roman", 15))
    text_area.place(relx=0.01, rely=0.15, relwidth=0.99, relheight=0.7)
    text_area.focus()

    Cad_Conclusao.button = Button(Cad_Conclusao, text='Voltar', height=5, width=15, font=('arial', '9', 'bold'), command=Cad_Conclusao.destroy)
    Cad_Conclusao.button.place(relx=0.01, rely=0.9, relwidth=0.2, relheight=0.1)

    Cad_Conclusao.button = Button(Cad_Conclusao, text='Salvar', height=5, width=15, font=('arial', '9', 'bold'), command=Cad_Conclusao.destroy)
    Cad_Conclusao.button.place(relx=0.79, rely=0.9, relwidth=0.2, relheight=0.1)
     
    # Display until closed manually.
    Cad_Conclusao.mainloop()
      

def AnaliseHanna(root):
    AnaliseHanna = Toplevel(root)
    AnaliseHanna.title("ANÁLISE DE DOCUMENTOS")
    AnaliseHanna.geometry("1100x700")
    AnaliseHanna.configure(borderwidth=8)
    AnaliseHanna.configure(background = '#1e3743')
    AnaliseHanna.minsize(width=1100, height=700)
    AnaliseHanna.focus_force()
    AnaliseHanna.grab_set()

    checkvar = list()
    checkbutton = list()
    acabou = False
        

    for i in range(8):
        for j in range(4):
            AnaliseHanna.Label = Label(AnaliseHanna, text = ("O Documento " + str((j+1)+(4*i)) + " Foi apresentado?"),font=('arial', '12'), background='#1e3743', foreground='white')
            AnaliseHanna.Label.place(relx=(0.01 + (j*0.25)), rely=(0.10 + (i*0.10)), relwidth=0.25, relheight=0.03)

            checkvar.append(IntVar())
            checkvar[j + (4*i)].set(0)

            checkbutton.append(Checkbutton(AnaliseHanna, text=('Documento' + str((j+1)+(4*i))), variable = checkvar[j + (4*i)]))
            checkbutton[j + (4*i)].place(relx=(0.02 + (j*0.25)), rely=(0.13 + (i*0.10)), relwidth=0.1, relheight=0.03)

            if ((j+1)+(4*i)) == 30:
                acabou = True
                break

        if acabou:
            break
            

    label = Label(AnaliseHanna, text = "POSSIVEIS DOCUMENTOS",font=('arial', '14'), background='#1e3743', foreground='white')
    label.place(relx=0.35, rely=0, relwidth=0.3, relheight=0.05)


    AnaliseHanna.button = Button(AnaliseHanna, text='Voltar', height=5, width=15, font=('arial', '9', 'bold'), command=AnaliseHanna.destroy)
    AnaliseHanna.button.place(relx=0.01, rely=0.9, relwidth=0.2, relheight=0.1)

    AnaliseHanna.button = Button(AnaliseHanna, text='Salvar', height=5, width=15, font=('arial', '9', 'bold'), command=AnaliseHanna.destroy)
    AnaliseHanna.button.place(relx=0.79, rely=0.9, relwidth=0.2, relheight=0.1)

    # Display until closed manually.
    AnaliseHanna.mainloop()


MainMenu()