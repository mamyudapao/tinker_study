import sys
import tkinter as tk

root = tk.Tk()

#ウィンドウのタイトルを定義する
root.title("ウィンドウサイズを変える")

#ここでウィンドウサイズを定義する
root.geometry("400x300")

#ラベルを使って文字を画面上に出す
Static1 = tk.Label(text="test", background="#90caf9")
Static1.pack()

root.mainloop()
