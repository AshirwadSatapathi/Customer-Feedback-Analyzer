from tkinter import*
import tkinter as tk
from tkinter import ttk
from textblob import TextBlob
import sqlite3

conn = sqlite3.connect('Customer.db')
c = conn.cursor()

name=''
regd=''
faculty=''
subject=''
score=''
text = ''

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS CustomerFeedback (order_id INT, name TEXT, Product TEXT, Seller TEXT, feed TEXT, score REAL)")
def input():
    global inputRes
    inputRes= result.get("1.0","end-1c")
    return inputRes
def data_entry():
    pass
   
    

def check():
    text = input()
    name = nameS.get()
    order_id = regdN.get()
    product = nameE.get()
    seller = subjectE.get()
    s = TextBlob(text)
    score = s.sentiment.polarity
    print(name)
    print(order_id)
    print(product)
    print(seller)
    print(text)
    print(score)
    create_table()
    c.execute("INSERT INTO CustomerFeedback(order_id,name,Product,Seller,feed,score) VALUES(?,?,?,?,?,?)",(order_id,name,product,seller,text,score))
    conn.commit()
    #c.close()
    #conn.close()

    data_entry()
    print("it's done")

def exit():
    c.close()
    conn.close()

root = tk.Tk()
root.title("Sentiment analysis on Customer feedback form")

Module = Label(root, text = "Customer Module", font =("arial",17,"bold"))
Module.grid(row = 0, column = 0, columnspan = 2, padx = 5, sticky = W)

customerName = Label(root, text = "Customer Name")
customerName.grid(row = 1, column = 0, columnspan = 1, padx = 5, sticky = W)

nameS = Entry(root, width = 50)
nameS.grid(row=1,column = 1)



regdNo = Label(root, text = "Order ID")
regdNo.grid(row = 2, column = 0, columnspan = 1, padx = 5, sticky = W)


regdN = Entry(root, width = 50)
regdN.grid(row=2,column = 1)


name = Label(root, text = "Prodcut Name")
name.grid(row = 3, column = 0, columnspan = 1, padx = 5, sticky = W)

nameE = tk.StringVar()                         # 2
nameChosen = ttk.Combobox(root, width=47, textvariable=nameE) #3
nameChosen['values'] = ('Select a Product','Redmi Note 7','Redmi Note 7 Pro','Samsung M10','Samsung M20','Realme 3')     # 4
nameChosen.grid(column=1, row=3,padx=5)              # 5
nameChosen.current(0)   


subject = Label(root, text = "Seller Name")
subject.grid(row = 4, column = 0, columnspan = 1, padx = 5, sticky = W)

subjectE = tk.StringVar()                         # 2
subjectChosen = ttk.Combobox(root, width=47, textvariable=subjectE) #3
subjectChosen['values'] = ('Select a Seller','Amazon','Flipkart','Snapdeal','Ebay')# 4
subjectChosen.grid(column=1, row=4,padx=5)              # 5
subjectChosen.current(0)   

feedback =  Label(root, text = "Feedback", font=("arial",14,"bold"))
feedback.grid(row = 5, column = 0, columnspan = 2, padx = 5, sticky = W)

result = Text(root, width = 60, height = 6, wrap = WORD)
result.grid(row = 6, column = 0, columnspan = 3, padx = 5, sticky = W)

check = Button(root, text = "Submit", command = check)
check.grid(row=7, columnspan = 3, pady=10)


root.mainloop()

