import sys,time,webbrowser,os,keyboard,requests
ErrorCodeList=['FAIL_TO_CREATE_FILE','FAIL_TO_LOAD_RECOVERY_MODE']
SomeKindOfWaitTimeIDK=2
MainMenuSoftware=['全部应用','应用商店','系统设置','安全中心','电源菜单']

def clear():
    os.system('cls')
def PrintStartIcon(msg,waitTime):
    clear()
    print('''
 ____            _____   ____       
/\  _`\         /\  __`\/\  _`\     
\ \ \L\ \__  __ \ \ \/\ \ \,\L\_\   
 \ \ ,__/\ \/\ \ \ \ \ \ \/_\__ \   
  \ \ \/\ \ \_\ \ \ \ \_\ \/\ \L\ \ 
   \ \_\ \/`____ \ \ \_____\ `\____、
    \/_/  `/___/> \ \/_____/\/_____/
             /\___/                
             \/__/                           
''')
    print('['+msg+']')
    print('---------------------------')
    time.sleep(waitTime)
def PrintErrorIcon():
    clear()
    print('''
 _____ ____  ____   ___  ____  
| ____|  _ \|  _ \ / _ \|  _ \ 
|  _| | |_) | |_) | | | | |_) |
| |___|  _ <|  _ <| |_| |  _ < 
|_____|_| \_\_| \_\\___/|_| \_\
''')
    print('---------------------------')
    print('很抱歉，PyOS遇到了一些问题，大部分问题的解决方案都可在PyOS论坛(forum.pyos.top)的FAQ板块中找到，如果你坚信这是一个BUG，请前往PyOS论坛的反馈板块进行反馈\n以下是可能导致这次崩溃的原因:')

def PyDefender():
    global SomeKindOfWaitTimeIDK
    clear()
    print('''
PPPPPPPPPPPPPPPPP                            
P::::::::::::::::P                           
P::::::PPPPPP:::::P                          
PP:::::P     P:::::P                         
  P::::P     P:::::Pyyyyyyy           yyyyyyy
  P::::P     P:::::P y:::::y         y:::::y 
  P::::PPPPPP:::::P   y:::::y       y:::::y  
  P:::::::::::::PP     y:::::y     y:::::y   
  P::::PPPPPPPPP        y:::::y   y:::::y    
  P::::P                 y:::::y y:::::y     
  P::::P                  y:::::y:::::y      
  P::::P                   y:::::::::y       
PP::::::PP                  y:::::::y        
P::::::::P                   y:::::y         
P::::::::P                  y:::::y          
PPPPPPPPPP                 y:::::y           
                          y:::::y            
                         y:::::y             
                        y:::::y              
                       y:::::y               
                      yyyyyyy      ____        __                _           
                                  |  _ \  ___ / _| ___ _ __   __| | ___ _ __ 
                                  | | | |/ _ \ |_ / _ \ '_ \ / _` |/ _ \ '__|
                                  | |_| |  __/  _|  __/ | | | (_| |  __/ |   
                                  |____/ \___|_|  \___|_| |_|\__,_|\___|_|   ''')
    print('Version 0.1')
    print('---------------------------')
    time.sleep(2)
    print('正在检查更新...')
    FPath=os.path.dirname(__file__)
    FFlag=os.path.exists(FPath+'/defender')
    if FFlag==False:
        os.makedirs(FPath+'/defender')
    def_temp=open('./defender/defender.log','w')
    def_temp.close()
    print('您使用的是最新版本！')
    time.sleep(SomeKindOfWaitTimeIDK)
    clear()
    print('''
PPPPPPPPPPPPPPPPP                            
P::::::::::::::::P                           
P::::::PPPPPP:::::P                          
PP:::::P     P:::::P                         
  P::::P     P:::::Pyyyyyyy           yyyyyyy
  P::::P     P:::::P y:::::y         y:::::y 
  P::::PPPPPP:::::P   y:::::y       y:::::y  
  P:::::::::::::PP     y:::::y     y:::::y   
  P::::PPPPPPPPP        y:::::y   y:::::y    
  P::::P                 y:::::y y:::::y     
  P::::P                  y:::::y:::::y      
  P::::P                   y:::::::::y       
PP::::::PP                  y:::::::y        
P::::::::P                   y:::::y         
P::::::::P                  y:::::y          
PPPPPPPPPP                 y:::::y           
                          y:::::y            
                         y:::::y             
                        y:::::y              
                       y:::::y               
                      yyyyyyy      ____        __                _           
                                  |  _ \  ___ / _| ___ _ __   __| | ___ _ __ 
                                  | | | |/ _ \ |_ / _ \ '_ \ / _` |/ _ \ '__|
                                  | |_| |  __/  _|  __/ | | | (_| |  __/ |   
                                  |____/ \___|_|  \___|_| |_|\__,_|\___|_|   ''')
    print('Version 0.1')
    print('---------------------------')
    time.sleep(SomeKindOfWaitTimeIDK)
    print('PyDefender还在开发中，暂时无法使用')
    time.sleep(SomeKindOfWaitTimeIDK)
    print('正在退出...')
    time.sleep(SomeKindOfWaitTimeIDK)
    return


PrintStartIcon('pyos_loader',2)
print('正在加载资源...')
time.sleep(2)
FilePath=os.path.dirname(__file__)
FileFlag=os.path.exists(FilePath+'/UserInfo.ini')
if FileFlag==True:
    print('continue to login')
    time.sleep(0.5)
elif FileFlag==False:
    print('file not found')
    time.sleep(1)
    PrintStartIcon('PyOS初始化向导',2)
    path_temp=os.path.dirname(__file__)
    os.makedirs(path_temp+'/lang')
    temp=open('UserInfo.ini','w')
    temp.close()
    if os.path.exists('UserInfo.ini')==True:
        username=input('请输入您的用户名(例如:Mark):')
        temp=open('UserInfo.ini','a')
        temp.write(username+'\n')
        temp.close()
        password=input('请输入您的密码:')
        temp=open('UserInfo.ini','a')
        temp.write(password+'\n')
        temp.close()
        password2=input('请重复输入一遍密码:')
        while password2!=password:
            password2=input('密码与前一次不同，请重试:')
        print('信息已保存')
        print('欢迎使用PyOS！')
        time.sleep(1)
        print('ending oobs process...')
        time.sleep(3)
    else:
        PrintErrorIcon()
        print('无法新建用户信息文件，请检查您是否拥有修改此目录的权限')
        print('ErrorCode: '+ErrorCodeList[0])
        print('按下空格键退出...')
        keyboard.wait('space')
        sys.exit(1)
PrintStartIcon('登录至PyOS',2)
print('选择要登录的用户：')
temp=open('UserInfo.ini','r')
userlist=[line.strip('\n') for line in temp.readlines()]
temp.close()
usernum=1
for i in range(len(userlist)):
    if i%2==0:
        print(str(usernum)+'. '+userlist[i])
        usernum+=1
ChooseUser=input('请输入序号:')
while ChooseUser.isdigit()!=True or int(ChooseUser)>len(userlist)//2:
    PrintStartIcon('登录至PyOS',0)
    print('选择要登录的用户：')
    temp=open('UserInfo.ini','r')
    userlist=[line.strip('\n') for line in temp.readlines()]
    temp.close()
    usernum=1
    for i in range(len(userlist)):
        if i%2==0:
            print(str(usernum)+'. '+userlist[i])
            usernum+=1
    ChooseUser=input('没有找到此用户，请重新输入:')
WaitToVerifyUser=userlist[int(ChooseUser)-1]
PrintStartIcon('登录至PyOS',0)
WaitToVerifyPwd=input('请输入'+WaitToVerifyUser+'的密码:')
UserPosition=userlist.index(WaitToVerifyUser)
while WaitToVerifyPwd!=userlist[UserPosition+1]:
    WaitToVerifyPwd=input('密码不正确，请输入'+WaitToVerifyUser+'的密码:')
PrintStartIcon('欢迎，'+WaitToVerifyUser+'!',2)
print('正在加载系统...')
time.sleep(2)
print('正在加载应用...')
time.sleep(SomeKindOfWaitTimeIDK)
while True:
    PrintStartIcon("PyOS主菜单",2)
    for i in range(len(MainMenuSoftware)):
        print(str(i+1)+'. '+MainMenuSoftware[i])
    temp_choice=input('请选择一个选项：')
    choice=MainMenuSoftware[int(temp_choice)-1]
    if choice=='安全中心':
        PyDefender()
    if choice=='电源菜单':
        sys.exit(1)