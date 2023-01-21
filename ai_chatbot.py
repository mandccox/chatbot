import tkinter as tk
from tkinter import filedialog
import openai

# Set the API key
openai.api_key = "user key"

def generate_text():
    # Get the prompt from the user input
    prompt = user_input.get()
    
    # Generate text using the GPT-3 API
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Insert the generated text into the Text widget
    generated_text.insert('end', completions.choices[0].text)

def clear_text():
    user_input.delete('0', 'end')

def save_text():
    # Get the contents of the Text widget
    text_content = generated_text.get('1.0', 'end')
    
    # Open a file dialog to select a file to save to
    file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    
    # Write the contents of the Text widget to the selected file
    if file:
        file.write(text_content)
        file.close()

  
# Create the main window
win = tk.Tk()
win.title("Chat Generator")

# Use a grid layout manager for the main window
win.grid_rowconfigure(0, weight=1)
win.grid_columnconfigure(0, weight=1)

# Create a Label widget to display instructions
label = tk.Label(win, text="Enter a prompt for the Chat:")
label.grid(row=0, column=0, pady=10, padx=10, sticky='W')

# Create an Entry widget for the user to input a prompt
user_input = tk.Entry(win, width = 100)
user_input.grid(row=1, column=0, pady=10, padx=10, sticky='W')

# Create a Button widget to generate text
generate_button = tk.Button(win, text="Generate Text", command=generate_text)
generate_button.grid(row=1, column=1, pady=10, padx=10)

# Create a Button widge to clear user input
clear_button = tk.Button(win, text="Clear Text", command=clear_text)
clear_button.grid(row=1, column=2, pady=10, padx=10)

# Create a Text widget to display the generated text
generated_text = tk.Text(win)
generated_text.config(bg='light blue', fg='black')
generated_text.grid(row=2, column=0, columnspan=3, pady=10, padx=10)

# Create a Button widget to save the generated text
save_button = tk.Button(win, text="Save Output", command=save_text)
save_button.grid(row=3, column=0, pady=10, padx=10)

# Create a Button widget to clear the generated text
clear_text_button = tk.Button(win, text="Clear Window", command=lambda: generated_text.delete('1.0', 'end'))
clear_text_button.grid(row=3, column=1, pady=10, padx=10)

# Start the main event loop
win.mainloop()
