import cards_tools as ct
while True:
    # TODO 显示菜单
    ct.show_menu()
    # num = int(input("Please input your choice:"))
    # 在需要用户输入内容时，尽量不要进行 int 转换，若用户输入的不是数字时，程序会报错
    num = input("Please input your choice:")
    if num in ['1','2','3']:
        #新增名片
        if num == '1':
            ct.new_card()
        #显示全部名片
        elif num == '2':
            ct.show_all()
        #查询名片
        elif num == '3':
            ct.search_cards()
        pass
    #在程序开发时不希望立即编写分支内部代码
    #可以是 pass 关键字，表示一个占位符，能够保证代码的结构正确！
    #程序运行时，pass 关键字不会执行任何操作！
    elif num == '0':
        print("欢迎再次使用！")
        break
    else:
        print("your input is error,please input again!")