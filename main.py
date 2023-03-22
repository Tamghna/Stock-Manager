import tkinter as tk
import os
from tkinter import messagebox
ver = open("ver.txt" , 'r').read()











def view_detail():


    def view_detail_process():
        
        
        try:
            detail_nm = win4_entry1.get()

            store = open(detail_nm , 'r').read()

        except Exception:
            
            
            
            messagebox.showerror("ERROR", "STOCK NOT FOUND")



        print(store)
        

        win5 = tk.Tk()
        win5.title("DETAILS OF : " + store)
        win5.geometry("800x600")

        win5_text1 = tk.Label(win5 , text=store , font=("Impact" , 50))
        win5_text1.place(x=1 , y=1)

        win5.mainloop()

        

    win4 = tk.Tk()

    win4.geometry("800x400")

    win4.geometry("800x400")

    win4_text1 = tk.Label(win4 , text="Stock name to view details" )
    win4_text1.place(x=1 , y=1)

    win4_entry1 = tk.Entry(win4)
    win4_entry1.place(x=200 , y=1)

    win4_button1 = tk.Button(win4  , text="SUBMIT" , command=view_detail_process)
    win4_button1.place(x=1 , y=50 )

    win4.mainloop()


    





















def remove_stock():

    def remove_stock_process():
        try:
            re_nm = win3_entry1.get()
            os.remove(re_nm)
            win3.destroy()
            messagebox.showinfo("COMPLETE", "SUCESSFULLY REMOVED STOCK | STOCK REMOVED :" + re_nm)
        except Exception:
            win3.destroy()
            messagebox.showerror("ERROR", "STOCK NOT FOUND  ")

    win3 = tk.Tk()

    win3.geometry("800x400")

    win3_text1 = tk.Label(win3 , text="STOCK NAME TO REMOVE" )
    win3_text1.place(x=1 , y=1)

    win3_entry1 = tk.Entry(win3)
    win3_entry1.place(x=200 , y=1)

    win3_button1 = tk.Button(win3  , text="SUBMIT" , command=remove_stock_process)
    win3_button1.place(x=1 , y=50 )



    win3.mainloop()










def view_list():
    win2 = tk.Tk()
    win2.geometry("800x400")



    w = os.listdir()

    
    w.remove("main.py")
    w.remove("ver.txt")

    print(w)
    
    

    
    win2_text1 = tk.Label(win2 , text=w  , font=("Impact" , 20))
    win2_text1.place(x=1 , y=1)

    win2.mainloop()

































#add to stock




def add_to_stock():
    def add_to_stock_process():
        nam_item = win1_entry1.get()
        stc_qun = win1_entry2.get()
        de_itm = win1_entry3.get()

        with open(nam_item, 'a')as a:
            a.write( "Name Of Item : "+ nam_item + "\n")
            a.write( "quantity :" + stc_qun+ "\n")
            a.write(  " DETAILS OF ITEM:"+ de_itm + "\n")

        win1.destroy()

        messagebox.showinfo("COMPLETE", "STOCK ADDED SUCESSFULLY")



    win1 = tk.Tk()

    win1.geometry("800x400")

    win1_text1 = tk.Label(win1 , text="Name of item")
    win1_text1.place(x=1 , y =1)

    win1_text2 = tk.Label(win1 , text="Stock Quantity")
    win1_text2.place(x=1 , y =50)

    win1_text3 = tk.Label(win1 , text="Details")
    win1_text3.place(x=1 , y =100)


    win1_entry1 = tk.Entry(win1)
    win1_entry1.place(x=100 , y=1)

    win1_entry2 = tk.Entry(win1)
    win1_entry2.place(x=100 , y=50)

    win1_entry3 = tk.Entry(win1)
    win1_entry3.place(x=100 , y=100)

    win1_button1 = tk.Button(win1 , text="Submit" , command=add_to_stock_process)
    win1_button1.place(x=1 , y=150)

    win1.mainloop()






































#the main window
main = tk.Tk()

main.title("Stock Manager by TSOFT | VER:" + ver)

main.geometry("800x400")

main_text1 = tk.Label(main , text="Welcome" , font=("ariel" , 20))
main_text1.place(x=1 , y=1)

main_btn1 = tk.Button(main , text="Add to Stock" , command=add_to_stock)
main_btn1.place(x=1 , y=50)

main_btn2 = tk.Button(main , text="View Stock List" , command=view_list)
main_btn2.place(x=1 , y=100)


main_btn3 = tk.Button(main , text="Remove From Stock" , command=remove_stock)
main_btn3.place(x=1 , y=150)

main_btn4 = tk.Button(main , text="View details of an item" , command=view_detail)
main_btn4.place(x=1 , y=200)











main.mainloop()