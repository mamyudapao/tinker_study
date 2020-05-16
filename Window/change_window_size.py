import sys
import tkinter as tk

root = tk.Tk()
root.title('ウィンドウサイズを変えてみる')

#ここでウィンドウサイズを変える
root.geometry('400x300')#英語でgeometryは幾何学

#ラベル
Static1 = tk.Label(text="test")
Static1.pack()

root.mainloop()
