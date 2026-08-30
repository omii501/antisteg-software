import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

from backend.main import analyze_file


def browse_file():
    path = filedialog.askopenfilename(
        title="Select image or file",
        filetypes=[("All files", "*.*")]
    )
    if path:
        entry.delete(0, tk.END)
        


def scan():
    path = entry.get().strip()
    if not path:
        messagebox.showerror("Error", "Select a file first")
        return

    output.delete("1.0", tk.END)
    output.insert(tk.END, "Scanning...\n\n")

    try:
        result = analyze_file(path)

        risk = result["risk_level"]
        color = {"LOW": "green", "MEDIUM": "orange", "HIGH": "red"}[risk]

        output.insert(tk.END, f"Risk Level: {risk}\n", ("risk",))
        output.insert(tk.END, f"Risk Score: {result['risk_score']}\n\n")
        output.insert(tk.END, "Reasons:\n")

        for r in result["reasons"]:
            output.insert(tk.END, f"- {r}\n")

        output.tag_config("risk", foreground=color, font=("Arial", 12, "bold"))

    except Exception as e:
        messagebox.showerror("Error", str(e))


root = tk.Tk()
root.title("AntiSteg - Steganography Detector")
root.geometry("700x450")
root.resizable(False, False)

tk.Label(root, text="AntiSteg", font=("Arial", 16, "bold")).pack(pady=10)

frame = tk.Frame(root)
frame.pack()

entry = tk.Entry(frame, width=65)
entry.pack(side=tk.LEFT, padx=5)

tk.Button(frame, text="Browse", command=browse_file).pack(side=tk.LEFT)
tk.Button(root, text="Scan File", command=scan, width=20).pack(pady=10)

output = scrolledtext.ScrolledText(root, width=85, height=15)
output.pack(padx=10, pady=10)

root.mainloop()
