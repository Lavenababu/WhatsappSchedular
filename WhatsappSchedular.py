from tkinter import *
import pywhatkit

root=Tk()
root.title("Python Project")
root.geometry('300x480')
# root['bg']='#075E54'
icon =  PhotoImage(file="WpLogo.png")
root.iconphoto(True, icon)

frame=Frame(root)
frame.grid(row=0, column=0)

#1st frame
def tab1():

    # 2nd frame
    def tab2():
        # to destroy all the widgets currently on the window
        for widgets in frame.winfo_children():
            widgets.destroy()

        label=Label(frame, text="History...", font="Times 12", bg="#075E54", fg="#ffffff")
        label.grid(row=0, column=0, ipadx=100, columnspan=8)
        txtarea = Text(frame, width=35, height=25)
        txtarea.grid(row=1, column=0, pady=10, columnspan=4)

        # to open History file in read only format
        tf = open("PyWhatKit_DB.txt")
        data = tf.read()
        txtarea.insert(END, data)
        tf.close()
        txtarea.configure(state='disabled')

        def back():
            # to destroy all the widgets currently on the window
            for widgets in frame.winfo_children():
                widgets.destroy()
            tab1()

        button2 = Button(frame, text="Back", command=back, bg="#075E54", fg="#ffffff")
        button2.grid(row=10, column=1, ipadx=10)

    title = Label(frame, text="Whatsapp Scheduler", font="times 15 bold", bg="#075E54", fg="#ffffff")
    title.grid(row=0, column=0, ipadx=70, columnspan=8)

    nameLabel = Label(frame, text="Message : ")
    nameLabel.grid(row=2, column=0, padx=20, pady=20, sticky=W)
    phoneLabel = Label(frame, text="Phone No. : ")
    phoneLabel.grid(row=3, column=0, padx=20, pady=20, sticky=W)
    timeLabel = Label(frame, text="Time : ")
    timeLabel.grid(row=4, column=0, padx=20, pady=20, sticky=W)

    msg = Entry(frame)
    msg.grid(row=2, column=2)

    text2 = Entry(frame)
    text2.insert(0, "+91 ")
    text2.grid(row=3, column=2)

    time = Entry(frame)
    time.grid(row=4, column=2)

    def onclick():
        # to get time from textbox and seprate and covert them from string to integer
        c = time.get()
        hr = str(c[0]) + str(c[1])
        min = str(c[3]) + str(c[4])

        pywhatkit.sendwhatmsg(text2.get(),
                              msg.get(),
                              int(hr), int(min))

    SendMsg = Button(frame, text="Send", command=onclick, bg="#075E54", fg="#ffffff")
    SendMsg.grid(row=6, column=2, padx=20, pady=20)

    ShowHistory = Button(frame, text="Show History", command=tab2, bg="#075E54", fg="#ffffff")
    ShowHistory.grid(row=8, column=0, padx=20, pady=20, sticky=W)

    # To send message to a group
    groupLabel = Label(frame, text="Group Link : ")
    groupLabel.grid(row=7, column=0, padx=20, pady=20)
    group = Entry(frame)
    group.grid(row=7, column=2)
    def onclickgrp():

        c = time.get()
        hr = str(c[0]) + str(c[1])
        min = str(c[3]) + str(c[4])

        pywhatkit.sendwhatmsg_to_group(group.get(),
                                       msg.get(),
                                       int(hr), int(min))
    SendGrpMsg = Button(frame, text="Send Msg to Grp", command=onclickgrp, bg="#075E54", fg="#ffffff")
    SendGrpMsg.grid(row=8, column=2, padx=20, pady=20)

tab1()
root.mainloop()
