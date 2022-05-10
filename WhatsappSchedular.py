import datetime
from tkinter import *
import pywhatkit
# from PIL import ImageTk
import pandas as pd
# from tkinter.filedialog import askopenfilename
import pyttsx3


root=Tk()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!Sir")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!Sir")

    else:
        speak("Good Evening!Sir")


root.title("Python Project")
root.geometry('400x620')
icon = PhotoImage(file="WpLogo.png")
# img = PhotoImage(file="ph.png")
# label = Label(root, image=img).grid(row=0,column=0, columnspan=50, rowspan=50)
root.iconphoto(True, icon)
root.resizable(False, False)

frame = Frame(root)
frame.grid(row=0, column=0)

filename = ''
df = ''
OptionList = ['']
noOfVar = 0
varList = []  # list of the var columns in order
variableCols = ''
DropDownCols = ' '

#1st frame
def tab1():

    # 2nd frame
    def tab2():
        # to destroy all the widgets currently on the window
        speak("your history will be reviewed now")
        for widgets in frame.winfo_children():
            widgets.destroy()

        label=Label(frame, text="History...", font="Times 14", bg="#075E54", fg="#ffffff")
        label.grid(row=0, column=1, ipadx=160, columnspan=8)
        space3 = Label(frame, text="", font="times, 25").grid(row=1, column=0)
        txtarea = Text(frame, width=45, height=30)
        txtarea.grid(row=1, column=1, pady=10, columnspan=4)

        # to open History file in read only format
        tf = open("PyWhatKit_DB.txt")
        data = tf.read()
        txtarea.insert(END, data)
        tf.close()
        txtarea.configure(state='disabled')

        def back():
            speak("return to the home page")
            # to destroy all the widgets currently on the window
            for widgets in frame.winfo_children():
                widgets.destroy()
            tab1()

        button2 = Button(frame, text="Back", command=back, bg="#075E54", fg="#ffffff", font="times 12")
        button2.grid(row=10, column=2, ipadx=10)

    title = Label(frame, text="AutoDroid", font="times 17 bold", bg="#075E54", fg="#ffffff")
    title.grid(row=0, column=0, ipadx=70, columnspan=10)

    space = Label(frame, text="").grid(row=1)

    nameLabel = Label(frame, text="Message : ", font="times 12")
    nameLabel.grid(row=2, column=0, padx=20, pady=20, sticky=W)
    phoneLabel = Label(frame, text="Phone No. : ", font="times 12")
    phoneLabel.grid(row=3, column=0, padx=20, pady=20, sticky=W)
    timeLabel = Label(frame, text="Time : ", font="times 12")
    timeLabel.grid(row=4, column=0, padx=20, pady=20, sticky=W)

    msg = Entry(frame, width=30)
    msg.grid(row=2, column=2)

    text2 = Entry(frame)
    text2.insert(0, "+91 ")
    text2.grid(row=3, column=2)

    time = Entry(frame)
    time.grid(row=4, column=2)

    def onclick():
        speak("your message assigned is schedule !! it  will be sent successfully")

        # to get time from textbox and seprate and covert them from string to integer
        c = time.get()
        hr = str(c[0]) + str(c[1])
        min = str(c[3]) + str(c[4])

        pywhatkit.sendwhatmsg(text2.get(),
                              msg.get(),
                              int(hr), int(min))


    SendMsg = Button(frame, text="Schedule", command=onclick, bg="#075E54", fg="#ffffff", font="times 12")
    SendMsg.grid(row=6, column=2, padx=20, pady=20)

    ShowHistory = Button(frame, text="Show History", command=tab2, bg="#075E54", fg="#ffffff", font="times 12")
    ShowHistory.grid(row=8, column=0, padx=20, pady=20, sticky=W)

    # To send message to a group
    groupLabel = Label(frame, text="Group Link : ", font="times 12")
    groupLabel.grid(row=7, column=0, padx=20, pady=20)
    group = Text(frame, height=1, width=30)
    group.grid(row=7, column=2)

    def onclickgrp():

        speak("your message will be sent on group")
        c = time.get()
        hr = str(c[0]) + str(c[1])
        min = str(c[3]) + str(c[4])

        pywhatkit.sendwhatmsg_to_group(group.get(),
                                       msg.get(),
                                       int(hr), int(min))
    SendGrpMsg = Button(frame, text="Send Msg to Grp", command=onclickgrp, bg="#075E54", fg="#ffffff", font="times 12")
    SendGrpMsg.grid(row=8, column=2, padx=20, pady=20)

    space1 = Label(frame, text="").grid(row=9)
    space2 = Label(frame, text="").grid(row=10)
    Label(frame,text="Message from developer", font=("Times 13 bold")).grid(row=11, column=0, columnspan=5)
    Label(frame,text=" Greetings to the user !! We are the Developers of AutoDroid Application !!!.\n Allen Joshua \n  Lavena Babu. \n Erica DSouza").grid(row=12, column=0, columnspan=5)

    wishMe()
    speak("please fill the following details and click on the schedule button ")




    def Refresh():
        global filename
        filename = "Contacts.xlsx"
        Label(frame, text="{}".format(filename), bg='white', fg="#0A5688", font=("Arial", 12, "bold")).grid(row=21,
                                                                                                                column=1)
        df = pd.read_excel((filename))
        OptionList = (list(df.columns))
        print(OptionList)
        if (len(varList) > 0):
            Label(frame, text="{}".format(varList), bg='white', fg="#0A5688", font=("Arial", 12, "bold")).grid(
                row=22,
                column=1)
        else:
            Label(frame, text="", bg='white', fg="#0A5688", font=("Arial", 12, "bold")).grid(row=22, column=1)
        DropDownNumber()
        VariableColumsDropDown()

    def DropDownNumber():
        OptionList = ["Allen", "Lavena", "Erica"]
        global DropDownCols
        DropDownCols = StringVar(frame)
        DropDownCols.set("Select contact")
        opt = OptionMenu(frame, DropDownCols, *OptionList)
        opt.config(width=15, font=('Times', 12))
        opt.grid(row=3, column=2, padx=10, pady=10, columnspan=5)

    def VariableColumsDropDown():
        global variableCols
        variableCols = StringVar(frame)
        variableCols.set(OptionList[0])
        opt2 = OptionMenu(frame, variableCols, *OptionList)
        opt2.config(width=15, font=('Times', 12))
        opt2.grid(row=25, column=5, padx=10, pady=10, columnspan=5)

    def AddVarList():
        global varList
        varList.append(str(variableCols.get()))
        dispVarList = ''
        for i in varList:
            if (len(dispVarList) < 1):
                dispVarList += i
            else:
                dispVarList += ',' + i

        Label(frame,
                 text='                                                                                                                                       ',
                 bg='white', fg="#0A5688", font=("Arial", 12, "bold")).grid(row=24, column=1)

        Label(frame, text='{}'.format(dispVarList), bg='white', fg="#0A5688", font=("Arial", 12, "bold")).grid(
            row=24,
            column=1)


    # Label(frame, text="Contact :", bg='white', fg="#0A5688", font=("Arial", 12, "bold")).grid(row=25, column=6)
    # DropDownNumber()
    # VariableColumsDropDown()

    # Button(frame, text='ADD', command=AddVarList, bg='#F9D162', fg="#0A5688", font=("Helvetica", 10, "bold"), height=3,
    #        width=3, activebackground="#F3954F").grid(row=27, column=0, padx=10, pady=20)


tab1()
root.mainloop()
