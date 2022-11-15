from metronomo import Metronomo
from threading import Thread
from tkinter import Tk
from tkinter import ttk
from time import sleep

# Funcoes
def add_metronomo(frame, bpm, vol, row_):
    global ativos, row

    # Instanciando objetos
    m = Metronomo(bpm, vol)
    t = Thread(target=m.beep)
    ativos.append(m)

    # Instanciando o frame do metronomo
    fr = ttk.Frame(frame)
    fr.grid(row=row_)

    # Adicionando o informativo
    ttk.Label(fr, text=str(bpm) + " BPM").grid(row=0, column=0)

    def destruct_func():
        index = ativos.index(m)
        m.setOn(False) # Termina a thread
        ativos.pop(index)
        fr.destroy()

    # Botao de destruir
    ttk.Button(fr, text="DESLIGAR", command=destruct_func).grid(row=0, column=1)

    row+=1
    t.start() # Iniciando a Thread

def sinc_metronomos():
    global ativos
    for i in ativos:
        i.setOn(False)
    
    sleep(1) # Para ser mais perceptivel o reinicio

    for i in ativos:
        i.setOn(True)
        Thread(target=i.beep).start()

def root_close():
    global ativos, root
    for m in ativos:
        m.setOn(False)
    
    root.destroy()

ativos = []

# Instancia da GUI
root = Tk()
root.geometry("615x500")
root.title("Metrônomo")

frm = ttk.Frame(root)
frm.grid()

row = 1 # Linha para adicionar o novo botao

# Criacao de novos metronomos

ttk.Label(frm, text="BPM / VOLUME").grid(column=0, row=0)
bpm_entry = ttk.Spinbox(frm, width=25, from_=1, to=300)
bpm_entry.grid(column=1, row=0)

vol_entry = ttk.Spinbox(frm, width=25, from_=1, to=10)
vol_entry.grid(column=2, row=0)

ttk.Button(frm, text="OK", command=lambda: add_metronomo(frm, int(bpm_entry.get()), int(vol_entry.get())/10, row)).grid(column=3, row=0)

# Sincronizacao dos metronomos
ttk.Button(frm, text="SINC", command=sinc_metronomos).grid(column=4, row=0)

root.protocol("WM_DELETE_WINDOW", root_close)
root.mainloop()