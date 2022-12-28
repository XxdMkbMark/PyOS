import time
import sys
import webbrowser


def calc(x, y, op):
    if op == "+":
        return x + y
    elif op == "-":
        return x - y
    elif op == "*":
        return x * y
    elif op == "/":
        return x / y
    elif op == "%":
        return x % y
    elif op == "//":
        return x // y
    if op == "**":
        return x ** y
    if op == "%":
        return x % y
    else:
        print("请输入正确的运算符！")


def web(url):
    webbrowser.open(url, new=0, autoraise=True)


cmd = ["help", "about", "ckupd", "catalog", "run mongodb", "run calc", "shutdown", "catalog -a", "run pybrowser"]
print("┌────────────────────┐")
print("│     欢迎使用PyOS    │")
print("└────────────────────┘")
print("PyOS，一个为Python设计的轻量操作系统")
print("请稍候，正在加载数据...")
time.sleep(0.7)
print("┌────────────────────┐")
print("│   PyOS初始化向导    │")
print("└────────────────────┘")
unm = input("请设置用户名:")
while unm=="" or unm==" ":
    print("用户名不合规")
    unm = input("请设置用户名:")
pwd = input("请设置密码:")
while pwd=="" or pwd==" ":
    print("密码不合规")
    pwd = input("请设置密码:")
repwd = input("请重复密码:")
while pwd != repwd:
    repwd = input("密码错误，请重复密码:")
print("┌────────────┐")
print("│   启动中    │")
print("└────────────┘")
print("正在载入系统，请稍候...")
time.sleep(1)
print("正在加载软件，请稍候...")
time.sleep(2)
print("┌──────────────┐")
print("│   PyOS登录   │")
print("└──────────────┘")
user = input("请输入用户名:")
while user != unm:
    user = input("没有找到此用户，请输入用户名:")
password = input("请输入密码:")
while password != pwd:
    password = input("密码错误，请输入密码:")
print("欢迎，" + user + "！")
time.sleep(1)
print("┌──────────┐")
print("│   PyOS   │")
print("└──────────┘")
print("您可以输入“help”获取PyOS的全部命令")
while True:
    command = input(">")
    if command == "":
        continue
    while command not in cmd:
        print(
            "\033[31mTraceback (most recent call last):\n  File 'PyOS_Core.py', line 1, in <module>\n    " + command + "\nCommandError: Command '" + command + "' is not defined. Did you mean: 'help'?\033[0m")
        print()
        break
    if command in cmd:
        for i in range(9):
            if command == cmd[i]:
                if cmd[i] == "help":
                    time.sleep(0.5)
                    print(
                        "help   显示此菜单\nabout   关于本系统\ncatalog   查看可运行的所有软件\n    -a   查看已安装的所有软件\nshutdown   退出系统\nrun "
                        "<软件名>   运行指定软件\nckupd   检查系统更新")
                    break
                elif cmd[i] == "about":
                    time.sleep(0.5)
                    print("┌──────────────┐")
                    print("│   关于PyOS   │")
                    print("└──────────────┘")
                    print("PyOS")
                    print("项目发起：XxdMkb_Mark")
                    print("合作开发：not_exist")
                    print("ver 1.9.6_P20221228")
                    print("支持与赞助：afdian.net/a/PythonOS")
                    print("项目源码：https://github.com/XxdMkbMark/PyOS/releases")
                    print("© XxdMkb_Mark。保留所有权利")
                    print("感谢您使用本操作系统")
                    break
                elif cmd[i] == "shutdown":
                    time.sleep(0.5)
                    print("正在退出...")
                    time.sleep(1)
                    print("现在可以安全退出程序了")
                    sys.exit(0)
                elif cmd[i] == "catalog":
                    time.sleep(0.5)
                    print("calculator   计算器\npybrowser   Py浏览器")
                    break
                elif cmd[i] == "catalog -a":
                    time.sleep(0.5)
                    print("mogodb   数据库\ncalculator   计算器\npybrowser   Py浏览器\nsys   PyOS")
                    break
                elif cmd[i] == "run pybrowser":
                    time.sleep(1)
                    print("欢迎使用PyBrowser")
                    url = input("请输入要访问的URL：")
                    web(url)
                    break
                elif cmd[i] == "run calc":
                    time.sleep(1)
                    print("++++++++++++++")
                    print("+. . . . . . +")
                    print("+. .计算器. . +")
                    print("+. . v1.1. . +")
                    print("+. by HAHA . +")
                    print("+. . . . . . +")
                    print("++++++++++++++")
                    num1 = float(input("请输入第一个数："))
                    num2 = float(input("请输入第二个数："))
                    op = input("请输入运算符(+ - * / ** // %)：")
                    res = calc(num1, num2, op)
                    if res != None:
                        print("结果是：", res)
                    break
                elif cmd[i] == "ckupd":
                    time.sleep(1)
                    print("正在检查更新...")
                    time.sleep(3)
                    print("未连接到互联网，请手动检查更新")
                    time.sleep(0.5)
                    web("https://github.com/XxdMkbMark/PyOS/releases")
