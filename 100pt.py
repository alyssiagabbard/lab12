#########################################
#
#         100pt - Working with Canvas
#
#########################################


# Add a button called "Right"
# Make it so that when you press the button, the oval moves to the left or right

from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=480,height=320, background='white')
oval = drawpad.create_oval(160,160,320,320, fill="red")

class MyApp:
	def __init__(self, parent):
	        global drawpad
		self.myParent = parent  
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		
		self.button1 = Button(self.myContainer1)
		self.button1.configure(text="Left", background= "green")
		self.button1.pack(side=LEFT)
		
	        self.button2 = Button(self.myContainer1)
	        self.button2.configure(text="Right", background= "red")
	        self.button2.pack(side=LEFT)
				
						
		self.button1.bind("<Button-1>", self.button1Click) 
		self.button2.bind("<Button-1>", self.button2Click)
		drawpad.pack(side=BOTTOM)
		

		
	def button1Click(self, event):   
		drawpad.move (oval,-100,0)
		global oval
		global drawpad
	
	def button2Click(self, event):
	    drawpad.move (oval,100,0)
	    global oval
	    global drawpad
	
		
myapp = MyApp(root)
root.mainloop()