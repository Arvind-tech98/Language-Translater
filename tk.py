from tkinter import *
from tkinter import ttk
from googletrans import Translator

def on_translate(text_entry, language_entry, translated_label):
    text = text_entry.get()
    language = language_entry.get()
    translator = Translator()
    translated_text = translator.translate(text, dest=language).text
    translated_label.config(text=translated_text)

def main():
    # Create the Tkinter window
    root = Tk()
    root.title("Language Translator")

    # Create the widgets
    text_label = Label(root, text="Text:")
    text_entry = Entry(root)
    language_label = Label(root, text="Language:")
    language_entry = Entry(root)
    translate_button = Button(root, text="Translate", command=lambda: on_translate(text_entry, language_entry, translated_label))
    translated_label = Label(root, text="")

    # Add the widgets to the Tkinter window
    text_label.grid(row=0, column=0)
    text_entry.grid(row=0, column=1)
    language_label.grid(row=1, column=0)
    language_entry.grid(row=1, column=1)
    translate_button.grid(row=2, column=0, columnspan=2)
    translated_label.grid(row=3, column=0, columnspan=2)

    # Start the Tkinter event loop
    root.mainloop()
    
if __name__ == "__main__":
    main()