from tkinter import *
import pywhatkit

root=Tk()
root.title("Python Project")
root.geometry('300x500')
icon =  PhotoImage(file="WpLogo.png")
root.iconphoto(True, icon)

frame=Frame(root)
# frame.pack(side="top", expand=True, fill="both")
frame.grid(row=0, column=0)

def tab1():

    def tab2():
        for widgets in frame.winfo_children():
            widgets.destroy()

        label=Label(frame, text="History...", font="Times 12")
        label.grid(row=0, column=0)
        txtarea = Text(frame, width=35, height=25)
        txtarea.grid(row=1, column=0, pady=10, columnspan=4)

        # def openFile():
        tf = open("PyWhatKit_DB.txt")
        data = tf.read()
        txtarea.insert(END, data)
        tf.close()
        txtarea.configure(state='disabled')

        # ShowHistory = Button(frame, text="Show History", command=openFile)
        # ShowHistory.grid(row=8, column=1,  padx=20, pady=20)

        def back():
            for widgets in frame.winfo_children():
                widgets.destroy()
            tab1()

        button2 = Button(frame, text="Back", command=back)
        button2.grid(row=10, column=1, ipadx=10)

    # Tab 1
    # title = Label(frame, text="Whatsapp Scheduler", font="times 15 bold", bg="#075E54", fg="#ffffff")
    # title.grid(row=0, column=0)
    # l=Label(frame, text="Page 1")
    # l.grid(row=1, column=0)
    # button = Button(frame, text="Next", command=tab2)
    # button.grid(row=2, column=0)

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

        c = time.get()
        hr = str(c[0]) + str(c[1])
        min = str(c[3]) + str(c[4])

        pywhatkit.sendwhatmsg(text2.get(),
                              msg.get(),
                              int(hr), int(min))

    # padx=30(length) pady=10(height) fg="blue"(text color) bg(background)
    SendMsg = Button(frame, text="Send", command=onclick)
    SendMsg.grid(row=6, column=2, padx=20, pady=20, sticky=W)

    NextPage = Button(frame, text="Show History", command=tab2)
    NextPage.grid(row=7, column=2, padx=20, pady=20, sticky=W)

tab1()
root.mainloop()
