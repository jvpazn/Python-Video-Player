import tkinter as tk
import vlc
from tkinter import filedialog
import platform
# Cria a instancia
instancia = vlc.Instance()

# Cria o objeto de midia
player = instancia.media_player_new()

#Procura um arquivo
def Procurarvideo():
    global player, instancia
    VideoID = filedialog.askopenfilename(
            title="Select a file",
        initialdir="/", 
        filetypes=(("Arquivos de vídeo", ("*.mp4", "*.mkv")), ("All files", "*.*"))
    )

    if not VideoID :
        pass
    else:
        media = instancia.media_new(VideoID)
        player.set_media(media)
        player.play()

# Cria a janela
janela_principal = tk.Tk()
janela_principal.title("Python Video Player")
janela_principal.geometry("1280x720")

#botao
btn = tk.Button(janela_principal, text="Procurar video", command=Procurarvideo, height=2)
btn.pack(side=tk.BOTTOM, fill=tk.X)

#Canvas Video
canvas = tk.Canvas(janela_principal, bg="black")
canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
# Funcionar em diferentes sistemas operacionais 
id_da_tela = canvas.winfo_id()

sistema = platform.system()

if sistema == "Windows":
    player.set_hwnd(id_da_tela)
elif sistema == "Linux":
    player.set_xwindow(id_da_tela)
elif sistema == "Darwin": # macOS
    player.set_nsobject(id_da_tela)


# Abre a janela
janela_principal.mainloop()