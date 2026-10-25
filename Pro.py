import tkinter as tk
from tkinter import messagebox

def display_bio():
    # Retrieve user input from entry fields
    name = entry_name.get().strip()
    age = entry_age.get().strip()
    email = entry_email.get().strip()
    occupation = entry_occupation.get().strip()
    bio_summary = text_bio.get("1.0", tk.END).strip()
    
    # Simple validation to ensure fields aren't completely blank
    if not name or not age or not email:
        messagebox.showwarning("Incomplete Form", "Please fill out at least Name, Age, and Email.")
        return

    # Construct the personal bio layout
    formatted_bio = (
        f"=== PERSONAL BIO ===\n\n"
        f"Name: {name}\n"
        f"Age: {age}\n"
        f"Email: {email}\n"
        f"Occupation: {occupation if occupation else 'Not specified'}\n\n"
        f"About Me:\n{bio_summary if bio_summary else 'No summary provided.'}"
    )
    
    # Update the display label to show the completed bio
    label_output.config(text=formatted_bio)

# 1. Create the main application window
root = tk.Tk()
root.title("Personal Bio Form")
root.geometry("450x550")
root.resizable(False, False)

# 2. Main Title Header
label_title = tk.Label(root, text="Personal Bio Form", font=("Arial", 16, "bold"), pady=10)
label_title.pack()

# 3. Create a Frame to keep grid elements organized and clean
form_frame = tk.Frame(root, padx=20, pady=10)
form_frame.pack(fill="x")

# Configure weights for the columns to make them resize nicely within the frame
form_frame.columnconfigure(1, weight=1)

# Name Row
label_name = tk.Label(form_frame, text="Full Name:", font=("Arial", 10, "bold"))
label_name.grid(row=0, column=0, sticky="w", pady=5)
entry_name = tk.Entry(form_frame, font=("Arial", 10))
entry_name.grid(row=0, column=1, sticky="ew", pady=5)

# Age Row
label_age = tk.Label(form_frame, text="Age:", font=("Arial", 10, "bold"))
label_age.grid(row=1, column=0, sticky="w", pady=5)
entry_age = tk.Entry(form_frame, font=("Arial", 10))
entry_age.grid(row=1, column=1, sticky="ew", pady=5)

# Email Row
label_age = tk.Label(form_frame, text="Email:", font=("Arial", 10, "bold"))
label_age.grid(row=2, column=0, sticky="w", pady=5)
entry_email = tk.Entry(form_frame, font=("Arial", 10))
entry_email.grid(row=2, column=1, sticky="ew", pady=5)

# Occupation Row
label_occ = tk.Label(form_frame, text="Occupation:", font=("Arial", 10, "bold"))
label_occ.grid(row=3, column=0, sticky="w", pady=5)
entry_occupation = tk.Entry(form_frame, font=("Arial", 10))
entry_occupation.grid(row=3, column=1, sticky="ew", pady=5)

# Short Bio Textbox Row
label_bio = tk.Label(form_frame, text="Short Bio:", font=("Arial", 10, "bold"))
label_bio.grid(row=4, column=0, sticky="nw", pady=5)
text_bio = tk.Text(form_frame, height=5, font=("Arial", 10))
text_bio.grid(row=4, column=1, sticky="ew", pady=5)

# 4. Action Button
btn_generate = tk.Button(root, text="Generate Bio", command=display_bio, bg="#4CAF50", fg="white", font=("Arial", 11, "bold"), pady=5)
btn_generate.pack(pady=10)

# 5. Output Label Frame (Displays the generated Bio)
output_frame = tk.LabelFrame(root, text="Generated Bio Summary", padx=15, pady=15, font=("Arial", 10, "italic"))
output_frame.pack(fill="both", expand=True, padx=20, pady=10)

label_output = tk.Label(output_frame, text="Fill out the form and click 'Generate Bio' above.", justify="left", anchor="nw", font=("Courier", 10))
label_output.pack(fill="both", expand=True)

# 6. Start the main event loop
root.mainloop()
