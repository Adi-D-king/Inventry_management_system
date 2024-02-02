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
1. Enter new Item.
2. View Inventry
0. Exit.''')
choice = int(input('Enter choice :>'))  #user input

if choice == 1:
    Sir_no = int(input("Sr_no:"))
    Product_name = input("Enter name Product:")
    Type = input("Enter type of product:")
    Price = float(input("Enter prince:"))
    sql = "insert into inventry (Sir_no, Product_name, Type, Price) value ({},'{}','{}',{});".format(Sir_no,Product_name,Type,Price)
    cursor.execute(sql)
    print("data entered")
    cursor.commit()

elif choice == 2:
    cursor.execute("select * from inventry")
    #row = cursor.fetchone() #get onr row
    rows = cursor.fetchall() #get all rows
    for i in rows:
        print(i)

else:
    print('Error')

    
cursor.close()
conn.close()