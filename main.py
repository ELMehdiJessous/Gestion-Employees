import tkinter as tk
from tkinter import ttk
import mysql.connector  

# link db with pyton code !
my_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "addEmployee",
)

# use cursor to be able to run msql_quries !
cr = my_db.cursor()

# App
app = tk.Tk()
app.geometry("456x789")

app.mainloop()