import tkinter as tk
from tkinter import messagebox, filedialog, IntVar
import faker
from faker import Faker
import os
import time
ruta_destino = ""

def CambiarDestino():
    global ruta_destino
    ruta_destino = filedialog.askdirectory()
    if ruta_destino:
        etiqueta_ruta.config(text="Ruta de destino cambiada: " + ruta_destino)
        etiqueta_ruta.pack()

def GenerarDatos():
    global hilos_stop_pls
    telefonos = int(input_telefonos.get())
    nombresyapellidos = int(input_nombresyapellidos.get())
    direccion = int(input_direcciones.get())

    with open(os.path.join(ruta_destino, 'Telefonos'), 'w') as file_telefonos:
        with open(os.path.join(ruta_destino, 'nombres_y_apellidos.txt'), 'w') as file_nombres:
            with open(os.path.join(ruta_destino, 'Direcciones.txt'), 'w') as file_direcciones:
                for _ in range(telefonos):
                    if hilos_stop_pls:
                        return
                    celular = faker.phone_number()
                    file_telefonos.write(celular + '\n')
                    time.sleep(0.5)

                for _ in range(nombresyapellidos):
                    if hilos_stop_pls:
                        return
                    nya = faker.name()
                    file_nombres.write(nya + '\n')
                    time.sleep(0.5)

                for _ in range(direccion):
                    if hilos_stop_pls:
                        return
                    D1 = faker.address()
                    file_direcciones.write(D1 + '\n')
                    time.sleep(0.5)
def CerrarVentana():
    global hilos_stop_pls
    hilos_stop_pls = True
    root.update()
    time.sleep(0.2)
    root.destroy()

faker = Faker()
root = tk.Tk()
root.title("Crear Datos Falsos")

# Crear el fram principal
frame = tk.Frame(root)
frame.pack()

etiqueta_ruta = tk.Label(root, text="Ruta de destino: " + ruta_destino)

# mostrar lo que se puede fabricar
frame_datos = tk.LabelFrame(frame, text="Datos que puede crear")
frame_datos.grid(row=0, column=0, padx=10, pady=10)

label_telefonos = tk.Label(frame_datos, text="Numeros de Telefonos")
label_telefonos.grid(row=0, column=0)

label_direcciones = tk.Label(frame_datos, text="Direcciones")
label_direcciones.grid(row=1, column=0)

label_nombres = tk.Label(frame_datos, text="Nombres y apellidos")
label_nombres.grid(row=2, column=0)

# label con inputs
intvar_telefonos = tk.IntVar()
input_telefonos = tk.Spinbox(frame_datos, from_=1, to='infinity', textvariable=intvar_telefonos)
input_telefonos.grid(row=0, column=1)

intvar_direcciones = tk.IntVar()
input_direcciones = tk.Spinbox(frame_datos, from_=1, to='infinity', textvariable=intvar_direcciones)
input_direcciones.grid(row=1, column=1)

intvar_nombresyapellidos = tk.IntVar()
input_nombresyapellidos = tk.Spinbox(frame_datos, from_=1, to='infinity', textvariable=intvar_nombresyapellidos)
input_nombresyapellidos.grid(row=2, column=1)

# frame con boton
frame_boton = tk.Frame(frame)
frame_boton.grid(row=3, column=0, padx=10, pady=10)

boton = tk.Button(frame_boton, text="BAKE", command=GenerarDatos)
boton.grid(row=1, column=2)

# Codigo del Menu bar
menu_bar = tk.Menu(root)
menu_archivo = tk.Menu(menu_bar, tearoff=0)
menu_archivo.add_command(label="Destino", command=CambiarDestino)
menu_archivo.add_command(label="Cambiar destino", command=CambiarDestino)
menu_bar.add_cascade(label="Destino", menu=menu_archivo)

root.config(menu=menu_bar)

for widget in frame_datos.winfo_children():
    widget.grid_configure(padx=20, pady=10)


root.mainloop()
