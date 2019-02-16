def call1():
    global root
    from tkinter import Button, Tk,Label,W
    from tkinter import messagebox
    root = Tk()
    root.title("tic-tac-toe")
    root.geometry("355x500")
    root.wm_minsize(width=70, height=100)
    # root.maxsize(width=100,height=100)
    ####################################################
    global flag1,flag,count123, count456, count789, count147, count258, count369, count159, count357
    global count0123, count0456, count0789, count0147, count0258, count0369, count0159, count0357
    flag1 = 0
    flag = 0
    count123, count456, count789, count147, count258, count369, count159, count357 = 0, 0, 0, 0, 0, 0, 0, 0
    count0123, count0456, count0789, count0147, count0258, count0369, count0159, count0357 = 0, 0, 0, 0, 0, 0, 0, 0

    def click1():
        global flag
        global flag1
        if l1["text"] == "X" and l2["text"] == "X" and l3["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l4["text"] == "X" and l5["text"] == "X" and l6["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l7["text"] == "X" and l8["text"] == "X" and l9["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l1["text"] == "X" and l4["text"] == "X" and l7["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l2["text"] == "X" and l5["text"] == "X" and l8["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l3["text"] == "X" and l6["text"] == "X" and l9["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l1["text"] == "X" and l5["text"] == "X" and l9["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l3["text"] == "X" and l5["text"] == "X" and l7["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        #############################################################################
        elif l1["text"] == "0" and l2["text"] == "0" and l3["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l4["text"] == "0" and l5["text"] == "0" and l6["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l7["text"] == "0" and l8["text"] == "0" and l9["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l1["text"] == "0" and l4["text"] == "0" and l7["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l2["text"] == "0" and l5["text"] == "0" and l8["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l3["text"] == "0" and l6["text"] == "0" and l9["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l1["text"] == "0" and l5["text"] == "0" and l9["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l3["text"] == "0" and l5["text"] == "0" and l7["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        #########################################################################
        elif flag == 0 and l1["text"] == "":
            l1.configure(text="X", bg="yellow")
            flag = 1
            flag1 = flag1 + 1
            # print(flag1)
        elif flag == 1 and l1["text"] == "":
            l1.configure(text="0", bg="cyan")
            flag = 0
            flag1 = flag1 + 1
            # print(flag1)
        winX()
        win0()

    def click2():
        global flag
        global flag1
        if l1["text"] == "X" and l2["text"] == "X" and l3["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l4["text"] == "X" and l5["text"] == "X" and l6["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l7["text"] == "X" and l8["text"] == "X" and l9["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l1["text"] == "X" and l4["text"] == "X" and l7["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l2["text"] == "X" and l5["text"] == "X" and l8["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l3["text"] == "X" and l6["text"] == "X" and l9["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l1["text"] == "X" and l5["text"] == "X" and l9["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l3["text"] == "X" and l5["text"] == "X" and l7["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        #####################################################################
        elif l1["text"] == "0" and l2["text"] == "0" and l3["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l4["text"] == "0" and l5["text"] == "0" and l6["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l7["text"] == "0" and l8["text"] == "0" and l9["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l1["text"] == "0" and l4["text"] == "0" and l7["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l2["text"] == "0" and l5["text"] == "0" and l8["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l3["text"] == "0" and l6["text"] == "0" and l9["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l1["text"] == "0" and l5["text"] == "0" and l9["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l3["text"] == "0" and l5["text"] == "0" and l7["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        ################################################################3
        elif flag == 0 and l2["text"] == "":
            l2.configure(text="X", bg="yellow")
            flag = 1
            flag1 = flag1 + 1
            # print(flag1)
        elif flag == 1 and l2["text"] == "":
            l2.configure(text="0", bg="cyan")
            flag = 0
            flag1 = flag1 + 1
            # print(flag1)
        winX()
        win0()

    def click3():
        global flag
        global flag1
        if l1["text"] == "X" and l2["text"] == "X" and l3["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l4["text"] == "X" and l5["text"] == "X" and l6["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l7["text"] == "X" and l8["text"] == "X" and l9["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l1["text"] == "X" and l4["text"] == "X" and l7["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l2["text"] == "X" and l5["text"] == "X" and l8["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l3["text"] == "X" and l6["text"] == "X" and l9["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l1["text"] == "X" and l5["text"] == "X" and l9["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l3["text"] == "X" and l5["text"] == "X" and l7["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        ############################################################################
        elif l1["text"] == "0" and l2["text"] == "0" and l3["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l4["text"] == "0" and l5["text"] == "0" and l6["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l7["text"] == "0" and l8["text"] == "0" and l9["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l1["text"] == "0" and l4["text"] == "0" and l7["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l2["text"] == "0" and l5["text"] == "0" and l8["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l3["text"] == "0" and l6["text"] == "0" and l9["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l1["text"] == "0" and l5["text"] == "0" and l9["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l3["text"] == "0" and l5["text"] == "0" and l7["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        ##############################################################
        elif flag == 0 and l3["text"] == "":
            l3.configure(text="X", bg="yellow")
            flag = 1
            flag1 = flag1 + 1
            # print(flag1)
        elif flag == 1 and l3["text"] == "":
            l3.configure(text="0", bg="cyan")
            flag = 0
            flag1 = flag1 + 1
            # print(flag1)
        winX()
        win0()

    def click4():
        global flag
        global flag1
        if l1["text"] == "X" and l2["text"] == "X" and l3["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l4["text"] == "X" and l5["text"] == "X" and l6["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l7["text"] == "X" and l8["text"] == "X" and l9["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l1["text"] == "X" and l4["text"] == "X" and l7["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l2["text"] == "X" and l5["text"] == "X" and l8["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l3["text"] == "X" and l6["text"] == "X" and l9["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l1["text"] == "X" and l5["text"] == "X" and l9["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l3["text"] == "X" and l5["text"] == "X" and l7["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        ##########################################################################
        elif l1["text"] == "0" and l2["text"] == "0" and l3["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l4["text"] == "0" and l5["text"] == "0" and l6["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l7["text"] == "0" and l8["text"] == "0" and l9["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l1["text"] == "0" and l4["text"] == "0" and l7["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l2["text"] == "0" and l5["text"] == "0" and l8["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l3["text"] == "0" and l6["text"] == "0" and l9["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l1["text"] == "0" and l5["text"] == "0" and l9["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l3["text"] == "0" and l5["text"] == "0" and l7["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        ######################################################################
        elif flag == 0 and l4["text"] == "":
            l4.configure(text="X", bg="yellow")
            flag = 1
            flag1 = flag1 + 1
            # print(flag1)
        elif flag == 1 and l4["text"] == "":
            l4.configure(text="0", bg="cyan")
            flag = 0
            flag1 = flag1 + 1
            # print(flag1)
        winX()
        win0()

    def click5():
        global flag
        global flag1
        if l1["text"] == "X" and l2["text"] == "X" and l3["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l4["text"] == "X" and l5["text"] == "X" and l6["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l7["text"] == "X" and l8["text"] == "X" and l9["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l1["text"] == "X" and l4["text"] == "X" and l7["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l2["text"] == "X" and l5["text"] == "X" and l8["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l3["text"] == "X" and l6["text"] == "X" and l9["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l1["text"] == "X" and l5["text"] == "X" and l9["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l3["text"] == "X" and l5["text"] == "X" and l7["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        #########################################################################
        elif l1["text"] == "0" and l2["text"] == "0" and l3["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l4["text"] == "0" and l5["text"] == "0" and l6["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l7["text"] == "0" and l8["text"] == "0" and l9["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l1["text"] == "0" and l4["text"] == "0" and l7["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l2["text"] == "0" and l5["text"] == "0" and l8["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l3["text"] == "0" and l6["text"] == "0" and l9["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l1["text"] == "0" and l5["text"] == "0" and l9["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l3["text"] == "0" and l5["text"] == "0" and l7["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        ########################################################################
        elif flag == 0 and l5["text"] == "":
            l5.configure(text="X", bg="yellow")
            flag = 1
            flag1 = flag1 + 1
            # print(flag1)
        elif flag == 1 and l5["text"] == "":
            l5.configure(text="0", bg="cyan")
            flag = 0
            flag1 = flag1 + 1
            # print(flag1)
        winX()
        win0()

    def click6():
        global flag
        global flag1
        if l1["text"] == "X" and l2["text"] == "X" and l3["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l4["text"] == "X" and l5["text"] == "X" and l6["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l7["text"] == "X" and l8["text"] == "X" and l9["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l1["text"] == "X" and l4["text"] == "X" and l7["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l2["text"] == "X" and l5["text"] == "X" and l8["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l3["text"] == "X" and l6["text"] == "X" and l9["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l1["text"] == "X" and l5["text"] == "X" and l9["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l3["text"] == "X" and l5["text"] == "X" and l7["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        ######################################################################
        elif l1["text"] == "0" and l2["text"] == "0" and l3["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l4["text"] == "0" and l5["text"] == "0" and l6["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l7["text"] == "0" and l8["text"] == "0" and l9["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l1["text"] == "0" and l4["text"] == "0" and l7["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l2["text"] == "0" and l5["text"] == "0" and l8["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l3["text"] == "0" and l6["text"] == "0" and l9["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l1["text"] == "0" and l5["text"] == "0" and l9["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l3["text"] == "0" and l5["text"] == "0" and l7["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        #####################################################################
        elif flag == 0 and l6["text"] == "":
            l6.configure(text="X", bg="yellow")
            flag = 1
            flag1 = flag1 + 1
            # print(flag1)
        elif flag == 1 and l6["text"] == "":
            l6.configure(text="0", bg="cyan")
            flag = 0
            flag1 = flag1 + 1
            # print(flag1)
        winX()
        win0()

    def click7():
        global flag
        global flag1
        if l1["text"] == "X" and l2["text"] == "X" and l3["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l4["text"] == "X" and l5["text"] == "X" and l6["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l7["text"] == "X" and l8["text"] == "X" and l9["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l1["text"] == "X" and l4["text"] == "X" and l7["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l2["text"] == "X" and l5["text"] == "X" and l8["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l3["text"] == "X" and l6["text"] == "X" and l9["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l1["text"] == "X" and l5["text"] == "X" and l9["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l3["text"] == "X" and l5["text"] == "X" and l7["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        #########################################################################
        elif l1["text"] == "0" and l2["text"] == "0" and l3["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l4["text"] == "0" and l5["text"] == "0" and l6["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l7["text"] == "0" and l8["text"] == "0" and l9["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l1["text"] == "0" and l4["text"] == "0" and l7["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l2["text"] == "0" and l5["text"] == "0" and l8["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l3["text"] == "0" and l6["text"] == "0" and l9["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l1["text"] == "0" and l5["text"] == "0" and l9["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l3["text"] == "0" and l5["text"] == "0" and l7["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        ###################################################################
        elif flag == 0 and l7["text"] == "":
            l7.configure(text="X", bg="yellow")
            flag = 1
            flag1 = flag1 + 1
            # print(flag1)
        elif flag == 1 and l7["text"] == "":
            l7.configure(text="0", bg="cyan")
            flag = 0
            flag1 = flag1 + 1
            # print(flag1)
        winX()
        win0()

    def click8():
        global flag
        global flag1
        if l1["text"] == "X" and l2["text"] == "X" and l3["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l4["text"] == "X" and l5["text"] == "X" and l6["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l7["text"] == "X" and l8["text"] == "X" and l9["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l1["text"] == "X" and l4["text"] == "X" and l7["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l2["text"] == "X" and l5["text"] == "X" and l8["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l3["text"] == "X" and l6["text"] == "X" and l9["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l1["text"] == "X" and l5["text"] == "X" and l9["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l3["text"] == "X" and l5["text"] == "X" and l7["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        ############################################################################
        elif l1["text"] == "0" and l2["text"] == "0" and l3["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l4["text"] == "0" and l5["text"] == "0" and l6["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l7["text"] == "0" and l8["text"] == "0" and l9["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l1["text"] == "0" and l4["text"] == "0" and l7["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l2["text"] == "0" and l5["text"] == "0" and l8["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l3["text"] == "0" and l6["text"] == "0" and l9["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l1["text"] == "0" and l5["text"] == "0" and l9["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l3["text"] == "0" and l5["text"] == "0" and l7["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        ############################################################################
        elif flag == 0 and l8["text"] == "":
            l8.configure(text="X", bg="yellow")
            flag = 1
            flag1 = flag1 + 1
            # print(flag1)
        elif flag == 1 and l8["text"] == "":
            l8.configure(text="0", bg="cyan")
            flag = 0
            flag1 = flag1 + 1
            # print(flag1)
        winX()
        win0()

    def click9():
        global flag
        global flag1
        if l1["text"] == "X" and l2["text"] == "X" and l3["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l4["text"] == "X" and l5["text"] == "X" and l6["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l7["text"] == "X" and l8["text"] == "X" and l9["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l1["text"] == "X" and l4["text"] == "X" and l7["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l2["text"] == "X" and l5["text"] == "X" and l8["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l3["text"] == "X" and l6["text"] == "X" and l9["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l1["text"] == "X" and l5["text"] == "X" and l9["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l3["text"] == "X" and l5["text"] == "X" and l7["text"] == "X":
            messagebox.showinfo("Reset", "reset the game and play again")
        ############################################################################
        elif l1["text"] == "0" and l2["text"] == "0" and l3["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l4["text"] == "0" and l5["text"] == "0" and l6["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l7["text"] == "0" and l8["text"] == "0" and l9["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")

        elif l1["text"] == "0" and l4["text"] == "0" and l7["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l2["text"] == "0" and l5["text"] == "0" and l8["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l3["text"] == "0" and l6["text"] == "0" and l9["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l1["text"] == "0" and l5["text"] == "0" and l9["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        elif l3["text"] == "0" and l5["text"] == "0" and l7["text"] == "0":
            messagebox.showinfo("Reset", "reset the game and play again")
        #########################################################################
        elif flag == 0 and l9["text"] == "":
            l9.configure(text="X", bg="yellow")
            flag = 1
            flag1 = flag1 + 1
            # print(flag1)
        elif flag == 1 and l9["text"] == "":
            l9.configure(text="0", bg="cyan")
            flag = 0
            flag1 = flag1 + 1
            # print(flag1)
        winX()
        win0()
        # tie()

    # file handling for X
    def fileX():
        fp1 = open("E:\\Py programs\\file handling\\New folder\\tac1.txt", "a")#E:\Py programs\file handling\New folder
        fp1.write("1st player is winner\n")
        # read file X
        fr1 = open("E:\\Py programs\\file handling\\New folder\\tac1.txt", "r")
        x = fr1.readlines()
        y = len(x)
        z = y + 1
        fr1.close()
        # read file 0
        fr2 = open("E:\\Py programs\\file handling\\New folder\\toe2.txt", "r")
        x1 = fr2.readlines()
        z1 = len(x1)
        fr2.close()
        label2.config(text="\t win X: %d\t\twin O: %d" % (z, z1), anchor=W)
        fp1.close()

    # file handling for 0
    def file0():
        fp2 = open("E:\\Py programs\\file handling\\New folder\\toe2.txt", "a")
        fp2.write("2nd player is winner\n")
        # read file 0
        fr2 = open("E:\\Py programs\\file handling\\New folder\\toe2.txt", "r")
        x = fr2.readlines()
        # print(x)
        y = len(x)
        z1 = y + 1
        fr2.close()
        # read file x
        fr1 = open("E:\\Py programs\\file handling\\New folder\\tac1.txt", "r")
        x = fr1.readlines()
        z = len(x)
        fr1.close()
        #####################
        label2.config(text="\t win X: %d\t\twin O: %d" % (z, z1), anchor=W)
        fp2.close()

    ########################################################################
    def winX():
        global flag1,count123,count456,count789,count147,count258,count369,count159,count357
        global z
        global count123, count456, count789, count147, count258, count369, count159, count357
        # count = 1
        if l1["text"] == "X" and l2["text"] == "X" and l3["text"] == "X":
            fileX()
            count123 = count123 + 1
            if count123 == 1:
                messagebox.showinfo("congrtulation", "1st player is winner")


        elif l4["text"] == "X" and l5["text"] == "X" and l6["text"] == "X":
            fileX()
            count456 = count456 + 1
            if count456 == 1:
                messagebox.showinfo("congrtulation", "1st player is winner")

        elif l7["text"] == "X" and l8["text"] == "X" and l9["text"] == "X":
            fileX()
            count789 += 1
            if count789 == 1:
                messagebox.showinfo("congrtulation", "1st player is winner")

        elif l1["text"] == "X" and l4["text"] == "X" and l7["text"] == "X":
            fileX()
            count147 += 1
            if count147 == 1:
                messagebox.showinfo("congrtulation", "1st player is winner")

        elif l2["text"] == "X" and l5["text"] == "X" and l8["text"] == "X":
            fileX()
            count258 += 1
            if count258 == 1:
                messagebox.showinfo("congrtulation", "1st player is winner")

        elif l3["text"] == "X" and l6["text"] == "X" and l9["text"] == "X":
            fileX()
            count369 += 1
            if count369 == 1:
                messagebox.showinfo("congrtulation", "1st player is winner")

        elif l1["text"] == "X" and l5["text"] == "X" and l9["text"] == "X":
            fileX()
            count159 += 1
            if count159 == 1:
                messagebox.showinfo("congrtulation", "1st player is winner")

        elif l3["text"] == "X" and l5["text"] == "X" and l7["text"] == "X":
            fileX()
            count357 += 1
            if count357 == 1:
                messagebox.showinfo("congrtulation", "1st player is winner")

        else:
            if flag1 == 9:
                messagebox.showinfo("oops", "game is tie")

    ####################################################################
    def win0():
        global count2
        global count0123, count0456, count0789, count0147, count0258, count0369, count0159, count0357
        global z1
        if l1["text"] == "0" and l2["text"] == "0" and l3["text"] == "0":
            file0()
            count0123 += 1
            if count0123 == 1:
                messagebox.showinfo("congrtulation", "2nd player is winner")

        elif l4["text"] == "0" and l5["text"] == "0" and l6["text"] == "0":
            file0()
            count0456 += 1
            if count0456 == 1:
                messagebox.showinfo("congrtulation", "2nd player is winner")

        elif l7["text"] == "0" and l8["text"] == "0" and l9["text"] == "0":
            file0()
            count0789 += 1
            if count0789 == 1:
                messagebox.showinfo("congrtulation", "2nd player is winner")

        elif l1["text"] == "0" and l4["text"] == "0" and l7["text"] == "0":
            file0()
            count0147 += 1
            if count0147 == 1:
                messagebox.showinfo("congrtulation", "2nd player is winner")

        elif l2["text"] == "0" and l5["text"] == "0" and l8["text"] == "0":
            file0()
            count0258 += 1
            if count0258 == 1:
                messagebox.showinfo("congrtulation", "2nd player is winner")

        elif l3["text"] == "0" and l6["text"] == "0" and l9["text"] == "0":
            file0()
            count0369 += 1
            if count0369 == 1:
                messagebox.showinfo("congrtulation", "2nd player is winner")


        elif l1["text"] == "0" and l5["text"] == "0" and l9["text"] == "0":
            file0()
            count0159 += 1
            if count0159 == 1:
                messagebox.showinfo("congrtulation", "2nd player is winner")

        elif l3["text"] == "0" and l5["text"] == "0" and l7["text"] == "0":
            file0()
            count0357 += 1
            if count0357 == 1:
                messagebox.showinfo("congrtulation", "2nd player is winner")

    #####################################################################
    def exit():
        quit()

    ##############
    def reset():
        # write "" in file x
        fw1 = open("F:\\New folder\\tac1.txt", "w")
        fw1.write("")
        fw1.close()
        # read file X
        fr1 = open("F:\\New folder\\tac1.txt", "r")
        ax = fr1.readlines()
        ax1 = len(ax)
        fr1.close()
        # write "" in file 0
        fw2 = open("F:\\New folder\\toe2.txt", "w")
        fw2.write("")
        fw2.close()
        # read file 0
        fr2 = open("F:\\New folder\\tac1.txt", "r")
        ax0 = fr2.readlines()
        ax2 = len(ax0)
        fr2.close()
        # put "" in lavel
        label2.config(text="\t win X: %d\t\twin O: %d" % (ax1, ax2), anchor=W)
    def call2():
        root.destroy()
        call1()
    #############################################################333####33
    l1 = Button(master=root, command=click1)
    l2 = Button(master=root, command=click2)
    l3 = Button(master=root, command=click3)
    l4 = Button(master=root, command=click4)
    l5 = Button(master=root, command=click5)
    l6 = Button(master=root, command=click6)
    l7 = Button(master=root, command=click7)
    l8 = Button(master=root, command=click8)
    l9 = Button(master=root, command=click9)
    label1 = Label(master=root, text="\t1st player is X\t2nd player is 0", bg="black", fg="white", anchor=W)
    # read file X ###################################################
    fr1 = open("F:\\New folder\\tac1.txt", "r")
    x = fr1.readlines()
    len1 = len(x)
    fr1.close()
    # read file 0  ###################################################
    fr2 = open("F:\\New folder\\toe2.txt", "r")
    x1 = fr2.readlines()
    len2 = len(x1)
    fr2.close()
    #######################################################
    label2 = Label(master=root, bg="black", fg="white", text=("\t win X: %d\t\twin O: %d" % (len1, len2)), anchor=W)
    b1 = Button(master=root, text="exit", bg="red", command=exit, relief="raised", borderwidth=4)
    b2 = Button(master=root, text="reset", bg="red", command=reset, relief="raised", borderwidth=4)
    b3=Button(master=root,text="play again",bg="red",command=call2,relief="raised",borderwidth=4)
    ##########################################
    l1.config(width=6, height=2)
    l2.config(width=6, height=2)
    l3.config(width=6, height=2)
    l4.config(width=6, height=2)
    l5.config(width=6, height=2)
    l6.config(width=6, height=2)
    l7.config(width=6, height=2)
    l8.config(width=6, height=2)
    l9.config(width=6, height=2)
    b1.config(width=6, height=1)
    b2.config(width=6, height=1)
    b3.config(width=8,height=1)
    #########################################
    l1.grid(ipady=30, ipadx=30, row=0, column=0)
    l2.grid(ipady=30, ipadx=30, row=0, column=1)
    l3.grid(ipady=30, ipadx=30, row=0, column=2)
    l4.grid(ipady=30, ipadx=30, row=1, column=0)
    l5.grid(ipady=30, ipadx=30, row=1, column=1)
    l6.grid(ipady=30, ipadx=30, row=1, column=2)
    l7.grid(ipady=30, ipadx=30, row=2, column=0)
    l8.grid(ipady=30, ipadx=30, row=2, column=1)
    l9.grid(ipady=30, ipadx=30, row=2, column=2)
    label1.place(x=0, y=350, width=500, height=60)
    label2.place(x=0, y=400, width=500, height=60)
    b1.place(x=108, y=460)
    b2.place(x=171, y=460)
    b3.place(x=240,y=460)
    #########################################
    root.mainloop()
call1()
