from tkinter import *
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox


root = Tk()
root.title("Contact List")
width = 700
height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="#6666ff")
#============================VARIABLES===================================
FIRSTNAME = StringVar()
LASTNAME = StringVar()
GENDER = StringVar()
AGE = StringVar()
ADDRESS = StringVar()
CONTACT = StringVar()
#============================METHODS=====================================
def Database():
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT, firstname TEXT, lastname TEXT, gender TEXT,
                   age TEXT, address TEXT, contact TEXT)""")   
    cursor.execute("SELECT * FROM `member` ORDER BY `lastname` ASC")   
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()
    
def SubmitData():
    if  FIRSTNAME.get() == "" or LASTNAME.get() == "" or GENDER.get() == "" or AGE.get() == "" or ADDRESS.get() == "" or CONTACT.get() == "":
        result = tkMessageBox.showwarning('', 'Please Complete The Required Field', icon="warning")
     else:
        tree.delete(*tree.get_children())
        conn = sqlite3.connect("pythontut.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO `member` (firstname, lastname, gender, age, address, contact) VALUES(?, ?, ?, ?, ?, ?)",
                       (str(FIRSTNAME.get()), str(LASTNAME.get()), str(GENDER.get()), int(AGE.get()), str(ADDRESS.get()), str(CONTACT.get())))
        conn.commit()
        cursor.execute("SELECT * FROM `member` ORDER BY `lastname` ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        FIRSTNAME.set("")     
        LASTNAME.set("")       
        GENDER.set("")       
        AGE.set("")       
        ADDRESS.set("")       
        CONTACT.set("")
        
def UpdateData():
    if GENDER.get() == "":
       result = tkMessageBox.showwarning('', 'Please Complete The Required Field', icon="warning")
    else:
        tree.delete(*tree.get_children())
        conn = sqlite3.connect("pythontut.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE `member` SET `firstname` = ?, `lastname` = ?, `gender` =?, `age` = ?,  `address` = ?, `contact` = ? WHERE `mem_id` = ?",
                       (str(FIRSTNAME.get()), str(LASTNAME.get()), str(GENDER.get()), str(AGE.get()), str(ADDRESS.get()), str(CONTACT.get()), int(mem_id)))
        conn.commit()
        cursor.execute("SELECT * FROM `member` ORDER BY `lastname` ASC")        fetch = cursor.fetchall()        for data in fetch:            tree.insert('', 'end', values=(data))        cursor.close()       
        conn.close()       
        FIRSTNAME.set("")       
        LASTNAME.set("")       
        GENDER.set("")       
        AGE.set("")       
        ADDRESS.set("")       
        CONTACT.set("")

def OnSelected(event):   
    global mem_id, UpdateWindow   
    curItem = tree.focus()   
    contents =(tree.item(curItem))   
    selecteditem = contents['values']   
    mem_id = selecteditem[0]   
    FIRSTNAME.set("")   
    LASTNAME.set("")   
    GENDER.set("")   
    AGE.set("")   
    ADDRESS.set("")   
    CONTACT.set("")   
    FIRSTNAME.set(selecteditem[1])   
    LASTNAME.set(selecteditem[2])   
    AGE.set(selecteditem[4])   
    ADDRESS.set(selecteditem[5])   
    CONTACT.set(selecteditem[6])   
    UpdateWindow = Toplevel()   
    UpdateWindow.title("Contact List")   
    width = 400   
    height = 300   
    screen_width = root.winfo_screenwidth()   
    screen_height = root.winfo_screenheight()   
    x = ((screen_width/2) + 450) - (width/2)   
    y = ((screen_height/2) + 20) - (height/2)   
    UpdateWindow.resizable(0, 0)   
    UpdateWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))   
    if 'NewWindow' in globals():       
             NewWindow.destroy()

#===================FRAMES==============================   
             FormTitle = Frame(UpdateWindow)   
             FormTitle.pack(side=TOP)   
             ContactForm = Frame(UpdateWindow)   
             ContactForm.pack(side=TOP, pady=10)   
             RadioGroup = Frame(ContactForm)   
             Male = Radiobutton(RadioGroup, text="Male", variable=GENDER, value="Male",  font=('arial', 14)).pack(side=LEFT)   
             Female = Radiobutton(RadioGroup, text="Female", variable=GENDER, value="Female",  font=('arial', 14)).pack(side=LEFT)
  #===================LABELS==============================
    lbl_title = Label(FormTitle, text="Updating Contacts", font=('arial', 16), bg="orange",  width = 300)
    lbl_title.pack(fill=X)
    lbl_firstname = Label(ContactForm, text="Firstname", font=('arial', 14), bd=5)
    lbl_firstname.grid(row=0, sticky=W)
    lbl_lastname = Label(ContactForm, text="Lastname", font=('arial', 14), bd=5)
    lbl_lastname.grid(row=1, sticky=W)
    lbl_gender = Label(ContactForm, text="Gender", font=('arial', 14), bd=5)
    lbl_gender.grid(row=2, sticky=W)
    lbl_age = Label(ContactForm, text="Age", font=('arial', 14), bd=5)
    lbl_age.grid(row=3, sticky=W)
    lbl_address = Label(ContactForm, text="Address", font=('arial', 14), bd=5)
    lbl_address.grid(row=4, sticky=W)
    lbl_contact = Label(ContactForm, text="Contact", font=('arial', 14), bd=5)
    lbl_contact.grid(row=5, sticky=W)    
#===================ENTRY===============================
    firstname = Entry(ContactForm, textvariable=FIRSTNAME, font=('arial', 14))   
    firstname.grid(row=0, column=1)   
    lastname = Entry(ContactForm, textvariable=LASTNAME, font=('arial', 14))   
    lastname.grid(row=1, column=1)   
    RadioGroup.grid(row=2, column=1)   
    age = Entry(ContactForm, textvariable=AGE,  font=('arial', 14))   
    age.grid(row=3, column=1)   
    address = Entry(ContactForm, textvariable=ADDRESS,  font=('arial', 14)) 
    address.grid(row=4, column=1)   
    contact = Entry(ContactForm, textvariable=CONTACT,  font=('arial', 14))   
    contact.grid(row=5, column=1)











        
