"""抽取学生实现"""
#############################初始化#############################
import random
import tkinter as tk

total_student = ["唐健程", "陈瑞格", "陈首名", "赵佳硕", "范志超", "王鹏茹", "杨冰", "卜炫安",
                 "袁希博", "张悦", "张烨铭", "朱继松", "史天琦", "程凯驰", "曹偲琪", "张莹", "赵浩言", "郑阳阳",
                 "陈紫西",
                 "李博奥", "姜宇轩", "孙佳琪", "寇栖源", "王嘉蔚", "谭奕萌", "周若雪", "林思琪",
                 "白梦涵", "魏宇佳", "王一涵", "唐静然",
                 "孟江楠", "李雪坤", "曹悦然", "曾祥钊", "杨迪", "张传业", "李政霖", "侯佳诚",
                 "郭展赫"]
root = tk.Tk()
root.title("小考批卷人员抽取")
root.geometry("1400x400")
root.resizable(True, True)
extra_list = ["高越", "赵轩", "陈尚言"]
goal_list = []
output = tk.Label(root, text=f"批卷人员为: {goal_list}", font=("Aril", 30))
rg = [0, 1, 2, 3]
tts = 0
resout = ""


def main():
    """定义主函数"""
    global goal_list
    global total_student
    global output
    global rg
    global tts
    global resout
    for i in range(4):
        c = len(total_student) - 1
        a = random.randint(0, c)
        goal_list.append(total_student[a])
        total_student.remove(total_student[a])
    if random.randint(0, 10) >= 3:
        goal_list[random.choice(rg)] = random.choice(extra_list)
    for i in range(len(goal_list)):
        resout += str(goal_list[i])
        resout += " "
        if i != len(goal_list) - 1:
            resout += ","
    output.configure(text=f"批卷人员为: {resout}")
    output.place(x=100, y=30)
    goal_list.clear()
    total_student = ["唐健程", "陈瑞格", "陈首名", "赵佳硕", "范志超", "王鹏茹", "杨冰", "卜炫安",
                     "袁希博", "张悦", "张烨铭", "朱继松", "史天琦", "程凯驰", "曹偲琪", "张莹", "赵浩言", "郑阳阳",
                     "陈紫西",
                     "李博奥", "姜宇轩", "孙佳琪", "寇栖源", "王嘉蔚", "谭奕萌", "周若雪", "林思琪",
                     "白梦涵", "魏宇佳", "王一涵", "唐静然",
                     "孟江楠", "李雪坤", "曹悦然", "曾祥钊", "杨迪", "张传业", "李政霖", "侯佳诚"]
    resout = ""
    return goal_list


start = tk.Button(root, text="抽取")
start.bind("<Button-1>", lambda e: main())
start.place(x=100, y=100)

root.mainloop()
