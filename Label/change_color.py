import sys
import tkinter as tk

root = tk.Tk()

#ウィンドウのタイトルを定義する
root.title("Labelを使ってみる")

#ここでウィンドウのサイズを定義する
root.geometry("400x300")

#ラベルを使って文字を画面上に出す
Static1 = tk.Label(text="test", foreground="#ff0000") #foregroundで文字色を変更
Static1.pack()

root.mainloop()
