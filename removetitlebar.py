from tkinter import *
root= Tk()
root.title("hi")
root.geometry("500x300")



#remove title bar
root.overrideredirect(True)

#create fake title bar
title_bar = Frame(root,bg="green",relief="raised",bd=1)
title_bar.pack(expand=1,fill=X)
title_label = Label(title_bar,text="Test App",bg="green",fg="black")
title_label.pack(side=LEFT,pady=4)

#binding title bar to make it dragable
def move_app(e):
	root.geometry(f'+{e.x_root}+{e.y_root}')
title_bar.bind("<B1-Motion>",move_app)



#button
my_button=Button(root,text="Close",command=root.quit)
my_button.pack(pady=100)



#x close butotn

close_label = Label(title_bar,text="  X  ",bg="green",fg="white")
close_label.pack(side=RIGHT,pady=4)







root.mainloop()