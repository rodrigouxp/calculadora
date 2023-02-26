# Importando as bibliotecas
from tkinter import *

# Inicialização da janela
root = Tk()
root.title('Calculadora')
root.geometry('406x355')
root.minsize(406,355)
root.maxsize(406,355)
root.configure(background='#282828')

# Globais
numero1 = ''
divide = FALSE
multiplica = FALSE
subtrai = FALSE
adiciona = FALSE



# Funções dos operadores
def botao_click(num):
    input.insert(END, num)
    return

def botao_divisao():
    global numero1
    global divide
    divide = TRUE
    numero1 = input.get()
    input.delete(0, END)

def botao_multiplicacao():
    global numero1
    global multiplica
    multiplica = TRUE
    numero1 = input.get()
    input.delete(0, END)

def botao_subtracao():
    global numero1
    global subtrai
    subtrai = TRUE
    numero1 = input.get()
    input.delete(0, END)

def botao_adicao():
    global numero1
    global adiciona
    adiciona = TRUE
    numero1 = input.get()
    input.delete(0, END)

def botao_limpa():
    global divide
    global multiplica
    global subtrai
    global adiciona
    divide = FALSE
    multiplica = FALSE
    subtrai = FALSE
    adiciona = FALSE
    input.delete(0, END)
    

def botao_igual():
    global divide
    global multiplica
    global subtrai
    global adiciona
    numero2 = input.get()
    input.delete(0, END)
    if divide == TRUE:
        input.insert(0, int(numero1) / int(numero2))
        divide == FALSE
    if multiplica == TRUE:
        input.insert(0, int(numero1) * int(numero2))
        multiplica == FALSE
    if subtrai == TRUE:
        input.insert(0, int(numero1) - int(numero2))
        subtrai == FALSE
    if adiciona == TRUE:
        input.insert(0, int(numero1) + int(numero2))
        adiciona == FALSE
    




# Top
# Input
input = Entry(root, 
                width=14, 
                borderwidth=2, 
                relief=FLAT, 
                fg='#FFFFFF', 
                bg='#a7a28f', 
                font=('courier', 25, 'bold'), 
                justify=CENTER
                )
input.grid(
    row=0,
    column=0,
    columnspan=4,
    padx=2,
    pady=2
)

divisao = Button(root,
                 text='÷',
                 padx=40,
                 pady=20,
                 command=botao_divisao,
                 fg='#FFFFFF',
                 activeforeground='#FFFFFF',
                 bg='#320064',
                 activebackground='#240046',
                 relief=FLAT,
                 font=('courier', 12, 'bold'),
                 )
divisao.grid(row=0, column=4)


# Primeira fileira
sete = Button(root,
                text='7',
                padx=40,
                pady=20,
                command=lambda: botao_click(7),
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('courier', 12, 'bold'),
                )
sete.grid(row=1, column=1)

oito = Button(root,
            text='8',
            padx=40,
            pady=20,
            command=lambda: botao_click(8),
            fg='#FFFFFF',
            activeforeground='#FFFFFF',
            bg='#320064',
            activebackground='#240046',
            relief=FLAT,
            font=('courier', 12, 'bold'),
            )
oito.grid(row=1, column=2)

nove = Button(root,
            text='9',
            padx=40,
            pady=20,
            command=lambda: botao_click(9),
            fg='#FFFFFF',
            activeforeground='#FFFFFF',
            bg='#320064',
            activebackground='#240046',
            relief=FLAT,
            font=('courier', 12, 'bold'),
            )
nove.grid(row=1, column=3)

multiplicacao = Button(root,
                       text='x',
                       padx=40,
                       pady=20,
                       command=botao_multiplicacao,
                       fg='#FFFFFF',
                       activeforeground='#FFFFFF',
                       bg='#320064',
                       activebackground='#240046',
                       relief=FLAT,
                       font=('courier', 12, 'bold'),
                       )
multiplicacao.grid(row=1, column=4)


# Segunda fileira
quatro = Button(root,
                text='4',
                padx=40,
                pady=20,
                command=lambda: botao_click(4),
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('courier', 12, 'bold'),
                )
quatro.grid(row=2, column=1)

cinco = Button(root,
            text='5',
            padx=40,
            pady=20,
            command=lambda: botao_click(5),
            fg='#FFFFFF',
            activeforeground='#FFFFFF',
            bg='#320064',
            activebackground='#240046',
            relief=FLAT,
            font=('courier', 12, 'bold'),
            )
cinco.grid(row=2, column=2)

seis = Button(root,
            text='6',
            padx=40,
            pady=20,
            command=lambda: botao_click(6),
            fg='#FFFFFF',
            activeforeground='#FFFFFF',
            bg='#320064',
            activebackground='#240046',
            relief=FLAT,
            font=('courier', 12, 'bold'),
            )
seis.grid(row=2, column=3)

subtracao = Button(root,
                   text='-',
                   padx=40,
                   pady=20,
                   command=botao_subtracao,
                   fg='#FFFFFF',
                   activeforeground='#FFFFFF',
                   bg='#320064',
                   activebackground='#240046',
                   relief=FLAT,
                   font=('courier', 12, 'bold'),
                   )
subtracao.grid(row=2, column=4)

# Terceira fileira
um = Button(root,
            text='1',
            padx=40,
            pady=20,
            command=lambda: botao_click(1),
            fg='#FFFFFF',
            activeforeground='#FFFFFF',
            bg='#320064',
            activebackground='#240046',
            relief=FLAT,
            font=('courier', 12, 'bold'),
            )
um.grid(row=3, column=1)

dois = Button(root,
            text='2',
            padx=40,
            pady=20,
            command=lambda: botao_click(2),
            fg='#FFFFFF',
            activeforeground='#FFFFFF',
            bg='#320064',
            activebackground='#240046',
            relief=FLAT,
            font=('courier', 12, 'bold'),
            )
dois.grid(row=3, column=2)

tres = Button(root,
            text='3',
            padx=40,
            pady=20,
            command=lambda: botao_click(3),
            fg='#FFFFFF',
            activeforeground='#FFFFFF',
            bg='#320064',
            activebackground='#240046',
            relief=FLAT,
            font=('courier', 12, 'bold'),
            )
tres.grid(row=3, column=3)

adicao = Button(root,
                   text='+',
                   padx=40,
                   pady=20,
                   command=botao_adicao,
                   fg='#FFFFFF',
                   activeforeground='#FFFFFF',
                   bg='#320064',
                   activebackground='#240046',
                   relief=FLAT,
                   font=('courier', 12, 'bold'),
                   )
adicao.grid(row=3, column=4)

# Quarta fileira
zero = Button(root,
            text='0',
            padx=91.5,
            pady=20,
            command=lambda: botao_click(0),
            fg='#FFFFFF',
            activeforeground='#FFFFFF',
            bg='#320064',
            activebackground='#240046',
            relief=FLAT,
            font=('courier', 12, 'bold'),
            )
zero.grid(row=4, column=1, columnspan=2)

limpa = Button(root,
                   text='C',
                   padx=40,
                   pady=20,
                   command=botao_limpa,
                   fg='#FFFFFF',
                   activeforeground='#FFFFFF',
                   bg='#320064',
                   activebackground='#240046',
                   relief=FLAT,
                   font=('courier', 12, 'bold'),
                   )
limpa.grid(row=4, column=3)

igual = Button(root,
                   text='=',
                   padx=40,
                   pady=20,
                   command=botao_igual,
                   fg='#FFFFFF',
                   activeforeground='#FFFFFF',
                   bg='#320064',
                   activebackground='#240046',
                   relief=FLAT,
                   font=('courier', 12, 'bold'),
                   )
igual.grid(row=4, column=4)



# Loop para a janela continuar aberta enquanto espera alguma ação do usuário
root.mainloop()