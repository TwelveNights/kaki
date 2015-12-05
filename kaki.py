from Tkinter import *

root = Tk()
root.title("kaki")
root.resizable(0,0)
points = []

tag = "line"

c = Canvas(root, bg="white", width=1280, height= 720)

def make_dot(x, y, xmax, ymax):
    dot = c.create_oval(x, y, xmax, ymax, fill="black")

def point(event):
    x = event.x - 2
    y = event.y - 2
    o = 4

    dot = make_dot(x, y, x+o, y+o)

    points.append(event.x)
    points.append(event.y)
    
def graph(event):
    global points

    x = event.x - 2
    y = event.y - 2
    o = 4

    dot = make_dot(x, y, x+o, y+o)

    points.append(event.x)
    points.append(event.y)
    
    line = c.create_line(points, tags=tag, fill="black", width=4)
    points = []

def clear_all(event=None):
    global points

    points = []
    c.delete(ALL)    

def move(event):
    points.append(event.x)
    points.append(event.y)
    x = event.x - 2
    y = event.y - 2
    o = 4

    dot = make_dot(x, y, x+o, y+o)

    return points

# Bind space to clear_all just in case
root.bind("<space>", clear_all)

c.pack()

c.bind("<ButtonRelease-1>", graph)
c.bind("<B1-Motion>", move)

b = Button(root, text = "Clear", command=clear_all, height=5, width=10, bg="#0AA62A")
b.place(relx=1.0, rely=1.0, x=-2, y=-2,anchor="se")

root.mainloop() 