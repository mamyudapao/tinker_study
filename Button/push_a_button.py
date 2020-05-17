import sys
import tkinter as tk


root = tk.Tk()

# ウインドウのタイトルを定義する
root.title(u'Buttonを使ってみる')

# ここでウインドウサイズを定義する
root.geometry('400x300')


# ボタンが押されたら呼び出される関数
def deleteEntry(event):
    # Entryの中身をすべて削除する
    Entry1.delete(0, tk.END)


# ラベルを使って文字を画面上に出す
Static1 = tk.Label(text=u'▼　Entryだぞ！　▼')
Static1.pack()

# Entryを出現させる
Entry1 = tk.Entry(width=50)                   # widthプロパティで大きさを変える
Entry1.insert(tk.END, u'挿入する文字列')        # 最初から文字を入れておく
Entry1.pack()

#Buttonを設置してみる
Button1 = tk.Button(text='消すボタン', width=50)
Button1.bind("<Button-1>", deleteEntry) #ボタンが押されたときに実行される関数をバインドする
Button1.pack()

root.mainloop()