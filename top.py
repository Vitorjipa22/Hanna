from tkinter import *
from tkinter import scrolledtext

def MainMenu():
    root = Tk() 

    root.geometry("450x300") 
    root.title('Hanna')
    root.geometry('300x200')
    root.configure(borderwidth=8)
    root.configure(background = '#1e3743')
    root.minsize(width=450, height=300)

    def handle_event(event):
        btn_name = event.widget.cget('text')
        if btn_name == "Hanna Cadastro":
            MenuCadastro(root)
        if btn_name.endswith('Hanna Análise'):
            pass
 
    for name in ("Hanna Cadastro", "Hanna Análise"):
        root.button = Button(root, text=name, height=5, width=15, font=('arial', '9', 'bold'))
        root.button.bind("<Button-1>", handle_event)
        root.button.pack(side='left', fill='x', expand=True)


    root.mainloop() 
    # root.pack(fill='both', expand=True)
    
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
     
    # Display until closed manually.
    Cad_Cabecalho.mainloop()
      

def MenuCadastro(root): 
     
    # Create widget
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
            pass
        if btn_name == 'Conclusão':
            pass
 

    for name in ("Cabeçalho", "Documentos", "Conclusão"):
        MenuCadastro.button = Button(MenuCadastro, text=name, height=5, width=15, font=('arial', '9', 'bold'))
        MenuCadastro.button.bind("<Button-1>", handle_event)
        MenuCadastro.button.pack(side='left', fill='x', expand=True)

    MenuCadastro.button = Button(MenuCadastro, text='Voltar', height=5, width=15, font=('arial', '9', 'bold'), command=MenuCadastro.destroy)
    MenuCadastro.button.place(relx=0.01, rely=0.9, relwidth=0.2, relheight=0.1)

    MenuCadastro.mainloop()
 

MainMenu()