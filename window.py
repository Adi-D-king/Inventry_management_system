import customtkinter
# import functions as ff
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry()
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(self)
        self.frame_left.grid(row=0, column=0, padx=20, pady=(10, 0), sticky="new")
        self.InvButton = customtkinter.CTkButton(self.frame_left, text="Inventry", command=self.Inventry)
        self.InvButton.grid(row=0, column=0, padx=(5,5), pady=(10, 0), sticky="n")
        self.t_itme=customtkinter.CTkLabel(self.frame_left,text="0000",text_color="white")
        self.t_itme.grid(row=0,column=1,padx=(20,0))
        self.InvButton1 = customtkinter.CTkButton(self.frame_left, text="Low_in_stock", command=self.Low_in_stock)
        self.InvButton1.grid(row=1, column=0, padx=(5,5), pady=(10, 10))
        self.l_itme=customtkinter.CTkLabel(self.frame_left,text="0000",text_color="white")
        self.l_itme.grid(row=1,column=1,padx=(20,0))

    def Inventry(self):
        self.frame_right1 = customtkinter.CTkScrollableFrame(self,width=1250,height=800)
        self.frame_right1.grid(row=0,column=1,padx=(5,5))
        self.frame_right_1_1 = customtkinter.CTkFrame(self.frame_right1,height=35,fg_color="light blue")
        self.frame_right_1_1.grid(row=0,column=0,padx=(30,20),pady=(10,0),sticky="w")
        self.frame_right_1_2 = customtkinter.CTkFrame(self.frame_right1,height=35,fg_color="light blue")
        self.frame_right_1_2.grid(row=0,column=1,padx=(15,20),pady=(10,0),sticky="w")
        self.frame_right_1_3 = customtkinter.CTkFrame(self.frame_right1,height=35,fg_color="light blue")
        self.frame_right_1_3.grid(row=0,column=2,padx=(15,20),pady=(10,0),sticky="w")
        self.frame_right_1_4 = customtkinter.CTkFrame(self.frame_right1,height=35,fg_color="light blue")
        self.frame_right_1_4.grid(row=0,column=3,padx=(15,30),pady=(10,0),sticky="e")
        self.Sir_no = customtkinter.CTkLabel(self.frame_right_1_1,text = "| _______________ Sir no.. _______________ |",text_color="black")
        self.Sir_no.grid(row=0,column=0,padx=(15,15),pady=(5,5))
        self.Name = customtkinter.CTkLabel(self.frame_right_1_2,text = "| _______________ Name _______________ |",text_color="black")
        self.Name.grid(row=0,column=0,padx=(15,15),pady=(5,5))
        self.Price = customtkinter.CTkLabel(self.frame_right_1_3,text = "| _______________ Price _______________ |",text_color="black")
        self.Price.grid(row=0,column=0,padx=(15,15),pady=(5,5))
        self.Quantity = customtkinter.CTkLabel(self.frame_right_1_4,text = "| _______________ Quantity _______________ |",text_color="black")
        self.Quantity.grid(row=0,column=0,padx=(15,15),pady=(5,5))
        
        

        # self.rows = ff.inventry()
        # for i in self.rows:
        #     print(i)
        


    def Low_in_stock(self):
        self.frame_right2 = customtkinter.CTkScrollableFrame(self,width=1250,height=800)
        self.frame_right2.grid(row=0,column=1,padx=(5,5))
        self.lable2 = customtkinter.CTkLabel(self.frame_right2,text="Low_in_stock")
        self.lable2.grid(row=0,column=0)


app=App()
app.mainloop()