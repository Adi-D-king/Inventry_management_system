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
        self.frame1.grid(row=0,column=0,padx=(5,0),pady=(0,5))
        self.refresh = customtkinter.CTkButton(self.frame1,text="Refresh",command=self.refresh_f)
        self.refresh.grid(row=0,column=0,padx=(20,20),pady=(20,20))
        #----------------------------------------------------------------
        #--------------------tab window----------------------------------
        self.tabWindow = customtkinter.CTkTabview(self,width=950,height=800,fg_color="transparent")
        self.tabWindow.grid(row=0,column=1,padx=(5,0),pady=(0,0))
        self.tabWindow.add("Inventry")
        self.tabWindow.add("Low")
        self.tabWindow.add("Outof")
        self.tabWindow.add("Add/Delete")
        #----------------------------------------------------------------
        #----------------------Inventry tab------------------------------
        self.inventry1 = customtkinter.CTkScrollableFrame(self.tabWindow.tab("Inventry"),width=1000,height=750,fg_color="black")
        self.inventry1.grid()
        self.rows = ff.inventry()
                                        # Sir No.. column
        self.Sir_no= customtkinter.CTkLabel(self.inventry1,text="| _____ Sir No.. _____ |")
        self.Sir_no.grid(row=0,column=0)
        for i in self.rows:
            self.sir_no = customtkinter.CTkLabel(self.inventry1,text=i[0])
            self.sir_no.grid(row=i[0],column=0)
                                        # Name column
        self.Name = customtkinter.CTkLabel(self.inventry1,text=" {} Name {} |".format("_"*20,"_"*20))
        self.Name.grid(row=0,column=1)
        for i in self.rows:
            self.name = customtkinter.CTkLabel(self.inventry1,text=i[1])
            self.name.grid(row=i[0],column=1)
                                        # Type column
        self.Type = customtkinter.CTkLabel(self.inventry1,text=" {} Type {} |".format("_"*20,"_"*20))
        self.Type.grid(row=0,column=2)
        for i in self.rows:
            self.type = customtkinter.CTkLabel(self.inventry1,text=i[2])
            self.type.grid(row=i[0],column=2)
                                        # Price
        self.Price= customtkinter.CTkLabel(self.inventry1,text=" _____ Price _____ |")
        self.Price.grid(row=0,column=3)
        for i in self.rows:
            self.price = customtkinter.CTkLabel(self.inventry1,text=i[3])
            self.price.grid(row=i[0],column=3)
                                    # Quantity 
        self.Quantity = customtkinter.CTkLabel(self.inventry1,text=" _______ Quantity _______ |")
        self.Quantity.grid(row=0,column=4)
        self.a=1
        #----------------------------------------------------------------
        #------------------------Low in stock tab---------------------------
        self.low_in_stock = customtkinter.CTkScrollableFrame(self.tabWindow.tab("Low"),width=1000,height=750,fg_color="black")
        self.low_in_stock.grid()
        # self.rows = ff.low_in_stock()
        #                                 # Sir No.. column
        self.Sir_no= customtkinter.CTkLabel(self.low_in_stock,text="| _____ Sir No.. _____ |")
        self.Sir_no.grid(row=0,column=0)
        # self.n = len(self.rows)
        # for i in range(self.n):
        #     self.sir_no = customtkinter.CTkLabel(self.low_in_stock,text=self.rows[i][0])
        #     self.sir_no.grid(row=i+1,column=0)
        #                                 # Name column
        self.Name = customtkinter.CTkLabel(self.low_in_stock,text=" {} Name {} |".format("_"*20,"_"*20))
        self.Name.grid(row=0,column=1)
        # for i in range(self.n):
        #     self.name = customtkinter.CTkLabel(self.low_in_stock,text=self.rows[i][1])
        #     self.name.grid(row=+1,column=1)
        #                                 # Type column
        self.Type = customtkinter.CTkLabel(self.low_in_stock,text=" {} Type {} |".format("_"*20,"_"*20))
        self.Type.grid(row=0,column=2)
        # for i in range(self.n):
        #     self.type = customtkinter.CTkLabel(self.low_in_stock,text=self.rows[i][2])
        #     self.type.grid(row=i+1,column=2)
        #                                 # Price
        self.Price= customtkinter.CTkLabel(self.low_in_stock,text=" _____ Price _____ |")
        self.Price.grid(row=0,column=3)
        #for i in range(self.n):
        #     self.price = customtkinter.CTkLabel(self.low_in_stock,text=self.rows[i][3])
        #     self.price.grid(row=i+1,column=3)
        #                                 # Quantity 
        self.Quantity = customtkinter.CTkLabel(self.low_in_stock,text=" _____ Quantity _____ |")
        self.Quantity.grid(row=0,column=4)
        #---------------------------------------------------------------------------
        #-------------------------Out of stock -------------------------------------
        self.out_of_stock=customtkinter.CTkScrollableFrame(self.tabWindow.tab("Outof"),width=1000,height=750,fg_color = "black")
        self.out_of_stock.grid()
        # self.rows = ff.out_of_stock()
        #                                 # Sir No.. column
        self.Sir_no= customtkinter.CTkLabel(self.out_of_stock,text="| _____ Sir No.. _____ |")
        self.Sir_no.grid(row=0,column=0)
        # self.n = len(self.rows)
        # for i in range(self.n):
        #     self.sir_no = customtkinter.CTkLabel(self.out_of_stock,text=self.rows[i][0])
        #     self.sir_no.grid(row=i+1,column=0)
        #                                 # Name column
        self.Name = customtkinter.CTkLabel(self.out_of_stock,text=" {} Name {} |".format("_"*20,"_"*20))
        self.Name.grid(row=0,column=1)
        # for i in range(self.n):q
        #     self.name = customtkinter.CTkLabel(self.out_of_stock,text=self.rows[i][1])
        #     self.name.grid(row=i+1,column=1)
        #                                 # Type column
        self.Type = customtkinter.CTkLabel(self.out_of_stock,text=" {} Type {} |".format("_"*20,"_"*20))
        self.Type.grid(row=0,column=2)
        # for i in range(self.n):
        #     self.type = customtkinter.CTkLabel(self.out_of_stock,text=self.rows[i][2])
        #     self.type.grid(row=i+1,column=2)
        #                                 # Price
        self.Price= customtkinter.CTkLabel(self.out_of_stock,text=" _____ Price _____ |")
        self.Price.grid(row=0,column=3)
        #for i in range(self.n):
        #     self.price = customtkinter.CTkLabel(self.out_of_stock,text=self.rows[i][3])
        #     self.price.grid(row=i+1,column=3)
        #                                 # Quantity 
        self.Quantity = customtkinter.CTkLabel(self.out_of_stock,text=" _____ Quantity _____ |")
        self.Quantity.grid(row=0,column=4)
        #---------------------------------------------------------------------------
        #--------------------------Add in inventry ----------------------------------
        self.Add=customtkinter.CTkScrollableFrame(self.tabWindow.tab("Add/Delete"),width=1000,height=750,fg_color="black")
        self.Add.grid()
        self.Quantity = customtkinter.CTkLabel(self.Add,text=" _____ Quantity _____ |")
        self.Quantity.grid(row=0,column=4)
        #----------------------------------------------------------------------------
        self.tabWindow.set("Inventry")
        
    def inventry_q(self):
        self.inventry = customtkinter.CTkScrollableFrame(self.tabWindow.tab("Inventry"),width=1000,height=750,fg_color="white")
        self.inventry.grid(row=0,column=0)
                                    # Sir No.. column
        self.Sir_no= customtkinter.CTkLabel(self.inventry,text="| _____ Sir No.. _____ |",text_color="black")
        self.Sir_no.grid(row=0,column=0)
        for i in self.rows:
            self.sir_no = customtkinter.CTkLabel(self.inventry,text=i[0],text_color="black")
            self.sir_no.grid(row=i[0],column=0)
                                        # Name column
        self.Name = customtkinter.CTkLabel(self.inventry,text=" {} Name {} |".format("_"*20,"_"*20),text_color="black")
        self.Name.grid(row=0,column=1)
        for i in self.rows:
            self.name = customtkinter.CTkLabel(self.inventry,text=i[1],text_color="black")
            self.name.grid(row=i[0],column=1)
                                        # Type column
        self.Type = customtkinter.CTkLabel(self.inventry,text=" {} Type {} |".format("_"*20,"_"*20),text_color="black")
        self.Type.grid(row=0,column=2)
        for i in self.rows:
            self.type = customtkinter.CTkLabel(self.inventry,text=i[2],text_color="black")
            self.type.grid(row=i[0],column=2)
                                        # Price
        self.Price= customtkinter.CTkLabel(self.inventry,text=" _____ Price _____ |",text_color="black")
        self.Price.grid(row=0,column=3)
        for i in self.rows:
            self.price = customtkinter.CTkLabel(self.inventry,text=i[3],text_color="black")
            self.price.grid(row=i[0],column=3)
                                    # Quantity 
        self.Quantity = customtkinter.CTkLabel(self.inventry,text=" _____ Quantity _____ |",text_color="black")
        self.Quantity.grid(row=0,column=4)
        

    def refresh_f(self):
        self.protocol(self.inventry1.destroy())
        print("end")
        if self.a==1:
            self.inventry_q()
            self.a=0

app=App()
app.mainloop()