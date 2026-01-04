def toggle_answer():
    global showing_answer

    if not current_card:
        return

    if not showing_answer:
        question_label.config(text=current_card["Answer: "])
        showing_answer = True
    else:
        show_card()