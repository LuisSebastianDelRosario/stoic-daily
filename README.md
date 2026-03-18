# 🏛️ Stoic Daily

A minimalist desktop app that gives you one Stoic question every day to reflect on. Built with Python as a personal development tool and portfolio project.

![Python](https://img.shields.io/badge/Python-3.14-blue?style=flat&logo=python)
![CustomTkinter](https://img.shields.io/badge/UI-CustomTkinter-5C85D6?style=flat)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)

---

## What It Does

- Displays a unique Stoic reflection question every day, seeded by the date (same question all day, different the next)
- Includes 255 handwritten questions across themes like discipline, mortality, virtue, courage, and self-knowledge
- "Random Question" button to explore any question from the pool
- Dark and light mode toggle
- Minimalist UI — no clutter, just the question

---

## Screenshots

> Dark Mode

![Dark Mode Screenshot](screenshots/dark.png)

> Light Mode

![Light Mode Screenshot](screenshots/light.png)

---

## Installation

**Requirements:** Python 3.8+

**1. Clone the repository**
```bash
git clone https://github.com/LuisSebastianDelRosario/stoic-daily.git
cd stoic-daily
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the app**
```bash
py main.py
```

---

## Project Structure
```
stoic-daily/
├── main.py          # App entry point and UI logic
├── questions.py     # Pool of 255 Stoic reflection questions
├── requirements.txt # Python dependencies
└── README.md
```

---

## How the Daily Question Works

The app uses Python's `random.Random` with a **date-based seed** — meaning the same question appears all day, but a new one unlocks every midnight. No database needed.
```python
def get_daily_question():
    today = datetime.date.today()
    day_seed = today.year * 1000 + today.timetuple().tm_yday
    rng = random.Random(day_seed)
    return rng.choice(QUESTIONS)
```

---

## Dependencies

| Package | Purpose |
|---|---|
| `customtkinter` | Modern UI framework built on tkinter |
| `darkdetect` | Detects system dark/light mode |

Install all with:
```bash
pip install -r requirements.txt
```

---

## Question Themes

The 255 questions are organized around core Stoic themes:

- **Marcus Aurelius** — self-discipline, inner life, ego
- **Seneca** — time, mortality, how we spend our days
- **Epictetus** — freedom, acceptance, what is in our control
- **Virtue & character** — justice, courage, temperance, honesty
- **Relationships** — listening, service, conflict, gratitude
- **Wealth & simplicity** — desire, envy, what we truly need
- **Obstacles & adversity** — reframing difficulty, resilience
- **Purpose & meaning** — legacy, priorities, direction
- **Death & impermanence** — mortality, urgency, regret
- **Self-knowledge** — blind spots, habits, private vs public self
- **Daily discipline** — consistency, focus, morning intention
- **Evening reflection** — review, learning, closure

---

## What I Learned Building This

- Structuring a Python project across multiple modules
- Using `datetime` and seeded `random` to create deterministic daily behavior
- Building a desktop GUI with `customtkinter`
- Implementing dark/light mode toggling with dynamic widget updates
- Git workflow: init → commit → push to GitHub

---

## Author

**Luis Sebastian Del Rosario**
- GitHub: [@LuisSebastianDelRosario](https://github.com/LuisSebastianDelRosario)

---

## License

MIT License — feel free to use, modify, and share.