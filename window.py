import tkinter as tk
from tkinter import ttk
import json
import tkinter.messagebox as messagebox
import subprocess
import html


def addBulletPoint():
    newItem = {
        'title': entryTitle.get(),
        # Escapar HTML e substituir quebras de linha por <br>
        'description': html.escape(entryDescription.get("1.0", tk.END)).replace('\n', '<br>'),
        'image': entryImage.get()
    }

    with open('data.json', 'r+', encoding='utf-8') as f:
        data = json.load(f)
        data['bulletPoints'].append(newItem)
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()

    entryTitle.delete(0, tk.END)
    entryDescription.delete("1.0", tk.END)  # Limpar o Text
    entryImage.delete(0, tk.END)

    messagebox.showinfo(
        "Sucesso", "Conteúdo inserido no arquivo JSON com sucesso!")


def callGenerateNewsletterScript():
    try:
        subprocess.run(["python", "generate.py"], check=True)
        messagebox.showinfo("Sucesso", "Newsletter gerada com sucesso!")
    except subprocess.CalledProcessError as e:
        messagebox.showerror(
            "Erro", f"Ocorreu um erro ao gerar a newsletter: {e}")


window = tk.Tk()
window.title("mth-create newsletter")

labelTitle = ttk.Label(window, text="Title:")
labelTitle.pack()

entryTitle = ttk.Entry(window)
entryTitle.pack()

labelDescription = ttk.Label(window, text="Description:")
labelDescription.pack()

entryDescription = tk.Text(window, height=5)
entryDescription.pack()

labelImage = ttk.Label(window, text="Image:")
labelImage.pack()

entryImage = ttk.Entry(window)
entryImage.pack()


buttonAdd = ttk.Button(window, text="Add to stack", command=addBulletPoint)
buttonAdd.pack(side=tk.LEFT)

buttonGenerate = ttk.Button(
    window, text="Generate newsletter", command=callGenerateNewsletterScript)
buttonGenerate.pack(side=tk.RIGHT)

window.mainloop()
