"""抽取学生实现"""
#############################初始化#############################
import random
import tkinter as tk

total_student = ["陈瑞格", "陈首名", "赵佳硕", "范志超", "王鹏茹", "杨冰", "卜炫安",
                 "袁希博", "张悦", "张烨铭", "朱继松", "史天琦", "曹偲琪", "张莹", "赵浩言", "郑阳阳",
                 "陈紫西",
                 "李博奥", "姜宇轩", "孙佳琪", "寇栖源", "王嘉蔚", "谭奕萌", "周若雪", "林思琪",
                 "白梦涵", "魏宇佳", "王一涵", "唐静然",
                 "孟江楠", "李雪坤", "曹悦然", "曾祥钊", "杨迪", "张传业", "李政霖", "侯佳诚",
                 "郭展赫", "陈尚言", "赵轩", "唐健程", "高越"]
root = tk.Tk()
root.title("小考批卷人员抽取")
root.geometry("1400x400")
root.resizable(True, True)
goal_list = []
output = tk.Label(root, text=f"批卷人员为: {goal_list}", font=("Aril", 30))
resout = ""


def main():
    """定义主函数"""
    global goal_list
    global total_student
    global output
    global resout
    for i in range(6):
        c = len(total_student) - 2
        a = random.randint(0, c)
        goal_list.append(total_student[a])
        total_student.remove(total_student[a])
    if random.randint(0, 100) <= 30:
        goal_list[random.randint(0, len(goal_list) - 1)] = total_student[-1]
    if random.randint(0, 100) <= 30:
        goal_list[random.randint(0, len(goal_list) - 1)] = total_student[-2]
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


start = tk.Button(root, text="抽取")
start.bind("<Button-1>", lambda e: main())
start.place(x=100, y=100)

root.mainloop()
