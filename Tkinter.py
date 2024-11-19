import tkinter as tk
from tkinter import filedialog

def submit():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    email = email_entry.get()
    age = age_entry.get()
    # You can process the file or display a message after submission
    print(f"Name: {first_name} {last_name}, Email: {email}, Age: {age}")
    print(f"File Uploaded: {file_path.get()}")

def upload_file():
    file = filedialog.askopenfilename(title="Choose a File")
    file_path.set(file)

# Create main application window
root = tk.Tk()
root.title("Healthify")
root.geometry("500x600")
root.configure(bg="#2c3e50")

# Heading
heading_label = tk.Label(root, text="HEALTHIFY", font=("Arial", 30), bg="#2c3e50", fg="white")
heading_label.pack(pady=10)

# Form frame
form_frame = tk.Frame(root, bg="#34495e", padx=100, pady=100)
form_frame.pack(pady=20)

tk.Label(form_frame, text="First Name", bg="#34495e", fg="white").grid(row=0, column=0, sticky="w", pady=5)
first_name_entry = tk.Entry(form_frame, width=30)
first_name_entry.grid(row=0, column=1, pady=5)
tk.Label(form_frame, text="Last Name", bg="#34495e", fg="white").grid(row=1, column=0, sticky="w", pady=5)
last_name_entry = tk.Entry(form_frame, width=30)
last_name_entry.grid(row=1, column=1, pady=5)


tk.Label(form_frame, text="Email", bg="#34495e", fg="white").grid(row=2, column=0, sticky="w", pady=5)
email_entry = tk.Entry(form_frame, width=30)
email_entry.grid(row=2, column=1, pady=5)


tk.Label(form_frame, text="Select Age", bg="#34495e", fg="white").grid(row=3, column=0, sticky="w", pady=5)
age_entry = tk.Entry(form_frame, width=30)
age_entry.grid(row=3, column=1, pady=5)




tk.Label(form_frame, text="Upload File", bg="#34495e", fg="white").grid(row=4, column=0, sticky="w", pady=5)
file_path = tk.StringVar()
file_button = tk.Button(form_frame, text="Choose File", command=upload_file)
file_button.grid(row=4, column=1, sticky="w", pady=5)
submit_button = tk.Button(root, text="Submit", command=submit, bg="#27ae60", fg="white", width=20)
submit_button.pack(pady=20)

root.mainloop()//Run
