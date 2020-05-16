import sys
import tkinter as tk

root = tk.Tk() #Tkinterのインスタンスを作成

#ウィンドウ上に文字を表示する
Static1 = tk.Label(text="test") #ラベルを指定
Static1.pack()#Static1インスタンスの中身を1次元的に配列

root.mainloop() #イベントループ