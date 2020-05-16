import sys
import tkinter as tk

root = tk.Tk()

#ウインドウのタイトルを定義する
root.title("ウィンドウのサイズを変えてみる")

#ここでウィンドウサイズを定義する
root.geometry('400x300')

#ラベルを使って文字を出す
Static1 = tk.Label(text="test", foreground="#ff0000", background="#ffaacc")
Static1.place(x=150, y=228)

root.mainloop()
