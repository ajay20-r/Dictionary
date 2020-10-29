from tkinter import*
from PIL import Image, ImageTk
import re
import os
import sys
import requests
from bs4 import BeautifulSoup
root=Tk()
root.title("Dictionary")
#Defining fonts_______________
font="Constantia"
bfonts=(font,20)
font="Valorant"
tfonts=(font,40)
#root.geometry("1920X1080")
#CANVAS_________________________________________________________
canvas=Canvas(root,height=700,width=800)
canvas.pack()
#testing
#FETCHING_________________________________________________________
def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)
def get_meaning(entry):
	global label
	lis=[]
	dis=[]
	final=[]
	url="https://www.vocabulary.com/dictionary/"+entry
	source_code=requests.get(url)
	plain_text=source_code.text
	soup=BeautifulSoup(plain_text,features="html5lib")
	for link in soup.findAll('h3',{'class':'definition'}):
		lis.append(link.text)
	for i in range(len(lis)):
		lis[i]=lis[i]+"."
	for i in lis:
		pattern=(r"[a-zA-z]+ [a-zA-z]+.+")
		result=re.findall(pattern,i)
		dis.append(result)
	for j in dis:
		for k in j:
			final.append(k)
	#LABEL________________________________
	for x in final:
		label=Label(frame2,text=x,font=("calibri",18,'bold'))
		label.pack()
#DISPLAYING_______________________________________________________

#Background_image__________________________________________________
im=Image.open("D:\\gui\\background_image.png")
im=im.resize((1920,1080))
bc_image=ImageTk.PhotoImage(im)
bc_label=Label(root,image=bc_image)
bc_label.place(relheight=1,relwidth=1)
title=Label(root,text="DICTIONARY",fg="black",font=tfonts)
title.place(relx=0.5,anchor=CENTER,rely=0.05)
#FRAME____________________________________________________________
frame=Frame(root,bg="#681111",bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.95, relheight=0.08, anchor='n')
frame2=Frame(root,bg="#681111",bd=3)
frame2.place(relx=0.5, rely=0.30, relwidth=0.95, relheight=0.6, anchor='n')

#Entry(search bar)________________________________________________
entry=Entry(frame,font=40)
entry.place(relwidth=0.65, relheight=1)
#Buttons__________________________________________________________
button1=Button(frame,text="Search",fg="#000000",font=bfonts,command=lambda :get_meaning(entry.get()))
button1.place(relx=0.7, relheight=1, relwidth=0.3)
button2=Button(root,text="Clear",fg="#000000",font=bfonts,command=restart_program)
button2.place(relx=0.5, rely=0.96, relwidth=0.3, relheight=0.07,anchor=CENTER)
#LABEL____________________________________________________________
display_label =Label(frame2)
display_label.place(relwidth=1, relheight=1)
root.mainloop()