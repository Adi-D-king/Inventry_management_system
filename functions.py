import MySQLdb as db
conn =db.connect(user='root',password='Adity@4410',host='localhost',database='testing')
cursor = conn.cursor() # creating cursor
cursor.execute("use testing;")
print("Conection sucessfull")
print("using testing database !!")
print(" "*5,"_"*10,"Wellcome to inventry managment system","_"*10)

# 1. function to show items in invetry
def inventry():
    cursor.execute("select * from inventry")
    #row = cursor.fetchone() #get one row
    rows = cursor.fetchall() #get all rows
    return rows
    # for i in rows:
    #     print(i,type(i))
    # print(type(rows))

# 2. function to show low in stocks items in inventry
def low_in_stock():
    cursor.execute("select * from inventry where Quantity < 100 ;")
    l_rows = cursor.fetchall()
    return l_rows

# 3. function to show item which are out of stock
def out_of_stock():
    cursor.execute("select * from inventry where Quantity = 0 ;")
    Orows = cursor.fetchall()
    return Orows


# 4. function for inserting new item to inventry
def new_item(sirno,prodno,typee,pricee,quantityy):
    Sir_no = sirno
    Product_name = prodno
    Type = typee
    Price = pricee
    Quantity = quantityy
    sql = "insert into inventry (Sir_no, Product_name, Type, Price, Quantity) value ({},'{}','{}',{},{});".format(Sir_no,Product_name,Type,Price,Quantity)
    cursor.execute(sql)
    conn.commit()
    return True


# 5. function to delet an itme from inventry 
def delet_itme(Sir_no):
    # Sir__no = int(input("Enter serale number:"))
    cursor.execute("select * from inventry;")
    cursor.execute("delete from inventry where Sir_no = {} and ".format(Sir_no))
    print("itme deleted")
    # conn.commit()
def billing(name):
    str = "select Price from inventry where Product_name = '{}'".format(name)
    cursor.execute(str)
    price = cursor.fetchone()
    return price[0]  # remaning to update inventry

# def grand_total function remaning 
