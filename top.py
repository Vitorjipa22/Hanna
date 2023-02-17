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
            MenuAnalise(root)
 
    for name in ("Hanna Cadastro", "Hanna Análise"):
        root.button = Button(root, text=name, height=5, width=15, font=('arial', '9', 'bold'))
        root.button.bind("<Button-1>", handle_event)
        root.button.pack(side='left', fill='x', expand=True)

    root.button = Button(root, text='Sair', height=5, width=15, font=('arial', '9', 'bold'), command=root.destroy)
    root.button.place(relx=0.01, rely=0.9, relwidth=0.2, relheight=0.1)


    root.mainloop() 


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
        if btn_name == 'Prova Documental':
            Cad_Documentos(MenuCadastro)
        if btn_name == 'Conclusão':
            Cad_Conclusao(MenuCadastro)
        if btn_name == 'Prova Pericial':
            Cad_Pericial(MenuCadastro)
        if btn_name == 'Prova Testemunhal':
            Cad_Testemunhal(MenuCadastro)
 

    for name in ("Cabeçalho", "Prova Documental", "Prova Pericial", "Prova Testemunhal", "Conclusão"):
        MenuCadastro.button = Button(MenuCadastro, text=name, height=5, width=15, font=('arial', '9', 'bold'))
        MenuCadastro.button.bind("<Button-1>", handle_event)
        MenuCadastro.button.pack(side='left', fill='x', expand=True)

    MenuCadastro.button = Button(MenuCadastro, text='Voltar', height=5, width=15, font=('arial', '9', 'bold'), command=MenuCadastro.destroy)
    MenuCadastro.button.place(relx=0.01, rely=0.9, relwidth=0.2, relheight=0.1)

    MenuCadastro.mainloop()


def MenuAnalise(root): 
    MenuAnalise = Toplevel(root)

    MenuAnalise.title('Menu Analise')
    MenuAnalise.geometry("900x500")
    MenuAnalise.configure(borderwidth=8)
    MenuAnalise.configure(background = '#1e3743')
    MenuAnalise.minsize(width=500, height=200)
    MenuAnalise.focus_force()
    MenuAnalise.grab_set()
     
    def handle_event(event):
        btn_name = event.widget.cget('text')
        if btn_name == 'Análise dos Documentos':
            Ana_documentos(MenuAnalise)
        if btn_name == 'Análise Pericial':
            Ana_Pericial(MenuAnalise)
        if btn_name == 'Análise Testemunhal':
            Ana_Testemunhal(MenuAnalise)
        if btn_name == 'Gerar Minuta':
            Gerar_Minuta(MenuAnalise)

    for name in ("Análise dos Documentos", "Análise Pericial", "Análise Testemunhal", "Gerar Minuta"):
        MenuAnalise.button = Button(MenuAnalise, text=name, height=5, width=15, font=('arial', '9', 'bold'))
        MenuAnalise.button.bind("<Button-1>", handle_event)
        MenuAnalise.button.pack(side='left', fill='x', expand=True)

    MenuAnalise.button = Button(MenuAnalise, text='Voltar', height=5, width=15, font=('arial', '9', 'bold'), command=MenuAnalise.destroy)
    MenuAnalise.button.place(relx=0.01, rely=0.9, relwidth=0.2, relheight=0.1)

    MenuAnalise.mainloop()


def Cad_Conclusao(MenuCadastro):
  
    Cad_Conclusao = Toplevel(MenuCadastro)
    Cad_Conclusao.title("Cadastro Cabeçalho")
    Cad_Conclusao.geometry("1300x700")
    Cad_Conclusao.configure(borderwidth=8)
    Cad_Conclusao.configure(background = '#1e3743')
    Cad_Conclusao.minsize(width=1300, height=700)
    Cad_Conclusao.focus_force()
    Cad_Conclusao.grab_set()
    text_area = list()

    def SalvarConclusao(text_area):
        for i in range(3):
            arquivo = open('conclusao' + str(i+1) + '.txt', 'w+')
            arquivo.writelines(str(text_area[i].get(1.0,END)))
            arquivo.close()
     
    for i in range(3):
        
        label = Label(Cad_Conclusao, text = "CONCLUSÃO " + str(i+1),font=('arial', '14'), background='#1e3743', foreground='white')
        label.place(relx=0.01 , rely=(0.01 + 0.27*i) , relwidth=0.11, relheight=0.07)
        
        text_area.append(scrolledtext.ScrolledText(Cad_Conclusao, wrap=WORD, width=2, height=80, font=("Times New Roman", 15)))
        text_area[i].place(relx=(0.01), rely=(0.09 + 0.27*i), relwidth=0.98, relheight=0.17)

        text_area[i].focus()

    Cad_Conclusao.button = Button(Cad_Conclusao, text='Voltar', height=5, width=15, font=('arial', '9', 'bold'), command=Cad_Conclusao.destroy)
    Cad_Conclusao.button.place(relx=0.01, rely=0.9, relwidth=0.2, relheight=0.1)

    Cad_Conclusao.button = Button(Cad_Conclusao, text='Salvar', height=5, width=15, font=('arial', '9', 'bold'), command=lambda: SalvarConclusao(text_area))
    Cad_Conclusao.button.place(relx=0.79, rely=0.9, relwidth=0.2, relheight=0.1)
     
    # Display until closed manually.
    Cad_Conclusao.mainloop()
      

def Cad_Cabecalho(MenuCadastro): 
     
    Cad_Cabecalho = Toplevel(MenuCadastro)
    Cad_Cabecalho.title("Cadastro Cabeçalho")
    Cad_Cabecalho.geometry("900x500")
    Cad_Cabecalho.configure(borderwidth=8)
    Cad_Cabecalho.configure(background = '#1e3743')
    Cad_Cabecalho.minsize(width=900, height=500)
    Cad_Cabecalho.focus_force()
    Cad_Cabecalho.grab_set()

    def SalvarCabecalho(text_area):
        arquivo = open('cabecalho.txt', 'w+')
        arquivo.writelines(str(text_area.get(1.0,END)))
        arquivo.close()
     
    # Create label
    label = Label(Cad_Cabecalho, text = "CABEÇALHO ",font=('arial', '14'), background='#1e3743', foreground='white')
    label.place(relx=0.4, rely=0.01, relwidth=0.2, relheight=0.1)
     

    text_area = scrolledtext.ScrolledText(Cad_Cabecalho, wrap=WORD, width=40, height=8, font=("Times New Roman", 15))
    text_area.place(relx=0.01, rely=0.15, relwidth=0.99, relheight=0.7)
    text_area.focus()

    Cad_Cabecalho.button = Button(Cad_Cabecalho, text='Voltar', height=5, width=15, font=('arial', '9', 'bold'), command=Cad_Cabecalho.destroy)
    Cad_Cabecalho.button.place(relx=0.01, rely=0.9, relwidth=0.2, relheight=0.1)

    Cad_Cabecalho.button = Button(Cad_Cabecalho, text='Salvar', height=5, width=15, font=('arial', '9', 'bold'), command=lambda:SalvarCabecalho(text_area))
    Cad_Cabecalho.button.place(relx=0.79, rely=0.9, relwidth=0.2, relheight=0.1)

    # Display until closed manually.
    Cad_Cabecalho.mainloop()
      

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

    def Save_inputs(inputs):
        documentos = list()
        documentos = [str(docs.get()) + '\n' for docs in inputs]

        arquivo = open('documentos.txt', 'w+')
        arquivo.writelines(documentos)
        arquivo.close()
     
        print(documentos)
        

    for i in range(2):
        for j in range(8):
            Cad_Documentos.Label = Label(Cad_Documentos, text = ("Documento " + str((j+1)+(8*i))),font=('arial', '14'), background='#1e3743', foreground='white')
            Cad_Documentos.Label.place(relx=(0.001 + (i*0.51)), rely=(0.08 + (j*0.1)), relwidth=0.15, relheight=0.03)

            inputs.append(Entry(Cad_Documentos))
            inputs[j + (8*i)].place(relx=(0.01 + (i*0.51)), rely=(0.11 + (j*0.1)), relwidth=0.47, relheight=0.05)


    # Create label
    label = Label(Cad_Documentos, text = "POSSÍVEIS DOCUMENTOS",font=('arial', '14'), background='#1e3743', foreground='white')
    label.place(relx=0.35, rely=0, relwidth=0.3, relheight=0.05)


    Cad_Documentos.button = Button(Cad_Documentos, text='Voltar', height=5, width=15, font=('arial', '9', 'bold'), command=Cad_Documentos.destroy)
    Cad_Documentos.button.place(relx=0.01, rely=0.9, relwidth=0.2, relheight=0.1)

    Cad_Documentos.button = Button(Cad_Documentos, text='Salvar', height=5, width=15, font=('arial', '9', 'bold'), command=lambda:Save_inputs(inputs))
    Cad_Documentos.button.place(relx=0.79, rely=0.9, relwidth=0.2, relheight=0.1)

    # Display until closed manually.
    Cad_Documentos.mainloop()
      

def Cad_Pericial(MenuCadastro):
    Cad_Pericial = Toplevel(MenuCadastro)
    Cad_Pericial.title("Cadastro de Perguntas")
    Cad_Pericial.geometry("700x700")
    Cad_Pericial.configure(borderwidth=8)
    Cad_Pericial.configure(background = '#1e3743')
    Cad_Pericial.minsize(width=700, height=700)
    Cad_Pericial.focus_force()
    Cad_Pericial.grab_set()

    inputs = list()

    def Save_inputs(inputs):
        perguntas = list()
        perguntas = [str(docs.get()) + "\n" for docs in inputs]

        arquivo = open('PerguntasPericial.txt', 'w+')
        arquivo.writelines(perguntas)
        arquivo.close()
        
    for i in range(5):
        Cad_Pericial.Label = Label(Cad_Pericial, text = ("Pergunta " + str(i+1)),font=('arial', '14'), background='#1e3743', foreground='white')
        Cad_Pericial.Label.place(relx=0.01, rely=(i*0.15 + 0.08), relwidth=0.20, relheight=0.03)

        inputs.append(Entry(Cad_Pericial))
        inputs[i].place(relx=0.01 , rely=(0.12 + (i*0.15)), relwidth=0.98, relheight=0.05)


    # Create label
    label = Label(Cad_Pericial, text = "PROVA PERICIAL",font=('arial', '14'), background='#1e3743', foreground='white')
    label.place(relx=0.35, rely=0, relwidth=0.3, relheight=0.05)


    Cad_Pericial.button = Button(Cad_Pericial, text='Voltar', height=5, width=15, font=('arial', '9', 'bold'), command=Cad_Pericial.destroy)
    Cad_Pericial.button.place(relx=0.01, rely=0.9, relwidth=0.2, relheight=0.1)

    Cad_Pericial.button = Button(Cad_Pericial, text='Salvar', height=5, width=15, font=('arial', '9', 'bold'), command=lambda:Save_inputs(inputs))
    Cad_Pericial.button.place(relx=0.79, rely=0.9, relwidth=0.2, relheight=0.1)

    # Display until closed manually.
    Cad_Pericial.mainloop()


def Cad_Testemunhal(MenuCadastro):
    Cad_Testemunhal = Toplevel(MenuCadastro)
    Cad_Testemunhal.title("Cadastro de Documentos")
    Cad_Testemunhal.geometry("700x700")
    Cad_Testemunhal.configure(borderwidth=8)
    Cad_Testemunhal.configure(background = '#1e3743')
    Cad_Testemunhal.minsize(width=700, height=700)
    Cad_Testemunhal.focus_force()
    Cad_Testemunhal.grab_set()

    inputs = list()

    def Save_inputs(inputs):
        perguntas = list()
        perguntas = [str(docs.get()) + "\n" for docs in inputs]

        arquivo = open('PerguntasTestemunhal.txt', 'w+')
        arquivo.writelines(perguntas)
        arquivo.close()
        
    for i in range(5):
        Cad_Testemunhal.Label = Label(Cad_Testemunhal, text = ("Pergunta " + str(i+1)),font=('arial', '14'), background='#1e3743', foreground='white')
        Cad_Testemunhal.Label.place(relx=0.01, rely=(i*0.15 + 0.08), relwidth=0.20, relheight=0.03)

        inputs.append(Entry(Cad_Testemunhal))
        inputs[i].place(relx=0.01 , rely=(0.12 + (i*0.15)), relwidth=0.98, relheight=0.05)


    # Create label
    label = Label(Cad_Testemunhal, text = "PROVA TESTEMUNHAL",font=('arial', '14'), background='#1e3743', foreground='white')
    label.place(relx=0.35, rely=0, relwidth=0.35, relheight=0.05)


    Cad_Testemunhal.button = Button(Cad_Testemunhal, text='Voltar', height=5, width=15, font=('arial', '9', 'bold'), command=Cad_Testemunhal.destroy)
    Cad_Testemunhal.button.place(relx=0.01, rely=0.9, relwidth=0.2, relheight=0.1)

    Cad_Testemunhal.button = Button(Cad_Testemunhal, text='Salvar', height=5, width=15, font=('arial', '9', 'bold'), command=lambda: Save_inputs(inputs))
    Cad_Testemunhal.button.place(relx=0.79, rely=0.9, relwidth=0.2, relheight=0.1)

    # Display until closed manually.
    Cad_Testemunhal.mainloop()


def Ana_documentos(MenuAnalise):
    AnaliseHanna = Toplevel(MenuAnalise)
    AnaliseHanna.title("ANÁLISE DE DOCUMENTOS")
    AnaliseHanna.geometry("900x700")
    AnaliseHanna.configure(borderwidth=8)
    AnaliseHanna.configure(background = '#1e3743')
    AnaliseHanna.minsize(width=900, height=700)
    AnaliseHanna.focus_force()
    AnaliseHanna.grab_set()
    ans = list()

    k = 0
    acabou = False

    def LendoDocumentos():
        try:
            arquivo = open('documentos.txt', 'r')
            linhas = arquivo.readlines()
            documentos = list()

            for linha in linhas:
                if linha != '\n':
                    documentos.append(linha)

            return documentos

        except Exception as e:
            print(e)
            pass


    def SalvandoEntradas(checks):
        n_checks = len(checks)

        for i in range(n_checks):
            ans.append(checks[i].get())
        
        Save_inputs(ans)
        

    def Save_inputs(inputs):
        documentos = LendoDocumentos()
        respostas = list()
        
        for i in range(len(inputs)):
            if inputs[i] == 1:
                respostas.append(documentos[i])


        arquivo = open('documentosApresentados.txt', 'w+')
        arquivo.writelines(respostas)
        arquivo.close()
     
        print(respostas)

    documentos = LendoDocumentos()
    print(documentos)
    ndoc = len(documentos)

    checkvar = list()
    checkbutton = list()

    AnaliseHanna.Label = Label(AnaliseHanna, text = ("Marque os documentos que forão apresentados"),font=('arial', '12'), background='#1e3743', foreground='green')
    AnaliseHanna.Label.place(relx=0.05, rely=0.03, relwidth=0.4, relheight=0.06)

    for i in range(8):
        for j in range(2):
            AnaliseHanna.Label = Label(AnaliseHanna, text = (documentos[k]), font=('arial', '10'), background='#1e3743', foreground='white')
            AnaliseHanna.Label.place(relx=(0.05 + (j*0.46)), rely=(0.1 + (i*0.1)), relwidth=0.4, relheight=0.06)

            checkvar.append(IntVar())
            checkvar[j + (2*i)].set(0)

            checkbutton.append(Checkbutton(AnaliseHanna, variable = checkvar[j + (2*i)]))
            checkbutton[j + (2*i)].place(relx=(0.46 + (j*0.46)), rely=(0.1 + (i*0.1)), relwidth=0.03, relheight=0.03)
            k = k+1

            if k == ndoc:
                acabou = True
                break

        if acabou:
            break

    label = Label(AnaliseHanna, text = "ANÁLISE DE DOCUMENTOS",font=('arial', '14'), background='#1e3743', foreground='white')
    label.place(relx=0.35, rely=0, relwidth=0.3, relheight=0.05)


    AnaliseHanna.button = Button(AnaliseHanna, text='Voltar', height=5, width=15, font=('arial', '9', 'bold'), command=AnaliseHanna.destroy)
    AnaliseHanna.button.place(relx=0.01, rely=0.9, relwidth=0.2, relheight=0.1)

    AnaliseHanna.button = Button(AnaliseHanna, text='Salvar', height=5, width=15, font=('arial', '9', 'bold'), command=lambda:SalvandoEntradas(checkvar))
    AnaliseHanna.button.place(relx=0.79, rely=0.9, relwidth=0.2, relheight=0.1)

    # Display until closed manually.
    AnaliseHanna.mainloop()


def Ana_Pericial(MenuAnalise):
    Ana_Pericial = Toplevel(MenuAnalise)
    Ana_Pericial.title("Cadastro de Perguntas")
    Ana_Pericial.geometry("1000x700")
    Ana_Pericial.configure(borderwidth=8)
    Ana_Pericial.configure(background = '#1e3743')
    Ana_Pericial.minsize(width=700, height=700)
    Ana_Pericial.focus_force()
    Ana_Pericial.grab_set()

    checkbutton = list()
    checkvar = list()

    k=0

    def SalvandoEntradas(checks):
        n_checks = len(checks)
        ans = list()

        for i in range(n_checks):
            ans.append(checks[i].get())

    def LendoDocumentos():
        try:
            arquivo = open('PerguntasPericial.txt', 'r')
            linhas = arquivo.readlines()
            documentos = list()

            for linha in linhas:
                if linha != '\n':
                    documentos.append(linha)

            return documentos

        except Exception as e:
            print(e)
            pass
        
    documentos = LendoDocumentos()
    ndoc = len(documentos)

    for i in range(5):
        Ana_Pericial.Label = Label(Ana_Pericial, text = (documentos[k]),font=('arial', '14'), background='#1e3743', foreground='white')
        Ana_Pericial.Label.place(relx=0.01, rely=(i*0.15 + 0.08), relwidth=0.16, relheight=0.04)

        checkvar.append(IntVar())
        checkvar[i].set(0)

        checkbutton.append(Checkbutton(Ana_Pericial, variable = checkvar[i]))
        checkbutton[i].place(relx=(0.05), rely=(0.13 + (i*0.15)), relwidth=0.03, relheight=0.03)
        k = k+1
        if k == ndoc:
            break

    # Create label
    label = Label(Ana_Pericial, text = "PROVA PERICIAL",font=('arial', '14'), background='#1e3743', foreground='white')
    label.place(relx=0.35, rely=0, relwidth=0.3, relheight=0.05)


    Ana_Pericial.button = Button(Ana_Pericial, text='Voltar', height=5, width=15, font=('arial', '9', 'bold'), command=Ana_Pericial.destroy)
    Ana_Pericial.button.place(relx=0.01, rely=0.9, relwidth=0.2, relheight=0.1)

    Ana_Pericial.button = Button(Ana_Pericial, text='Salvar', height=5, width=15, font=('arial', '9', 'bold'), command=lambda:SalvandoEntradas(checkvar))
    Ana_Pericial.button.place(relx=0.79, rely=0.9, relwidth=0.2, relheight=0.1)

    # Display until closed manually.
    Ana_Pericial.mainloop()


def Ana_Testemunhal(MenuAnalise):
    Ana_Testemunhal = Toplevel(MenuAnalise)
    Ana_Testemunhal.title("Cadastro de Perguntas")
    Ana_Testemunhal.geometry("1000x700")
    Ana_Testemunhal.configure(borderwidth=8)
    Ana_Testemunhal.configure(background = '#1e3743')
    Ana_Testemunhal.minsize(width=700, height=700)
    Ana_Testemunhal.focus_force()
    Ana_Testemunhal.grab_set()

    checkbutton = list()
    checkvar = list()

    k = 0

    def LendoDocumentos():
        try:
            arquivo = open('PerguntasTestemunhal.txt', 'r')
            linhas = arquivo.readlines()
            documentos = list()

            for linha in linhas:
                if linha != '\n':
                    documentos.append(linha)

            return documentos

        except Exception as e:
            print(e)
            pass

    documentos = LendoDocumentos()
    ndoc = len(documentos)

    for i in range(5):
        Ana_Testemunhal.Label = Label(Ana_Testemunhal, text = (documentos[k]),font=('arial', '14'), background='#1e3743', foreground='white')
        Ana_Testemunhal.Label.place(relx=0.01, rely=(i*0.15 + 0.08), relwidth=0., relheight=0.04)

        checkvar.append(IntVar())
        checkvar[i].set(0)

        checkbutton.append(Checkbutton(Ana_Testemunhal, variable = checkvar[i]))
        checkbutton[i].place(relx=(0.05), rely=(0.13 + (i*0.15)), relwidth=0.03, relheight=0.03)
        k=k+1

        if k == ndoc:
            break

    label = Label(Ana_Testemunhal, text = "PROVA TESTEMUNHAL",font=('arial', '14'), background='#1e3743', foreground='white')
    label.place(relx=0.35, rely=0, relwidth=0.3, relheight=0.05)

    Ana_Testemunhal.button = Button(Ana_Testemunhal, text='Voltar', height=5, width=15, font=('arial', '9', 'bold'), command=Ana_Testemunhal.destroy)
    Ana_Testemunhal.button.place(relx=0.01, rely=0.9, relwidth=0.2, relheight=0.1)

    Ana_Testemunhal.button = Button(Ana_Testemunhal, text='Salvar', height=5, width=15, font=('arial', '9', 'bold'), command=Ana_Testemunhal.destroy)
    Ana_Testemunhal.button.place(relx=0.79, rely=0.9, relwidth=0.2, relheight=0.1)

    # Display until closed manually.
    Ana_Testemunhal.mainloop()


def Gerar_Minuta(MenuAnalise):
    Minuta = Toplevel(MenuAnalise)
    Minuta.title("Cadastro de Perguntas")
    Minuta.geometry("1000x700")
    Minuta.configure(borderwidth=8)
    Minuta.configure(background = '#1e3743')
    Minuta.minsize(width=700, height=700)
    Minuta.focus_force()
    Minuta.grab_set()


    def LendoDocumentos():

        doc_final = list()
        try:
            arquivo = open('documentosApresentados.txt', 'r')
            linhas = arquivo.readlines()
            documentos = list()

            for linha in linhas:
                if linha != '\n':
                    documentos.append(linha)

            arquivo.close()
            arquivo = open('cabecalho.txt')
            linhas = arquivo.readlines()
            cabecalho = list()

            for linha in linhas:
                if linha != '\n':
                    cabecalho.append(linha)
                
            arquivo.close()
            arquivo = open('conclusao1.txt')
            linhas = arquivo.readlines()
            conclusao = list()

            for linha in linhas:
                if linha != '\n':
                    conclusao.append(linha)

            doc_final.extend(cabecalho)
            doc_final.extend(documentos)
            doc_final.extend(conclusao)

            print(doc_final)

        except Exception as e:
            print(e)
            pass
    

    LendoDocumentos()
    
    Minuta.mainloop()


MainMenu()