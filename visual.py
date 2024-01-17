from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import base64
root = Tk()
def rgb_hack(rgb):
    return "#%02x%02x%02x" % rgb




# название сам придумай
root.geometry('500x500')
root.title(' ')
root.attributes("-fullscreen", False)
root.maxsize(500,500)

# тут я скипнул диапозон а то его сложно впихнуть и уж думаю его и так понятно
canvas = Canvas(root, height= 500,width=500,borderwidth=2, relief="ridge",bg=rgb_hack((112,128,144)))
canvas.create_text(250,20,anchor=CENTER,text='Введите IP-адресс узла и префикс:',font=('Comic Sans MS','10'))
canvas.create_text(250,125,anchor=CENTER,text='Маска (двоичная):',font=('Comic Sans MS','10'))
canvas.create_text(250,75,anchor=CENTER,text='IP-адресс узла (двоичная):',font=('Comic Sans MS','10'))
canvas.create_text(250,175,anchor=CENTER,text='Номер сети (двоичная):',font=('Comic Sans MS','10'))
canvas.create_text(250,225,anchor=CENTER,text='Широковещательный IP-адрес в сети (двоичная):',font=('Comic Sans MS','10'))
canvas.create_text(125,275,anchor=CENTER,text='IP-адресс узла:',font=('Comic Sans MS','10'))
canvas.create_text(375,275,anchor=CENTER,text='Маска:',font=('Comic Sans MS','10'))
canvas.create_text(125,325,anchor=CENTER,text='Номер сети:',font=('Comic Sans MS','10'))
canvas.create_text(375,325,anchor=CENTER,text='Широковещательный:',font=('Comic Sans MS','10'))
canvas.create_text(125,375,anchor=CENTER,text='Адрес первого узла:',font=('Comic Sans MS','10'))
canvas.create_text(375,375,anchor=CENTER,text='Адрес последнего узла:',font=('Comic Sans MS','10'))
canvas.create_text(125,425,anchor=CENTER,text='количество адресов:',font=('Comic Sans MS','10'))
canvas.pack()


frame = Frame(root,bg=rgb_hack((176,196,222)),borderwidth=3,relief="ridge")
frame.place(relx=0.5, rely=0.1,anchor=CENTER, relwidth=0.8, relheight=0.05)
frame2 = Frame(root,bg=rgb_hack((176,196,222)),borderwidth=3,relief="ridge")
frame2.place(relx=0.5, rely=0.2,anchor=CENTER, relwidth=0.8, relheight=0.05)
frame3 = Frame(root,bg=rgb_hack((176,196,222)),borderwidth=3,relief="ridge")
frame3.place(relx=0.5, rely=0.3,anchor=CENTER, relwidth=0.8, relheight=0.05)
frame4 = Frame(root,bg=rgb_hack((176,196,222)),borderwidth=3,relief="ridge")
frame4.place(relx=0.5, rely=0.4,anchor=CENTER, relwidth=0.8, relheight=0.05)
frame5 = Frame(root,bg=rgb_hack((176,196,222)),borderwidth=3,relief="ridge")
frame5.place(relx=0.5, rely=0.5,anchor=CENTER, relwidth=0.8, relheight=0.05)
frame6 = Frame(root,bg=rgb_hack((176,196,222)),borderwidth=3,relief="ridge")
frame6.place(relx=0.25, rely=0.6,anchor=CENTER, relwidth=0.3, relheight=0.05)
frame7 = Frame(root,bg=rgb_hack((176,196,222)),borderwidth=3,relief="ridge")
frame7.place(relx=0.75, rely=0.6,anchor=CENTER, relwidth=0.3, relheight=0.05)
frame8 = Frame(root,bg=rgb_hack((176,196,222)),borderwidth=3,relief="ridge")
frame8.place(relx=0.25, rely=0.7,anchor=CENTER, relwidth=0.3, relheight=0.05)
frame9 = Frame(root,bg=rgb_hack((176,196,222)),borderwidth=3,relief="ridge")
frame9.place(relx=0.75, rely=0.7,anchor=CENTER, relwidth=0.3, relheight=0.05)
frame10 = Frame(root,bg=rgb_hack((176,196,222)),borderwidth=3,relief="ridge")
frame10.place(relx=0.25, rely=0.8,anchor=CENTER, relwidth=0.3, relheight=0.05)
frame11 = Frame(root,bg=rgb_hack((176,196,222)),borderwidth=3,relief="ridge")
frame11.place(relx=0.75, rely=0.8,anchor=CENTER, relwidth=0.3, relheight=0.05)
frame12 = Frame(root,bg=rgb_hack((176,196,222)),borderwidth=3,relief="ridge")
frame12.place(relx=0.25, rely=0.9,anchor=CENTER, relwidth=0.3, relheight=0.05)
frame13 = Frame(root,bg=rgb_hack((176,196,222)),borderwidth=3,relief="ridge")
frame13.place(relx=0.75, rely=0.9,anchor=CENTER, relwidth=0.3, relheight=0.05)

# вместо текста будет textvariable по расчитаному тобой 
loginInput = Entry(frame,bg=rgb_hack((176,196,222)),width=50,font=('Comic Sans MS','10'))
ip2lable = ttk.Label(frame2,background=rgb_hack((176,196,222)),width=100,font=('Comic Sans MS','10'),text="255.255.255.255",)
maska2lable=ttk.Label(frame3,background=rgb_hack((176,196,222)),width=100,font=('Comic Sans MS','10'),text="255.255.255.255")
nomerseti2lable=ttk.Label(frame4,background=rgb_hack((176,196,222)),width=100,font=('Comic Sans MS','10'),text="255.255.255.255")
shiroko2lable=ttk.Label(frame5,background=rgb_hack((176,196,222)),width=100,font=('Comic Sans MS','10'),text="255.255.255.255")
iplable=ttk.Label(frame6,background=rgb_hack((176,196,222)),width=100,font=('Comic Sans MS','10'),text="255.255.255.255")
maskalable=ttk.Label(frame7,background=rgb_hack((176,196,222)),width=100,font=('Comic Sans MS','10'),text="255.255.255.255")
nomersetilable=ttk.Label(frame8,background=rgb_hack((176,196,222)),width=100,font=('Comic Sans MS','10'),text="255.255.255.255")
shirokolable=ttk.Label(frame9,background=rgb_hack((176,196,222)),width=100,font=('Comic Sans MS','10'),text="255.255.255.255")
adr1lable=ttk.Label(frame10,background=rgb_hack((176,196,222)),width=100,font=('Comic Sans MS','10'),text="255.255.255.255")
adr2lable=ttk.Label(frame11,background=rgb_hack((176,196,222)),width=100,font=('Comic Sans MS','10'),text="255.255.255.255")
coladrlable=ttk.Label(frame12,background=rgb_hack((176,196,222)),width=100,font=('Comic Sans MS','10'),text="255.255.255.255")
ip2lable.pack()
loginInput.pack()
maska2lable.pack()
nomerseti2lable.pack()
shiroko2lable.pack()
iplable.pack()
maskalable.pack()
nomersetilable.pack()
shirokolable.pack()
adr1lable.pack()
adr2lable.pack()
coladrlable.pack()

# ну тут функция для вычесления
btn = Button(frame13, text = "Выполнить",background=rgb_hack((176,196,222)) )
btn.pack(fill=X)

root.mainloop()