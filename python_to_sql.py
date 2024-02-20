import MySQLdb as db
conn = db.connect(user="root",password="Adity@4410",host="localhost",database="testing")
coursor = conn.cursor()
coursor.execute("use testing;")
Sir_no = [11]
Product_name=["Tasty Nuts"]
Type = ["Snack"]
Price = [5.00]
Quantity = [0]
# Quantity = [99,100,100,100,100,100,100,100,100,100]
for i in range(len(Quantity)):
    sql = "insert into inventry (Sir_no, Product_name, Type, Price,Quantity) value ({},'{}','{}',{},{});".format(Sir_no[0],Product_name[0],Type[0],Price[0],Quantity[0])
    # sql = "update inventry set Quantity = {} where Sir_no = {} ;".format(Quantity[i],Sir_no[i])
    coursor.execute(sql)
    conn.commit()
    print(i,Quantity[i])
coursor.execute("select * from inventry;")
rows = coursor.fetchall()
for i in rows:
    print(i)

