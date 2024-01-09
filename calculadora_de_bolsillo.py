from tkinter import Tk, Entry, Button, StringVar, END, Label
#crea ventana
root = Tk()
root.geometry("340x400+50+50")
root.title("Calculadora de bolsillo")
background_root = "#5C26E0"
background_root_nigth = "#12001A"
root["bg"]=background_root
#root.iconbitmap("images\Calculator_30001.ico")

#configuracion de botones
alto_boton= 2
ancho_boton= 3
pading_x=10
pading_y=10
background_boton= "#9826E0"
foreground_boton= "#FFFFFF"
active_bg_boton= "#D626E0"

background_boton_nigth= "#2A003B"
foreground_boton_nigth= "#7D576E"
active_bg_boton_nigth= "#520073"


def modo_app():
	if  root["bg"] == background_root:
		print("1")
		root["bg"] = background_root_nigth
		
	elif root["bg"] == background_root_nigth:
		print("2")
		root["bg"] = background_root
	else:
		print("Opcion Invalida")

#se crea el display
control_display = StringVar()
pantalla = Entry(root, bg="lightgray", fg="black", font=("Arial", 18, "bold"), 
				 justify="right", textvariable=control_display, width=24, borderwidth=5)
pantalla.grid(row=0, column=0, columnspan=6, padx=10,pady=5)

#funciones
#limpia la pantalla
def clean():
    control_display.set("")
#envia el  numero pulsado
def envia_boton(valor):
	anterior = pantalla.get()
	pantalla.delete(0, END)
	pantalla.insert(0, str(anterior) + str(valor))
#operaciones
def suma():
	global num1
	global operacion
	num1 = pantalla.get()
	num1 = float(num1)
	pantalla.delete(0,END)
	operacion = "+"
	
def resta():
	global num1
	global operacion
	num1 = pantalla.get()
	num1 = float(num1)
	pantalla.delete(0,END)
	operacion = "-"
	
def multiplicacion():
	global num1
	global operacion
	num1 = pantalla.get()
	num1 = float(num1)
	pantalla.delete(0,END)
	operacion = "*"
	
def division():
	global num1
	global operacion
	num1 = pantalla.get()
	num1 = float(num1)
	pantalla.delete(0,END)
	operacion = "/"

def igual():
	global num2
	num2 = pantalla.get()
	pantalla.delete(0, END)

	if operacion == "+":
		pantalla.insert(0, num1 + float(num2))
	if operacion == "-":
		pantalla.insert(0, num1 - float(num2))
	if operacion == "*":
		pantalla.insert(0, num1 * float(num2))
	if operacion == "/":
		pantalla.insert(0, num1 / float(num2))


#botones generales
boton_7 = Button(root, text="7", font=("Arial", 12),command=lambda: envia_boton(7),
				 width=ancho_boton, height=alto_boton, padx=pading_x, pady=pading_y, bg=background_boton,fg=foreground_boton, activebackground=active_bg_boton).grid(row=2, column=0)
boton_8 = Button(root, text="8", font=("Arial", 12),command=lambda: envia_boton(8),
				 width=ancho_boton, height=alto_boton, padx=pading_x, pady=pading_y, bg=background_boton,fg=foreground_boton, activebackground=active_bg_boton).grid(row=2, column=1)
boton_9 = Button(root, text="9", font=("Arial", 12),command=lambda: envia_boton(9),
				 width=ancho_boton, height=alto_boton, padx=pading_x, pady=pading_y, bg=background_boton,fg=foreground_boton, activebackground=active_bg_boton).grid(row=2, column=2)

boton_4 = Button(root, text="4", font=("Arial", 12),command=lambda: envia_boton(4),
				 width=ancho_boton, height=alto_boton, padx=pading_x, pady=pading_y, bg=background_boton,fg=foreground_boton, activebackground=active_bg_boton).grid(row=3, column=0)
boton_5 = Button(root, text="5", font=("Arial", 12),command=lambda: envia_boton(5),
				 width=ancho_boton, height=alto_boton, padx=pading_x, pady=pading_y, bg=background_boton,fg=foreground_boton, activebackground=active_bg_boton).grid(row=3, column=1)
boton_6 = Button(root, text="6", font=("Arial", 12),command=lambda: envia_boton(6),
				 width=ancho_boton, height=alto_boton, padx=pading_x, pady=pading_y, bg=background_boton,fg=foreground_boton, activebackground=active_bg_boton).grid(row=3, column=2)

boton_1 = Button(root, text="1", font=("Arial", 12),command=lambda: envia_boton(1),
				 width=ancho_boton, height=alto_boton, padx=pading_x, pady=pading_y, bg=background_boton,fg=foreground_boton, activebackground=active_bg_boton).grid(row=4, column=0)
boton_2 = Button(root, text="2", font=("Arial", 12),command=lambda: envia_boton(2),
				 width=ancho_boton, height=alto_boton, padx=pading_x, pady=pading_y, bg=background_boton,fg=foreground_boton, activebackground=active_bg_boton).grid(row=4, column=1)
boton_3 = Button(root, text="3", font=("Arial", 12),command=lambda: envia_boton(3),
				 width=ancho_boton, height=alto_boton, padx=pading_x, pady=pading_y, bg=background_boton,fg=foreground_boton, activebackground=active_bg_boton).grid(row=4, column=2)

boton_0 = Button(root, text="0", font=("Arial", 12),command=lambda: envia_boton(0),
				 width=ancho_boton, height=alto_boton, padx=pading_x, pady=pading_y, bg=background_boton,fg=foreground_boton, activebackground=active_bg_boton).grid(row=5, column=0)
boton_punto = Button(root, text=".", font=("Arial", 12),command=lambda: envia_boton("."),
					 width=ancho_boton, height=alto_boton, padx=pading_x, pady=pading_y, bg=background_boton,fg=foreground_boton, activebackground=active_bg_boton).grid(row=5, column=1)

#botones de operacion
boton_clean = Button(root, text="C", font=("Arial", 12), command=clean,width=ancho_boton, height=alto_boton,
					  padx=pading_x, pady=pading_y, bg=background_boton,fg=foreground_boton, activebackground=active_bg_boton).grid(row=5, column=2)
boton_div = Button(root, text="/", font=("Arial", 12),command=division,width=ancho_boton, height=alto_boton,
				    padx=pading_x, pady=pading_y, bg=background_boton,fg=foreground_boton, activebackground=active_bg_boton).grid(row=2, column=3)
boton_multiplica = Button(root, text="X", font=("Arial", 12),command=multiplicacion,width=ancho_boton, 
						  height=alto_boton, padx=pading_x, pady=pading_y, bg=background_boton,fg=foreground_boton, activebackground=active_bg_boton).grid(row=3, column=3)
boton_resta = Button(root, text="-", font=("Arial", 12),command=resta,width=ancho_boton, 
					 height=alto_boton, padx=pading_x, pady=pading_y, bg=background_boton,fg=foreground_boton, activebackground=active_bg_boton).grid(row=4, column=3)
boton_suma = Button(root, text="+", font=("Arial", 12),command=suma,width=ancho_boton, 
					height=alto_boton, padx=pading_x, pady=pading_y, bg=background_boton,fg=foreground_boton, activebackground=active_bg_boton).grid(row=5, column=3)
boton_igual = Button(root, text="=", font=("Arial", 12),command=igual,width=ancho_boton, height=alto_boton, 
					 padx=pading_x, pady=pading_y, bg=background_boton,fg=foreground_boton, activebackground=active_bg_boton).grid(row=5, column=4)





#botones adicionales
boton_salir = Button(root, text="Quit", command= root.destroy,width=ancho_boton, height=alto_boton, 
					 padx=pading_x, pady=pading_y, bg=background_boton,fg=foreground_boton, activebackground=active_bg_boton).grid(row=3, column=4)
boton_modo = Button(root, text="Mode",width=ancho_boton, height=alto_boton, padx=pading_x, pady=pading_y, 
					bg=background_boton,fg=foreground_boton, activebackground=active_bg_boton, command=modo_app).grid(row=4, column=4)

anuncio = Label(root, text="Desarrollada by Daniel Alcazar", font=("Arial", 7, "bold"), 
				justify="center", pady=20, bg=background_root, fg=foreground_boton, height=5).grid(row=8, column= 0, columnspan= 5)
#bucle de ventana
root.mainloop()