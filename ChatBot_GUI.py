from Chatbot_Exp import get_response
from tkinter import *
windows = Tk()
windows.title('ChatBot')
windows.geometry('600x400')


def send():
    send="You: "+message_windows.get("1.0", "1.0 lineend")
    chat_windows.insert(END, "\n"+send)
    chat_windows.insert(END,'\n'+'Bot: ' + get_response(message_windows.get("1.0", "1.0 lineend"))+'\n')
    message_windows.delete(1.0,END)


chat_windows=Text(windows, bg='lightblue', width=40, height=5)
chat_windows.place(x=5, y=5, height=290, width=575)

scrollbar = Scrollbar(windows ,command=chat_windows.yview)
scrollbar.place(x=580, y=5, height=290)

message_windows=Text(windows, bg='lightblue', width=20, height=2.5)
message_windows.place(x=5, y=300, height=88, width=510)

Button=Button(windows, text='Send', font=('Arial',10), bg='grey', activebackground='dark grey', width=12, height=5, command=send)
Button.place(x=520, y=300, height='88', width='76')

windows.mainloop()
