from tkinter import *
from tkinter import ttk
import ipaddress as ipa

root = Tk()


def click(event):
    ip2lable.config(text = ipabin())
    maska2lable.config(text=prefix())
    nomersetilable.config(text=ipa.ip_network(loginInput.get(),False))
    maskalable.config(text=net())
    nomerseti2lable.config(text=netipbin())
    shirokolable.config(text=shiro()) 
    shiroko2lable.config(text=shirobin())
    coladrlable.config(text=count())
    adr1lable.config(text=firsthost())
    adr2lable.config(text=lasthost())
    
def rgb_hack(rgb):
    return "#%02x%02x%02x" % rgb

def rgb_hock(gbr):
    frame.configure(bg=gbr)
    frame2.configure(bg=gbr)
    frame3.configure(bg=gbr)
    frame4.configure(bg=gbr)
    frame5.configure(bg=gbr)
    frame6.configure(bg=gbr)
    frame7.configure(bg=gbr)
    frame8.configure(bg=gbr)
    frame9.configure(bg=gbr)
    frame10.configure(bg=gbr)
    frame11.configure(bg=gbr)
    frame12.configure(bg=gbr)
    frame13.configure(bg=gbr)
    frame14.configure(bg=gbr)
    loginInput.configure(background=gbr)
    loginInput.configure(background=gbr)
    ip2lable.configure(background=gbr)
    maska2lable.configure(background=gbr)
    nomerseti2lable.configure(background=gbr)
    shiroko2lable.configure(background=gbr)
    maskalable.configure(background=gbr)
    nomersetilable.configure(background=gbr)
    shirokolable.configure(background=gbr)
    adr1lable.configure(background=gbr)
    adr2lable.configure(background=gbr)
    coladrlable.configure(background=gbr)
    btn.configure(background=gbr)
    btnt.configure(background=gbr)

def callbackTheme():
    # СИНИЙ ЦВЕТ
    if comboboxtheme.get() == "Blue/cyan":
        rgb_hock('#B0C4DE')
        canvas.configure(background=rgb_hack((112,128,144)))
    # СЕРЫЙ ЦВЕТ
    if comboboxtheme.get() == "Gray":
        canvas.configure(background=rgb_hack((131,131,131)))
        rgb_hock('#B2B2B2')
    # КРАСНЫЙ ЦВЕТ
    if comboboxtheme.get() == "Red":
        canvas.configure(background=rgb_hack((144,112,112)))
        rgb_hock('#FFCCCC')
    # ЗЕЛЁНЫЙ ЦВЕТ
    if comboboxtheme.get() == "Green":
        canvas.configure(background=rgb_hack((112,144,112)))
        rgb_hock('#CCFFCC')
    # БЕЛЫЙ ЦВЕТ
    if comboboxtheme.get() == "White":
        canvas.configure(background=rgb_hack((255,255,255)))
        rgb_hock('#FFFFFF')


def ipabin():
    binip=''
    ipr=loginInput.get()
    ind=ipr.index('/')
    ipn=ipr[:ind]
    for x in (ipn):
        iprs=str(ipn).split('.')

    for x in iprs:
        b=bin(int(x))[2:]
        ipoct=b[::-1]+'0'*(8-len(b))
        binip+=ipoct[::-1]+'.'
    return binip[:-1]

def prefix():
    ipr=loginInput.get()
    ind=ipr.index('/')+1
    ipm=ipr[ind:]
    mask='1'*int(ipm)+'0'*(32-int(ipm))
    bitmask=mask[:8]+'.'+mask[8:]
    bitmask=bitmask[:17]+'.'+bitmask[17:]
    bitmask=bitmask[:26]+'.'+bitmask[26:]
    return bitmask

def firsthost():
    ip=ipa.ip_network(loginInput.get(),False)
    c=0
    for addr in ip:
        ipf=addr
        c+=1
        if c==2:
            break
    return ipf

def lasthost():
    ip=ipa.ip_network(loginInput.get(),False)
    c=0
    for addr in ip:
        ipf=addr
        c+=1
        if c==count()+1:
            break
    return ipf

def count():
    net=ipa.IPv4Network(loginInput.get(),False)
    return net.num_addresses-2

def net():
    interface = ipa.IPv4Interface(loginInput.get())
    net=str(interface.with_netmask)
    ind=net.index('/')+1
    net=net[ind:]
    return net

def netipbin():
    mask=(str(ipa.ip_network(loginInput.get(),False)))
    ind=(mask).index('/')
    mask=mask[:ind]
    netbin=''
    for x in (mask):
        iprs=str(mask).split('.')
    for x in iprs:
        b=bin(int(x))[2:]
        ipoct=b[::-1]+'0'*(8-len(b))
        netbin+=ipoct[::-1]+'.'
    return netbin[:-1]

def shiro():
    ip=loginInput.get()
    ind=ip.index('/')
    ipn=ip[:ind]
    ips=ipa.IPv4Network(ipn+'/'+net(),False)
    return ips.broadcast_address

def shirobin():
    binip=''
    ipr=str(shiro())

    for x in (ipr):
        iprs=str(ipr).split('.')
    for x in iprs:
        b=bin(int(x))[2:]
        ipoct=b[::-1]+'0'*(8-len(b))
        binip+=ipoct[::-1]+'.'
    return binip[:-1]
    

# название сам придумай
root.geometry('500x500')
root.title('IP Calculator')
root.attributes("-fullscreen", False)
root.maxsize(500,500)

# тут я скипнул диапозон а то его сложно впихнуть и уж думаю его и так понятно
canvas = Canvas(root, height= 500,width=500,borderwidth=2, relief="ridge",bg=rgb_hack((112,128,144)))
canvas.create_text(250,20,anchor=CENTER,text='Введите IP-адресс узла и префикс:',font=('Comic Sans MS','10'))
canvas.create_text(250,125,anchor=CENTER,text='Маска (двоичная):',font=('Comic Sans MS','10'))
canvas.create_text(250,75,anchor=CENTER,text='IP-адресс узла (двоичная):',font=('Comic Sans MS','10'))
canvas.create_text(250,175,anchor=CENTER,text='Номер сети (двоичная):',font=('Comic Sans MS','10'))
canvas.create_text(250,225,anchor=CENTER,text='Широковещательный IP-адрес в сети (двоичная):',font=('Comic Sans MS','10'))
canvas.create_text(375,275,anchor=CENTER,text='Маска:',font=('Comic Sans MS','10'))
canvas.create_text(125,275,anchor=CENTER,text='Номер сети:',font=('Comic Sans MS','10'))
canvas.create_text(375,325,anchor=CENTER,text='Широковещательный:',font=('Comic Sans MS','10'))
canvas.create_text(125,325,anchor=CENTER,text='Адрес первого узла:',font=('Comic Sans MS','10'))
canvas.create_text(375,375,anchor=CENTER,text='Адрес последнего узла:',font=('Comic Sans MS','10'))
canvas.create_text(125,375,anchor=CENTER,text='количество адресов:',font=('Comic Sans MS','10'))
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
frame6= Frame(root,bg=rgb_hack((176,196,222)),borderwidth=3,relief="ridge")
frame6.place(relx=0.75, rely=0.9,anchor=CENTER, relwidth=0.3, relheight=0.05)
frame7 = Frame(root,bg=rgb_hack((176,196,222)),borderwidth=3,relief="ridge")
frame7.place(relx=0.75, rely=0.6,anchor=CENTER, relwidth=0.3, relheight=0.05)
frame8 = Frame(root,bg=rgb_hack((176,196,222)),borderwidth=3,relief="ridge")
frame8.place(relx=0.25, rely=0.6,anchor=CENTER, relwidth=0.3, relheight=0.05)
frame9 = Frame(root,bg=rgb_hack((176,196,222)),borderwidth=3,relief="ridge")
frame9.place(relx=0.75, rely=0.7,anchor=CENTER, relwidth=0.3, relheight=0.05)
frame10 = Frame(root,bg=rgb_hack((176,196,222)),borderwidth=3,relief="ridge")
frame10.place(relx=0.25, rely=0.7,anchor=CENTER, relwidth=0.3, relheight=0.05)
frame11 = Frame(root,bg=rgb_hack((176,196,222)),borderwidth=3,relief="ridge")
frame11.place(relx=0.75, rely=0.8,anchor=CENTER, relwidth=0.3, relheight=0.05)
frame12 = Frame(root,bg=rgb_hack((176,196,222)),borderwidth=3,relief="ridge")
frame12.place(relx=0.25, rely=0.8,anchor=CENTER, relwidth=0.3, relheight=0.05)
frame13 = Frame(root,bg=rgb_hack((176,196,222)),borderwidth=3,relief="ridge")
frame13.place(relx=0.25, rely=0.9,anchor=CENTER, relwidth=0.3, relheight=0.05)
frame14 = Frame(root,bg=rgb_hack((176,196,222)),borderwidth=3,relief="ridge")
frame14.place(relx=0.75, rely=0.95,anchor=CENTER, relwidth=0.3, relheight=0.05)


# вместо текста будет textvariable по расчитаному тобой 
loginInput = Entry(frame,bg=rgb_hack((176,196,222)),width=50,font=('Comic Sans MS','10'))
ip2lable = ttk.Label(frame2,background=rgb_hack((176,196,222)),width=100,font=('Comic Sans MS','10'))
maska2lable=ttk.Label(frame3,background=rgb_hack((176,196,222)),width=100,font=('Comic Sans MS','10'),)
nomerseti2lable=ttk.Label(frame4,background=rgb_hack((176,196,222)),width=100,font=('Comic Sans MS','10'))
shiroko2lable=ttk.Label(frame5,background=rgb_hack((176,196,222)),width=100,font=('Comic Sans MS','10'))
maskalable=ttk.Label(frame7,background=rgb_hack((176,196,222)),width=100,font=('Comic Sans MS','10'))
nomersetilable=ttk.Label(frame8,background=rgb_hack((176,196,222)),width=100,font=('Comic Sans MS','10'))
shirokolable=ttk.Label(frame9,background=rgb_hack((176,196,222)),width=100,font=('Comic Sans MS','10'))
adr1lable=ttk.Label(frame10,background=rgb_hack((176,196,222)),width=100,font=('Comic Sans MS','10'))
adr2lable=ttk.Label(frame11,background=rgb_hack((176,196,222)),width=100,font=('Comic Sans MS','10'))
coladrlable=ttk.Label(frame12,background=rgb_hack((176,196,222)),width=100,font=('Comic Sans MS','10'))
ip2lable.pack()
loginInput.pack()
maska2lable.pack()
nomerseti2lable.pack()
shiroko2lable.pack()
maskalable.pack()
nomersetilable.pack()
shirokolable.pack()
adr1lable.pack()
adr2lable.pack()
coladrlable.pack()
 
color = ["Blue/cyan","Gray","Red","Green","White"]
comboboxtheme = ttk.Combobox(frame6,values = color, state = "readonly")
comboboxtheme.pack()


btn = Button(frame13, text = "Выполнить",background=rgb_hack((176,196,222)))
btnt = Button(frame14, text = "Изменить", command = callbackTheme,background=rgb_hack((176,196,222)))
btn.pack(fill=X)
btn.bind('<Button-1>',click)
btnt.pack(fill=X)
root.mainloop()