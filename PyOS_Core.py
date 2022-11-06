import time

cmd=["help","about","ckupd","catalog","run mogodb","run cal"]
print("PyOS，一个为Pyhon设计的轻量操作系统")
print("请稍候，正在加载数据...")
time.sleep(0.5)
print("error: no such file or directory")
time.sleep(0.7)
print("====PyOS OOBS====")
unm=input("请设置用户名:")
pwd=input("请设置密码:")
repwd=input("请重复密码:")
while pwd!=repwd:
    repwd=input("密码错误，请重复密码:")
print("====Booting====")
print("正在载入系统，请稍候...")
time.sleep(2)
print("====PyOS Login====")
user=input("请输入用户名:")
while user!=unm:
    user=input("没有找到此用户，请输入用户名:")
password=input("请输入密码:")
while password!=pwd:
    password=input("密码错误，请输入密码:")
print("欢迎，"+user+"！")
print("====PyOS====")
print("您可以输入“help”获取PyOS的全部命令")
command=input(">")
while True:
    while command not in cmd:
        print("Traceback (most recent call last):\n  File 'PyOS_Core.py', line 1, in <module>\n    "+command+"\nCommandError: Command '"+command+"' is not defined. Did you mean: '餛斤拷█ﻻ'?")
        print()
        break
    command=input(">")
    if command in cmd:
        for i in range(6):
            if command==cmd[i]:
                if cmd[i]=="help":
                    print("help   显示此菜单\nabout   关于本系统\nckupd   检查更新")
                    break
                elif cmd[i]=="about":     
                    print("====About PyOS====")
                    print("PyOS/PyDOS")
                    print("XxdMkb_Mark")
                    print("版本 1.0.1Patch 3")
                    print("© XxdMkb_Mark。保留所有权利")
                    print("感谢您使用本操作系统")
                    break
                elif cmd[i]=="ckupd":
                    print("====Update====")
                    print("已是最新版本")
                    break
                
