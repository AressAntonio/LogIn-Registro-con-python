import tkinter
from flask import Flask, render_template
from tkinter import*
from tkinter import messagebox
import pymysql
from tkinter import ttk

app = Flask(__name__)

@app.route('/')
##codigo para ventana principal##
def menu_inicio():
    global inicio
    inicio=Tk()
    inicio.geometry("1800x900")
    inicio.title("Bienvenido a ReptilGames")
    inicio.iconbitmap("Reptil.ico")

    image=PhotoImage(file="reptilgames.gif")
    image=image.subsample(2,2)
    label=Label(image=image)
    label.pack()

    Label(text="ReptilGames\n Lobby", bg="gray17", fg="gray59", width="800", height="4", font=("Arial", 21)).pack()
    Label(text="").pack()

    Button(text="Iniciar Sesion", bg="chartreuse4", fg="black", width="30", height="2", font=("Arial", 16), command=comenzar_secion).pack()
    Label(text="").pack()

    Button(text="Registrar", bg="red4", fg="black", width="20", height="2", font=("Arial", 16), command=registro).pack()
    Label(text="").pack()

    inicio.mainloop()
#seccion de codigo para entrar a la ventana de iniciar secion
def comenzar_secion():
    global pantalla1
    pantalla1 = Toplevel(inicio)
    pantalla1.geometry("450x300")
    pantalla1.title("Inicio de sesion")
    pantalla1.iconbitmap("Reptil.ico")

    Label(pantalla1, text="Ingresar Usuario y Contraseña", bg="gray17", fg="gray59", width="50", height="4", font=("Arial", 16)).pack()
    Label(pantalla1, text="").pack()

    global nombreusuario_verify
    global contraseña_verify

    nombreusuario_verify=StringVar()
    contraseña_verify=StringVar()

    global nombre_usuario_entry
    global contraseña_usuario_entry

    Label(pantalla1, text="Usuario Reptil").pack()
    nombre_usuario_entry = Entry(pantalla1, textvariable=nombreusuario_verify)
    nombre_usuario_entry.pack()
    Label(pantalla1).pack()

    Label(pantalla1, text="Contraseña").pack()
    contraseña_usuario_entry = Entry(pantalla1, show="*", textvariable=contraseña_verify)
    contraseña_usuario_entry.pack()
    Label(pantalla1).pack()

    Button(pantalla1, text="Comenzar", bg="red4", fg="black", font=("Arial", 16), command=validacion_datos).pack()
#Seccion de codigo para ventana de registro de nuevos usuarios
def registro():
    global pantalla2
    pantalla2 = Toplevel(inicio)
    pantalla2.geometry("400x450")
    pantalla2.title("Nuevo en ReptilGames")
    pantalla2.iconbitmap("Reptil.ico")

    global nombreusuario_entry
    global contraseña_entry

    nombreusuario_entry=StringVar()
    contraseña_entry=StringVar()

    Label(pantalla2, text="¡Vamos no seas timido\n Registrate!", bg="gray17", fg="gray59", width="50", height="4", font=("Arial", 16)).pack()
    Label(pantalla2, text="").pack()

    Label(pantalla2, text="Ingrese nuevo Usuario Reptil").pack()
    nombreusuario_entry = Entry(pantalla2)
    nombreusuario_entry.pack()
    Label(pantalla2).pack()

    Label(pantalla2, text="Ingrese nueva Contraseña").pack()
    contraseña_entry = Entry(pantalla2, show="*")
    contraseña_entry.pack()
    Label(pantalla2).pack()

    Button(pantalla2, text="Registrar", bg="red4", fg="black", font=("Arial", 16), command=inserta_datos).pack()
 #seccion de codigo para el registro de nuevos usuarios en la bd   
def inserta_datos():
    bd=pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        db="pd2"
        )

    fcursor=bd.cursor()

    sql="INSERT INTO login (usuario, contrasena) VALUES ('{0}', '{1}')".format(nombreusuario_entry.get(), contraseña_entry.get())

    try:
        fcursor.execute(sql)
        bd.commit()
        messagebox.showinfo(message="¡Ya eres parte de ReptilGames\n Bienvenido!", title="ReptilGames_Info.")
        
    except:
        bd.rollback()
        messagebox.showinfo(message="¡Lo sentimos algo salio mal\n Recarga la pagina y vuelve a intentarlo!", title="ReptilGames_Info.")
            
    bd.close()
#seccion de codigo para comunicacion con BD y verificar usuario
def validacion_datos():
     bd=pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        db="pd2"
        )

     fcursor=bd.cursor()

     fcursor.execute("SELECT contrasena FROM login WHERE usuario='"+nombreusuario_verify.get()+"' and contrasena='"+contraseña_verify.get()+"'")

     if fcursor.fetchall():
        messagebox.showinfo(title="Inicio de Sesion\n correcto", message="¡Perfecto Accediste\n A ReptilGames!")
        #ventana de productos
        global pantalla3
        pantalla3 = Toplevel(inicio)
        pantalla3.geometry("2000x1800")
        pantalla3.title("Productos ReptilGames")
        pantalla3.iconbitmap("Reptil.ico")
        pantalla3.configure(background="chartreuse4")
        Label(text="ReptilGames\n Tienda", bg="gray17", fg="gray59", width="800", height="4", font=("Arial", 21)).pack()
        Label(text="").pack()
        arbol=ttk.Treeview(pantalla3,columns=("Precio","Cantidad"))
        arbol.insert("",END,text="Mouse", values=("$150","Unidades 20"))
        arbol.insert("",END,text="Teclado con luces led", values=("$350","Unidades 15"))
        arbol.insert("",END,text="Monitor Curvo", values=("$10000","Unidades 10"))
        arbol.insert("",END,text="Disco duro", values=("$2000","Unidades 16"))
        arbol.insert("",END,text="Gabinete", values=("$3500","Unidades 10"))
        arbol.insert("",END,text="Kit desarmadores", values=("$350","Unidades 12"))
        arbol.insert("",END,text="Pasta termica", values=("$60","Unidades 9"))
        arbol.insert("",END,text="Aire comprimido", values=("$85","Unidades 7"))
        arbol.insert("",END,text="SSD", values=("$2500","Unidades 10"))
        arbol.heading("#0",text="Producto")
        arbol.heading("Precio",text="Precio")
        arbol.heading("Cantidad",text="Cantidad")
        arbol.place(x=10,y=10)
        Button(pantalla3, text="¿Vez algo que te guste?", bg="red4", fg="black", font=("Arial", 16)).pack()
        Button.place(x=15,y=-15).pack()
        

     else:
         messagebox.showinfo(title="Fallo en Inicio de Sesion", message="¡Lo sentimos al parecer no eres parte de ReptilGames\n Pero oye no todo esta perdido te puedes registrar!")           

     bd.close()

   


menu_inicio()

def cambiar():
	comida = combo.get()
	if comida=="Frutas":
		combo2["values"]=("Manzana","Mandarina","Naranja")
	if comida=="Verduras":
		combo2["values"]=("Lechuga","Cebolla")
	if comida=="Carnes":
		combo2["values"]=("Pollo","Pescado","Res")
	combo2.current(0)

ventana = Tk(pantalla3)
ventana.geometry("300x300")
ventana.title("Combobox")

etiqueta = Label(ventana,text="¿Qué deseas comer?")
etiqueta.place(x=100,y=40)

combo = ttk.Combobox(ventana,state="readonly")
combo.place(x=100,y=70)
combo["values"]=("Frutas","Verduras","Carnes")
combo.current(0)

boton = Button(ventana,text="Cargar",command=cambiar)
boton.place(x=100,y=100)

combo2 = ttk.Combobox(ventana,state="readonly")
combo2.place(x=100,y=130)

ventana.mainloop()

if __name__ == '__main__':
    app.run()


    

    
