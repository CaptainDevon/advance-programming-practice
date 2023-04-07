from lzma import CHECK_UNKNOWN
import customtkinter as ctk
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

window=ctk.CTk()
window.geometry("500x350")

def registration():
    print("registration Sucessful")

frame=ctk.CTkFrame(master=window)
frame.pack(pady=20,padx=60,fill="both",expand=True)

label_login_system=ctk.CTkLabel(master=frame,text="login system")
label_login_system.pack(pady=12,padx=10)

entry_username=ctk.CTkEntry(master=frame,placeholder_text="Username")
entry_username.pack(pady=12,padx=10)

entry_address=ctk.CTkEntry(master=frame,placeholder_text="Password",show="*")
entry_address.pack(pady=12,padx=10)

button_login=ctk.CTkButton(master=frame,text="Login",command=registration())
button_login.pack(pady=12,padx=10)

checkbox=ctk.CTkCheckBox(master=window,text="Remember Me")
checkbox.pack(pady=12,padx=10)
window.mainloop()

