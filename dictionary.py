from tkinter import*
from PIL import Image, ImageTk
import re
import os
import sys
import requests
from bs4 import BeautifulSoup


#Defining fonts
bfonts=("Constantia",20)
tfonts=("Valorant",40)

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
#FETCHING
def fetching(entry):
	lis=[]
	dis=[]
	final=[]
	url="https://www.merriam-webster.com/dictionary/"+entry
	source_code=requests.get(url)
	plain_text=source_code.text
	soup=BeautifulSoup(plain_text,features="lxml")
	
	# Fetch meanings from HTML using BeautifulSoup
	for meaning in soup.findAll('span',{'class':'dtText'}):
		lis.append(meaning.text)
	print(lis)
	
	# Extract relevant information from meanings
	for i in range(len(lis)):
		lis[i]=lis[i]+"."
	for i in lis:
		pattern=(r"[a-zA-z]+ [a-zA-z]+.+")
		result=re.findall(pattern,i)
		dis.append(result)
	for j in dis:
		for k in j:
			final.append(k)
	# DISPLAY OUTPUT
	for x in final:
		label=Label(frame2,text=x,font=("calibri",18,'bold'))
		label.pack()

#USER INTERFACE
root=Tk()
root.title("Dictionary")
canvas=Canvas(root,height=700,width=800)
canvas.pack()

#Background_image
im=Image.open("C:\\Users\\iamaj\\Downloads\\background_image.PNG")
im=im.resize((1920,1080))
bc_image=ImageTk.PhotoImage(im)
bc_label=Label(root,image=bc_image)
bc_label.place(relheight=1,relwidth=1)

#TITLE
title=Label(root,text="DICTIONARY",fg="black",font=tfonts)
title.place(relx=0.5,anchor=CENTER,rely=0.05)

#FRAME
frame=Frame(root,bg="#681111",bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.95, relheight=0.08, anchor='n')
frame2=Frame(root,bg="#681111",bd=3)
frame2.place(relx=0.5, rely=0.30, relwidth=0.95, relheight=0.6, anchor='n')

#Entry(search bar)
entry=Entry(frame,font=40)
entry.place(relwidth=0.65, relheight=1)

#Buttons
button1=Button(frame,text="Search",fg="#000000",font=bfonts,command=lambda :fetching(entry.get()))
button1.place(relx=0.7, relheight=1, relwidth=0.3)
button2=Button(root,text="Clear",fg="#000000",font=bfonts,command=restart_program)
button2.place(relx=0.5, rely=0.96, relwidth=0.3, relheight=0.07,anchor=CENTER)

#OUTPUT LABEL
display_label =Label(frame2)
display_label.place(relwidth=1, relheight=1)
root.mainloop()
