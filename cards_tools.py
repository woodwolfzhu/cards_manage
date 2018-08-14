card_list = []
#记录所有名片的字典
def show_menu():

    """显示菜单"""
    print("*" * 50)
    print("1.  新增名片")
    print("2.  显示全部名片")
    print("3.  查询名片")
    print("*" * 50)

def new_card():

    """新增名片"""
    print("新增名片")
    name_str = input("请输入姓名：")
    phone_str = input("请输入电话号：")
    card_dict = {"name":name_str,
                 "phone":phone_str}
    card_list.append(card_dict)



def show_all():

    """显示所有名片"""
    #显示表头
    print("*" * 50)
    print("显示所有名片")
    if len(card_list) == 0:
        print("no cards,please add new card!")
        return
    for name in ["姓名","电话号"]:
        print(name,end="\t\t")
    print("")
    print("-" * 50)
    for card_dict in card_list:
        print("%s\t\t%s\t\t" % (card_dict["name"],
                                card_dict["phone"]))



def search_cards():

    """查询名片"""
    print("查询名片")
    print("*" * 50)
    name_str = input("请输入要查询的姓名：")
    for card_dict in card_list:
        if name_str == card_dict["name"]:
            for name in ["姓名", "电话号"]:
                print(name, end="\t\t")
            print("")
            print("-" * 50)
            print("%s\t\t%s\t\t" % (card_dict["name"],
                                    card_dict["phone"]))
            card_deal(card_dict)
            break
    else:
        print("this name is not exist in cards!")


def card_deal(card_dict):
    """对查找到的名片进行处理

    :param card_dict: 查找到的名片
    :return: 
    """
    print("please input your choice:")
    choice = input("1.delete this card\t\t2.revise this card\t\t0.go back")
    if choice == "1":
        card_list.remove(card_dict)
    elif choice == "2":
        card_dict["name"] = input_card  (card_dict["name"],"please input his/her name:(if not revise,please press 'enter')")
        card_dict["phone"] = input_card(card_dict["phone"],"please input his/her phone number:(if not revise,please press 'enter')")
    elif choice == "0":
        return
    else:
        print("your input is error,please input again!")
        card_deal(card_dict)


def input_card(dict_value,tip_message):

    #提示用户输入信息
    """输入名片信息

    :param dict_value: 字典原来的值
    :param tip_message: 要输出的提示信息
    :return: 
    """
    result_str = input(tip_message)
    #对用户输入数据进行判断，如果用户输入了内容，直接返回结果。
    if len(result_str) > 0:
        return result_str
    #如果用户没有输入数据，就返回 字典原来的 value
    else:
        return dict_value


