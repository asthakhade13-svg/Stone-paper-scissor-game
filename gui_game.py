import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Stone Paper Scissors")
        self.root.geometry("460x540")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e2f")

        self.cscore = 0
        self.hscore = 0
        self.choices = {1: "Stone 🪨", 2: "Paper 📄", 3: "Scissor ✂️"}

        self.create_widgets()

    def create_widgets(self):
        # Title
        title_label = tk.Label(
            self.root,
            text="Stone • Paper • Scissor",
            font=("Helvetica", 18, "bold"),
            bg="#1e1e2f",
            fg="#f5f6fa",
            pady=15
        )
        title_label.pack()

        # Scoreboard Frame
        score_frame = tk.Frame(self.root, bg="#2d3436", bd=0, padx=20, pady=12)
        score_frame.pack(fill="x", padx=30, pady=10)

        self.human_score_label = tk.Label(
            score_frame,
            text="👤 You: 0",
            font=("Helvetica", 13, "bold"),
            bg="#2d3436",
            fg="#00cec9"
        )
        self.human_score_label.pack(side="left")

        self.comp_score_label = tk.Label(
            score_frame,
            text="🤖 Computer: 0",
            font=("Helvetica", 13, "bold"),
            bg="#2d3436",
            fg="#ff7675"
        )
        self.comp_score_label.pack(side="right")

        # Status / Result display
        self.display_frame = tk.Frame(self.root, bg="#27293d", padx=15, pady=20, relief="groove")
        self.display_frame.pack(fill="both", padx=30, pady=15)

        self.user_choice_label = tk.Label(
            self.display_frame,
            text="Your Choice: -",
            font=("Helvetica", 11),
            bg="#27293d",
            fg="#dfe6e9"
        )
        self.user_choice_label.pack(pady=3)

        self.comp_choice_label = tk.Label(
            self.display_frame,
            text="Computer Choice: -",
            font=("Helvetica", 11),
            bg="#27293d",
            fg="#dfe6e9"
        )
        self.comp_choice_label.pack(pady=3)

        self.result_label = tk.Label(
            self.display_frame,
            text="Choose your move to start!",
            font=("Helvetica", 14, "bold"),
            bg="#27293d",
            fg="#fdcb6e",
            pady=10
        )
        self.result_label.pack()

        # Buttons Frame
        btn_frame = tk.Frame(self.root, bg="#1e1e2f")
        btn_frame.pack(pady=15)

        btn_style = {
            "font": ("Helvetica", 12, "bold"),
            "width": 10,
            "height": 2,
            "cursor": "hand2",
            "bd": 0,
            "fg": "white"
        }

        self.stone_btn = tk.Button(
            btn_frame,
            text="Stone 🪨",
            bg="#6c5ce7",
            activebackground="#a29bfe",
            command=lambda: self.play_round(1),
            **btn_style
        )
        self.stone_btn.grid(row=0, column=0, padx=6)

        self.paper_btn = tk.Button(
            btn_frame,
            text="Paper 📄",
            bg="#0984e3",
            activebackground="#74b9ff",
            command=lambda: self.play_round(2),
            **btn_style
        )
        self.paper_btn.grid(row=0, column=1, padx=6)

        self.scissor_btn = tk.Button(
            btn_frame,
            text="Scissor ✂️",
            bg="#e17055",
            activebackground="#fab1a0",
            command=lambda: self.play_round(3),
            **btn_style
        )
        self.scissor_btn.grid(row=0, column=2, padx=6)

        # Reset button
        self.reset_btn = tk.Button(
            self.root,
            text="🔄 Restart Game",
            font=("Helvetica", 10, "bold"),
            bg="#636e72",
            fg="white",
            bd=0,
            padx=10,
            pady=6,
            cursor="hand2",
            command=self.reset_game
        )
        self.reset_btn.pack(pady=10)

    def play_round(self, user):
        com = random.randint(1, 3)

        user_name = self.choices[user]
        com_name = self.choices[com]

        self.user_choice_label.config(text=f"Your Choice: {user_name}")
        self.comp_choice_label.config(text=f"Computer Choice: {com_name}")

        # Exact same logic as original code
        if (user == 1 and com == 3) or (user == 2 and com == 1) or (user == 3 and com == 2):
            self.result_label.config(text="🎉 You win!", fg="#00cec9")
            self.hscore += 1
        elif user == com:
            self.result_label.config(text="🤝 Draw!", fg="#fdcb6e")
            self.hscore += 0
        else:
            self.result_label.config(text="💥 Computer wins!", fg="#ff7675")
            self.cscore += 1

        self.update_scores()

        if self.cscore == 5:
            messagebox.showinfo("Game Over", "Computer wins the game!")
            self.disable_buttons()
        elif self.hscore == 5:
            messagebox.showinfo("Game Over", "You win the game!")
            self.disable_buttons()

    def update_scores(self):
        self.human_score_label.config(text=f"👤 You: {self.hscore}")
        self.comp_score_label.config(text=f"🤖 Computer: {self.cscore}")

    def disable_buttons(self):
        self.stone_btn.config(state="disabled")
        self.paper_btn.config(state="disabled")
        self.scissor_btn.config(state="disabled")

    def enable_buttons(self):
        self.stone_btn.config(state="normal")
        self.paper_btn.config(state="normal")
        self.scissor_btn.config(state="normal")

    def reset_game(self):
        self.cscore = 0
        self.hscore = 0
        self.update_scores()
        self.user_choice_label.config(text="Your Choice: -")
        self.comp_choice_label.config(text="Computer Choice: -")
        self.result_label.config(text="Choose your move to start!", fg="#fdcb6e")
        self.enable_buttons()

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsGUI(root)
    root.mainloop()
