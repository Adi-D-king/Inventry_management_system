import customtkinter as ctk

def Check_Login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "root" and password == "0123":
        Login_Window.after(100, Open_New_Window)
        Login_Window.withdraw()
    else:
        error_label.configure(text="Invalid username or password", text_color="red", fg_color="transparent")

def Open_New_Window():
    New_Window = ctk.CTkToplevel(Login_Window)
    New_Window.title("Welcome Page - 1")
    # New_Window.geometry("400x250")
    label = ctk.CTkLabel(New_Window, text="Welcome! You have successfully logged in.", text_color="green", fg_color="transparent")
    label.pack(padx=20, pady=20)

    # Bind the closing event of the new window to a function
    New_Window.protocol("WM_DELETE_WINDOW", Complete_Closing)

def Complete_Closing():
    # Destroy the main login window when the new window is closed
    Login_Window.destroy()

# Create main login window
Login_Window = ctk.CTk()
Login_Window.title("Login Window")
Login_Window.geometry("250x250")

# Username Label and Entry
username_label = ctk.CTkLabel(Login_Window, text="Username:")
username_label.pack(pady=(10, 0))
username_entry = ctk.CTkEntry(Login_Window)
username_entry.pack(pady=(5, 10))

# Password Label and Entry
password_label = ctk.CTkLabel(Login_Window, text="Password:")
password_label.pack(pady=5)
password_entry = ctk.CTkEntry(Login_Window, show="*")
password_entry.pack(pady=(0, 10))

# Error Label
error_label = ctk.CTkLabel(Login_Window, text="")
error_label.pack()

# Login Button
login_button = ctk.CTkButton(Login_Window, text="Login", command=Check_Login)
login_button.pack(pady=5)

Login_Window.mainloop()