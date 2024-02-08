import customtkinter as ctk
import tkinter.messagebox as thmb

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("green")

root = ctk.CTk()
def login_page():
    app = ctk.CTk()
    app.geometry("400x400")
    app.title("Modern Login UI using Customtkinter")
    label = ctk.CTkLabel(app,text="This is the main UI page") 

    label.pack(pady=20) 


    frame = ctk.CTkFrame(master=app) 
    frame.pack(pady=20,padx=40,fill='both',expand=True) 

    label = ctk.CTkLabel(master=frame,text='Modern Login System UI') 
    label.pack(pady=12,padx=10) 


    user_entry= ctk.CTkEntry(master=frame,placeholder_text="Username") 
    user_entry.pack(pady=12,padx=10) 

    user_pass= ctk.CTkEntry(master=frame,placeholder_text="Password",show="*") 
    user_pass.pack(pady=12,padx=10) 


    button = ctk.CTkButton(master=frame,text='Login',command=newwindow) 
    button.pack(pady=12,padx=10) 

    checkbox = ctk.CTkCheckBox(master=frame,text='Remember Me') 
    checkbox.pack(pady=12,padx=10) 

    app.mainloop()

def newwindow():
    username = "root"
    password = "root"
    new_window = ctk.CTkToplevel(app) 
    new_window.title("New Window") 
    new_window.geometry("350x150")
	
    if login_page.user_entry.get() == username and login_page.user_pass.get() == password:
        opt = thmb.showinfo(title="Login Successful",message="You have logged in Successfully")
        ctk.CTkLabel(new_window,text="GeeksforGeeks is best for learning ANYTHING !!").pack() 
        if opt == "ok":
            login_page.destroy()
    elif login_page.user_entry.get() == username and login_page.user_pass.get() != password: 
        thmb.showwarning(title='Wrong password',message='Please check your password') 
    elif login_page.user_entry.get() != username and login_page.user_pass.get() == password: 
        thmb.showwarning(title='Wrong username',message='Please check your username') 
    else: 
        thmb.showerror(title="Login Failed",message="Invalid Username and password")

login_page()
root.mainloop