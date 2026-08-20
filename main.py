"""抽取学生实现"""
#############################初始化#############################
import random
import tkinter as tk
from json import loads, dumps
import os
import sys


def resource_path(relative_path):
    """寻找路径"""
    base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


root = tk.Tk()
root.title("小考批卷人员抽取")
root.geometry("1600x400")
root.resizable(True, True)
goal_list = []
output = tk.Label(root, text=f"批卷人员为: {goal_list}", font=("Aril", 30))
resout = ""


def main():
    """定义主函数"""
    global goal_list
    global output
    global resout
    f = open('data.json', encoding='utf-8')
    a = loads(f.read())
    total_student = a['stu']
    much = a['num']
    for i in range(much):
        c = len(total_student) - 2
        a = random.randint(0, c)
        goal_list.append(total_student[a])
        total_student.remove(total_student[a])
    for i in range(len(goal_list)):
        resout += str(goal_list[i])
        resout += " "
        if i != len(goal_list) - 1:
            resout += ","
    output.configure(text=f"批卷人员为: {resout}")
    output.place(x=100, y=30)
    total_student += goal_list
    goal_list.clear()
    resout = ""
    return goal_list


def cal():
    import os
    path = resource_path("backup.exe")
    os.system(path)


start = tk.Button(root, text="抽取")
start.bind("<Button-1>", lambda e: main())
start.place(x=100, y=100)
conf = tk.Button(root, text="设置")
conf.bind("<Button-1>", lambda e: cal())
conf.place(x=100, y=150)

root.mainloop()
