from tkinter import *
from tkinter import ttk
import os
import time
import pickle
from tkinter import messagebox
from tkinter import simpledialog

screen = "lockscreen"
btnclr = 'SteelBlue3'
thistle = "SteelBlue1"
lightclr ="LightSkyBlue1"
correct = False
today = time.strftime("%Y/%m/%d")
books = ["ID-8878 Data Structures by Charles E. leirson" ,"ID-8868 Engineering Maths by Harper Lee", "ID-6878 C Programming by Zora Neale ","ID-6478 Learn Python by Zed Shaw","ID-8748 Deep Learning by Aaron Courville","ID-6154 Animal Farm by George Orwell","ID-1544 Higher Engineering by BS Grewal","ID-5485 Basic Engineering Maths by J. Bird"]
issuedbooks = ["No Record Found"]
name = "user4"
password = "12345"
def filechecker(filename):

	if os.path.isfile(filename):
		pass
	else:
		file = open(filename,"w+")
		file.close()

filechecker("library.txt")
filechecker("issued.txt")
filechecker("passwords.txt")
passlist = []
passlist.append(name)
passlist.append(password)
if os.path.getsize("passwords.txt")==0:
	with open('passwords.txt','wb') as fp:
		pickle.dump(passlist,fp)
		fp.close()

if os.path.getsize("library.txt") == 0 and len(books) !=0:

	with open('library.txt','wb') as fp:
		pickle.dump(books,fp)
		fp.close()

with open('library.txt', 'rb') as fp:
	books = pickle.load(fp)
	fp.close()

if os.path.getsize("issued.txt") == 0 and len(issuedbooks) !=0:
	with open('issued.txt', 'wb') as fp:
		pickle.dump(issuedbooks,fp)
		fp.close()

with open('issued.txt', 'rb') as fp:
	issuedbooks = pickle.load(fp)
	fp.close()

if len(issuedbooks) >1:
	del issuedbooks[0]

#=================================Library Class==============================================

class Library:

	def __init__(self,main):
	
#============================Library functions======================================
		def add_book():
			global books
			if len(self.idText.get())==0 or len(self.authorText.get())==0 or len(self.nameText.get())==0:
				messagebox.showinfo("Error","Please fill required entries: \n Book ID, Book Name and Author Name")
			else:
				text = f"ID-{self.idText.get()} {self.nameText.get().capitalize()} by {self.authorText.get().capitalize()}"
				books.append(text)
				self.bookList.insert(END,text)
				with open('library.txt', 'wb') as fp:
					pickle.dump(books, fp)
					fp.close()
				text2 = f"ID-{self.idText.get()} {self.nameText.get().capitalize()} by {self.authorText.get().capitalize()} added to library on {today}"
			 
		def issue_book():
			global issuedbooks
			if len(self.issueText.get())==0 or len(self.issuenameText.get())==0 or len(self.idText.get())==0 or len(self.returnText.get())==0:
				messagebox.showinfo("Error","Please fill required entries: \n Issuer Name , Book ID and Return Date")
			
			else:
				text = f"ID-{self.idText.get()} {self.nameText.get().capitalize()} issued by {self.issuenameText.get().capitalize()} on {today}  due date {self.issuenameText.get()}"
				issuedbooks.append(text)
				self.issuebookList.insert(0,text)
				with open('issued.txt', 'wb') as fp:
					pickle.dump(issuedbooks, fp)
					fp.close()

		def return_book():
			global books
			if len(self.issuenameText.get())==0 or len(self.idText.get())==0 or len(self.authorText.get())==0:
				messagebox.showinfo("Error","Please fill the entries: \n Book ID, Returner name and Book Author Name")
		
			else:
				text = f"ID-{self.idText.get()} {self.nameText.get()} by {self.authorText.get().capitalize()}"

				books.append(text)
				self.bookList.insert(END,text)
				with open('library.txt', 'wb') as fp:
					pickle.dump(books, fp)
					fp.close()

				text2 = f"ID-{self.idText.get()} {self.nameText.get().capitalize()} returned by {self.issuenameText.get().capitalize()} on {today}"
				issuedbooks.append(text2)
				self.issuebookList.insert(0,text2)
				with open('issued.txt', 'wb') as fp:
					pickle.dump(issuedbooks, fp)
					fp.close()

		def del_book():
			global books
			try:
				s = self.bookList.get(ACTIVE)
				books.remove(s)
				self.bookList.delete(ACTIVE)
				with open('library.txt', 'wb') as fp:
					pickle.dump(books, fp)
					fp.close()
				text = f"{s} deleted from library on {today}"
				issuedbooks.append(text)
				self.issuebookList.insert(0,text)
				with open('issued.txt', 'wb') as fp:
					pickle.dump(issuedbooks, fp)
					fp.close()
			except:
				pass
#==============================Menu functions===================================	
		def savefile():
			pass	
		def undo():
			self.main.event_generate("<<Undo>>")
		def cut():
			pass
		def copy():
			pass
		def paste():
			pass
		def quit():
			self.msg = messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
			if self.msg =="yes":
				self.main.destroy()

		def about():
			messagebox.showinfo("About","Library Management Project for ACEM ")
		def helper():
			messagebox.showinfo("Help","Enter the book name, ID and the author name to enter a book in library \n Enter bookID, issuer name and due date to issue a book \n Select a entry from the shown books list to delete a book from the library" )		
		def changepass():
			global passlist 
			newpasslist = []
			
			self.newusername = simpledialog.askstring("New username", "New Username")
			self.newpass = simpledialog.askstring("New Password", "New Password")
			newpasslist.append(self.newusername)
			newpasslist.append(self.newpass)
			with open('passwords.txt','wb') as fp:
				pickle.dump(newpasslist,fp)
				fp.close()

		self.main = main
		self.w, self.h = self.main.winfo_screenwidth(), self.main.winfo_screenheight()
		self.main.geometry("%dx%d" % (self.w, self.h))
		
		self.main.title("Library")
		self.main.configure(bg = "light sky blue")


#==============================Menubar=======================================================

		self.mainmenu = Menu(self.main)

		self.filemenu = Menu(self.mainmenu, tearoff=0, bg="grey")
		self.filemenu.add_command(label="Save", command = savefile)
		self.mainmenu.add_cascade(menu=self.filemenu,label="File")

		self.editmenu = Menu(self.mainmenu,tearoff=0,bg="grey")
		self.editmenu.add_command(label="Undo", command = undo)
		self.editmenu.add_command(label="Cut", command = cut)
		self.editmenu.add_command(label="Copy", command = copy)
		self.editmenu.add_command(label="Paste", command = paste)
		self.editmenu.add_command(label="Change Paasword", command = changepass)
		self.mainmenu.add_cascade(menu=self.editmenu,label="Edit")

		self.aboutmenu = Menu(self.mainmenu,tearoff=0,bg="grey")
		self.aboutmenu.add_command(label="About", command = about)
		self.aboutmenu.add_command(label="Exit", command = quit)
		self.aboutmenu.add_command(label="Help", command = helper)

		self.mainmenu.add_cascade(menu=self.aboutmenu,label="About")

		self.main.config(menu=self.mainmenu)

#============================Frames ==========================================================

		self.mainframe = Frame(self.main,bg = "light sky blue")
		self.mainframe.pack()
		self.tlf = Frame(self.mainframe,bd=4,relief= SUNKEN,bg=thistle)
		self.tlf.grid(row=0,column=0)
		self.trf = Frame(self.mainframe,bd=4,relief= SUNKEN,bg=thistle)
		self.trf.grid(row=0,column=1)
		self.blf = Frame(self.mainframe,bd=4,relief = SUNKEN,bg=thistle)
		self.blf.grid(row=1,column=0)
		self.brf = Frame(self.mainframe,bd=4,relief = SUNKEN,bg=thistle)
		self.brf.grid(row=1,column=1)

#==============================inside frames==============================================

#==============================Top Right Frame============================================

		Label(self.trf,text="Available books in library",font="consolas 18 bold",bg=thistle).pack(fill=X)
		self.f1 = Frame(self.trf,bg=thistle)
		self.f1.pack(fill=BOTH)
		self.scrollbooklist = Scrollbar(self.f1)
		self.scrollbooklist.pack(side=RIGHT,fill=Y)
		self.bookList = Listbox(self.f1,font="century 15 bold",bg="LightBlue1",yscrollcommand = self.scrollbooklist.set,width=34,height=15)
		self.bookList.pack(fill=X)
		for book in books:
			self.bookList.insert(END,book)

		self.scrollbooklist.config(command=self.bookList.yview)

		
#=============================Top Left Frame======================================

		Label(self.tlf,text="**Records**",font="consolas 18 bold",bg=thistle).pack(fill=X)
		self.f2 = Frame(self.tlf,bg=thistle)
		self.f2.pack(fill=BOTH)
		self.scrollissuebooklist = Scrollbar(self.f2)
		self.scrollissuebooklist.pack(side=RIGHT,fill=Y)
		self.issuebookList = Listbox(self.f2,font="century 15 bold",bg="LightBlue1",yscrollcommand = self.scrollissuebooklist.set,width=72,height=15)
		self.issuebookList.pack()

		for book in issuedbooks:
			self.issuebookList.insert(0,book)
		self.scrollissuebooklist.config(command=self.issuebookList.yview)

#=============================Bottom Left Frame==================================
		self.f3 = Frame(self.blf,bg=thistle)
		self.f3.pack(fill=Y)
		self.issueText = StringVar()
		self.issueText.set(today)
		self.returnText = StringVar()
		self.issuenameText = StringVar()
		self.authorText = StringVar()
		self.idText = StringVar()
		Label(self.f3,text="Fill Details to issue remove add or delete a book",height=2,font="consolas 20 bold",bg=thistle).grid(columnspan=2)
		self.nameText = StringVar()


		self.bookLabel = Label(self.f3,text="Book Name",width=45,bg=thistle,font="verdana 15 bold")
		self.bookLabel.grid(row =1,column=0)
		self.bookEntry = Entry(self.f3,textvariable=self.nameText,width=40,bg=lightclr,relief=SOLID)
		self.bookEntry.grid(row = 1,column=1,pady=3)

		self.idLabel = Label(self.f3,text="Book ID",bg=thistle,font="verdana 15 bold")
		self.idLabel.grid(row = 2,column=0)
		self.idEntry = Entry(self.f3,textvariable=self.idText,width=40,bg=lightclr,relief=SOLID)
		self.idEntry.grid(row = 2,column=1,pady=3)

		self.idLabel = Label(self.f3,text="Author Name",bg=thistle,font="verdana 15 bold")
		self.idLabel.grid(row = 3,column=0)
		self.idEntry = Entry(self.f3,textvariable=self.authorText,width=40,bg=lightclr,relief=SOLID)
		self.idEntry.grid(row = 3,column=1,pady=3)

		self.idLabel = Label(self.f3,text="Issue Date",bg=thistle,font="verdana 15 bold")
		self.idLabel.grid(row = 4,column=0)
		self.idEntry = Entry(self.f3,textvariable=self.issueText,width=40,bg=lightclr,relief=SOLID)
		self.idEntry.grid(row = 4,column=1,pady=3)

		self.idLabel = Label(self.f3,text="Due Date",bg=thistle,font="verdana 15 bold")
		self.idLabel.grid(row = 5,column=0)
		self.idEntry = Entry(self.f3,textvariable=self.returnText,width=40,bg=lightclr,relief=SOLID)
		self.idEntry.grid(row = 5,column=1,columnspan =2,pady=3)

		self.issueLabel = Label(self.f3,text="Name of issuer",bg=thistle,font="verdana 16 bold")
		self.issueLabel.grid(row = 6,column=0)
		self.issueEntry = Entry(self.f3,textvariable=self.issuenameText,width=40,bg=lightclr,relief=SOLID)
		self.issueEntry.grid(row = 6,column=1,pady=3)


		
#===========================Bottom Right Frame========================================

		Label(self.brf,text="Perform operations",font="consolas 18 bold",bg=thistle,width=33,height=2).pack()
		self.addbtn = Button(self.brf,font="verdana 11 bold",text="Add to Library",command =add_book,relief=GROOVE,bg =btnclr,width = 40,height=2)
		self.addbtn.pack(fill="x")
		self.dltbtn = Button(self.brf,font="verdana 11 bold",text="Remove from Library",command =del_book,relief=GROOVE,bg =btnclr,width = 40,height=2)
		self.dltbtn.pack(fill="x")
		self.issuebtn = Button(self.brf,font="verdana 11 bold",text="Issue Book",command =issue_book,relief=GROOVE,bg =btnclr,width = 40,height=2)
		self.issuebtn.pack(fill="x")
		self.returnbtn = Button(self.brf,font="verdana 11 bold",text="Return Book",command =return_book,relief=GROOVE,bg =btnclr,width = 40,height=2)
		self.returnbtn.pack(fill="x")


#==================================Login===========================================================	
class Lock:
	def __init__(self,main):
		self.namevar = StringVar()
		self.passvar = StringVar()
		def logger():
			global correct
			global screen
			global passlist
			with open('passwords.txt', 'rb') as fp:
				passlist = pickle.load(fp)
				fp.close()

			if self.namevar.get()== passlist[0] and self.passvar.get()== passlist[1]:
				correct=True
				screen=="mainscreen"
				self.main.destroy()
			else:
				messagebox.showerror("Error","Wrong Username or Password")

		self.main = main
		self.main.geometry("300x300")
		self.main.title("Library")
		self.main.configure(bg = "sky blue")

		self.user = Label(self.main,text="User Name",font="consolas 20 bold",bg="sky blue")
		self.user.grid(row=0,column = 0)
		self.username = Entry(self.main,textvariable=self.namevar)
		self.username.grid(row=0,column = 1)
		self.upass = Label(self.main,text="Password",font="consolas 20 bold",bg="sky blue")
		self.upass.grid(row=1,column = 0)
		self.userpass = Entry(self.main,textvariable=self.passvar)
		self.userpass.grid(row=1,column = 1)
		Button(self.main,text="Log In",command=logger,font="consolas 10 bold",width=25).grid(row=2,column = 0,columnspan=2,pady =20)

if screen=="lockscreen":
	main=Tk()
	app = Lock(main)
	main.mainloop()
	if correct == True:
		screen="mainscreen"

if screen=="mainscreen":
	main=Tk()
	app = Library(main)
	main.mainloop()
