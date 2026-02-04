# 📚 Flashcard App — Python Desktop Application

A **Python-based desktop flashcard application** built with **Tkinter** that demonstrates GUI design, state management, data persistence, and clean modular programming.  
Designed for efficient studying through **creation, review, and quiz workflows** with persistent local storage.

---

## 🎯 Project Overview

This project showcases my ability to:
- Build **user-friendly desktop applications**
- Manage **application state** and **persistent data**
- Design **modular, maintainable Python code**
- Implement **event-driven programming** with GUIs

The app allows users to **add, quiz, view, and delete flashcards**, with automatic saving to a JSON file.

---

## ✨ Key Features

- **GUI-based Flashcard Management**
  - Add question–answer pairs via popup interface
  - Delete flashcards safely with confirmation prompts

- **Quiz Mode**
  - Randomized flashcard selection
  - Immediate correctness feedback

- **Persistent Storage**
  - Flashcards automatically saved to `flashcards.json`
  - Data persists across application restarts

- **Clean UI & UX**
  - Consistent styling
  - Scrollable flashcard viewer
  - Responsive pop-up windows

---

## 🛠️ Technologies & Skills Demonstrated

| Category | Details |
|--------|---------|
| Language | Python 3 |
| GUI | Tkinter |
| Data Persistence | JSON |
| Concepts | Event-driven programming, file I/O, modular design |
| Libraries | `tkinter`, `json`, `random` |

---

## 🧠 Engineering Highlights

- Clear **separation of concerns** between UI logic and data handling
- Centralized **state management** for flashcards
- **Graceful error handling** for invalid inputs and missing files
- Reusable UI components through styled button abstraction

---

## 📂 Project Structure

```text
flashcard-app/
├── flashcards_gui.py      # Main application logic & UI
├── flashcards.json        # Persistent flashcard storage
└── README.md              # Documentation
```

---

## 🚀 How to Run

```bash
git clone https://github.com/your-username/flashcard-app.git
cd flashcard-app
python flashcards_gui.py
```

**Requirements**
- Python 3.8+
- No external dependencies

---

## 📊 Example Data Format

```json
{
  "Question: ": "What is photosynthesis?",
  "Answer: ": "The process by which plants convert light energy into chemical energy"
}
```

---

## 🎥 Demo

![Flashcard App Demo](flashcard-desktop-application%20recording.gif)

---

## 🔮 Potential Enhancements

- Case-insensitive answer matching
- Flashcard editing
- Scoring and progress tracking
- Import/export functionality
- Conversion to a web app (Flask / React)

---

## 👨‍💻 Author

**Chris Jung**   
Computer Science @ University of California, Riverside
