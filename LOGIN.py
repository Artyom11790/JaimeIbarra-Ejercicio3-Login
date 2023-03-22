from tkinter import*
from PIL import ImageTk,Image
root= Tk()

ventanaprincipal=Frame(root)
ventanaprincipal.grid()
contras=StringVar()
confirmo=StringVar()


def contraseñas():
    if contras.get()==confirmo.get():
        print("Sesion Iniciada")
        ventanaprincipal.config(bg="#00FF00")
        
    else:
        print("Contraseña Incorrecta")



titulo=Label(ventanaprincipal,text="Inicar sesion",font=("roboto",20))
titulo.grid(row=3,column=1,columnspan=2)


NAME=Label(ventanaprincipal,text="NOMBRE:",font=("roboto",16)).grid(row=4,column=1,padx=30,pady=30)
textonombre=Entry(ventanaprincipal,font=("roboto",16)).grid(row=4,column=2,padx=30,pady=16)
CONTRA=Label(ventanaprincipal,text="CONTRASEÑA:",font=("roboto",16)).grid(row=5,column=1,padx=16,pady=30)
textocontra=Entry(ventanaprincipal,font=("roboto",16),textvariable=contras).grid(row=5,column=2,padx=30,pady=16)
CONFIRM=Label(ventanaprincipal,text="CONFIRMAR\n CONTRASEÑA:",font=("roboto",16)).grid(row=6,column=1,padx=10,pady=30)
textoconfir=Entry(ventanaprincipal,font=("roboto",16),textvariable=confirmo).grid(row=6,column=2,padx=30,pady=16)
control1=IntVar()
HOMBRE=Checkbutton(ventanaprincipal, text="HOMBRE",variable=control1,font=("roboto",16))
HOMBRE.grid(row=7,column=1,padx=20)
control2=IntVar()
MUJER=Checkbutton(ventanaprincipal, text="MUJER",variable=control2,font=("roboto",16))
MUJER.grid(row=7,column=2)
control3=IntVar()
acepto=Checkbutton(ventanaprincipal, text="ACEPTO TERMINOS",variable=control3,font=("roboto",16))
acepto.grid(row=8,column=1,columnspan=2)
iniciar=Button(ventanaprincipal,text="INICIAR",command=contraseñas,width=20,height=2).grid(row=9,column=1,columnspan=2)


img=Image.open('C:\\Users\\Junio\\OneDrive\\Escritorio\\PROGRAMAS DE PYTHON\\INTERFAZ_GRAFICA\\Logo7.png')#variable q contiene el nombre de la imagen
imagenmusica=img.resize((150,150))
imag=ImageTk.PhotoImage(imagenmusica)
mititulo=Label(ventanaprincipal,image=imag)
mititulo.grid(row=1,column=1,padx=10,pady=20,columnspan=2,rowspan=1)

root.mainloop()