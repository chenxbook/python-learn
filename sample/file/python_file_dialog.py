# coding:utf-8
import win32ui
from tkinter.filedialog import *

print("===================基于win32ui构建文件对话框========================================================")
# 1.基于win32构建文件对话框
# 创建打开文件对话框
dlg = win32ui.CreateFileDialog(1)
# 为对话框创建一个模式窗口
# dlg.DoModal()
print("===================基于tkinter构建文件对话框========================================================")

filetype = [('Python Files', '*.py *.pyw'),
            ('Text Files', '*.txt'),
            ('All Files', '*.*')]


def saveFileDialog():
    "保存对话框"
    filename = asksaveasfilename(
        # 默认扩展名，.号可带可不带
        defaultextension='.py',
        # 文件类型选项
        filetypes=filetype,
        # 初始目录，默认当前目录
        initialdir='C:\\Users',
        # 初始文件名，默认为空
        initialfile='Test',
        # 打开的位置，默认是根窗口
        parent=root,
        # 窗口标题
        title="另存为")
    print(filename)


def openFileDialog():
    "打开对话框,参数与保存对话框相同.略"
    filename = askopenfilename(filetypes=filetype)
    print(filename)


root = Tk()
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='打开', command=openFileDialog)
filemenu.add_command(label='保存', command=saveFileDialog)
menubar.add_cascade(label='文件', menu=filemenu)
root['menu'] = menubar
root.title('文件对话框')
root.mainloop()
