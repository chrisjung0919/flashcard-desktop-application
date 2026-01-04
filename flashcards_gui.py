import tkinter as tk
import json
import random
from tkinter import messagebox

# -------------------------
# UI Styling
# -------------------------

BG_COLOR = "#f4f4f4"
CARD_COLOR = "#ffffff"
ACCENT_COLOR = "#4a90e2"

FONT_TITLE = ("Segoe UI", 24, "bold")
FONT_TEXT = ("Segoe UI", 14)
FONT_BUTTON = ("Segoe UI", 11)

def save_flashcards(flashcards):
    with open("flashcards.json", "w") as file:
        json.dump(flashcards, file)

def load_flashcards():
    try:
        with open("flashcards.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def add_flashcard_gui():
    popup = tk.Toplevel()
    popup.title("Add Flashcard")
    popup.geometry("420x360")
    popup.configure(bg=BG_COLOR)

    tk.Label(
        popup,
        text="Question:",
        font=FONT_TEXT,
        bg=BG_COLOR,
        fg="#333333"
    ).pack(pady=5)

    question_entry = tk.Entry(popup, width=40)
    question_entry.pack(pady=5)

    tk.Label(
        popup,
        text="Answer:",
        font=FONT_TEXT,
        bg=BG_COLOR,
        fg="#333333"
    ).pack(pady=5)

    answer_entry = tk.Entry(popup, width=40)
    answer_entry.pack(pady=5)

    def save_new_card():
        question = question_entry.get().strip()
        answer = answer_entry.get().strip()

        if not question or not answer:
            return

        flashcards.append({
            "Question: ": question,
            "Answer: ": answer
        })

        save_flashcards(flashcards)
        question_label.config(text="Flashcard added!")
        popup.destroy()

    styled_button(popup, "Save", save_new_card).pack(pady=10)

def quiz_flashcards_popup():
    if not flashcards:
        question_label.config(text="No flashcards available.")
        return

    card = random.choice(flashcards)

    popup = tk.Toplevel()
    popup.title("Quiz Flashcard")
    popup.geometry("420x360")
    popup.configure(bg=BG_COLOR)

    tk.Label(
        popup,
        text=card["Question: "],
        wraplength=360,
        font=FONT_TEXT,
        bg=BG_COLOR,
        fg="#333333",
        justify="center"
    ).pack(pady=20)

    answer_entry = tk.Entry(popup, width=30)
    answer_entry.pack(pady=5)

    result_label = tk.Label(
        popup,
        text="",
        font=FONT_TEXT,
        bg=BG_COLOR
    )
    result_label.pack(pady=10)

    def check_answer():
        user_answer = answer_entry.get().strip()

        if user_answer == card["Answer: "]:
            result_label.config(text="✅ Correct!", fg="green")
        else:
            result_label.config(
                text=f"❌ Wrong! Answer: {card['Answer: ']}",
                fg="red"
            )

    styled_button(popup, "Submit Answer", check_answer).pack(pady=10)
    styled_button(popup, "Close", popup.destroy).pack(pady=5)    

def show_flashcard_list():
    if not flashcards:
        question_label.config(text="No flashcards available.")
        return

    popup = tk.Toplevel()
    popup.title("Your Flashcards")
    popup.geometry("500x400")
    popup.configure(bg=BG_COLOR)

    tk.Label(
        popup,
        text="Your Flashcards",
        font=FONT_TITLE,
        bg=BG_COLOR,
        fg="#222222"
    ).pack(pady=(15, 5))

    divider = tk.Frame(popup, height=1, bg="#cccccc")
    divider.pack(fill="x", padx=30, pady=10)

    container = tk.Frame(popup, bg=BG_COLOR)
    container.pack(expand=True, fill="both", padx=15, pady=10)

    scrollbar = tk.Scrollbar(container)
    scrollbar.pack(side="right", fill="y")

    text_widget = tk.Text(
        container,
        wrap="word",
        font=FONT_TEXT,
        bg=CARD_COLOR,
        fg="#333333",
        yscrollcommand=scrollbar.set,
        bd=0,
        padx=10,
        pady=10
    )
    text_widget.pack(expand=True, fill="both")
    scrollbar.config(command=text_widget.yview)

    text_widget.delete("1.0", "end")

    for i, card in enumerate(flashcards, start=1):
        text_widget.insert(
            "end",
            f"{i}. Question:\n{card['Question: ']}\n\n"
            f"Answer:\n{card['Answer: ']}\n\n"
            + "—" * 20 + "\n\n"
        )

    text_widget.config(state="disabled")

    styled_button(popup, "Close", popup.destroy).pack(pady=15)

def delete_flashcard_gui():
    if not flashcards:
        question_label.config(text="No flashcards to delete.")
        return

    popup = tk.Toplevel()
    popup.title("Delete Flashcard")
    popup.geometry("420x360")
    popup.configure(bg=BG_COLOR)

    # Title
    tk.Label(
        popup,
        text="Delete Flashcard",
        font=FONT_TITLE,
        bg=BG_COLOR,
        fg="#222222"
    ).pack(pady=(15, 5))

    divider = tk.Frame(popup, height=1, bg="#cccccc")
    divider.pack(fill="x", padx=30, pady=10)

    # Instructions
    tk.Label(
        popup,
        text="Enter the number of the flashcard to delete:",
        font=FONT_TEXT,
        bg=BG_COLOR,
        fg="#333333"
    ).pack(pady=10)

    entry = tk.Entry(popup, width=10, font=FONT_TEXT, justify="center")
    entry.pack(pady=5)

    feedback_label = tk.Label(
        popup,
        text="",
        font=FONT_TEXT,
        bg=BG_COLOR
    )
    feedback_label.pack(pady=10)

    def confirm_delete():
        try:
            index = int(entry.get()) - 1
            if index < 0 or index >= len(flashcards):
                feedback_label.config(text="❌ Invalid flashcard number.", fg="red")
                return

            confirm = messagebox.askyesno(
                "Confirm Delete",
                "Are you sure you want to delete this flashcard?"
            )
            if not confirm:
                return

            removed = flashcards.pop(index)
            save_flashcards(flashcards)
            question_label.config(text=f"Deleted: {removed['Question: ']}")
            popup.destroy()

        except ValueError:
            feedback_label.config(text="❌ Please enter a valid number.", fg="red")

    # Buttons
    button_container = tk.Frame(popup, bg=BG_COLOR)
    button_container.pack(pady=20)

    styled_button(button_container, "Delete", confirm_delete).grid(row=0, column=0, padx=6)
    styled_button(button_container, "Cancel", popup.destroy).grid(row=0, column=1, padx=6)

def main():
    global question_label, flashcards, current_card, showing_answer

    flashcards = load_flashcards()
    current_card = None
    showing_answer = False

    window = tk.Tk()
    window.title("Flashcard App")
    window.geometry("420x360")
    window.configure(bg=BG_COLOR)

    title_label = tk.Label(
        window,
        text="Flashcard App",
        font=FONT_TITLE,
        bg=BG_COLOR,
        fg="#222222"
    )
    title_label.pack(pady=(15, 5))

    divider = tk.Frame(window, height=1, bg="#cccccc")
    divider.pack(fill="x", padx=30, pady=10)

    question_label = tk.Label(
        window,
        text="Select an option to begin",
        wraplength=360,
        font=FONT_TEXT,
        bg=BG_COLOR,
        fg="#333333",
        justify="center"
    )
    question_label.pack(pady=15)

    button_frame = tk.Frame(window, bg=BG_COLOR)
    button_frame.pack(pady=20)

    quiz_button = styled_button(button_frame, "Quiz", quiz_flashcards_popup)
    quiz_button.grid(row=0, column=0, padx=6, pady=6)

    show_button = styled_button(button_frame, "Show Cards", show_flashcard_list)
    show_button.grid(row=0, column=1, padx=6, pady=6)

    add_button = styled_button(button_frame, "Add Card", add_flashcard_gui)
    add_button.grid(row=1, column=0, padx=6, pady=6)

    delete_button = styled_button(button_frame, "Delete Card", delete_flashcard_gui)
    delete_button.grid(row=1, column=1, padx=6, pady=6)

    exit_button = styled_button(button_frame, "Exit", lambda: exit_app(window))
    exit_button.grid(row=2, column=0, columnspan=2, pady=10)

    window.mainloop()

def styled_button(parent, text, command):
    return tk.Button(
        parent,
        text=text,
        command=command,
        width=16,
        font=FONT_BUTTON,
        bg=CARD_COLOR,
        fg="#333333",
        activebackground="#e6e6e6",
        relief="flat",
        bd=1,
        cursor="hand2"
    )

def exit_app(window):
    save_flashcards(flashcards)
    window.destroy()

if __name__ == "__main__":
    main()
