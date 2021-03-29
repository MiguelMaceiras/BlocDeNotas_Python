from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile

#FUNCIONES

def nuevo():
    editor.delete(1.0, END)

def abrir():
    documento = askopenfile(filetypes = [("Archivo de texto", "*.txt")])
    if documento != None:
        editor.insert(1.0, documento.read())

def guardar():
    documento = asksaveasfile(filetypes = [("Archivo de texto", "*.txt")])
    print(documento.write(editor.get(1.0, END)))

def deshacer():
    editor.edit_undo()

def hacer():
    editor.edit_redo()

def copiar():
    editor.clipboard_clear()
    editor.clipboard_append(editor.selection_get())

def pegar():
    editor.insert(INSERT, editor.clipboard_get())

def cortar():
    editor.clipboard_clear()
    editor.clipboard_append(editor.selection_get())
    editor.delete("sel.first", "sel.last")

def acerca():
    messagebox.showinfo("Acerca de Bloc de notas", "Este bloc de notas está creado por el programador M²A")

if __name__ == "__main__":
    ventana = Tk()

    ventana.title("Bloc de notas")
    ventana.geometry("695x424")


    menubar = Menu(ventana)

    ventana.config(menu = menubar)

#MENÚ ARCHIVO

    archivo = Menu(menubar, tearoff=0)
    menubar.add_cascade(label = "Archivo", menu = archivo)

    archivo.add_command(label = "Nuevo    ", command = nuevo)
    archivo.add_command(label = "Abrir    ", command = abrir)
    archivo.add_command(label = "Guardar    ", command = guardar)
    archivo.add_command(label = "Salir    ", command = ventana.quit)

#MENÚ EDICIÓN

    editar = Menu(menubar, tearoff = 0)
    editar.add_command(label = "Deshacer    ", command = deshacer)
    editar.add_command(label = "Rehacer    ", command = hacer)
    editar.add_separator()
    editar.add_command(label = "Copiar    ", command = copiar)
    editar.add_command(label = "Pegar    ", command = pegar)
    editar.add_command(label = "Cortar    ", command = cortar)
    menubar.add_cascade(label = "Edición", menu = editar)

#MENÚ AYUDA

    ayuda = Menu(menubar, tearoff = 0)
    ayuda.add_command(label = "Acerca de Bloc de notas    ", command = acerca)
    menubar.add_cascade(label = "Ayuda", menu = ayuda)

    editor = Text(ventana, undo = "true")
    editor.pack(side = TOP, fill = BOTH, expand = 1)

    ventana.mainloop()