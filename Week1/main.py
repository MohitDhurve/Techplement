# importing Python Libraries
import random
import string
from tkinter import *
from tkinter import messagebox


# Function to generate the password
def generate_password(length, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    # Define character sets based on user preferences
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase  # Uppercase Letters like A, B,....Z
    if use_lowercase:
        characters += string.ascii_lowercase  # Lowercase Letters like a, b,...z
    if use_digits:
        characters += string.digits  # Digits
    if use_special:
        characters += string.punctuation  # Special Characters like ? / $ etc

    # Ensure there is at least one character set selected
    if not characters:
        raise ValueError("At least one character type must be selected")

    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))

    return password


# Function to handle the generation process when the button is clicked
def on_generate():
    try:
        length = int(entry_length.get())
        use_uppercase = var_uppercase.get()
        use_lowercase = var_lowercase.get()
        use_digits = var_digits.get()
        use_special = var_special.get()

        # Generate the password
        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
        # Display the password in the result entry
        entry_result.delete("1.0", END)
        entry_result.insert(END, password)
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))
    except Exception as e:
        messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    # Create the main window
    root = Tk()
    root.title("Password Generator")
    photo = PhotoImage(file='lock.png')
    root.iconphoto(False,photo)

    # Create and place the welcome label
    welcome_label = Label(root, text="Welcome to Password Generator !", font=('Helvetica', 14, 'bold'))
    welcome_label.pack(pady=10)

    # Create a frame for the input fields and other widgets
    frame = Frame(root)
    frame.pack(padx=10, pady=10)

    # Create and place the widgets
    Label(frame, text="Enter the length of the password:").grid(row=0, column=0, sticky=W)
    entry_length = Entry(frame)
    entry_length.grid(row=0, column=1)

    var_uppercase = BooleanVar(value=True)
    Checkbutton(frame, text="Include uppercase letters", variable=var_uppercase).grid(row=1, columnspan=2, sticky=W)

    var_lowercase = BooleanVar(value=True)
    Checkbutton(frame, text="Include lowercase letters", variable=var_lowercase).grid(row=2, columnspan=2, sticky=W)

    var_digits = BooleanVar(value=True)
    Checkbutton(frame, text="Include digits", variable=var_digits).grid(row=3, columnspan=2, sticky=W)

    var_special = BooleanVar(value=True)
    Checkbutton(frame, text="Include special characters", variable=var_special).grid(row=4, columnspan=2, sticky=W)

    Button(frame, text="Generate Password", command=on_generate).grid(row=5, columnspan=2, pady=10)

    Label(frame, text="Generated Password:").grid(row=6, column=0, sticky=W)
    entry_result = Text(frame, height=1, wrap=NONE)
    entry_result.grid(row=6, column=1, sticky="ew")

    # Make the column containing the Text widget expandable
    frame.grid_columnconfigure(1, weight=1)

    # Run the main event loop
    root.mainloop()
