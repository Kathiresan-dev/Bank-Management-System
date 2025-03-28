import tkinter as tk
from tkinter import messagebox
import mysql.connector as mysql

class bank():
    def __init__(self, root):
        self.root = root
        self.root.title("Bank Management System")
        
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")
        self.root.configure(bg='#08192D')
        
        mainLabel = tk.Label(self.root, text="Bank Account Management System", font=("Arial",40,"bold"), bg="#fe0058", bd=5, relief='groove')
        mainLabel.pack(side='top', fill='x')    
        
        mainFrame = tk.Frame(self.root, bg='#383870', bd=5, relief='ridge')
        mainFrame.place(x=525, y=120, width=450, height=550)
        
        openACBtn = tk.Button(mainFrame, command=self.openAc, width=20, text='Open Account', bg='#fe0058', bd=3, relief='raised', font=("Arial",20,"bold"))
        openACBtn.grid(row=0, column=0, padx=40, pady=60)
        
        depBtn = tk.Button(mainFrame, command=self.deposit , width=20,  text='Deposit', bg='#fe0058', bd=3, relief='raised',  font=("Arial",20,"bold"))
        depBtn.grid(row=1, column=0, padx=40, pady=60)
        
        wdBtn = tk.Button(mainFrame,command=self.wd ,width=20, text='Withdraw', bg='#fe0058', bd=3, relief='raised', font=("Arial",20,"bold"))
        wdBtn.grid(row=2, column=0, padx=40, pady=60)

    def openAc(self):
        self.openAcFrame = tk.Frame(self.root, bg="#383870", bd=5, relief='ridge')
        self.openAcFrame.place(x=525, y=120, width=450, height=550)
        
        uNameLabel = tk.Label(self.openAcFrame, text="User Name:", bg="#383870", font=("Arial",15,"bold"))
        uNameLabel.grid(row=0, column=0, padx=20, pady=30)
        
        self.uNameIn = tk.Entry(self.openAcFrame, width=15, font=("Arial",15))
        self.uNameIn.grid(row=0, column=1, padx=5, pady=30)
        
        uPWLabel = tk.Label(self.openAcFrame, text="Enter Password:", bg="#383870", font=("Arial",15,"bold"))
        uPWLabel.grid(row=1, column=0, padx=20, pady=30)
        
        self.uPWIn = tk.Entry(self.openAcFrame, width=15, font=("Arial",15))
        self.uPWIn.grid(row=1, column=1, padx=5, pady=30)
        
        confirmLabel = tk.Label(self.openAcFrame, text="Confirm Password:", bg="#383870", font=("Arial",15,"bold"))
        confirmLabel.grid(row=2, column=0, padx=20, pady=30)
        
        self.confirmIn = tk.Entry(self.openAcFrame, width=15, font=("Arial",15))
        self.confirmIn.grid(row=2, column=1, padx=5, pady=30)
        
        okBtn =tk.Button(self.openAcFrame,command=self.insert,text="OK",width=10,bg='#fe0058',bd=3,relief='raised',font=("Arial",15,"bold"))
        okBtn.grid(row=3,column=0,padx=40,pady=90)
        
        closeBtn =tk.Button(self.openAcFrame,command=self.close_openAc,text="Close",width=10,bg='#fe0058',bd=3,relief='raised',font=("Arial",15,"bold"))
        closeBtn.grid(row=3,column=1,padx=40,pady=90)
        
    def close_openAc(self):
        self.openAcFrame.destroy()
        
    def insert(self):
        uName = self.uNameIn.get()
        uPW = self.uPWIn.get()
        confirm = self.confirmIn.get()
        
        if not uName or not uPW:
            tk.messagebox.showerror("Error", "Both Username and Password are required!")
            return

        
        
        if uPW == confirm:
            con= mysql.connect(host="localhost",user="root",passwd="K@30020160",port="3306",database='sample12')
            cursor=con.cursor()
            cursor.execute("INSERT INTO account (userName, userPw,balance) VALUES (%s, %s,0)", (uName, uPW))
            con.commit()
            con.close()
            tk.messagebox.showinfo("Success","Account Opened Successfully")
            self.clear()
        else:
            tk.messagebox.showerror("Error","Both Passwords Should Same!")
            self.clear()
            
    def clear(self):
        self.uNameIn.delete(0,tk.END)
        self.uPWIn.delete(0,tk.END)
        self.confirmIn.delete(0,tk.END)    
            
    def deposit(self):
        self.depFrame = tk.Frame(self.root, bg="#383870", bd=5, relief='ridge')
        self.depFrame.place(x=525, y=120, width=450, height=550)
        
        NameLabel = tk.Label(self.depFrame, text="User Name:", bg="#383870", font=("Arial",15,"bold"))
        NameLabel.grid(row=0, column=0, padx=20, pady=30)
        
        self.NameIn = tk.Entry(self.depFrame, width=15, font=("Arial",15))
        self.NameIn.grid(row=0, column=1, padx=5, pady=30)
        
        amountLabel = tk.Label(self.depFrame, text="Enter Amount", bg="#383870", font=("Arial",15,"bold"))
        amountLabel.grid(row=1, column=0, padx=20, pady=30)
        
        self.amountIn = tk.Entry(self.depFrame, width=15, font=("Arial",15))
        self.amountIn.grid(row=1, column=1, padx=5, pady=30)
        
        okBtn = tk.Button(self.depFrame, command=self.deposit_fun, text="Deposit", width=10, bg='#fe0058', bd=3, relief='raised', font=("Arial", 15, "bold"))
        okBtn.grid(row=2,column=0,padx=40,pady=150)
        
        closeBtn =tk.Button(self.depFrame,command=self.close_deposit,text="Close",width=10,bg='#fe0058',bd=3,relief='raised',font=("Arial",15,"bold"))
        closeBtn.grid(row=2,column=1,padx=40,pady=150)
        
    def deposit_fun(self):
        name = self.NameIn.get()
        amount = int(self.amountIn.get()) 
        
        con= mysql.connect(host="localhost",user="root",passwd="K@30020160",port="3306",database='sample12')
        cur=con.cursor()
        cur.execute("select balance from account where userName=%s",(name,))
        data= cur.fetchone()
        if data:
            balance = data[0]
            if data[0] is None:
                balance=0
            update = balance +amount
            cur.execute("update account set balance=%s where userName=%s" , (update,name))
            con.commit()
            con.close()
            tk.messagebox.showinfo("Success","Operation was Successful")
        
        else:
            tk.messagebox.showerror("Error","Invalid Customer Name!")
    def close_deposit(self):
        self.depFrame.destroy()
        
    def wd(self):
        self.wdFrame = tk.Frame(self.root, bg="#383870", bd=5, relief='ridge')
        self.wdFrame.place(x=525, y=120, width=450, height=550)
        
        cNameLabel = tk.Label(self.wdFrame, text="User Name:", bg="#383870", font=("Arial",15,"bold"))
        cNameLabel.grid(row=0, column=0, padx=20, pady=30)
        
        self.cNameIn = tk.Entry(self.wdFrame, width=15, font=("Arial",15))
        self.cNameIn.grid(row=0, column=1, padx=5, pady=30)
        
        cPWLabel = tk.Label(self.wdFrame, text="Enter Password:", bg="#383870", font=("Arial",15,"bold"))
        cPWLabel.grid(row=1, column=0, padx=20, pady=30)
        
        self.cPWIn = tk.Entry(self.wdFrame, width=15, font=("Arial",15))
        self.cPWIn.grid(row=1, column=1, padx=5, pady=30)
        
        wdLabel = tk.Label(self.wdFrame, text="Enter Amount:", bg="#383870", font=("Arial",15,"bold"))
        wdLabel.grid(row=2, column=0, padx=20, pady=30)
        
        self.wdIn = tk.Entry(self.wdFrame, width=15, font=("Arial",15))
        self.wdIn.grid(row=2, column=1, padx=5, pady=30)
        
        okBtn =tk.Button(self.wdFrame,command=self.wd_fun,text="Withdraw",width=10,bg='#fe0058',bd=3,relief='raised',font=("Arial",15,"bold"))
        okBtn.grid(row=3,column=0,padx=40,pady=90)
        
        closeBtn =tk.Button(self.wdFrame,command=self.close_wd,text="Close",width=10,bg='#fe0058',bd=3,relief='raised',font=("Arial",15,"bold"))
        closeBtn.grid(row=3,column=1,padx=40,pady=90)
        
    def wd_fun(self):
        name = self.cNameIn.get()
        pw = self.cPWIn.get()
        amount = int(self.wdIn.get())
        
        
        con= mysql.connect(host="localhost",user="root",passwd="K@30020160",port="3306",database='sample12')
        cur=con.cursor()
        cur.execute("select userPW,balance from account where userName=%s",(name,))
        data = cur.fetchone()
        if data:
            if data[0]==pw:
                if data[1] >= amount:
                    update = data[1] - amount
                    cur.execute("update account set balance=%s where userName=%s",(update,name))
                    con.commit()
                    con.close()
                    tk.messagebox.showinfo("Success","Operation was successful")
                else:
                    tk.messagebox.showerror("Error","Invalid Insufficient Balance!")
                
            else:
                tk.messagebox.showerror("Error","Invalid Customer password!")    
            
        else:
            tk.messagebox.showerror("Error","Invalid Customer Name!")   
        
    def close_wd(self):
        self.wdFrame.destroy()
        
# Main loop
root = tk.Tk()
obj = bank(root)
root.mainloop()