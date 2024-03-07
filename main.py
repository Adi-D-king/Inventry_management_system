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
        self.frame1 = customtkinter.CTkFrame(self,width=600,height=800,fg_color="white").grid(row=0,column=0,padx=(5,0),pady=(15,5),sticky="n")
        self.refresh = customtkinter.CTkButton(self.frame1,text="Refresh",command=self.refresh_f).grid(row=0,column=0,padx=(20,20),pady=(20,20),sticky="n")
        #----------------------------------------------------------------
        #--------------------tab window----------------------------------
        self.tabWindow = customtkinter.CTkTabview(self,width=950,height=800,fg_color="transparent").grid(row=0,column=1,padx=(5,0),pady=(0,0),sticky="n")
        self.tabWindow.add("Bill")
        self.tabWindow.add("Inventry")
        self.tabWindow.add("Low")
        self.tabWindow.add("Outof")
        self.tabWindow.add("Add/Delet")
        #----------------------------------------------------------------
        #----------------------Inventry tab------------------------------
        self.inventry1 = customtkinter.CTkScrollableFrame(self.tabWindow.tab("Inventry"),width=1000,height=750,fg_color="black").grid()
        self.rows = ff.inventry()
                                        # Sir No.. column
        self.Sir_no= customtkinter.CTkLabel(self.inventry1,text="| _____ Sir No.. _____ |").grid(row=0,column=0)
        for i in self.rows:
            self.sir_no = customtkinter.CTkLabel(self.inventry1,text=i[0]).grid(row=i[0],column=0)
                                        # Name column
        self.Name = customtkinter.CTkLabel(self.inventry1,text=" {} Name {} |".format("_"*20,"_"*20)).grid(row=0,column=1)
        for i in self.rows:
            self.name = customtkinter.CTkLabel(self.inventry1,text=i[1]).grid(row=i[0],column=1)
                                        # Type column
        self.Type = customtkinter.CTkLabel(self.inventry1,text=" {} Type {} |".format("_"*20,"_"*20)).grid(row=0,column=2)
        for i in self.rows:
            self.type = customtkinter.CTkLabel(self.inventry1,text=i[2]).grid(row=i[0],column=2)
                                        # Price
        self.Price= customtkinter.CTkLabel(self.inventry1,text=" _____ Price _____ |").grid(row=0,column=3)
        for i in self.rows:
            self.price = customtkinter.CTkLabel(self.inventry1,text=i[3]).grid(row=i[0],column=3)
                                    # Quantity 
        self.Quantity = customtkinter.CTkLabel(self.inventry1,text=" _______ Quantity _______ |").grid(row=0,column=4)
        for i in self.rows:
            self.price = customtkinter.CTkLabel(self.inventry1,text=i[4]).grid(row=i[0],column=4)
        self.a=1
        #----------------------------------------------------------------
        #------------------------Low in stock tab---------------------------
        self.low_in_stock = customtkinter.CTkScrollableFrame(self.tabWindow.tab("Low"),width=1000,height=750,fg_color="black").grid()
        self.rows = ff.low_in_stock()
        #                                 # Sir No.. column
        self.Sir_no= customtkinter.CTkLabel(self.low_in_stock,text="| _____ Sir No.. _____ |").grid(row=0,column=0)
        self.n = len(self.rows)
        for i in range(0,self.n):
            self.sir_no = customtkinter.CTkLabel(self.low_in_stock,text=self.rows[i][0]).grid(row=i+1,column=0)
                                        # Name column
        self.Name = customtkinter.CTkLabel(self.low_in_stock,text=" {} Name {} |".format("_"*20,"_"*20)).grid(row=0,column=1)
        for i in range(self.n):
            self.name = customtkinter.CTkLabel(self.low_in_stock,text=self.rows[i][1]).grid(row=i+1,column=1)
        #                                 # Type column
        self.Type = customtkinter.CTkLabel(self.low_in_stock,text=" {} Type {} |".format("_"*20,"_"*20)).grid(row=0,column=2)
        for i in range(self.n):
            self.type = customtkinter.CTkLabel(self.low_in_stock,text=self.rows[i][2]).grid(row=i+1,column=2)
        #                                 # Price
        self.Price= customtkinter.CTkLabel(self.low_in_stock,text=" _____ Price _____ |").grid(row=0,column=3)
        for i in range(self.n):
            self.price = customtkinter.CTkLabel(self.low_in_stock,text=self.rows[i][3]).grid(row=i+1,column=3)
        #                                 # Quantity 
        self.Quantity = customtkinter.CTkLabel(self.low_in_stock,text=" _____ Quantity _____ |").grid(row=0,column=4)
        for i in range(self.n):
            self.price = customtkinter.CTkLabel(self.low_in_stock,text=self.rows[i][4]).grid(row=i+1,column=4)
        #---------------------------------------------------------------------------
        #-------------------------Out of stock -------------------------------------
        self.out_of_stock=customtkinter.CTkScrollableFrame(self.tabWindow.tab("Outof"),width=1000,height=750,fg_color = "black").grid()
        self.rows = ff.out_of_stock()
        #                                 # Sir No.. column
        self.Sir_no= customtkinter.CTkLabel(self.out_of_stock,text="| _____ Sir No.. _____ |").grid(row=0,column=0)
        self.n = len(self.rows)
        for i in range(self.n):
            self.sir_no = customtkinter.CTkLabel(self.out_of_stock,text=self.rows[i][0]).grid(row=i+1,column=0)
        #                                 # Name column
        self.Name = customtkinter.CTkLabel(self.out_of_stock,text=" {} Name {} |".format("_"*20,"_"*20)).grid(row=0,column=1)
        for i in range(self.n):
            self.name = customtkinter.CTkLabel(self.out_of_stock,text=self.rows[i][1]).grid(row=i+1,column=1)
        #                                 # Type column
        self.Type = customtkinter.CTkLabel(self.out_of_stock,text=" {} Type {} |".format("_"*20,"_"*20)).grid(row=0,column=2)
        for i in range(self.n):
            self.type = customtkinter.CTkLabel(self.out_of_stock,text=self.rows[i][2]).grid(row=i+1,column=2)
        #                                 # Price
        self.Price= customtkinter.CTkLabel(self.out_of_stock,text=" _____ Price _____ |").grid(row=0,column=3)
        for i in range(self.n):
            self.price = customtkinter.CTkLabel(self.out_of_stock,text=self.rows[i][3]).grid(row=i+1,column=3)
        #                                 # Quantity 
        self.Quantity = customtkinter.CTkLabel(self.out_of_stock,text=" _____ Quantity _____ |").grid(row=0,column=4)
        for i in range(self.n):
            self.price = customtkinter.CTkLabel(self.out_of_stock,text=self.rows[i][4]).grid(row=i+1,column=4)
        #---------------------------------------------------------------------------
        #--------------------------Add/Delet in inventry ----------------------------------
                                        #Add
        self.Add_delet=customtkinter.CTkFrame(self.tabWindow.tab("Add/Delet"),width=1100,height=750,fg_color="black").grid()
        self.add_frame = customtkinter.CTkFrame(self.Add_delet,width=990,height=365,fg_color="red").grid(row=0,pady=(10,10))
        self.add_frame_0= customtkinter.CTkFrame(self.add_frame,).grid(row=0,padx=(20,20))
        self.Il_Sir_no = customtkinter.CTkLabel(self.add_frame_0,text="Enter Sir_no:").grid(row=0,column=0,padx=(5,2),pady=(5,5))
        self.Input_Sir_no_ = customtkinter.CTkEntry(self.add_frame_0,width=120).grid(row=0,column=1,padx=(5,0))
        self.Il_Name = customtkinter.CTkLabel(self.add_frame_0,text="Enter Name:").grid(row=0,column=2,padx=(5,0),pady=(5,5))
        self.Input_Name = customtkinter.CTkEntry(self.add_frame_0,width=250).grid(row=0,column=3,padx=(5,10))
        self.Il_Price = customtkinter.CTkLabel(self.add_frame_0,text="Enter Price:").grid(row=0,column=4,padx=(5,2))
        self.Input_Price = customtkinter.CTkEntry(self.add_frame_0,width=120).grid(row=0,column=5,padx=(5,10))
        self.add_frame_1= customtkinter.CTkFrame(self.add_frame,fg_color="green").grid(row=1,padx=(20,20),sticky="nw")
        self.Il_Type = customtkinter.CTkLabel(self.add_frame_1,text="Enter type:").grid(row=0,column=0,padx=(5,2),pady=(5,5))
        self.Input_Type = customtkinter.CTkEntry(self.add_frame_1,width=250).grid(row=0,column=1,padx=(5,5))
        self.Il_Quantity = customtkinter.CTkLabel(self.add_frame_1,text="Enter quantity:").grid(row=0,column=2,padx=(5,2),pady=(5,5))
        self.Input_Quantity = customtkinter.CTkEntry(self.add_frame_1,width=250).grid(row=0,column=3,padx=(5,5))
        self.add_frame_2 = customtkinter.CTkFrame(self.add_frame,fg_color="white",).grid(row=2)
        self.Add_button = customtkinter.CTkButton(self.add_frame_2,text="Add",width=80,command=self.addFunction).grid(row=0,column=0,padx=(10,100),pady=(5,5))
                                      #Delet
        self.delet_frame = customtkinter.CTkFrame(self.Add_delet,width=990,height=375,fg_color="pink").grid(row=1,pady=(0,5))
        #----------------------------------------------------------------------------
        self.tabWindow.set("Add/Delet")     #########################################################################################################################
        
    def inventry_q(self): #------------for refresh option
        self.rows = ff.inventry()
        self.inventry = customtkinter.CTkScrollableFrame(self.tabWindow.tab("Inventry"),width=1000,height=750,fg_color="white").grid(row=0,column=0)
                               # Sir No.. column
        self.Sir_no= customtkinter.CTkLabel(self.inventry,text="| _____ Sir No.. _____ |",text_color="black").grid(row=0,column=0)
        for i in self.rows:
            self.sir_no = customtkinter.CTkLabel(self.inventry,text=i[0],text_color="black").grid(row=i[0],column=0)
                                        # Name column
        self.Name = customtkinter.CTkLabel(self.inventry,text=" {} Name {} |".format("_"*20,"_"*20),text_color="black").grid(row=0,column=1)
        for i in self.rows:
            self.name = customtkinter.CTkLabel(self.inventry,text=i[1],text_color="black").grid(row=i[0],column=1)
                                        # Type column
        self.Type = customtkinter.CTkLabel(self.inventry,text=" {} Type {} |".format("_"*20,"_"*20),text_color="black").grid(row=0,column=2)
        for i in self.rows:
            self.type = customtkinter.CTkLabel(self.inventry,text=i[2],text_color="black").grid(row=i[0],column=2)
                                        # Price
        self.Price= customtkinter.CTkLabel(self.inventry,text=" _____ Price _____ |",text_color="black").grid(row=0,column=3)
        for i in self.rows:
            self.price = customtkinter.CTkLabel(self.inventry,text=i[3],text_color="black").grid(row=i[0],column=3)
                                    # Quantity 
        self.Quantity = customtkinter.CTkLabel(self.inventry,text=" _____ Quantity _____ |",text_color="black").grid(row=0,column=4)
        

    def refresh_f(self): # for freresh main function
        self.protocol(self.inventry1.destroy())
        print("end")
        if self.a==1:
            self.inventry_q()
            self.a=0
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

    # def deleteFunction(self):
    #     self.sir_no = 
app=App()
app.mainloop()