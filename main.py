from tkinter import *
from tkinter import ttk
from deep_translator import GoogleTranslator


# FUNCTIONS
def translate_text():
    text_to_translate = enter_field.get("1.0", "end-1c")
    selected_language = selected_language_var.get()
    translated_text = GoogleTranslator(source='auto', target=selected_language).translate(text_to_translate)
    output_field.config(state=NORMAL)
    output_field.delete("1.0", END)
    output_field.insert(END, translated_text)
    output_field.config(state=DISABLED)


def clear_text():
    enter_field.delete(1.0, END)
    
    
    

# WINDOW root
window = Tk()
window.title("Simple Translator")
window.minsize(900,650)
window.resizable(width=False,height=False)
window.config(bg="#2C3E4C")


# FRAMES
top_frame = Frame(window,bg="#2C3E4C")
bottom_frame = Frame(window)


top_frame.pack(padx=15,pady=15)
bottom_frame.pack(padx=10,pady=10)


# LANGUAGE SETTINGS
# Initialize an instance of the class
translator = GoogleTranslator()

# Get available languages
available_languages = translator.get_supported_languages()


# Label for "Auto Detected Lang"
language_label = Label(window, text="Auto Detected Language",font=("Helvetica", 12),bg="gray",fg="white", borderwidth=2, relief="ridge")
language_label.place(x=10,y=15)

# Combobox (Language Options)
selected_language_var = StringVar(value="Choose Language")
language_combobox = ttk.Combobox(window, textvariable=selected_language_var, values=available_languages, font=("Helvetica",12))
language_combobox.place(x=740,y=15)



# FIELDS
# Enter field
enter_field = Text(bottom_frame,font=("Helvetica", 15),borderwidth=5, relief="ridge",width=40,height=25)
enter_field.focus()
enter_field.pack(side=LEFT, padx=5,pady=5)

# Output field
output_field = Text(bottom_frame,font=("Helvetica", 15),borderwidth=5, relief="ridge",width=40,height=25)
output_field.pack(side=LEFT, padx=5,pady=5)





# BUTTON translate text
button_translate = Button(window, text="Translate",bg="gray",fg="white", font=("Arial", 10),borderwidth=5,relief="raised", activebackground="#59788E",activeforeground="black", command=translate_text)
button_translate.place(x=848,y=603)


# BUTTON clear fields
button_clear = Button(window, text="Clear",bg="gray",fg="white", font=("Arial", 10),borderwidth=5,relief="raised", activebackground="#59788E",activeforeground="black", command=clear_text)
button_clear.place(x=772,y=603)




window.mainloop()