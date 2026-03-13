import customtkinter as ctk
import datetime
import random
from questions import QUESTIONS

def get_daily_question():
    """Returns the same question for the whole day, different each day."""
    today = datetime.date.today()
    day_seed = today.year * 1000 + today.timetuple().tm_yday
    rng = random.Random(day_seed)
    return rng.choice(QUESTIONS)

def get_random_question(exclude=None):
    """Returns a random question, optionally different from the current one."""
    choices = [q for q in QUESTIONS if q != exclude]
    return random.choice(choices)

class StoicApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Stoic Daily")
        self.geometry("720x480")
        self.resizable(False, False)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.current_question = get_daily_question()
        self._build_ui()



    def _build_ui(self):
        # Outer frame
        self.frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.frame.pack(fill="both", expand=True, padx=48, pady=48)

        # Top label
        self.label_top = ctk.CTkLabel(
            self.frame,
            text="TODAY'S REFLECTION",
            font=ctk.CTkFont(size=11, weight="normal"),
            text_color="#666666",
            anchor="w"
        )
        self.label_top.pack(anchor="w", pady=(0, 20))

        # Question card
        self.card = ctk.CTkFrame(
            self.frame,
            corner_radius=16,
            fg_color="#1a1a2e",
            border_color="#2a2a4a",
            border_width=1
        )
        self.card.pack(fill="x", pady=(0, 28))

        self.question_label = ctk.CTkLabel(
            self.card,
            text=self.current_question,
            font=ctk.CTkFont(size=20, weight="normal"),
            text_color="#e8e8f0",
            wraplength=580,
            justify="left",
            anchor="w"
        )
        self.question_label.pack(padx=32, pady=40)

        # Date label
        today_str = datetime.date.today().strftime("%A, %B %d, %Y")
        self.date_label = ctk.CTkLabel(
            self.frame,
            text=today_str,
            font=ctk.CTkFont(size=13),
            text_color="#555555",
            anchor="w"
        )
        self.date_label.pack(anchor="w", pady=(0, 24))

        # Button row
        btn_frame = ctk.CTkFrame(self.frame, fg_color="transparent")
        btn_frame.pack(fill="x")

        self.daily_btn = ctk.CTkButton(
            btn_frame,
            text="Today's Question",
            font=ctk.CTkFont(size=14),
            height=44,
            corner_radius=10,
            fg_color="#2a2a4a",
            hover_color="#3a3a6a",
            command=self.show_daily
        )
        self.daily_btn.pack(side="left", padx=(0, 12))

        self.random_btn = ctk.CTkButton(
            btn_frame,
            text="Random Question",
            font=ctk.CTkFont(size=14),
            height=44,
            corner_radius=10,
            fg_color="#1e3a5f",
            hover_color="#2a4e7a",
            command=self.show_random
        )
        self.random_btn.pack(side="left")

        # Footer
        self.footer = ctk.CTkLabel(
            self.frame,
            text="\"Begin at once to live, and count each separate day as a separate life.\" — Seneca",
            font=ctk.CTkFont(size=11, slant="italic"),
            text_color="#3a3a5a",
            wraplength=580,
            anchor="w"
        )
        self.footer.pack(anchor="w", pady=(28, 0))


    def show_daily(self):
        self.current_question = get_daily_question()
        self.question_label.configure(text=self.current_question)

    def show_random(self):
        q = get_random_question(exclude=self.current_question)
        self.current_question = q
        self.question_label.configure(text=q)

if __name__ == "__main__":
    app = StoicApp()
    app.mainloop()

