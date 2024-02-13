import functions as ff

def Mainmenu():
    print('''Options:-
      1.New_itme
      2.List inventry
      3.Low in stock
      4.Out of stock''')
    choice = int(input("Enter Choice :"))
    if choice == 1:
        ff.new_itme()
        Mainmenu()
    elif choice==2:
        ff.inventry()
        Mainmenu()
    elif choice==3:
        ff.low_in_stock()
        Mainmenu()
    elif choice==4:
        ff.out_of_stock()
        Mainmenu()
    else:
        print("Exit...")

Mainmenu()
    