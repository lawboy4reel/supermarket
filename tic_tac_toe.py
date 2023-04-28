import tkinter as tk
from tkinter import messagebox
from tkinter import Menu
from tkinter import DISABLED
import random
if __name__=="__main__":

# tkinter window interphase
    main_container = tk.Tk()
    main_container.title("welcome to LAWBOY GAME")
    main_container.geometry("340x280")
    main_container.resizable(False, False)
    main_container.config(bg="#a0b0a0")


    head_label_frame =tk.LabelFrame(main_container, borderwidth=20, background='white')
    body_label_frame = tk.LabelFrame(main_container,borderwidth=20,background='black')
    foot_label_frame = tk.LabelFrame(main_container, borderwidth=20, background='red')

    head_label_frame.grid(row=0, column=1, padx=10, pady=10)
    body_label_frame.grid(row=0, column=2, padx=10, pady=10)
    foot_label_frame.grid(row=0, column=3, padx=10, pady=10)


#  X Starts so true
    clicked = True
    count = 0
    
    
# disable all the buttons
    def disable_all_buttons():
        butt1.config(state=DISABLED)
        butt2.config(state=DISABLED)
        butt3.config(state=DISABLED)
        butt4.config(state=DISABLED)
        butt5.config(state=DISABLED)
        butt6.config(state=DISABLED)
        butt7.config(state=DISABLED)
        butt8.config(state=DISABLED)
        butt9.config(state=DISABLED)


# button clicked function
    def butt_clicked(butt):
        global clicked, count
    
        if  butt["text"] == '+' and clicked == True:
            butt["text"] = "X"
            clicked = False
            count += 1
            checkifwon()
    
        elif butt["text"] == '+' and clicked == False:
            butt["text"] = "O"
            (clicked) = True
            count += 1
            checkifwon()
            
        else: 
            messagebox.showerror("Hey! box already occupied")
    
    
# to check if there is a winner
    def checkifwon():
        global winner
        winner = False

        if  butt1["text"] == "X" and butt2["text"] == "X" and butt3["text"] == "X":
            butt1.config(bg="green") 
            butt2.config(bg="green") 
            butt3.config(bg="green")
            winner = True
            messagebox.showinfo("tic tac toe", "congratulations X WINS!!!") 
            disable_all_buttons()
        
        elif  butt4["text"] == "X" and butt5["text"] == "X" and butt6["text"] == "X":
            butt4.config(bg="green") 
            butt5.config(bg="green") 
            butt6.config(bg="green")
            winner = True
            messagebox.showinfo("tic tac toe", "congratulations X WINS!!!") 
            disable_all_buttons()
            
        if  butt1["text"] == "X" and butt2["text"] == "X" and butt3["text"] == "X":
            butt1.config(bg="green") 
            butt2.config(bg="green") 
            butt3.config(bg="green")
            winner = True
            messagebox.showinfo("tic tac toe", "congratulations X WINS!!!") 
            disable_all_buttons()

        elif  butt7["text"] == "X" and butt8["text"] == "X" and butt9["text"] == "X":
            butt7.config(bg="green") 
            butt8.config(bg="green") 
            butt9.config(bg="green")
            winner = True
            messagebox.showinfo("tic tac toe", "congratulations X WINS!!!") 
            disable_all_buttons()

        elif  butt1["text"] == "X" and butt4["text"] == "X" and butt7["text"] == "X":
            butt1.config(bg="green") 
            butt4.config(bg="green") 
            butt7.config(bg="green")
            winner = True
            messagebox.showinfo("tic tac toe", "congratulations X WINS!!!") 
            disable_all_buttons()

        elif  butt2["text"] == "X" and butt5["text"] == "X" and butt8["text"] == "X":
            butt2.config(bg="green") 
            butt5.config(bg="green") 
            butt8.config(bg="green")
            winner = True
            messagebox.showinfo("tic tac toe", "congratulations X WINS!!!") 
            disable_all_buttons()

        elif  butt3["text"] == "X" and butt6["text"] == "X" and butt9["text"] == "X":
            butt3.config(bg="green") 
            butt6.config(bg="green") 
            butt9.config(bg="green")
            winner = True
            messagebox.showinfo("tic tac toe", "congratulations X WINS!!!") 
            disable_all_buttons()

        elif  butt1["text"] == "X" and butt5["text"] == "X" and butt9["text"] == "X":
            butt1.config(bg="green") 
            butt5.config(bg="green") 
            butt9.config(bg="green")
            winner = True
            messagebox.showinfo("tic tac toe", "congratulations X WINS!!!") 
            disable_all_buttons()

        elif  butt3["text"] == "X" and butt5["text"] == "X" and butt7["text"] == "X":
            butt3.config(bg="green") 
            butt5.config(bg="green") 
            butt7.config(bg="green")
            winner = True
            messagebox.showinfo("tic tac toe", "congratulations X WINS!!!") 
            disable_all_buttons()

# check for O
        if  butt1["text"] == "O" and butt2["text"] == "O" and butt3["text"] == "O":
                butt1.config(bg="green") 
                butt2.config(bg="green") 
                butt3.config(bg="green")
                winner = True
                messagebox.showinfo("tic tac toe", "congratulations O WINS!!!") 
                disable_all_buttons()
        
        elif  butt4["text"] == "O" and butt5["text"] == "O" and butt6["text"] == "O":
                butt4.config(bg="green") 
                butt5.config(bg="green") 
                butt6.config(bg="green")
                winner = True
                messagebox.showinfo("tic tac toe", "congratulations O WINS!!!") 
                disable_all_buttons()

        elif  butt7["text"] == "O" and butt8["text"] == "O" and butt9["text"] == "O":
                butt7.config(bg="green") 
                butt8.config(bg="green") 
                butt9.config(bg="green")
                winner = True
                messagebox.showinfo("tic tac toe", "congratulations O WINS!!!") 
                disable_all_buttons()

        elif  butt1["text"] == "O" and butt4["text"] == "O" and butt7["text"] == "O":
                butt1.config(bg="green") 
                butt4.config(bg="green") 
                butt7.config(bg="green")
                winner = True
                messagebox.showinfo("tic tac toe", "congratulations O WINS!!!") 
                disable_all_buttons()

        elif  butt2["text"] == "O" and butt5["text"] == "O" and butt8["text"] == "O":
                butt2.config(bg="green") 
                butt5.config(bg="green") 
                butt8.config(bg="green")
                winner = True
                messagebox.showinfo("tic tac toe", "congratulations O WINS!!!") 
                disable_all_buttons()

        elif  butt3["text"] == "O" and butt6["text"] == "O" and butt9["text"] == "O":
                butt3.config(bg="green") 
                butt6.config(bg="green") 
                butt9.config(bg="green")
                winner = True
                messagebox.showinfo("tic tac toe", "congratulations O WINS!!!") 
                disable_all_buttons()
        elif  butt1["text"] == "O" and butt5["text"] == "O" and butt9["text"] == "O":
                butt1.config(bg="green") 
                butt5.config(bg="green") 
                butt9.config(bg="green")
                winner = True
                messagebox.showinfo("tic tac toe", "congratulations O WINS!!!") 
                disable_all_buttons()

        elif  butt3["text"] == "O" and butt5["text"] == "O" and butt7["text"] == "O":
                butt3.config(bg="green") 
                butt5.config(bg="green") 
                butt7.config(bg="green")
                winner = True
                messagebox.showinfo("tic tac toe", "congratulations O WINS!!!") 
                disable_all_buttons()
#Check if its a tie
        if count ==9 and winner == False:
                butt3.config(bg="green") 
                butt5.config(bg="green") 
                butt7.config(bg="green")
                butt2.config(bg="green") 
                butt1.config(bg="green") 
                butt9.config(bg="green")
                butt4.config(bg="green")  
                butt6.config(bg="green")
                butt8.config(bg="green")
                messagebox.showinfo("tic tac toe", "it's a Tie!\nNo Winner!")
    
# restart game
    def reset():
# build our button 
        global butt1, butt2, butt3, butt4, butt5, butt6, butt7, butt8, butt9
        global clicked, count
        clicked = True
        count = 0
        butt1 = tk.Button(body_label_frame, text='+', font=('arial' , 12, 'bold'),background='gold', width=7, height=3, command=lambda: butt_clicked(butt1)) 
        butt1.grid(column=0, row=0)

        butt2 = tk.Button(body_label_frame, text='+' , font=('arial' , 12, 'bold'),background='gold', width=7, height=3, command=lambda: butt_clicked(butt2)) 
        butt2.grid(column=1, row=0)

        butt3 = tk.Button(body_label_frame, text='+' , font=('arial' , 12, 'bold'),background='gold', width=7, height=3, command=lambda: butt_clicked(butt3)) 
        butt3.grid(column=2, row=0)

        butt4 = tk.Button(body_label_frame, text='+' , font=('arial' , 12, 'bold'),background='gold', width=7, height=3, command=lambda: butt_clicked(butt4)) 
        butt4.grid(column=0, row=1)

        butt5 = tk.Button(body_label_frame, text='+' , font=('arial' , 12, 'bold'),background='gold', width=7, height=3, command=lambda: butt_clicked(butt5)) 
        butt5.grid(column=1, row=1)

        butt6 = tk.Button(body_label_frame, text='+' , font=('arial' , 12, 'bold'),background='gold', width=7, height=3, command=lambda: butt_clicked(butt6)) 
        butt6.grid(column=2, row=1)

        butt7 = tk.Button(body_label_frame, text='+' , font=('arial' , 12, 'bold'),background='gold', width=7, height=3, command=lambda: butt_clicked(butt7)) 
        butt7.grid(column=0, row=2)

        butt8 = tk.Button(body_label_frame, text='+' , font=('arial' , 12, 'bold'),background='gold', width=7, height=3, command=lambda: butt_clicked(butt8)) 
        butt8.grid(column=1, row=2)

        butt9 = tk.Button(body_label_frame, text='+' , font=('arial' , 12, 'bold'),background='gold', width=7, height=3, command=lambda: butt_clicked(butt9)) 
        butt9.grid(column=2, row=2)
   
# create Main menu
    main_menu = Menu(main_container)
    main_container.config(menu=main_menu)

# Creating opition Menu
    option_menu = Menu(main_menu,tearoff=False)
    main_menu.add_cascade(label="Options", menu=option_menu)
    option_menu.add_command(label="Restart Game", command=reset)
    

    reset()
    
    main_container.mainloop()
