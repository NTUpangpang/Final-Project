import tkinter as tk
# 放一個顯示"/ 100"的 label 
# 放一個會隨著選擇動作體力改變的值
mywindow = tk.Tk()

mywindow.title("體力計算機")
mywindow.geometry("500x300")
var = tk.StringVar()
var.set("100")  # 體力初始值是100
changing_energy = tk.Label(mywindow, textvariable=var, fg="black", width=4, height=2)
changing_energy.pack()
original = tk.Label(mywindow, text="/ 100", width=4, height=2)
original.pack()
entry = tk.Entry(mywindow, show=None)
entry.pack()
energy_used_today = []  # 用來裝目前的剩餘的體力


def energy_spent():
    """會根據任務所花費的體力值變動"""
    what_i_type = entry.get()
    if what_i_type != "":
        what_i_type = int(what_i_type)
    if len(energy_used_today) == 0:
        cost = (100 - what_i_type)
        energy_used_today.append(cost)
    else:
        cost = (energy_used_today[-1] - what_i_type)
        # [-1] 這項表示目前剩餘的體力
        energy_used_today.append(cost)
    remain = energy_used_today[-1]
    # 看體力值足不足夠
    if remain >= 0:
        var.set(remain)
    else:
        tkinter.messagebox.showerror(title="！", message="沒體力了a")
        yes_or_no = tkinter.messagebox.askquestion(title="該怎辦呢？", message="要睡覺回復體力嗎？")
        if yes_or_no == "yes":
            clear_today()
        else:
            tkinter.messagebox.showerror(title="不行喔", message="給我去睡覺")
            clear_today()


def clear_today():
    """每過一天，就讓體力回復至100，之前花費的就清除不管"""
    var.set("100")
    energy_used_today.clear()


bTm = tk.Button(mywindow, text="Energy Cost", width=10, height=1, command=energy_spent)
bTm.pack()
# bTm 這個按鈕的功能是讓 energy spent 做事

clear_button = tk.Button(mywindow, text="Next Day", width=10, height=1, command=clear_today)
clear_button.pack()
# clear 這個按鈕就是讓 clear 這個函數做事
mywindow.mainloop()
