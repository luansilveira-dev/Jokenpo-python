from tkinter import * 
from tkinter import ttk, messagebox
import random
from PIL import Image, ImageTk

branco = '#FBFBF2'
laranja = '#E3884E'
vermelho = '#AB0A2A'
roxo_escuro = '#27032A'
size_geral = largura_img, altura_img = 370, 520
pontos_player , pontos_bot = 0, 0
vitoria_player, vitoria_bot = 0, 0


janela = Tk()
janela.title('')
janela.iconbitmap('img\jokenpo.ico')
janela.geometry('1075x650')
janela.configure(background=branco)
janela.resizable(width=FALSE, height=FALSE)
style = ttk.Style(janela).theme_use('clam')



def op_bot():
    global image, bot
    lista = ['pedra', 'papel','tesoura']
    bot = random.randint(0,2)
    image = Image.open(f'img/ktzm/{lista[bot]}.png').resize((size_geral))
    image = ImageTk.PhotoImage(image)
    Label(janela, image=image, text='Bot'.upper(), font='Ivy 16 bold' , compound='top', bg=branco, fg=roxo_escuro).place(x=620, y=-100)
    return bot

def pedra():
    global image_pedra, pontos_player, pontos_bot
    image_pedra = Image.open(f'img/jdrhz/pedra.png').resize((size_geral))
    image_pedra = ImageTk.PhotoImage(image_pedra)
    Label(janela, image=image_pedra,text='Você'.upper(), font='Ivy 16 bold', compound='top', bg=branco, fg=roxo_escuro).place(x=100, y=-100)
    op_bot()
    if bot == 0:
        ...
    elif bot == 1:
        pontos_bot += 1
    else:
        pontos_player += 1
        
    pontuacao()
        
def papel():
    global image_papel, pontos_player, pontos_bot
    image_papel = Image.open(f'img/jdrhz/papel.png').resize((size_geral))
    image_papel = ImageTk.PhotoImage(image_papel)
    Label(janela, image=image_papel,text='Você'.upper(), font='Ivy 16 bold', compound='top', bg=branco, fg=roxo_escuro).place(x=100, y=-100)
    op_bot()
    if bot == 0:
        pontos_player += 1
    elif bot == 1:
        ...
    else:
        pontos_bot += 1
    pontuacao()
    
def tesoura():
    global image_tesoura, pontos_player, pontos_bot
    image_tesoura = Image.open(f'img/jdrhz/tesoura.png').resize((size_geral))
    image_tesoura = ImageTk.PhotoImage(image_tesoura)
    Label(janela, image=image_tesoura,text='Você'.upper(), font='Ivy 16 bold', compound='top', bg=branco, fg=roxo_escuro).place(x=100, y=-100)
    op_bot()
    if bot == 0:
        pontos_bot += 1
    elif bot == 1:
        pontos_player += 1
    else:
        ...
    pontuacao()
    
def pontuacao():
    global pontos_player, pontos_bot, vitoria_bot, vitoria_player
    
    
    if pontos_player == 10:
        messagebox.showinfo('','            Você Ganhou!            '.upper()) 
        pontos_bot -= pontos_bot
        pontos_player -= pontos_player
        vitoria_player += 1
    elif pontos_bot == 10:
        messagebox.showerror('','            você perdeu            '.upper())
        pontos_bot -= pontos_bot
        pontos_player -= pontos_player
        vitoria_bot += 1
    
    Label(janela, text=f'Vitória: {vitoria_player}', font='Ivy 16 bold', fg=vermelho, bg=branco).place(x=20, y=50)
    Label(janela, text=f'Vitória: {vitoria_bot}', font='Ivy 16 bold', fg=vermelho, bg=branco).place(x=950, y=50)
    
    Label(janela, text=f'{pontos_player} - {pontos_bot}', font='Ivy 20 bold', fg=roxo_escuro, bg=branco).place(x=520, y=100) 
    
    if vitoria_player == 10 : 
        messagebox.showinfo('','      Vitória      '.upper()) 
        janela.destroy()
    
    elif vitoria_bot == 10:
        messagebox.showerror('','            Vitória para o Bot            '.upper())
        janela.destroy()
pontuacao()
## Vs - Pontos

Label(janela, text='Vs', font='Ivy 60 bold', fg=roxo_escuro, bg=branco).place(x=500, y=200)

## Nome dos desputadores 

# Criando botôes 
Button(janela, command=pedra, text='Pedra'.upper(), width=15 ,font='Ivy 20 bold',bg=laranja, fg=branco, relief='groove').place(x=150,y=505)
Button(janela, command=papel, text='Papel'.upper(), width=15 ,font='Ivy 20 bold',bg=laranja, fg=branco, relief='groove').place(x=435,y=505)
Button(janela, command=tesoura, text='Tesoura'.upper(), width=15 ,font='Ivy 20 bold',bg=laranja, fg=branco, relief='groove').place(x=720,y=505)

Label(janela, text='Você'.upper(), font='Ivy 20 bold', bg=branco, fg=roxo_escuro).place(x=200, y=220)
Label(janela, text='bot'.upper(), font='Ivy 20 bold', bg=branco, fg=roxo_escuro).place(x=780, y=220)

janela.mainloop()