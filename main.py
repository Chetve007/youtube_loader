from tkinter import *
import pytube
from tkinter import messagebox


root = Tk()
root.geometry("600x350")
root.resizable(False, False)

root.title("Леха крут!")

root.config(bg='#D3D3D3')


def download():
    try:
        ytlink = link1.get()
        youtubelink = pytube.YouTube(ytlink)
        video = youtubelink.streams.get_lowest_resolution()
        video.download()
        result = "Загрузка завершена"
        messagebox.showinfo("Готово", result)
    except Exception:
        result = "Ссылка не работает"
        messagebox.showerror("Ошибка", result)


def reset():
    link1.set("")


def exit_():
    root.destroy()


lb = Label(root, text="---Загрузка видео с YouTube---", font='Arial,15,bold', bg='#D3D3D3')
lb.pack(pady=15)

lb1 = Label(root, text="Ссылка на видео:", font='Arial,15,bold', bg='#D3D3D3')
lb1.place(x=10, y=80)

link1 = StringVar()
En1 = Entry(root, textvariable=link1, font='Arial,15,bold')
En1.place(x=230, y=80)

btn1 = Button(root, text="Скачать", font='Arial,10,bold', bd=4, command=download)
btn1.place(x=330, y=130)

btn2 = Button(root, text="Очистить", font='Arial,10,bold', bd=4, command=reset)
btn2.place(x=160, y=190)

btn3 = Button(root, text="Выход", font='Arial,10,bold', bd=4, command=exit_)
btn3.place(x=280, y=190)


root.mainloop()
