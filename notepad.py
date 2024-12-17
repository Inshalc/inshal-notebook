import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

# Function to save the file to a chosen location
def save_file():
    # Ask the user for the file name and location
    file_location = asksaveasfilename(
        defaultextension="txt",  # Default file extension
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]  # Allowed file types
    )
    if not file_location:  # If the user cancels, do nothing
        return

    # Save the content of the text editor to the file
    with open(file_location, "w") as file_output:
        text = text_edit.get(1.0, tk.END)  # Get all text from the editor
        file_output.write(text)

    # Update the window title to show the saved file name
    root.title(f"INSHAL'S NOTEBOOK - {file_location}")

# Function to open an existing file
def open_file():
    # Ask the user to select a file to open
    file_location = askopenfilename(
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if not file_location:  # If no file is selected, do nothing
        return

    # Clear the text editor and load the file content
    text_edit.delete(1.0, tk.END)  # Clear existing text
    with open(file_location, "r") as file_input:
        text = file_input.read()  # Read file content
        text_edit.insert(tk.END, text)  # Insert content into text editor

    # Update the window title to show the opened file name
    root.title(f"INSHAL'S NOTEBOOK - {file_location}")

# Function to center the window on the screen
def center_window(window, width=800, height=600):
    # Get the screen dimensions
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    # Calculate x and y coordinates to center the window
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    # Set the window size and position
    window.geometry(f"{width}x{height}+{x}+{y}")

# Function to apply consistent styles to widgets
def style_widgets():
    # Style the text editor
    text_edit.configure(bg="wheat", font=("Courier", 12))
    # Style the button frame
    frame_button.configure(bg="burlywood")
    # Style individual buttons
    button_open.configure(bg="wheat", font=("Courier", 10))
    button_save.configure(bg="wheat", font=("Courier", 10))
    button_new.configure(bg="wheat", font=("Courier", 10))

# Function to update the status bar with line number and word count
def update_status_bar(event=None):
    row = text_edit.index(tk.INSERT).split(".")[0]  # Current line number
    content = text_edit.get(1.0, tk.END).strip()  # Get all text
    word_count = len(content.split()) if content else 0  # Count words
    status_bar.config(text=f"Line: {row}, Word Count: {word_count}")

# Function to create a new file (clear the text editor)
def new_file():
    text_edit.delete(1.0, tk.END)  # Clear all content
    root.title("INSHAL'S NOTEBOOK - New File")  # Reset window title

# Functions for button hover effects
def on_hover(event):
    event.widget.config(bg="lightgoldenrodyellow")  # Change background color on hover

def off_hover(event):
    event.widget.config(bg="wheat")  # Restore background color

# Function to clear the default placeholder text
def clear_placeholder(event):
    if text_edit.get("1.0", "2.0").strip() == "TAKE YOUR NOTES...":  # Check for default text
        text_edit.delete("1.0", "end")  # Remove placeholder text

# Initialize the main Tkinter window
root = tk.Tk()
root.title("INSHAL'S NOTEBOOK")  # Window title
root.rowconfigure(0, weight=1)  # Make text editor expand vertically
root.columnconfigure(1, weight=1)  # Make text editor expand horizontally
root.config(bg="#6f4f37")  # Set background color for the window

# Create the main text editor widget
text_edit = tk.Text(root, wrap="word", padx=5, pady=5, font=("Courier", 12), bg="wheat", yscrollcommand=None)
text_edit.grid(row=0, column=1, sticky="nsew")  # Position the text editor

# Add a placeholder text to the editor
text_edit.insert("1.0", "TAKE YOUR NOTES...\n")

# Clear placeholder text when user focuses on the editor
text_edit.bind("<FocusIn>", clear_placeholder)

# Create a frame to hold the buttons
frame_button = tk.Frame(root, relief=tk.RAISED, bd=3)
frame_button.grid(row=0, column=0, sticky="ns")  # Place the frame on the left

# Create the "Open File" button
button_open = tk.Button(frame_button, text="OPEN FILE", command=open_file)
button_open.grid(row=0, column=0, padx=5, pady=5, ipadx=10, ipady=10)
button_open.bind("<Enter>", on_hover)  # Add hover effect
button_open.bind("<Leave>", off_hover)

# Create the "New File" button
button_new = tk.Button(frame_button, text="NEW FILE", command=new_file)
button_new.grid(row=1, column=0, padx=5, pady=5, ipadx=10, ipady=10)
button_new.bind("<Enter>", on_hover)
button_new.bind("<Leave>", off_hover)

# Create the "Save As" button
button_save = tk.Button(frame_button, text="SAVE AS", command=save_file)
button_save.grid(row=2, column=0, padx=5, pady=5, ipadx=10, ipady=10)
button_save.bind("<Enter>", on_hover)
button_save.bind("<Leave>", off_hover)

# Create a status bar to display line and word count
status_bar = tk.Label(root, text="Line: 1, Word Count: 0", anchor="e", bg="wheat")
status_bar.grid(row=1, column=0, columnspan=3, sticky="we")

# Update the status bar whenever a key is released or the user clicks
text_edit.bind("<KeyRelease>", update_status_bar)
text_edit.bind("<ButtonRelease>", update_status_bar)

# Center the window on the screen and style all widgets
center_window(root, width=900, height=600)
style_widgets()

# Start the Tkinter event loop
root.mainloop()
