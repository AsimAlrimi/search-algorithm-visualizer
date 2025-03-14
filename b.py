import tkinter as tk
from tkinter import *
from collections import deque

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if key < root.key:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root


Node_location = {}


def visualize_binary_tree(root, canvas, x, y, level=0, dx=350, dy=140):
    if root is not None:
        oval_radius = 39  # Increase this value to make the oval larger

        canvas.create_oval(x - oval_radius, y - oval_radius, x + oval_radius, y + oval_radius,
                            outline="black", fill="white", width=2)
        canvas.create_text(x, y, text=str(root.key), font=("Arial", 12), fill="black")
        Node_location[root.key] = x - oval_radius, y - oval_radius, x + oval_radius, y + oval_radius

        if root.left:
            canvas.create_line(x, y + oval_radius, x - dx / 2, y + dy, width=2)
            visualize_binary_tree(root.left, canvas, x - dx / 2, y + dy, level + 1, dx / 2, dy)
        if root.right:
            canvas.create_line(x, y + oval_radius, x + dx / 2, y + dy, width=2)
            visualize_binary_tree(root.right, canvas, x + dx / 2, y + dy, level + 1, dx / 2, dy)


def clear_canvas():
    clicked.set("SELECT GOAL")
    clicked2.set("SELECT ALGORITHM")
    canvas.delete("all")
    visualize_binary_tree(root, canvas, 400, 50)


the_path = []


def BFS(root, g):
    if root is None:
        return
    queue = deque([root])
    while queue:
        current_node = queue.popleft()
        the_path.append(current_node.key)
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)


def DFS(root, g):
    if root is None:
        return
    the_path.append(root.key)
    DFS(root.left, g)
    DFS(root.right, g)


def shaker(i, color):
    a1, a2, a3, a4 = Node_location[i]
    canvas.create_oval(a1, a2, a3, a4, outline="black", fill=color, width=2)
    canvas.create_text(a1 + 39, a2 + 39, text=str(i), font=("Arial", 12), fill="black")


def show():
    g = clicked.get()
    a = clicked2.get()

    the_path.clear()

    if a == "BFS" and g != "SELECT GOAL":
        BFS(root, g)

        def animate_path(index=0):
            if index < len(the_path):
                i = the_path[index]
                if str(i) == str(g):
                    shaker(i, "red")
                else:
                    shaker(i, "light green")
                    root_tk.after(1000, lambda: animate_path(index + 1))
        animate_path()
    elif a == "DFS" and g != "SELECT GOAL":
        DFS(root, g)

        def animate_path(index=0):
            if index < len(the_path):
                i = the_path[index]
                if str(i) == str(g):
                    shaker(i, "red")
                else:
                    shaker(i, "light green")
                    root_tk.after(1000, lambda: animate_path(index + 1))

        animate_path()
    else:
        print("error")


root = None
keys = [5, 3, 7, 2, 4, 6, 8]

for key in keys:
    root = insert(root, key)

root_tk = tk.Tk()
root_tk.title("Visualization")


screen_width = root_tk.winfo_screenwidth()
screen_height = root_tk.winfo_screenheight()
root_tk.geometry(f"{screen_width}x{screen_height}")

frame = tk.Frame(root_tk)
frame.pack()

canvas = Canvas(frame, width=800, height=500)
canvas.pack()

visualize_binary_tree(root, canvas, 400, 50)

options = ["5", "3", "7", "2", "4", "6", "8"]
clicked = StringVar()
clicked.set("SELECT GOAL")
drop = OptionMenu(root_tk, clicked, *options)
drop.config(font=("Arial", 12))  # Increase font size
drop.place(x=20, y=470)  # Adjust position

options2 = ["BFS", "DFS"]
clicked2 = StringVar()
clicked2.set("SELECT ALGORITHM")
drop = OptionMenu(root_tk, clicked2, *options2)
drop.config(font=("Arial", 12))  # Increase font size
drop.place(x=20, y=510)  # Adjust position

button = Button(root_tk, text="Click Me", command=show)
button.config(font=("Arial", 12))  # Increase font size
button.place(x=20, y=550)  # Adjust position

button_clear = Button(root_tk, text="Clear", command=clear_canvas)
button_clear.config(font=("Arial", 12))  # Increase font size
button_clear.place(x=20, y=590)  # Adjust position

root_tk.mainloop()
