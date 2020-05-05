from tkinter import *

def calculate():
    value_1 = float(entry_field_1.get())
    value_2 = float(entry_field_2.get())
    value_3 = value_1 * value_1
    resultado = value_2 / value_3

    result_field.delete(0, END)
    result_field.insert(0, resultado)

root = Tk()
root.title('Calculadora IMC')
root.geometry('300x300')
root.configure(bg='light blue')

windows_title = Label(root, text='Calculadora IMC', bg='light blue', font=('Arial', 18)).place(x=50, y=10)

label_1 = Label(root, text='Informe sua altura\n com ponto', bg='light blue', font=('Arial', 14)).place(x=10, y=75)
entry_field_1 = Entry(root, text='Altura', width=10)
entry_field_1.place(x=230, y=80)

label_2 = Label(root, text='Informe seu peso', bg='light blue', font=('Arial', 14)).place(x=10, y=120)
entry_field_2 = Entry(root, text='peso', width=10)
entry_field_2.place(x=230, y=120)

botao = Button(root, text='Calcular', command=calculate, width='20').place(x=75, y=200)

label_3 = Label(root, text='Resultado').place(x=120, y=235)
result_field = Entry(root)
result_field.place(x=85, y=265)

root.mainloop()