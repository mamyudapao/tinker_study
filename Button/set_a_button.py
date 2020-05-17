import  sys
import tkinter as tk

root = tk.Tk()

#ウィンドウのタイトルを定義する
root.title('Entryを使ってみる')

#ここでウィンドウサイズを定義する
root.geometry('400x300')

#ラベルを使って文字を画面上に出す
Static1 = tk.Label(text="Entryだぞ！！！")
Static1.pack()

#Entryを出現させる
Entry1 = tk.Entry(width=50)
Entry1.insert(tk.END, '挿入する文字列')
Entry1.pack()

#Buttonを設置してみる
Button1 = tk.Button(text="何も怒らないボタン")
Button1.pack()

root.mainloop()