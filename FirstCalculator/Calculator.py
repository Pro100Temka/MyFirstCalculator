# Modul for GUI interface. 
from tkinter import *
from tkinter import messagebox
# Modul for some mathematical operations.
import math
import sys

# Main frame. 
root = Tk();
root.title("Calculator");

# List of usable buttons. 
bttn_list = ["1", "2", "3", "+", "*",
			 "4", "5", "6", "-", "/",
			 "7", "8", "9", "=", "xⁿ",
			 "0", ".", "±", "C", "<-",
			 "Exit", "sin°", "cos°", "π",
			 "(", ")", "n!", "√n", "|n|"
			 ];

# Location and function of buttons.  
r = 1;
c = 0;
for i in bttn_list:
	def cmd(x=i):
		calc(x);
	bt = Button(root, text = i, command = cmd, width = 7, background = "#555", 
				foreground = "#ccc", font = ("Verdana", 16, "bold"));
	bt.grid(row = r, column = c);
	c += 1;
	if c > 4:
		c = 0;
		r += 1;

# Data input/output field. 
ent = Entry(root, width = 50, font = ("Verdana", 12, "bold"));
ent.grid(row = 0, column = 0, columnspan = 5);

# Logic of calculator. 
def calc(num):
	if num == "=":
		frst = ".0123456789-+*/)(";
		if ent.get()[0] not in frst:
			ent.insert(END, "You have to enter a number!");
			messagebox.showerror("Error!", "You did not enter number!");
		try:
			global result; 
			result = eval(ent.get());
			ent.insert(END, "=" + str(result));
		except:
			ent.delete(0, END);
			ent.insert(END, str(result));
	
	elif num == "C":
		ent.delete(0, END);

	elif num == "<-":
		sec = ent.get()[:-1];
		ent.delete(0, END);
		ent.insert(0, sec);
	
	elif num == "±":
		if "=" in ent.get():
			 ent.delete(0, END);
		try:
			if ent.get()[0] == "-":
				ent.delete(0);
			else:
				ent.insert(0, "-");
		except IndexError:
			pass

	elif num == "π":
		ent.insert(END, math.pi);

	elif num == "Exit":
		root.after(1, root.destroy);
		sys.exit

	elif num == "xⁿ":
		ent.insert(END, "**");

	elif num == "sin°":
		ent.insert(END, "=" + str(math.sin(math.degrees(float(ent.get())))));

	elif num == "cos°":
		ent.insert(END, "=" + str(math.cos(math.degrees(float(ent.get())))));

	elif num == "(":
		ent.insert(END, "(");

	elif num == ")":
		ent.insert(END, ")");

	elif num == "n!":
		ent.insert(END, "=" + str(math.factorial(int(ent.get()))));

	elif num == "√n":
		ent.insert(END, "=" + str(math.sqrt(int(ent.get()))));

	elif num == "|n|":
		ent.insert(END, "=" + str(math.fabs(int(ent.get()))));

	else:
		if "=" in ent.get():
			ent.delete(0, END);
			if "=)(" not in ent.get():
				ent.insert(END, str(result));
		ent.insert(END, num);

root.mainloop()

		