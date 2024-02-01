import MySQLdb as db
print('*************************************** ',end="")
print('Wellcome to inventeri managment system.',end="")
print(' ***************************************')

#connecting database
conn = db.connect(host = 'localhost', database= 'testing', user = 'root', password = 'Adity@4410')
cursor = conn.cursor() # creating cursor
cursor.execute("select * from inventry;")

#user options 
print('''Plese enter choice.
1. Enter new Item.
2. View Inventeri 
0. Exit.''')
choice = int(input('Enter choice :>'))  #user input

if choice == 1:
    Sir_no = int(input("Sr_no:"))
    P_name = input("Product_name:")
    P_type = input('Type:')
    Price = float(input('Price:'))
    sql = "INSERT INTO Inventry (Sir_no, Product_name, Type, Price) VALUES (%i, %s, %s, %f)".format(Sir_no,P_name,P_type,Price)
    val = (Sir_no,P_name,P_type,Price)
    cursor.execute(sql)

elif choice == 2:
    #row = cursor.fetchone() #get onr row
    rows = cursor.fetchall() #get all rows
    for i in rows:
        print(i)

else:
    print('Error')

    
cursor.close()
conn.close()