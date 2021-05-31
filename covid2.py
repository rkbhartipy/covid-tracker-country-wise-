from tkinter import *
from tkinter import messagebox
from covid import Covid

def check_status():
    covid=Covid()

    get_country_name=entry.get()
    print(get_country_name)
    

    cases=covid.get_status_by_country_name(get_country_name)

    try :
        pady=0
        for i in cases:
            label=Label(root,text=str(i) + ":" + str(cases[i]),bg="skyblue",width=25,justify="left",font=("verdana",15,"bold"))
            label.place(x=20,y=pady+50)
            pady+=30

    except :
        messagebox.showinfo("error","check country name or connection")     
        
root=Tk()
root.geometry("400x350")
root.resizable(False,False)
root.title("covid-19 status")

entry=Entry(root,width=17,bg="skyblue",font=("verdana",10,"bold"))
entry.place(x=20,y=20)

btn=Button(root,text="check",width=10,font=("time",7,"bold"),bg="red",bd=5,command=check_status)
btn.place(x=200,y=20)

root.mainloop()








