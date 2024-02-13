import MySQLdb as db
conn =db.connect(user='root',password='Adity@4410',host='localhost',database='testing')
cursor = conn.cursor() # creating cursor
cursor.execute("use testing;")
print("Conection sucessfull")
print("using testing!")

# 1. function for inserting new itme to inventry
def new_itme():
    Sir_no = int(input("Sr_no:"))
    Product_name = input("Enter name Product:")
    Type = input("Enter type of product:")
    Price = float(input("Enter prince:"))
    sql = "insert into inventry (Sir_no, Product_name, Type, Price) value ({},'{}','{}',{});".format(Sir_no,Product_name,Type,Price)
    cursor.execute(sql)
    conn.commit()
    print("data entered")
# 2. function to show itmes in invetry
def inventry():
    cursor.execute("select * from inventry")
    #row = cursor.fetchone() #get onr row
    rows = cursor.fetchall() #get all rows
    for i in rows:
        print(i)
# 3. function to show low in stocks items in inventry
def low_in_stock():
    cursor.execute("select Price from inventry where Stock <= 5 ;")
    row = cursor.fetchall()
    for i in row :
        print(i)
# 4. function to show item which are out of stock
def out_of_stock():
    cursor.execute("select Price from inventry where Stock = 0 ;")
    row = cursor.fetchall()
    for i in row :
        print(i)
