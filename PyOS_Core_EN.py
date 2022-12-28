import time
import sys
import webbrowser


def web(url):
    webbrowser.open(url, new=0, autoraise=True)


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
    elif op == "**":
        return x ** y
    else:
        print("Please enter the right operator!")


cmd = ["help", "about", "ckupd", "catalog", "run mongodb", "run cal", "shutdown", "catalog -a", "run pybrowser"]
print("┌───────────────────┐")
print("│  Welcome to PyOS  │")
print("└───────────────────┘")
print("PyOS，a very light OS designed for Python")
print("Please wait, loading data...")
time.sleep(0.5)
print("error: no such file or directory")
time.sleep(0.7)
print("┌───────────────┐")
print("│   PyOS OOBS   │")
print("└───────────────┘")
unm = input("New username:")
pwd = input("New password:")
repwd = input("Enter password again:")
while pwd != repwd:
    repwd = input("Wrong, please enter password again:")
print("┌─────────────┐")
print("│   Booting   │")
print("└─────────────┘")
print("Loading system, please wait...")
time.sleep(1)
print("Loading program, please wait...")
time.sleep(2)
print("┌────────────────┐")
print("│   PyOS Login   │")
print("└────────────────┘")
user = input("Username:")
while user != unm:
    user = input("Cannot find this username, Username:")
password = input("Password:")
while password != pwd:
    password = input("Wrong password, Password:")
print("Welcome, " + user + "!")
time.sleep(1)
print("┌──────────┐")
print("│   PyOS   │")
print("└──────────┘")
print("Type“help”to see all PyOS command")
#print("This was a pre-release version of PyOS, it may contain bugs that cause crash, use as your own risk")
command = input(">")
while True:
    while command not in cmd:
        print(
            "\033[31mTraceback (most recent call last):\n  File 'PyOS_Core.py', line 1, in <module>\n    " + command + "\nCommandError: Command '" + command + "' is not defined. Did you mean: 'help'?\033[0m")
        print()
        break
    command = input(">")
    if command in cmd:
        for i in range(8):
            if command == cmd[i]:
                if cmd[i] == "help":
                    time.sleep(0.5)
                    print(
                        "help   Show this menu\nabout   About PyOS\ncatalog   Look for all runnable program\n    -a   Look for all installed program\nshutdown   Shutdown\nrun <APP>   Run program\nckupd   Check update")
                    break
                elif cmd[i] == "about":
                    time.sleep(0.5)
                    print("==================")
                    print("====About PyOS====")
                    print("==================")
                    print("PyOS")
                    print("XxdMkb_Mark")
                    print("ver 1.9.6")
                    print("© XxdMkb_Mark. All right reserved")
                    print("Thank you for using PyOS")
                    break
                elif cmd[i] == "shutdown":
                    time.sleep(0.5)
                    print("Exiting...")
                    time.sleep(1)
                    print("现在可以安全退出程序了")
                    sys.exit(0)
                elif cmd[i] == "catalog":
                    time.sleep(0.5)
                    print("pybrowser   Open Website\ncal   calculator")
                    break
                elif cmd[i] == "catalog -a":
                    time.sleep(0.5)
                    print("pybrowser   Open Website\ncal   calculator\nsys   PyOS")
                    break
                elif cmd[i] == "run cal":
                    time.sleep(1)
                    num1 = float(input("Please enter the first number: "))
                    num2 = float(input("Please enter the second number: "))
                    op = input("Please enter operator(+-*/): ")
                    res = calc(num1, num2, op)
                    if res != None:
                        print("The answer is: ", res)
                    break
                elif cmd[i] == "run pybrowser":
                    time.sleep(1)
                    print("Welcome using PyBrowser")
                    url = input("Please enter the URL that you want to visit:")
                    web(url)
                    break
                elif cmd[i] == "ckupd":
                    time.sleep(1)
                    print("Checking update...")
                    time.sleep(3)
                    print("No internet connection, please check manually")
                    time.sleep(0.5)
                    web("https://github.com/XxdMkbMark/PyOS/releases")
