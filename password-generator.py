from  tkinter import *
import string
from random import randint,choice

def generate_password():
    password_min=6
    password_max=12
    all_chars=string.ascii_letters + string.punctuation + string.digits
    
    password = "".join(choice(all_chars) for x in range(randint(password_min, password_max)))
    password_entry.delete(0,END)
    password_entry.insert(0,password)
    
    with open("password.txt","a+") as file:
        
        file.write(password+"\n")
        file.close()

#créer une fenetre

window = Tk()
window.title("My application")
window.iconbitmap("logo.ico")
window.geometry("720x480")
window.minsize(480,360)
window.config(background="#6e6046")

#variables:
width = 300
height = 300
background="#6e6046"

#créer le frame principal
frame = Frame(window, bg=background)

#créer une image

image = PhotoImage(file="login.png").zoom(15).subsample(32)

canvas = Canvas(frame, width=width, height=height, bg=background, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0, column=0, sticky=W)

#creer une sous boite
right_frame = Frame(frame,bg=background)


#titre:
label_title = Label(right_frame, text = "Mot de pass", font=("Helvetica", 20), bg=background, fg="white")
label_title.pack()

#input:
password_entry= Entry(right_frame, font=("Helvetica", 20), bg=background, fg="white")
password_entry.pack()

#bouton:
generate = Button(right_frame, text = "générer", font=("Helvetica", 20), bg=background, fg="white", command=generate_password)
generate.pack(fill=X)

#on place la sous boite à droite de la frame principale
right_frame.grid(row=0, column=1, sticky=W)

#afficher frame
frame.pack(expand=YES)

#créer navbar
menu_bar = Menu(window)

# créer un premier menu
file_menu = Menu(menu_bar, tearoff = 0)
file_menu.add_command(label="Nouveau",command=generate_password)
file_menu.add_command(label="Quitter",command=window.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)

#configurer la fenetre pour ajouter cette navbar
window.config(menu=menu_bar)

#ouvrir la fenetre
window.mainloop()
