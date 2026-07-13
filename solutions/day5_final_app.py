# Day 5 - Final App (Complete)
# IWU Crypt v1.0 - Working Encryption/Decryption Desktop App

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import base64

class IWUCrypt:
    def __init__(self, root):
        self.root = root
        root.title("IWU Crypt v1.0")
        root.geometry("600x500")
        root.configure(bg="#0a0a15")
        root.resizable(False, False)
        
        # Style
        self.fg = "#ddd"
        self.bg = "#0a0a15"
        self.card = "#131325"
        self.accent = "#c00"
        
        # Title
        tk.Label(root, text="IWU CRYPT v1.0", font=("Arial", 16, "bold"),
                 fg="#fff", bg=self.bg).pack(pady=(15,5))
        tk.Label(root, text="Encryption / Decryption Tool", font=("Arial", 9),
                 fg="#888", bg=self.bg).pack(pady=(0,15))
        
        # Main frame
        main = tk.Frame(root, bg=self.bg)
        main.pack(fill="both", expand=True, padx=20)
        
        # Cipher selection
        tk.Label(main, text="Cipher:", fg=self.fg, bg=self.bg,
                 font=("Arial", 9)).grid(row=0, column=0, sticky="w", pady=(0,5))
        self.cipher_var = tk.StringVar(value="Caesar")
        cipher_menu = ttk.Combobox(main, textvariable=self.cipher_var,
            values=["Caesar Cipher", "XOR Cipher", "Base64"], state="readonly", width=20)
        cipher_menu.grid(row=0, column=1, sticky="w", pady=(0,5))
        
        # Mode
        tk.Label(main, text="Mode:", fg=self.fg, bg=self.bg,
                 font=("Arial", 9)).grid(row=1, column=0, sticky="w", pady=(0,5))
        self.mode_var = tk.StringVar(value="Encrypt")
        mode_menu = ttk.Combobox(main, textvariable=self.mode_var,
            values=["Encrypt", "Decrypt"], state="readonly", width=20)
        mode_menu.grid(row=1, column=1, sticky="w", pady=(0,5))
        
        # Message
        tk.Label(main, text="Message:", fg=self.fg, bg=self.bg,
                 font=("Arial", 9)).grid(row=2, column=0, sticky="w", pady=(5,2))
        self.entry_text = tk.Text(main, height=3, width=50, bg="#1a1a30",
                                   fg="#fff", insertbackground="#fff",
                                   font=("Courier", 10), relief="flat")
        self.entry_text.grid(row=3, column=0, columnspan=2, pady=(0,8))
        
        # Key (for Caesar/XOR)
        tk.Label(main, text="Key (shift):", fg=self.fg, bg=self.bg,
                 font=("Arial", 9)).grid(row=4, column=0, sticky="w", pady=(0,3))
        self.entry_key = tk.Entry(main, width=15, bg="#1a1a30", fg="#fff",
                                   insertbackground="#fff", font=("Courier", 10),
                                   relief="flat")
        self.entry_key.grid(row=4, column=1, sticky="w", pady=(0,3))
        self.entry_key.insert(0, "3")
        
        # Buttons frame
        btn_frame = tk.Frame(main, bg=self.bg)
        btn_frame.grid(row=5, column=0, columnspan=2, pady=10)
        
        tk.Button(btn_frame, text="RUN", command=self.run_cipher,
                  bg=self.accent, fg="white", font=("Arial", 10, "bold"),
                  width=12, relief="flat", cursor="hand2").pack(side="left", padx=5)
        tk.Button(btn_frame, text="Clear", command=self.clear_all,
                  bg="#333", fg="white", font=("Arial", 10),
                  width=8, relief="flat", cursor="hand2").pack(side="left", padx=5)
        tk.Button(btn_frame, text="Save File", command=self.save_file,
                  bg="#222", fg="white", font=("Arial", 10),
                  width=10, relief="flat", cursor="hand2").pack(side="left", padx=5)
        tk.Button(btn_frame, text="Load File", command=self.load_file,
                  bg="#222", fg="white", font=("Arial", 10),
                  width=10, relief="flat", cursor="hand2").pack(side="left", padx=5)
        
        # Output
        tk.Label(main, text="Output:", fg=self.fg, bg=self.bg,
                 font=("Arial", 9)).grid(row=6, column=0, sticky="w", pady=(5,2))
        self.output = tk.Text(main, height=5, width=50, bg="#1a1a30",
                               fg="#0f0", insertbackground="#fff",
                               font=("Courier", 10), relief="flat")
        self.output.grid(row=7, column=0, columnspan=2, pady=(0,5))
        
        # Copy button
        tk.Button(main, text="Copy Output", command=self.copy_output,
                  bg="#222", fg="white", font=("Arial", 9),
                  width=12, relief="flat", cursor="hand2").grid(row=8, column=0, columnspan=2, pady=5)
        
        # Status
        self.status = tk.Label(main, text="Ready", fg="#555", bg=self.bg,
                                font=("Arial", 8))
        self.status.grid(row=9, column=0, columnspan=2, pady=5)
    
    def caesar(self, text, shift):
        result = ""
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - base + shift) % 26 + base)
            else:
                result += char
        return result
    
    def xor_cipher(self, text, key):
        result = ""
        for char in text:
            result += chr(ord(char) ^ key)
        return result
    
    def run_cipher(self):
        text = self.entry_text.get(1.0, tk.END).strip()
        if not text:
            messagebox.showwarning("Input Error", "Enter a message first.")
            return
        
        cipher = self.cipher_var.get()
        mode = self.mode_var.get()
        key_text = self.entry_key.get().strip()
        
        try:
            if cipher == "Caesar Cipher":
                shift = int(key_text) if key_text else 3
                if mode == "Encrypt":
                    result = self.caesar(text, shift)
                else:
                    result = self.caesar(text, -shift)
                self.output.delete(1.0, tk.END)
                self.output.insert(1.0, result)
                self.status.config(text=f"✓ Caesar {mode.lower()}ed with shift {shift}")
            
            elif cipher == "XOR Cipher":
                key = ord(key_text[0]) if key_text else 42
                result = self.xor_cipher(text, key)
                encoded = base64.b64encode(result.encode()).decode()
                self.output.delete(1.0, tk.END)
                if mode == "Encrypt":
                    self.output.insert(1.0, encoded)
                    self.status.config(text=f"✓ XOR encrypted (base64 safe) with key '{chr(key)}'")
                else:
                    decoded = base64.b64decode(text).decode()
                    result = self.xor_cipher(decoded, key)
                    self.output.insert(1.0, result)
                    self.status.config(text=f"✓ XOR decrypted with key '{chr(key)}'")
            
            elif cipher == "Base64":
                if mode == "Encrypt":
                    result = base64.b64encode(text.encode()).decode()
                    self.status.config(text="✓ Base64 encoded")
                else:
                    result = base64.b64decode(text).decode()
                    self.status.config(text="✓ Base64 decoded")
                self.output.delete(1.0, tk.END)
                self.output.insert(1.0, result)
        
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.status.config(text="✗ Error occurred")
    
    def clear_all(self):
        self.entry_text.delete(1.0, tk.END)
        self.output.delete(1.0, tk.END)
        self.status.config(text="Cleared")
    
    def copy_output(self):
        text = self.output.get(1.0, tk.END).strip()
        if text:
            self.root.clipboard_clear()
            self.root.clipboard_append(text)
            self.status.config(text="✓ Copied to clipboard")
    
    def save_file(self):
        text = self.output.get(1.0, tk.END).strip()
        if not text:
            messagebox.showwarning("No Output", "Nothing to save.")
            return
        path = filedialog.asksaveasfilename(defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if path:
            with open(path, "w") as f:
                f.write(text)
            self.status.config(text=f"✓ Saved to {path}")
    
    def load_file(self):
        path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if path:
            with open(path) as f:
                content = f.read()
            self.entry_text.delete(1.0, tk.END)
            self.entry_text.insert(1.0, content)
            self.status.config(text=f"✓ Loaded {path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = IWUCrypt(root)
    root.mainloop()
