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
        
        # Define colors
        self.bg_color = "#f5f5f5"
        self.primary_color = "#4a90e2"
        self.active_button = "#357ABD"
        
        self.root.configure(bg=self.bg_color)

        # Style configuration for buttons
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TButton",
                        font=self.default_font,
                        padding=6,
                        background=self.primary_color,
                        foreground="white")
        style.map("TButton", background=[("active", self.active_button)])
        
        # Header
        self.header = tk.Label(self.root, text="Adaptive Multi-Agent Chatbot",
                               font=("Segoe UI", 16, "bold"), bg=self.primary_color,
                               fg="white", pady=15)
        self.header.pack(fill=tk.X)

        # Chat display area within a frame for extra padding
        self.chat_frame = tk.Frame(self.root, bg=self.bg_color)
        self.chat_frame.pack(padx=20, pady=15, fill=tk.BOTH, expand=True)
        self.chat_display = scrolledtext.ScrolledText(self.chat_frame, wrap=tk.WORD,
                                                      font=self.default_font, bg="white",
                                                      fg="black", borderwidth=1, relief="solid")
        self.chat_display.pack(fill=tk.BOTH, expand=True)
        self.chat_display.configure(state='disabled')

        # Input area frame
        self.input_frame = tk.Frame(self.root, bg=self.bg_color)
        self.input_frame.pack(padx=20, pady=10, fill=tk.X)

        # User input entry with border style
        self.user_input = tk.Entry(self.input_frame, font=self.default_font,
                                   relief="solid", borderwidth=1)
        self.user_input.pack(side=tk.LEFT, padx=(0, 10), pady=5, ipady=5, fill=tk.X, expand=True)
        self.user_input.bind("<Return>", self.send_message)

        # Send button
        self.send_button = ttk.Button(self.input_frame, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.RIGHT)

    def send_message(self, event=None):
        query = self.user_input.get().strip()
        if not query:
            return

        self.append_text(f"You: {query}\n")
        self.user_input.delete(0, tk.END)

        try:
            response = requests.get(API_URL, params={"query": query})
            json_data = response.json()
            # Handle nested response dictionaries
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
