import tkinter as tk
from json import loads, dumps

configing = tk.Tk()
configing.title("设置")
configing.resizable(width=False, height=False)
configing.geometry("400x400")
origin_list = ["董子墨", "陈首名", "李汪恩熙", "范志超", "王鹏茹", "杨冰", "卜炫安",
               "袁希博", "张悦", "张烨铭", "朱继松", "史天琦", "曹偲琪", "张莹", "张子安", "郑阳阳",
               "陈紫西",
               "李博奥", "姜宇轩", "孙佳琪", "寇栖源", "王嘉蔚", "谭奕萌", "周若雪", "林思琪",
               "白梦涵", "魏宇佳", "王一涵", "唐静然",
               "孟江楠", "李雪坤", "曹悦然", "曾祥钊", "杨迪", "张传业", "李政霖", "侯佳诚",
               "郭展赫", "陈尚言", "赵轩", "唐健程", "高越"]
with open('data.json', encoding='utf-8') as f:
    temp = loads(f.read())
    temp1 = temp['stu']
    temp2 = temp['num']


def insert_student(new_student):
    global temp1
    global temp
    f = open('data.json', 'w', encoding='utf-8')
    temp['stu'].append(new_student)
    f.write(dumps(temp))
    f.close()


def delete_student(goal):
    global temp1
    global temp
    f = open('data.json', 'w', encoding='utf-8')
    temp1.remove(goal)
    temp['stu'] = temp1
    f.write(dumps(temp))
    f.close()


def change_len(goal):
    global temp2
    f = open('data.json', 'w', encoding='utf-8')
    temp['num'] = int(goal)
    f.write(dumps(temp))
    f.close()


def check():
    f = open('data.json', encoding='utf-8')
    print(loads(f.read()))
    f.close()


def reset():
    f = open('data.json', 'w', encoding='utf-8')
    qi = {'stu': origin_list, 'num': 0}
    f.write(dumps(qi))
    f.close()


p1_1 = tk.StringVar()
p1 = tk.Spinbox(configing, textvariable=p1_1)
p1.place(x=100, y=100)
d1_1 = tk.Button(configing, text="添加", command=lambda: insert_student(p1_1.get()))
d1_1.place(x=260, y=100)
l1_1 = tk.Label(configing, text="添加学生")
l1_1.place(x=100, y=70)
p1_2 = tk.StringVar()
p2 = tk.Spinbox(configing, textvariable=p1_2)
p2.place(x=100, y=150)
d1_2 = tk.Button(configing, text="删除", command=lambda: delete_student(p1_2.get()))
d1_2.place(x=260, y=150)
l2_1 = tk.Label(configing, text="删除学生")
l2_1.place(x=100, y=125)
p2_1 = tk.IntVar()
p2 = tk.Spinbox(configing, textvariable=p2_1)
p2.place(x=100, y=200)
d2_1 = tk.Button(configing, text="变更", command=lambda: change_len(p2_1.get()))
d2_1.place(x=260, y=200)
l3_1 = tk.Label(configing, text="抽取人数")
l3_1.place(x=100, y=175)
d3_1 = tk.Button(configing, text="查看现有学生（将在控制台输出）", command=lambda: check())
d3_1.place(x=100, y=260)
d3_2 = tk.Button(configing, text="重置为初始值", command=lambda: reset())
d3_2.place(x=150, y=230)
ed = tk.Button(configing, text="确认", command=lambda: configing.destroy())
ed.place(x=150, y=320)

configing.mainloop()
