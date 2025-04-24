import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class ATMGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM Machine")
        self.root.geometry("400x500")

        # Initialize ATM data
        self.balance = 1000
        self.pin = "1234"
        self.transactions = []

        # Create main frame
        self.main_frame = ttk.Frame(root, padding="20")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Create and place widgets
        self.create_widgets()

    def create_widgets(self):
        # Title
        title_label = ttk.Label(self.main_frame, text="ATM Machine", font=('Helvetica', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=2, pady=20)

        # Buttons
        ttk.Button(self.main_frame, text="Check Balance", command=self.check_balance).grid(row=1, column=0,
                                                                                           columnspan=2, pady=5,
                                                                                           sticky=tk.EW)
        ttk.Button(self.main_frame, text="Withdraw Money", command=self.show_withdraw_window).grid(row=2, column=0,
                                                                                                   columnspan=2, pady=5,
                                                                                                   sticky=tk.EW)
        ttk.Button(self.main_frame, text="Deposit Money", command=self.show_deposit_window).grid(row=3, column=0,
                                                                                                 columnspan=2, pady=5,
                                                                                                 sticky=tk.EW)
        ttk.Button(self.main_frame, text="Change PIN", command=self.show_pin_window).grid(row=4, column=0, columnspan=2,
                                                                                          pady=5, sticky=tk.EW)
        ttk.Button(self.main_frame, text="Transaction History", command=self.show_history).grid(row=5, column=0,
                                                                                                columnspan=2, pady=5,
                                                                                                sticky=tk.EW)
        ttk.Button(self.main_frame, text="Exit", command=self.root.quit).grid(row=6, column=0, columnspan=2, pady=20,
                                                                              sticky=tk.EW)

    def check_balance(self):
        messagebox.showinfo("Balance", f"Your current balance is: ${self.balance:.2f}")

    def show_withdraw_window(self):
        withdraw_window = tk.Toplevel(self.root)
        withdraw_window.title("Withdraw Money")
        withdraw_window.geometry("300x150")

        ttk.Label(withdraw_window, text="Enter amount to withdraw:").pack(pady=10)
        amount_entry = ttk.Entry(withdraw_window)
        amount_entry.pack(pady=5)

        def withdraw():
            try:
                amount = float(amount_entry.get())
                if amount <= 0:
                    messagebox.showerror("Error", "Please enter a valid amount!")
                elif amount > self.balance:
                    messagebox.showerror("Error", "Insufficient funds!")
                else:
                    self.balance -= amount
                    self.transactions.append(f"Withdrawal: ${amount:.2f}")
                    messagebox.showinfo("Success", f"Withdrawn ${amount:.2f}\nNew balance: ${self.balance:.2f}")
                    withdraw_window.destroy()
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid number!")

        ttk.Button(withdraw_window, text="Withdraw", command=withdraw).pack(pady=10)

    def show_deposit_window(self):
        deposit_window = tk.Toplevel(self.root)
        deposit_window.title("Deposit Money")
        deposit_window.geometry("300x150")

        ttk.Label(deposit_window, text="Enter amount to deposit:").pack(pady=10)
        amount_entry = ttk.Entry(deposit_window)
        amount_entry.pack(pady=5)

        def deposit():
            try:
                amount = float(amount_entry.get())
                if amount <= 0:
                    messagebox.showerror("Error", "Please enter a valid amount!")
                else:
                    self.balance += amount
                    self.transactions.append(f"Deposit: ${amount:.2f}")
                    messagebox.showinfo("Success", f"Deposited ${amount:.2f}\nNew balance: ${self.balance:.2f}")
                    deposit_window.destroy()
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid number!")

        ttk.Button(deposit_window, text="Deposit", command=deposit).pack(pady=10)

    def show_pin_window(self):
        pin_window = tk.Toplevel(self.root)
        pin_window.title("Change PIN")
        pin_window.geometry("300x200")

        ttk.Label(pin_window, text="Current PIN:").pack(pady=5)
        current_pin_entry = ttk.Entry(pin_window, show="*")
        current_pin_entry.pack(pady=5)

        ttk.Label(pin_window, text="New PIN:").pack(pady=5)
        new_pin_entry = ttk.Entry(pin_window, show="*")
        new_pin_entry.pack(pady=5)

        def change_pin():
            current = current_pin_entry.get()
            new = new_pin_entry.get()

            if current != self.pin:
                messagebox.showerror("Error", "Incorrect current PIN!")
            elif not new.isdigit() or len(new) != 4:
                messagebox.showerror("Error", "PIN must be 4 digits!")
            else:
                self.pin = new
                self.transactions.append("PIN changed")
                messagebox.showinfo("Success", "PIN changed successfully!")
                pin_window.destroy()

        ttk.Button(pin_window, text="Change PIN", command=change_pin).pack(pady=10)

    def show_history(self):
        history_window = tk.Toplevel(self.root)
        history_window.title("Transaction History")
        history_window.geometry("300x400")

        history_text = tk.Text(history_window, height=20, width=35)
        history_text.pack(pady=10, padx=10)

        if not self.transactions:
            history_text.insert(tk.END, "No transactions yet!")
        else:
            for transaction in self.transactions:
                history_text.insert(tk.END, transaction + "\n")

        history_text.config(state=tk.DISABLED)


# Create and run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ATMGUI(root)
    root.mainloop()