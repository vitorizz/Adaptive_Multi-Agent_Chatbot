import requests
import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk

API_URL = "http://127.0.0.1:8000/query"

class ChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Adaptive Multi-Agent Chatbot")
        self.root.geometry("700x500")
        self.default_font = ("Segoe UI", 11)
        self.root.configure(bg="#e6ecf0")

        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TButton",
                        font=self.default_font,
                        padding=6,
                        background="#0078D7",
                        foreground="white")

        self.header = tk.Label(self.root, text="Adaptive Multi-Agent Chatbot", font=("Segoe UI", 14, "bold"), bg="#0078D7", fg="white", pady=10)
        self.header.pack(fill=tk.X)

        self.chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20, font=self.default_font, bg="white", fg="black", borderwidth=0)
        self.chat_display.pack(padx=10, pady=(10, 0))

        self.input_frame = tk.Frame(root, bg="#e6ecf0")
        self.input_frame.pack(padx=10, pady=(0, 10), fill=tk.X)

        self.user_input = tk.Entry(self.input_frame, width=60, font=self.default_font, relief=tk.FLAT)
        self.user_input.pack(side=tk.LEFT, padx=(0, 10), pady=5, ipady=6, expand=True, fill=tk.X)
        self.user_input.bind("<Return>", self.send_message)

        self.send_button = ttk.Button(self.input_frame, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.RIGHT)

    def send_message(self, event=None):
        query = self.user_input.get().strip()
        if query == "":
            return

        self.append_text(f"You: {query}\n")
        self.user_input.delete(0, tk.END)

        try:
            response = requests.get(API_URL, params={"query": query})
            json_data = response.json()

            # Handle case where response is a nested dict
            if isinstance(json_data.get("response"), dict):
                answer = json_data["response"].get("response", "No response from server.")
            else:
                answer = json_data.get("response", "No response from server.")
        except Exception as e:
            answer = f"Error: {str(e)}"

        self.append_text(f"Bot: {answer}\n")

    def append_text(self, text):
        self.chat_display.configure(state='normal')
        self.chat_display.insert(tk.END, text)
        self.chat_display.configure(state='disabled')
        self.chat_display.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatApp(root)
    root.mainloop()