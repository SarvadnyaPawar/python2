import tkinter as tk
from tkinter import messagebox
import mysql.connector

# MySQL connection
def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",   # change this to your password
        database="test"
    )

# Submit button action
def submit_data():
    name = entry_name.get()
    email = entry_email.get()

    if name and email:
        try:
            conn = connect_to_db()
            cursor = conn.cursor()
            sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
            cursor.execute(sql, (name, email))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Data submitted successfully!")
            entry_name.delete(0, tk.END)
            entry_email.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to insert data: {e}")
    else:
        messagebox.showwarning("Input Error", "Please fill all fields.")

# GUI setup
root = tk.Tk()
root.title("User Form")

tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=10)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Email:").grid(row=1, column=0, padx=10, pady=10)
entry_email = tk.Entry(root)
entry_email.grid(row=1, column=1, padx=10, pady=10)

submit_btn = tk.Button(root, text="Submit", command=submit_data)
submit_btn.grid(row=2, column=0, columnspan=2, pady=20)

root.mainloop()
