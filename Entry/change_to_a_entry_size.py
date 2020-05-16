import sys
import tkinter as tk


root = tk.Tk()

# ウインドウのタイトルを定義する
root.title(u'Entryを使ってみる')

# ここでウインドウサイズを定義する
root.geometry('400x300')

# ラベルを使って文字を画面上に出す
Static1 = tk.Label(text=u'▼　Entryだぞ！　▼')
Static1.pack()

#Entryを出現させる
Entry1 = tk.Entry(width=50)#インスタンス時に横幅を指定すれば良い
Entry1.insert(tk.END, "挿入する文字列")
Entry1.pack()

root.mainloop()