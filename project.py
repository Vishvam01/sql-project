
import tkinter as tk
from tkinter import messagebox, ttk


class OnlineVotingSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Online Voting System")
        self.root.geometry("1000x700")
        self.password = "admin123"

        # In-memory storage for voters and candidates
        self.voters = {}
        self.candidates = {
            "Prince": 0,
            "Vishvam": 0,
            "Yash": 0,
            "Rajeev": 0
        }

        self.create_widgets()

    def create_widgets(self):
        # Title
        title = tk.Label(self.root, text="Online Voting System", font=("Arial", 24), bg="blue", fg="white")
        title.pack(pady=10)

        # Voter Registration Section
        self.voter_frame = tk.Frame(self.root, bg="lightgray")
        self.voter_frame.pack(pady=20, padx=20)

        tk.Label(self.voter_frame, text="Name:", bg="lightgray").grid(row=0, column=0)
        self.voter_name = tk.Entry(self.voter_frame)
        self.voter_name.grid(row=0, column=1)

        tk.Label(self.voter_frame, text="Email:", bg="lightgray").grid(row=1, column=0)
        self.voter_email = tk.Entry(self.voter_frame)
        self.voter_email.grid(row=1, column=1)

        tk.Button(self.voter_frame, text="Register Voter", command=self.register_voter, bg="green", fg="white").grid(row=2, columnspan=2)

        # Voting Section
        self.vote_frame = tk.Frame(self.root, bg="lightyellow")
        self.vote_frame.pack(pady=20, padx=20)

        tk.Label(self.vote_frame, text="Select Candidate:", bg="lightyellow").grid(row=0, column=0)
        self.candidate_combobox = ttk.Combobox(self.vote_frame, values=list(self.candidates.keys()))
        self.candidate_combobox.grid(row=0, column=1)

        tk.Button(self.vote_frame, text="Vote", command=self.cast_vote, bg="green", fg="white").grid(row=1, columnspan=2)

        # Display Results Button with password
        tk.Button(self.root, text="Show Results", command=self.check_password_results, bg="purple", fg="white").pack(pady=20)

        # View Voters Button with password
        tk.Button(self.root, text="View Voters", command=self.check_password_voters, bg="purple", fg="white").pack(pady=10)

        # Delete Voter Button with password
        tk.Button(self.root, text="Delete Voter Data", command=self.check_password_delete_voter, bg="red", fg="white").pack(pady=10)

        # Delete All Data Button with password
        tk.Button(self.root, text="Delete All Data", command=self.check_password_delete_all_data, bg="red", fg="white").pack(pady=10)

    def register_voter(self):
        name = self.voter_name.get().strip()
        email = self.voter_email.get().strip()

        if not name or not email:
            messagebox.showerror("Error", "All fields are required!")
            return

        if email in self.voters:
            messagebox.showerror("Error", "This email is already registered!")
            return

        self.voters[email] = {"name": name, "has_voted": False}
        messagebox.showinfo("Success", "Voter registered successfully!")
        self.voter_name.delete(0, tk.END)
        self.voter_email.delete(0, tk.END)

    def cast_vote(self):
        email = self.voter_email.get().strip()
        candidate_name = self.candidate_combobox.get()

        if not email or not candidate_name:
            messagebox.showerror("Error", "Please enter your email and select a candidate!")
            return

        if email not in self.voters:
            messagebox.showerror("Error", "Voter not registered!")
            return

        if self.voters[email]["has_voted"]:
            messagebox.showwarning("Warning", "You have already voted!")
            return

        if candidate_name not in self.candidates:
            messagebox.showerror("Error", "Selected candidate does not exist.")
            return

        # Record the vote
        self.candidates[candidate_name] += 1
        self.voters[email]["has_voted"] = True
        messagebox.showinfo("Success", "Vote cast successfully!")

    def check_password_results(self):
        self.prompt_password(self.show_results)

    def check_password_voters(self):
        self.prompt_password(self.view_voters)

    def check_password_delete_voter(self):
        self.prompt_password(self.delete_voter)

    def check_password_delete_all_data(self):
        self.prompt_password(self.delete_all_data)

    def prompt_password(self, success_callback):
        password_window = tk.Toplevel(self.root)
        password_window.title("Enter Password")
        password_window.geometry("300x100")

        tk.Label(password_window, text="Enter Password:").pack(pady=10)
        password_entry = tk.Entry(password_window, show="*")
        password_entry.pack()

        def check_password():
            if password_entry.get() == self.password:
                password_window.destroy()
                success_callback()
            else:
                messagebox.showerror("Error", "Incorrect password!")
                password_window.destroy()

        tk.Button(password_window, text="Submit", command=check_password).pack(pady=10)

    def show_results(self):
        result_message = "Voting Results:\n"
        for candidate, count in self.candidates.items():
            result_message += f"{candidate}: {count} votes\n"
        messagebox.showinfo("Results", result_message)

    def view_voters(self):
        voter_list = "Registered Voters:\n"
        for email, info in self.voters.items():
            voter_list += f"{info['name']} ({email})\n"
        messagebox.showinfo("Voters", voter_list)

    def delete_voter(self):
        email = self.voter_email.get().strip()
        if not email:
            messagebox.showerror("Error", "Please enter the email of the voter to delete.")
            return

        if email in self.voters:
            del self.voters[email]
            messagebox.showinfo("Success", "Voter deleted successfully!")
            self.voter_email.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Voter not found!")

    def delete_all_data(self):
        self.voters.clear()
        for candidate in self.candidates:
            self.candidates[candidate] = 0
        messagebox.showinfo("Success", "All data deleted successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = OnlineVotingSystem(root)
    root.mainloop()


# import tkinter as tk
# from tkinter import messagebox, ttk
# import mysql.connector

# class OnlineVotingSystem:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Online Voting System")
#         self.root.geometry("1000x700")
#         self.password = "admin123"

#         # Establish database connection
#         try:
#             self.conn = mysql.connector.connect(
#                 host="localhost",
#                 user="your_username",     # Replace with your MySQL username
#                 password="your_password", # Replace with your MySQL password
#                 database="vote"           # Database name created above
#             )
#             self.cursor = self.conn.cursor()
#         except mysql.connector.Error as err:
#             messagebox.showerror("Database Error", f"Error connecting to database: {err}")
#             self.root.destroy()  # Close app if connection fails
#             return

#         self.create_widgets()
#         self.populate_candidates()

#     def create_widgets(self):
#         # Title
#         title = tk.Label(self.root, text="Online Voting System", font=("Arial", 24), bg="blue", fg="white")
#         title.pack(pady=10)

#         # Voter Registration Section
#         self.voter_frame = tk.Frame(self.root, bg="lightgray")
#         self.voter_frame.pack(pady=20, padx=20)

#         tk.Label(self.voter_frame, text="Name:", bg="lightgray").grid(row=0, column=0)
#         self.voter_name = tk.Entry(self.voter_frame)
#         self.voter_name.grid(row=0, column=1)

#         tk.Label(self.voter_frame, text="Email:", bg="lightgray").grid(row=1, column=0)
#         self.voter_email = tk.Entry(self.voter_frame)
#         self.voter_email.grid(row=1, column=1)

#         tk.Button(self.voter_frame, text="Register Voter", command=self.register_voter, bg="green", fg="white").grid(row=2, columnspan=2)

#         # Voting Section
#         self.vote_frame = tk.Frame(self.root, bg="lightyellow")
#         self.vote_frame.pack(pady=20, padx=20)

#         tk.Label(self.vote_frame, text="Select Candidate:", bg="lightyellow").grid(row=0, column=0)
#         self.candidate_combobox = ttk.Combobox(self.vote_frame)
#         self.candidate_combobox.grid(row=0, column=1)

#         tk.Button(self.vote_frame, text="Vote", command=self.cast_vote, bg="green", fg="white").grid(row=1, columnspan=2)

#         # Display Results Button with password
#         tk.Button(self.root, text="Show Results", command=self.check_password_results, bg="purple", fg="white").pack(pady=20)

#         # View Voters Button with password
#         tk.Button(self.root, text="View Voters", command=self.check_password_voters, bg="purple", fg="white").pack(pady=10)

#         # Delete Voter Button with password
#         tk.Button(self.root, text="Delete Voter Data", command=self.check_password_delete_voter, bg="red", fg="white").pack(pady=10)

#         # Delete All Data Button with password
#         tk.Button(self.root, text="Delete All Data", command=self.check_password_delete_all_data, bg="red", fg="white").pack(pady=10)

#     def register_voter(self):
#         name = self.voter_name.get().strip()
#         email = self.voter_email.get().strip()

#         if not name or not email:
#             messagebox.showerror("Error", "All fields are required!")
#             return

#         try:
#             self.cursor.execute("INSERT INTO voters (name, email) VALUES (%s, %s)", (name, email))
#             self.conn.commit()
#             messagebox.showinfo("Success", "Voter registered successfully!")
#         except mysql.connector.Error as err:
#             messagebox.showerror("Database Error", f"Error: {err}")
#         finally:
#             self.voter_name.delete(0, tk.END)
#             self.voter_email.delete(0, tk.END)

#     def populate_candidates(self):
#         try:
#             self.cursor.execute("SELECT name FROM candidates")
#             candidates = [row[0] for row in self.cursor.fetchall()]
#             self.candidate_combobox['values'] = candidates
#         except mysql.connector.Error as err:
#             messagebox.showerror("Database Error", f"Error: {err}")

#     def cast_vote(self):
#         email = self.voter_email.get().strip()
#         candidate_name = self.candidate_combobox.get()

#         if not email or not candidate_name:
#             messagebox.showerror("Error", "Please enter your email and select a candidate!")
#             return

#         try:
#             self.cursor.execute("SELECT has_voted FROM voters WHERE email = %s", (email,))
#             result = self.cursor.fetchone()

#             if result is None:
#                 messagebox.showerror("Error", "Voter not registered!")
#                 return

#             has_voted = result[0]
#             if has_voted:
#                 messagebox.showwarning("Warning", "You have already voted!")
#                 return

#             self.cursor.execute("SELECT id FROM candidates WHERE name = %s", (candidate_name,))
#             candidate = self.cursor.fetchone()
#             if candidate is None:
#                 messagebox.showerror("Error", "Selected candidate does not exist.")
#                 return

#             candidate_id = candidate[0]

#             self.cursor.execute("INSERT INTO votes (voter_id, candidate_id) VALUES ((SELECT id FROM voters WHERE email = %s), %s)", (email, candidate_id))
#             self.cursor.execute("UPDATE voters SET has_voted = TRUE WHERE email = %s", (email,))
#             self.conn.commit()
#             messagebox.showinfo("Success", "Vote cast successfully!")

#         except mysql.connector.Error as err:
#             messagebox.showerror("Database Error", f"Error: {err}")

#     def check_password_results(self):
#         self.prompt_password(self.show_results)

#     def check_password_voters(self):
#         self.prompt_password(self.view_voters)

#     def check_password_delete_voter(self):
#         self.prompt_password(self.delete_voter)

#     def check_password_delete_all_data(self):
#         self.prompt_password(self.delete_all_data)

#     def prompt_password(self, success_callback):
#         password_window = tk.Toplevel(self.root)
#         password_window.title("Enter Password")
#         password_window.geometry("300x100")

#         tk.Label(password_window, text="Enter Password:").pack(pady=10)
#         password_entry = tk.Entry(password_window, show="*")
#         password_entry.pack()

#         def check_password():
#             if password_entry.get() == self.password:
#                 password_window.destroy()
#                 success_callback()
#             else:
#                 messagebox.showerror("Error", "Incorrect password!")
#                 password_window.destroy()

#         tk.Button(password_window, text="Submit", command=check_password).pack(pady=10)

#     def show_results(self):
#         try:
#             self.cursor.execute("SELECT candidates.name, COUNT(votes.candidate_id) AS vote_count FROM candidates LEFT JOIN votes ON candidates.id = votes.candidate_id GROUP BY candidates.name")
#             results = self.cursor.fetchall()
#             result_message = "Voting Results:\n"
#             for candidate, count in results:
#                 result_message += f"{candidate}: {count} votes\n"
#             messagebox.showinfo("Results", result_message)
#         except mysql.connector.Error as err:
#             messagebox.showerror("Database Error", f"Error: {err}")

#     def view_voters(self):
#         try:
#             self.cursor.execute("SELECT name, email FROM voters")
#             voters = self.cursor.fetchall()
#             voter_list = "Registered Voters:\n"
#             for name, email in voters:
#                 voter_list += f"{name} ({email})\n"
#             messagebox.showinfo("Voters", voter_list)
#         except mysql.connector.Error as err:
#             messagebox.showerror("Database Error", f"Error: {err}")

#     def delete_voter(self):
#         email = self.voter_email.get().strip()
#         if not email:

# import tkinter as tk
# from tkinter import messagebox, ttk
# import mysql.connector

# class OnlineVotingSystem:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Online Voting System")
#         self.root.geometry("1000x700")
#         self.password = "admin123"

#         # Establish database connection
#         # try:
#         #     self.conn = mysql.connector.connect(
#         #         host="localhost",
#         #         user="root",     # Replace with your MySQL username
#         #         password="root", # Replace with your MySQL password
#         #         database="vote",
#         #         port=3306  # replace with your port if different
#         #     )
#         #     self.cursor = self.conn.cursor()
#         # except mysql.connector.Error as err:
#         #     messagebox.showerror("Database Error", f"Error connecting to database: {err}")
#         #     self.root.destroy()  # Close app if connection fails
#         #     return

#         self.create_widgets()
#         self.populate_candidates()

#     def create_widgets(self):
#         # Title
#         title = tk.Label(self.root, text="Online Voting System", font=("Arial", 24), bg="blue", fg="white")
#         title.pack(pady=10)

#         # Voter Registration Section
#         self.voter_frame = tk.Frame(self.root, bg="lightgray")
#         self.voter_frame.pack(pady=20, padx=20)

#         tk.Label(self.voter_frame, text="Name:", bg="lightgray").grid(row=0, column=0)
#         self.voter_name = tk.Entry(self.voter_frame)
#         self.voter_name.grid(row=0, column=1)

#         tk.Label(self.voter_frame, text="Email:", bg="lightgray").grid(row=1, column=0)
#         self.voter_email = tk.Entry(self.voter_frame)
#         self.voter_email.grid(row=1, column=1)

#         tk.Button(self.voter_frame, text="Register Voter", command=self.register_voter, bg="green", fg="white").grid(row=2, columnspan=2)

#         # Voting Section
#         self.vote_frame = tk.Frame(self.root, bg="lightyellow")
#         self.vote_frame.pack(pady=20, padx=20)

#         tk.Label(self.vote_frame, text="Select Candidate:", bg="lightyellow").grid(row=0, column=0)
#         self.candidate_combobox = ttk.Combobox(self.vote_frame)
#         self.candidate_combobox.grid(row=0, column=1)

#         tk.Button(self.vote_frame, text="Vote", command=self.cast_vote, bg="green", fg="white").grid(row=1, columnspan=2)

#         # Display Results Button with password
#         tk.Button(self.root, text="Show Results", command=self.check_password_results, bg="purple", fg="white").pack(pady=20)

#         # View Voters Button with password
#         tk.Button(self.root, text="View Voters", command=self.check_password_voters, bg="purple", fg="white").pack(pady=10)

#         # Delete Voter Button with password
#         tk.Button(self.root, text="Delete Voter Data", command=self.check_password_delete_voter, bg="red", fg="white").pack(pady=10)

#         # Delete All Data Button with password
#         tk.Button(self.root, text="Delete All Data", command=self.check_password_delete_all_data, bg="red", fg="white").pack(pady=10)

#     def register_voter(self):
#         name = self.voter_name.get().strip()
#         email = self.voter_email.get().strip()

#         if not name or not email:
#             messagebox.showerror("Error", "All fields are required!")
#             return

#         try:
#             self.cursor.execute("INSERT INTO voters (name, email) VALUES (%s, %s)", (name, email))
#             self.conn.commit()  # Save changes to the database
#             messagebox.showinfo("Success", "Voter registered successfully!")
#         except mysql.connector.Error as err:
#             messagebox.showerror("Database Error", f"Error: {err}")
#         finally:
#             self.voter_name.delete(0, tk.END)
#             self.voter_email.delete(0, tk.END)

#     def populate_candidates(self):
#         try:
#             self.cursor.execute("SELECT name FROM candidates")
#             candidates = [row[0] for row in self.cursor.fetchall()]
#             self.candidate_combobox['values'] = candidates
#         except mysql.connector.Error as err:
#             messagebox.showerror("Database Error", f"Error: {err}")

#     def cast_vote(self):
#         email = self.voter_email.get().strip()
#         candidate_name = self.candidate_combobox.get()

#         if not email or not candidate_name:
#             messagebox.showerror("Error", "Please enter your email and select a candidate!")
#             return

#         try:
#             # Check if the voter has already voted
#             self.cursor.execute("SELECT has_voted FROM voters WHERE email = %s", (email,))
#             result = self.cursor.fetchone()

#             if result is None:
#                 messagebox.showerror("Error", "Voter not registered!")
#                 return

#             has_voted = result[0]
#             if has_voted:
#                 messagebox.showwarning("Warning", "You have already voted!")
#                 return

#             # Get candidate ID
#             self.cursor.execute("SELECT id FROM candidates WHERE name = %s", (candidate_name,))
#             candidate = self.cursor.fetchone()
#             if candidate is None:
#                 messagebox.showerror("Error", "Selected candidate does not exist.")
#                 return

#             candidate_id = candidate[0]

#             # Record the vote
#             self.cursor.execute("INSERT INTO votes (voter_id, candidate_id) VALUES ((SELECT id FROM voters WHERE email = %s), %s)", (email, candidate_id))
#             self.cursor.execute("UPDATE voters SET has_voted = TRUE WHERE email = %s", (email,))
#             self.conn.commit()
#             messagebox.showinfo("Success", "Vote cast successfully!")

#         except mysql.connector.Error as err:
#             messagebox.showerror("Database Error", f"Error: {err}")

#     def check_password_results(self):
#         self.prompt_password(self.show_results)

#     def check_password_voters(self):
#         self.prompt_password(self.view_voters)

#     def check_password_delete_voter(self):
#         self.prompt_password(self.delete_voter)

#     def check_password_delete_all_data(self):
#         self.prompt_password(self.delete_all_data)

#     def prompt_password(self, success_callback):
#         password_window = tk.Toplevel(self.root)
#         password_window.title("Enter Password")
#         password_window.geometry("300x100")

#         tk.Label(password_window, text="Enter Password:").pack(pady=10)
#         password_entry = tk.Entry(password_window, show="*")
#         password_entry.pack()

#         def check_password():
#             if password_entry.get() == self.password:
#                 password_window.destroy()
#                 success_callback()
#             else:
#                 messagebox.showerror("Error", "Incorrect password!")
#                 password_window.destroy()

#         tk.Button(password_window, text="Submit", command=check_password).pack(pady=10)

#     def show_results(self):
#         try:
#             self.cursor.execute("SELECT candidates.name, COUNT(votes.candidate_id) AS vote_count FROM candidates LEFT JOIN votes ON candidates.id = votes.candidate_id GROUP BY candidates.name")
#             results = self.cursor.fetchall()
#             result_message = "Voting Results:\n"
#             for candidate, count in results:
#                 result_message += f"{candidate}: {count} votes\n"
#             messagebox.showinfo("Results", result_message)
#         except mysql.connector.Error as err:
#             messagebox.showerror("Database Error", f"Error: {err}")

#     def view_voters(self):
#         try:
#             self.cursor.execute("SELECT name, email FROM voters")
#             voters = self.cursor.fetchall()
#             voter_list = "Registered Voters:\n"
#             for name, email in voters:
#                 voter_list += f"{name} ({email})\n"
#             messagebox.showinfo("Voters", voter_list)
#         except mysql.connector.Error as err:
#             messagebox.showerror("Database Error", f"Error: {err}")

#     def delete_voter(self):
#         email = self.voter_email.get().strip()
#         if not email:
#             messagebox.showerror("Error", "Please enter the email of the voter to delete.")
#             return

#         try:
#             self.cursor.execute("DELETE FROM voters WHERE email = %s", (email,))
#             self.conn.commit()
#             messagebox.showinfo("Success", "Voter deleted successfully!")
#             self.voter_email.delete(0, tk.END)
#         except mysql.connector.Error as err:
#             messagebox.showerror("Database Error", f"Error: {err}")

#     def delete_all_data(self):
#         try:
#             self.cursor.execute("DELETE FROM voters")
#             self.cursor.execute("DELETE FROM votes")
#             self.conn.commit()
#             messagebox.showinfo("Success", "All data deleted successfully!")
#         except mysql.connector.Error as err:
#             messagebox.showerror("Database Error", f"Error: {err}")

#     def close_connection(self):
#         if self.cursor:
#             self.cursor.close()
#         if self.conn:
#             self.conn.close()

# # Ensure the connection is closed when the application exits
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = OnlineVotingSystem(root)
#     root.protocol("WM_DELETE_WINDOW", app.close_connection)
#     root.mainloop()
