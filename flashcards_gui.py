import tkinter as tk
import json
import random

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

    tk.Label(popup, text="Question:").pack(pady=5)
    question_entry = tk.Entry(popup, width=40)
    question_entry.pack(pady=5)

    tk.Label(popup, text="Answer:").pack(pady=5)
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

    tk.Button(popup, text="Save", command=save_new_card).pack(pady=10)

def quiz_flashcards_popup():
    if not flashcards:
        question_label.config(text="No flashcards available.")
        return

    card = random.choice(flashcards)

    popup = tk.Toplevel()
    popup.title("Quiz Flashcard")
    popup.geometry("420x360")

    tk.Label(
        popup,
        text=card["Question: "],
        wraplength=360,
        font=("Arial", 14),
        justify="center"
    ).pack(pady=15)

    answer_entry = tk.Entry(popup, width=30)
    answer_entry.pack(pady=5)

    result_label = tk.Label(popup, text="", font=("Arial", 12))
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

    tk.Button(popup, text="Submit Answer", command=check_answer).pack(pady=5)
    tk.Button(popup, text="Close", command=popup.destroy).pack(pady=5)    

def show_flashcard_list():
    if not flashcards:
        question_label.config(text="No flashcards available.")
        return

    text = ""
    for i, card in enumerate(flashcards, start=1):
        text += (
            f"{i}. Question: {card['Question: ']}\n"
            f"   Answer: {card['Answer: ']}\n\n"
        )

    popup = tk.Toplevel()
    popup.title("Your Flashcards")
    popup.geometry("420x360")

    label = tk.Label(
        popup,
        text=text,
        wraplength=350,
        justify="left",
        font=("Arial", 14)
    )
    label.pack(padx=10, pady=10)

def delete_flashcard_gui():
    if not flashcards:
        question_label.config(text="No flashcards to delete.")
        return

    popup = tk.Toplevel()
    popup.title("Delete Flashcard")
    popup.geometry("420x360")

    tk.Label(popup, text="Enter flashcard number to delete:").pack(pady=5)
    entry = tk.Entry(popup)
    entry.pack(pady=5)

    def confirm_delete():
        try:
            index = int(entry.get()) - 1
            if index < 0 or index >= len(flashcards):
                return
            removed = flashcards.pop(index)
            save_flashcards(flashcards)
            question_label.config(text=f"Deleted: {removed['Question: ']}")
            popup.destroy()
        except:
            pass

    tk.Button(popup, text="Delete", command=confirm_delete).pack(pady=5)

def main():
    global question_label, flashcards, current_card, showing_answer

    flashcards = load_flashcards()
    current_card = None
    showing_answer = False

    window = tk.Tk()
    window.title("Flashcard App")
    window.geometry("420x360")

    title_label = tk.Label(
        window,
        text="Flashcard App",
        font=("Arial", 25, "bold"),
        justify="center"
    )
    title_label.pack(pady=10)

    question_label = tk.Label(
    window,
    text="",
    wraplength=380,
    font=("Arial", 14),
    justify="center"
    )
    question_label.pack(pady=20)

    button_frame = tk.Frame(window)
    button_frame.pack(pady=10)

    add_button = tk.Button(button_frame, text="Add Card", width=14, command=add_flashcard_gui)
    add_button.grid(row=1, column=0, pady=5)

    quiz_button = tk.Button(button_frame, text="Quiz", width=14, command=quiz_flashcards_popup)
    quiz_button.grid(row=0, column=0, padx=5)

    show_button = tk.Button(button_frame, text="Show Cards", width=14, command=show_flashcard_list)
    show_button.grid(row=0, column=1, padx=5)

    delete_button = tk.Button(button_frame, text="Delete Card", width=14, command=delete_flashcard_gui)
    delete_button.grid(row=1, column=1, padx=5, pady=5)

    exit_button = tk.Button(button_frame, text="Exit", width=14, command=lambda: exit_app(window))
    exit_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    window.mainloop()

def exit_app(window):
    save_flashcards(flashcards)
    window.destroy()

if __name__ == "__main__":
    main()
