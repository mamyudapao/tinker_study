import sys
import tkinter as tk


root = tk.Tk()

# ウインドウのタイトルを定義する
root.title(u'Buttonを使ってみる')

# ここでウインドウサイズを定義する
root.geometry('400x300')

# ラベルを使って文字を画面上に出す
Static1 = tk.Label(text=u'▼　Entryだぞ！　▼')
Static1.pack()

# Entryを出現させる
Entry1 = tk.Entry(width=50)                   # widthプロパティで大きさを変える
Entry1.insert(tk.END, u'挿入する文字列')        # 最初から文字を入れておく
Entry1.pack()

#Buttonを設置してみる
Button1 = tk.Button(text="何も怒らないボタン", width=50)
Button1.pack()

root.mainloop()