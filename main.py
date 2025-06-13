# --- Standard and Third-party Library Imports ---
from tkinter import *
from tkinter import ttk # Themed Tkinter widgets for a more modern look
from deep_translator import GoogleTranslator

# --- Core Functions ---

def translate_text():
    """
    Translates the text from the input field to the language selected in the combobox.
    Updates the output field with the translated text.
    """
    text_to_translate = enter_field.get("1.0", "end-1c").strip()
    selected_language = selected_language_var.get()

    # Validate that there is text to translate.
    if not text_to_translate:
        output_field.config(state=NORMAL)
        output_field.delete("1.0", END)
        output_field.insert(END, "Please enter text to translate.")
        output_field.config(state=DISABLED)
        return

    try:
        # Use GoogleTranslator to perform the translation.
        # Source language is auto-detected, target is set by the user.
        translated_text = GoogleTranslator(source='auto', target=selected_language).translate(text_to_translate)
        
        # Enable the output field to insert text, then disable it again to make it read-only.
        output_field.config(state=NORMAL)
        output_field.delete("1.0", END)
        output_field.insert(END, translated_text)
        output_field.config(state=DISABLED)

    except Exception as e:
        # Handle potential errors (e.g., network issues, invalid language).
        output_field.config(state=NORMAL)
        output_field.delete("1.0", END)
        output_field.insert(END, f"An error occurred:\n{e}")
        output_field.config(state=DISABLED)


def clear_text():
    """Clears the text from the input and output fields."""
    enter_field.delete(1.0, END)
    output_field.config(state=NORMAL)
    output_field.delete(1.0, END)
    output_field.config(state=DISABLED)
    

# --- GUI Initialization ---

# Create the main application window (root).
window = Tk()
window.title("Simple Translator")
window.minsize(900, 650)
window.resizable(width=False, height=False) # Lock the window size.
window.config(bg="#2C3E4C")


# --- Frame Setup ---
# Using frames helps organize the layout.
top_frame = Frame(window, bg="#2C3E4C")
bottom_frame = Frame(window, bg="#2C3E4C") # Set background to match window

top_frame.pack(padx=15, pady=15)
bottom_frame.pack(padx=10, pady=10)


# --- Language Selection Setup ---
# Initialize an instance of the translator to get available languages.
translator = GoogleTranslator()
# Fetch a list of all supported languages for the dropdown menu.
available_languages = list(translator.get_supported_languages(as_dict=True).values())


# Label indicating that the source language is auto-detected.
language_label = Label(window, text="Auto Detected Language", font=("Helvetica", 12),
                       bg="gray", fg="white", borderwidth=2, relief="ridge")
language_label.place(x=10, y=15)

# Combobox (dropdown menu) for selecting the target language.
selected_language_var = StringVar(value="english") # Default to English
language_combobox = ttk.Combobox(window, textvariable=selected_language_var,
                                 values=available_languages, font=("Helvetica", 12),
                                 state="readonly") # Make the combobox read-only
language_combobox.place(x=740, y=15)


# --- Text Fields Setup ---

# Input field (Text widget) for the user to enter text.
enter_field = Text(bottom_frame, font=("Helvetica", 15), borderwidth=5, relief="ridge",
                   width=40, height=25, wrap="word") # wrap="word" improves text wrapping
enter_field.focus()
enter_field.pack(side=LEFT, padx=5, pady=5)

# Output field (Text widget) to display the translated text.
output_field = Text(bottom_frame, font=("Helvetica", 15), borderwidth=5, relief="ridge",
                    width=40, height=25, wrap="word")
output_field.config(state=DISABLED) # Start in a disabled (read-only) state.
output_field.pack(side=LEFT, padx=5, pady=5)


# --- Action Buttons Setup ---

# Button to trigger the translation.
button_translate = Button(window, text="Translate", bg="gray", fg="white", font=("Arial", 10),
                          borderwidth=5, relief="raised", activebackground="#59788E",
                          activeforeground="black", command=translate_text)
button_translate.place(x=820, y=603) # Adjusted position slightly

# Button to clear the text fields.
button_clear = Button(window, text="Clear", bg="gray", fg="white", font=("Arial", 10),
                      borderwidth=5, relief="raised", activebackground="#59788E",
                      activeforeground="black", command=clear_text)
button_clear.place(x=760, y=603) # Adjusted position slightly


# --- Main Event Loop ---
# Starts the Tkinter event loop, which listens for user actions.
window.mainloop()
