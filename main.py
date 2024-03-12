import customtkinter
import functions as ff
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Inventry")
        self.geometry()
        self.propagate(0)
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        #---------------------user profile-------------------------------
        self.frame1 = customtkinter.CTkFrame(self,width=600,height=800,fg_color="white")
        self.frame1.grid(row=0,column=0,padx=(5,0),pady=(15,5),sticky="n")
        self.refresh = customtkinter.CTkButton(self.frame1,text="Refresh",command=self.refresh_f)
        self.refresh.grid(row=0,column=0,padx=(20,20),pady=(20,20),sticky="n")
        #----------------------------------------------------------------
        #--------------------tab window----------------------------------
        self.tabWindow = customtkinter.CTkTabview(self,width=950,height=800,fg_color="transparent")
        self.tabWindow.grid(row=0,column=1,padx=(5,0),pady=(0,0),sticky="n")
        self.tabWindow.add("Bill")
        self.tabWindow.add("Inventry")
        self.tabWindow.add("Low")
        self.tabWindow.add("Outof")
        self.tabWindow.add("Add/Delete")
        #----------------------------------------------------------------
        #----------------------Billing System ---------------------------
        self.b_fram = customtkinter.CTkFrame(self.tabWindow.tab("Bill"),width=950,height=750,fg_color="white")
        self.b_fram.grid(row=0,column=0)
        self.b_Name_lable = customtkinter.CTkLabel(self.b_fram,text="Enter Name :",text_color="black")
        self.b_Name_lable.grid(row=0,column=0,padx=(10,10),pady=(10,10))
        self.b_Name_Entry = customtkinter.CTkEntry(self.b_fram,width=200)
        self.b_Name_Entry.grid(row=0,column=1,padx=(0,10),pady=(10,10))
        self.b_Quantity_lable = customtkinter.CTkLabel(self.b_fram,text="Enter Quantity :",text_color="black")
        self.b_Quantity_lable.grid(row=0,column=2,padx=(10,10),pady=(10,10))
        self.b_Quantity_Entry = customtkinter.CTkEntry(self.b_fram,width=200)
        self.b_Quantity_Entry.grid(row=0,column=3,padx=(0,10),pady=(10,10))
        self.b_button_next = customtkinter.CTkButton(self.b_fram,text="Next")
        self.b_button_next.grid(row=0,column=4,padx=(0,10),pady=(10,10))
        self.b_button_gb = customtkinter.CTkButton(self.b_fram,text="Total")
        self.b_button_gb.grid(row=0,column=5,padx=(0,10),pady=(10,10))
        self.list_Name=[]
        self.list_Quantity = []
        #----------------------Inventry tab------------------------------
        self.inventry1 = customtkinter.CTkScrollableFrame(self.tabWindow.tab("Inventry"),width=1000,height=750)
        self.inventry1.grid()
        self.inventry_q("Inventry")
        self.a=1
        #----------------------------------------------------------------
        #------------------------Low in stock tab---------------------------
        self.low_in_stock = customtkinter.CTkScrollableFrame(self.tabWindow.tab("Low"),width=1000,height=750)
        self.low_in_stock.grid()
        self.rows = ff.low_in_stock()
        #                                 # Sir No.. column
        self.Sir_no= customtkinter.CTkLabel(self.low_in_stock,text="| _____ Sir No.. _____ |")
        self.Sir_no.grid(row=0,column=0)
        self.n = len(self.rows)
        for i in range(0,self.n):
            self.sir_no = customtkinter.CTkLabel(self.low_in_stock,text=self.rows[i][0])
            self.sir_no.grid(row=i+1,column=0)
                                        # Name column
        self.Name = customtkinter.CTkLabel(self.low_in_stock,text=" {} Name {} |".format("_"*20,"_"*20))
        self.Name.grid(row=0,column=1)
        for i in range(self.n):
            self.name = customtkinter.CTkLabel(self.low_in_stock,text=self.rows[i][1])
            self.name.grid(row=i+1,column=1)
        #                                 # Type column
        self.Type = customtkinter.CTkLabel(self.low_in_stock,text=" {} Type {} |".format("_"*20,"_"*20))
        self.Type.grid(row=0,column=2)
        for i in range(self.n):
            self.type = customtkinter.CTkLabel(self.low_in_stock,text=self.rows[i][2])
            self.type.grid(row=i+1,column=2)
        #                                 # Price
        self.Price= customtkinter.CTkLabel(self.low_in_stock,text=" _____ Price _____ |")
        self.Price.grid(row=0,column=3)
        for i in range(self.n):
            self.price = customtkinter.CTkLabel(self.low_in_stock,text=self.rows[i][3])
            self.price.grid(row=i+1,column=3)
        #                                 # Quantity 
        self.Quantity = customtkinter.CTkLabel(self.low_in_stock,text=" _____ Quantity _____ |")
        self.Quantity.grid(row=0,column=4)
        for i in range(self.n):
            self.quantity = customtkinter.CTkLabel(self.low_in_stock,text=self.rows[i][4])
            self.quantity.grid(row=i+1,column=4)
        #---------------------------------------------------------------------------
        #-------------------------Out of stock -------------------------------------
        self.out_of_stock=customtkinter.CTkScrollableFrame(self.tabWindow.tab("Outof"),width=1000,height=750)
        self.out_of_stock.grid()
        self.rows = ff.out_of_stock()
        #                                 # Sir No.. column
        self.Sir_no= customtkinter.CTkLabel(self.out_of_stock,text="| _____ Sir No.. _____ |")
        self.Sir_no.grid(row=0,column=0)
        self.n = len(self.rows)
        for i in range(self.n):
            self.sir_no = customtkinter.CTkLabel(self.out_of_stock,text=self.rows[i][0])
            self.sir_no.grid(row=i+1,column=0)
        #                                 # Name column
        self.Name = customtkinter.CTkLabel(self.out_of_stock,text=" {} Name {} |".format("_"*20,"_"*20))
        self.Name.grid(row=0,column=1)
        for i in range(self.n):
            self.name = customtkinter.CTkLabel(self.out_of_stock,text=self.rows[i][1])
            self.name.grid(row=i+1,column=1)
        #                                 # Type column
        self.Type = customtkinter.CTkLabel(self.out_of_stock,text=" {} Type {} |".format("_"*20,"_"*20))
        self.Type.grid(row=0,column=2)
        for i in range(self.n):
            self.type = customtkinter.CTkLabel(self.out_of_stock,text=self.rows[i][2])
            self.type.grid(row=i+1,column=2)
        #                                 # Price
        self.Price= customtkinter.CTkLabel(self.out_of_stock,text=" _____ Price _____ |")
        self.Price.grid(row=0,column=3)
        for i in range(self.n):
            self.price = customtkinter.CTkLabel(self.out_of_stock,text=self.rows[i][3])
            self.price.grid(row=i+1,column=3)
        #                                 # Quantity 
        self.Quantity = customtkinter.CTkLabel(self.out_of_stock,text=" _____ Quantity _____ |")
        self.Quantity.grid(row=0,column=4)
        for i in range(self.n):
            self.quantity = customtkinter.CTkLabel(self.out_of_stock,text=self.rows[i][4])
            self.quantity.grid(row=i+1,column=4)
        #---------------------------------------------------------------------------
        #--------------------------Add/Delete in inventry ----------------------------------
                                        #Add
        self.Add_Delete=customtkinter.CTkFrame(self.tabWindow.tab("Add/Delete"),width=1100,height=750)
        self.Add_Delete.grid()
        self.add_frame = customtkinter.CTkFrame(self.Add_Delete,width=990,height=365)
        self.add_frame.grid(row=0,pady=(10,10))
        self.add_frame_0= customtkinter.CTkFrame(self.add_frame,)
        self.add_frame_0.grid(row=0,padx=(20,20),pady=(10,10))
        self.Il_Sir_no = customtkinter.CTkLabel(self.add_frame_0,text="Enter Sir_no:")
        self.Il_Sir_no.grid(row=0,column=0,padx=(5,2),pady=(5,5))
        self.Input_Sir_no_ = customtkinter.CTkEntry(self.add_frame_0,width=120)
        self.Input_Sir_no_.grid(row=0,column=1,padx=(5,0))
        self.Il_Name = customtkinter.CTkLabel(self.add_frame_0,text="Enter Name:")
        self.Il_Name.grid(row=0,column=2,padx=(5,0),pady=(5,5))
        self.Input_Name = customtkinter.CTkEntry(self.add_frame_0,width=250)
        self.Input_Name.grid(row=0,column=3,padx=(5,10))
        self.Il_Price = customtkinter.CTkLabel(self.add_frame_0,text="Enter Price:")
        self.Il_Price.grid(row=0,column=4,padx=(5,2))
        self.Input_Price = customtkinter.CTkEntry(self.add_frame_0,width=120)
        self.Input_Price.grid(row=0,column=5,padx=(5,10))
        self.add_frame_1= customtkinter.CTkFrame(self.add_frame)
        self.add_frame_1.grid(row=1,padx=(20,20),pady=(10,10),sticky="nw")
        self.Il_Type = customtkinter.CTkLabel(self.add_frame_1,text="Enter type:")
        self.Il_Type.grid(row=0,column=0,padx=(5,2),pady=(5,5))
        self.Input_Type = customtkinter.CTkEntry(self.add_frame_1,width=250)
        self.Input_Type.grid(row=0,column=1,padx=(5,5))
        self.Il_Quantity = customtkinter.CTkLabel(self.add_frame_1,text="Enter quantity:")
        self.Il_Quantity.grid(row=0,column=2,padx=(5,2),pady=(5,5))
        self.Input_Quantity = customtkinter.CTkEntry(self.add_frame_1,width=250)
        self.Input_Quantity.grid(row=0,column=3,padx=(5,5))
        self.add_frame_2 = customtkinter.CTkFrame(self.add_frame,)
        self.add_frame_2.grid(row=2,pady=(10,10))
        self.Add_button = customtkinter.CTkButton(self.add_frame_2,text="Add",width=80,command=self.addFunction)
        self.Add_button.grid(row=0,column=0,padx=(10,100),pady=(5,5))
                                      #Delete
        self.Delete_frame = customtkinter.CTkFrame(self.Add_Delete,width=990,height=375)
        self.Delete_frame.grid(row=1,pady=(0,5))
        self.d_Sir_no = customtkinter.CTkLabel(self.Delete_frame,text="Enter Sir_no :")
        self.d_Sir_no.grid(row=0,column=0,padx=(10,5))
        self.d_entry_sir_no = customtkinter.CTkEntry(self.Delete_frame)
        self.d_entry_sir_no.grid(row=0,column=1,padx=(5,10))
        self.d_Name = customtkinter.CTkLabel(self.Delete_frame,text="Enter Item Name :")
        self.d_Name.grid(row=0,column=2,padx=(10,5))
        self.d_entry_name = customtkinter.CTkEntry(self.Delete_frame,width=200)
        self.d_entry_name.grid(row=0,column=3,padx=(5,10))
        self.d_button = customtkinter.CTkButton(self.Delete_frame,text="Delete")
        self.d_button.grid(row=1,column=0,padx=(10,10),pady=(20,10))
        self.d_cf_lab=customtkinter.CTkLabel(self.Delete_frame,text="No. of item deleted = ")
        self.d_cf_lab.grid(row=1,column=2,padx=(10,10),pady=(20,10))
        #----------------------------------------------------------------------------
        self.tabWindow.set("Inventry")     #########################################################################################################################
        
    def inventry_q(self,inventry):
        self.tabWindow.set("Inventry") #------------for refresh option
        self.rows = ff.inventry()
        self.inventry = customtkinter.CTkScrollableFrame(self.tabWindow.tab(inventry),width=1000,height=750)
        self.inventry.grid(row=0,column=0)
                               # Sir No.. column
        self.Sir_no= customtkinter.CTkLabel(self.inventry,text="| _____ Sir No.. _____ |",text_color="white")
        self.Sir_no.grid(row=0,column=0)
        for i in self.rows:
            self.sir_no = customtkinter.CTkLabel(self.inventry,text=i[0],text_color="white")
            self.sir_no.grid(row=i[0],column=0)
                                        # Name column
        self.Name = customtkinter.CTkLabel(self.inventry,text=" {} Name {} |".format("_"*20,"_"*20),text_color="white")
        self.Name.grid(row=0,column=1)
        for i in self.rows:
            self.name = customtkinter.CTkLabel(self.inventry,text=i[1],text_color="white")
            self.name.grid(row=i[0],column=1)
                                        # Type column
        self.Type = customtkinter.CTkLabel(self.inventry,text=" {} Type {} |".format("_"*20,"_"*20),text_color="white")
        self.Type.grid(row=0,column=2)
        for i in self.rows:
            self.type = customtkinter.CTkLabel(self.inventry,text=i[2],text_color="white")
            self.type.grid(row=i[0],column=2)
                                        # Price
        self.Price= customtkinter.CTkLabel(self.inventry,text=" _____ Price _____ |",text_color="white")
        self.Price.grid(row=0,column=3)
        for i in self.rows:
            self.price = customtkinter.CTkLabel(self.inventry,text=i[3],text_color="white")
            self.price.grid(row=i[0],column=3)
                                    # Quantity 
        self.Quantity = customtkinter.CTkLabel(self.inventry,text=" _____ Quantity _____ |",text_color="white")
        self.Quantity.grid(row=0,column=4)
        for i in self.rows:
            self.price = customtkinter.CTkLabel(self.inventry,text=i[4],text_color="white")
            self.price.grid(row=i[0],column=4)
        

    def refresh_f(self): # for freresh main function
        self.protocol(self.inventry1.destroy())
        print("end")
        if self.a==1:
            self.inventry_q("Inventry")
    def addFunction(self): # function to add into inventry!
        self.sirno = self.Input_Sir_no_.get()
        self.prodno = self.Input_Name.get()
        self.typee = self.Input_Type.get()
        self.pricee = self.Input_Price.get()
        self.quantityy = self.Input_Quantity.get()
        self.confur = ff.new_item(self.sirno,self.prodno,self.typee,self.pricee,self.quantityy)
        if self.confur==True :
            print("data entered")
        else :
            print("False")

    # def DeleteeFunction(self):
    #     self.sir_no = self.d_entry_sir_no.get()
            
    def next(self):
        self.list_Name.append(self.b_Name_Entry.get())
        self.list_Quantity.append(self.b_Quantity_Entry.get())
        

app=App()
app.mainloop()