from tkinter import *
logs = Tk()
logs.geometry('600x800+600+150')

label1=Label(text='Hello, World!',font=('Arial','24'),fg='red')
label1.pack(padx=100, pady=30)
label2=Label(text='Hello, Me!',font=('Arial','24'),fg='red')
label2.pack(padx=100, pady=30)
label3=Label(text='Ka tev sauc?',font=('Arial','24'),fg='blue')
label3.pack(padx=100, pady=30)
text=Entry(font=('Arial','24'))
text.pack(padx=100, pady=30)
btn1=Button(text='Saglabat',font=('Arial','24'),bg='red',fg='blue')
btn1.pack(padx=100, pady=30)
btn2=Button(text='Izeja',font=('Arial','24'),bg='green',fg='blue')
btn2.pack(pady=50,side=BOTTOM)
logs.mainloop()