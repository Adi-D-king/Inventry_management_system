import MySQLdb as db 
print('*************************************** ',end="")
print('Wellcome to inventeri managment system.',end="")
print(' ***************************************')

#connecting database
conn =db.connect(user='root',password='Adity@4410',host='localhost',database='testing')
cursor = conn.cursor() # creating cursor
cursor.execute("use testing;")
print("using testing!")

#user options 
print('''Plese enter choice.
1. Bill Genration
2. Enter new Item.
3. View Inventry
0. Exit.''')
choice = int(input('Enter choice :>'))  #user input

if choice == 1:
    itme_list = []
    quantity = []
    O ='y'
    while O == 'y':
        itme_list.append(str(input("Enter product name:")))
        quantity.append(int(input("Enter quantitya:")))
        O = input("y= next_item/n= exit :")
    n = len(itme_list)
    sum = 0
    for i in range(0,n):
        print(i)
        sql = "select Price from inventry where Product_name = '{}';".format(itme_list[i])
        cursor.execute(sql)
        a = cursor.fetchone()
        sum += a[0]*quantity[i]
        print(itme_list[i],' = ',a[0]*quantity[i])
    print("Total bill is = ",sum)
elif choice == 2:
    Sir_no = int(input("Sr_no:"))
    Product_name = input("Enter name Product:")
    Type = input("Enter type of product:")
    Price = float(input("Enter prince:"))
    sql = "insert into inventry (Sir_no, Product_name, Type, Price) value ({},'{}','{}',{});".format(Sir_no,Product_name,Type,Price)
    cursor.execute(sql)
    print("data entered")
    conn.commit()

elif choice == 3:
    cursor.execute("select * from inventry")
    #row = cursor.fetchone() #get onr row
    rows = cursor.fetchall() #get all rows
    for i in rows:
        print(i)

else:
    print('Error')

    
cursor.close()
conn.close()