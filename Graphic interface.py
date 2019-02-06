from tkinter import *
from tkinter import font
from PIL import Image,ImageTk
import time as tm
from tkinter import  messagebox
from tkinter import ttk
#Principal
raiz=Tk() #Crear la ventana
raiz.title('REGISTRO DE ASPIRANTES')#dAR UN TITULO A LA VENTANA
raiz.iconbitmap('ima.ico')#Asignar un icono a la ventana
raiz.geometry('1000x450')#Tamaño de la ventana
raiz.config(bg='old lace')
text = Label(raiz, text=' REGISTRO DE USUARIOS ', bg='old lace', width='50', height='3',font=( "Times New Roman", 18))  # underline permite subbrayar una letra| fg='color' permite dar color al texto
text.pack()





#Logo
img = Image.open('rbota.jpg')
img.thumbnail((80,80), Image.ANTIALIAS)
tkimage = ImageTk.PhotoImage(img)
tr=Label(raiz,image=tkimage).place(x=910, y=360)



#Listbox
lst=Listbox(raiz,width=50,font=( "Times New Roman", 14))
lst.place(x=400,y=100)




#########################################################################################################################
#Crear archivos con cabezera
#

#aspirantes=open('Aspirantes.csv','a')
#aspirantes.write('Matrícula;Categoría;Nombre;Carrera;Número de teléfono;E-mail\n')
#aspirantes.close()
#
#directiva=open('Directiva.csv','a')
#directiva.write('Matrícula;Categoría;Nombre;Carrera;Número de teléfono;E-mail\n')
#directiva.close()
#
#latente=open('Latente.csv','a')
#latente.write('Matrícula;Categoría;Nombre;Carrera;Número de teléfono;E-mail\n')
#latente.close()
#
#miembro_activo=open('Mimebros_activos.csv','a')
#miembro_activo.write('Matrícula;Categoría;Nombre;Carrera;Número de teléfono;E-mail\n')
#miembro_activo.close()

#######################################################################################################
#FUNCIONES
def guardar():
    if E1.get() and   E2.get() and  E4.get() and  E5.get() and  E6.get() and box.get() and box2.get() and box1.get() :
        if box.get().upper() =='ASPIRANTE':
            aspirantes = open('Aspirantes.csv', 'a')
            aspirantes.write('%s;%s;%s;%s;%s;%s\n'%(E4.get(),box2.get(),E1.get(),E2.get(),E5.get(),(E6.get()+box1.get())))
            aspirantes.close()
            alerta()
        elif box.get().upper() == 'DIRECTIVA':
            directiva = open('Directiva.csv', 'a')
            directiva.write('%s;%s;%s;%s;%s;%s\n'%(E4.get(),box2.get(),E1.get(),E2.get(),E5.get(),(E6.get()+box1.get())))
            directiva.close()
            alerta()

        elif box.get().upper() == 'LATENTE':
            latente = open('Latente.csv', 'a')
            latente.write('%s;%s;%s;%s;%s;%s\n'%(E4.get(),box2.get(),E1.get(),E2.get(),E5.get(),(E6.get()+box1.get())))
            latente.close()
            alerta()

        elif box.get().upper() == 'MIEMBRO ACTIVO':
            miembro_activo = open('Miembros_activos.csv', 'a')
            miebro_activo.write('%s;%s;%s;%s;%s;%s\n'%(E4.get(),box2.get(),E1.get(),E2.get(),E5.get(),(E6.get()+box1.get())))
            miembro_activo.close()
            alerta()
    else:
        vacio()



def limpiar():
    E1.delete(0, 'end')
    E2.delete(0, 'end')
    E4.delete(0, 'end')
    E5.delete(0, 'end')
    E6.delete(0, 'end')
def limpiarlabel():
    lst.delete(0, 'end')

def agrega():

    if box3.get()=='Aspirantes':
        limpiarlabel()
        lst.insert(0,'Información de aspirantes:')
        aspirantes=open('Aspirantes.csv','r')
        aspirantes.readline()
        lst.insert(END,'Matrícula:        Categoría:         Nombre:')
        for i in aspirantes:
            lista=i.strip().split(';')
            matrícula=lista[0]
            categoria=lista[1]
            nombre=lista[2]
            string=matrícula+'       '+categoria+'         '+nombre
            lst.insert(END,string)
            

        
    elif box3.get()=='Miembros Activos':
        limpiarlabel()
        lst.insert(0,'Información de miembros activos:')
        miembros_activos=open('Mimebros_activos.csv','r')
        miembros_activos.readline()
        lst.insert(END,'Matrícula:        Categoría:         Nombre:')
        for i in miembros_activos:
            lista=i.strip().split(';')
            matrícula=lista[0]
            categoria=lista[1]
            nombre=lista[2]
            string=matrícula+'       '+categoria+'         '+nombre
            lst.insert(END,string)
        
        
    elif box3.get()=='Directiva':
        limpiarlabel()
        lst.insert(0,'Información de Directiva:')
        directiva=open('Directiva.csv','r')
        directiva.readline()
        lst.insert(END,'Matrícula:        Categoría:         Nombre:')
        for i in directiva:
            lista=i.strip().split(';')
            matrícula=lista[0]
            categoria=lista[1]
            nombre=lista[2]
            string=matrícula+'       '+categoria+'         '+nombre
            lst.insert(END,string)
        
    elif box3.get()=='Latente':
        limpiarlabel()
        lst.insert(0,'Información de Latentes:')
        latente=open('Latente.csv','r')
        latente.readline()
        lst.insert(END,'Matrícula:        Categoría:         Nombre:')
        for i in latente:
            lista=i.strip().split(';')
            matrícula=lista[0]
            categoria=lista[1]
            nombre=lista[2]
            string=matrícula+'       '+categoria+'         '+nombre
            lst.insert(END,string)
        
        

def alerta():
    messagebox.showinfo("Roboto", "Se ha guardado correctamente la información.")
def vacio():
    messagebox.showerror('Roboto','Exiten campos vacios, por favor verifique\nla información ingresada.')


#########################################################################################################################



#Entry
y=StringVar()
label=Label(raiz,text='Nombre:',font=( "Times New Roman", 13),bg='old lace').place(x=20,y=70)
E1=Entry(raiz,width=55)
E1.place(x=20,y=100)
label=Label(raiz,text='Carrera:',font=( "Times New Roman", 13),bg='old lace').place(x=20,y=130)
E2=Entry(raiz,width=55)
E2.place(x=20,y=160)
label=Label(raiz,text='Estatus:',font=( "Times New Roman", 13),bg='old lace').place(x=20,y=190)
#E3=Entry(raiz,width=55)
label=Label(raiz,text='Categoria:',font=( "Times New Roman", 13),bg='old lace').place(x=200,y=190)
#E3.place(x=20,y=220)

label=Label(raiz,text='Matricula:',font=( "Times New Roman", 13),bg='old lace').place(x=20,y=250)
E4=Entry(raiz,width=55)
E4.place(x=20,y=280)
label=Label(raiz,text='Número de telefono:',font=( "Times New Roman", 13),bg='old lace').place(x=20,y=310)
E5=Entry(raiz,width=55)
E5.place(x=20,y=340)
label=Label(raiz,text='E-mail:',font=( "Times New Roman", 13),bg='old lace').place(x=20,y=370)
E6=Entry(raiz,width=30)
E6.place(x=20,y=400)
label=Label(raiz,text='Mostrar registro de:',font=( "Times New Roman", 13),bg='old lace').place(x=400,y=70)



#Botones
buttonagregar = Button(raiz, text='Vizualizar', height=2, width=20, command=agrega).place(x=560, y=390)
buttonguardar = Button(raiz, text='Guardar', height=2, width=20, command=guardar).place(x=720, y=390)
nuttonrefresh = Button(raiz, text='Actualizar', height=2, width=20, command=limpiar).place(x=400, y=390)


#menu desplazable
box=ttk.Combobox(raiz,state="readonly")
box["values"] = ["Aspirante", "Miembro Activo", "Latente", "Directiva"]
box.place(x=20, y=220)

box1=ttk.Combobox(raiz,state="readonly")
box1["values"] = ["@gmail.com", "@outlook.com", "@espol.edu.ec", "@hotmail.com",'@live.com']
box1.place(x=170, y=400)

box2=ttk.Combobox(raiz,state="readonly")
box2["values"] = ['Soccer','Batalla 1 lb','Batalla 2 lb','Batalla 3 lb','Insecto','Laberinto','Seguidor de Línea','Sumo autonomo','Voladores']
box2.place(x=200, y=220)

box3=ttk.Combobox(raiz,state="readonly")
box3["values"] = ['Aspirantes','Miembros Activos','Directiva','Latente']
box3.place(x=550, y=72)


#buble
raiz.mainloop()#Crear un buble infinito para que la ventana este abierta durante todo el proceso