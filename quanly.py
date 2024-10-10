import tkinter as tk
from tkinter import messagebox
import csv
from datetime import datetime

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
class SportMatch:
    def __init__(self):
        self.teams = []
        self.matches = []
        self.players = []
        self.load_teams_from_csv()
        self.load_results_from_csv()
        self.load_players_from_csv()

    def load_teams_from_csv(self):
        pass

    def load_results_from_csv(self):
        pass

    def load_players_from_csv(self):
        pass

    def save_players_to_csv(self):
        pass

class SportMatchApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Hệ Thống Quản Lý Thể Thao")
        
        self.users = []
        self.load_users_from_csv()

        self.sport_match = SportMatch()

        self.login_frame = tk.Frame(self.master)
        self.login_frame.pack(pady=20)

        tk.Label(self.login_frame, text="Tên Người Dùng:").grid(row=0, column=0)
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.grid(row=0, column=1)

        tk.Label(self.login_frame, text="Mật Khẩu:").grid(row=1, column=0)
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.grid(row=1, column=1)

        self.login_button = tk.Button(self.login_frame, text="Đăng Nhập", command=self.login)
        self.login_button.grid(row=2, column=0)

        self.register_button = tk.Button(self.login_frame, text="Đăng Kí", command=self.show_register_interface)
        self.register_button.grid(row=2, column=1)

        self.username_entry.bind("<Return>", lambda event: self.login())
        self.password_entry.bind("<Return>", lambda event: self.login())

        self.admin_frame = None
        self.current_function_frame = None

    def load_users_from_csv(self):
        try:
            with open('users.csv', 'r', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if row:
                        username, password = row
                        self.users.append(User(username, password))
        except FileNotFoundError:
            print("Tệp users.csv không tồn tại. Một tệp mới sẽ được tạo khi đăng kí người dùng.")

    def save_users_to_csv(self):
        with open('users.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            for user in self.users:
                writer.writerow([user.username, user.password])

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        for user in self.users:
            if user.username == username and user.password == password:
                messagebox.showinfo("Đăng Nhập Thành Công", f"Chào mừng, {username}!")
                self.show_admin_interface()
                return
        messagebox.showerror("Lỗi Đăng Nhập", "Tên người dùng hoặc mật khẩu không đúng.")

    def show_admin_interface(self):
        self.login_frame.pack_forget()

        self.admin_frame = tk.Frame(self.master)
        self.admin_frame.pack(pady=20)

        tk.Label(self.admin_frame, text="Quản Lý Hệ Thống", font=("Arial", 16)).grid(row=0, columnspan=2)

        self.add_team_button = tk.Button(self.admin_frame, text="Thêm/Xóa Đội", command=self.show_add_team_interface)
        self.add_team_button.grid(row=1, column=0)

        self.add_player_button = tk.Button(self.admin_frame, text="Thêm Cầu Thủ", command=self.show_add_player_interface)
        self.add_player_button.grid(row=1, column=1)

        self.schedule_match_button = tk.Button(self.admin_frame, text="Lên Lịch Trận Đấu", command=self.show_schedule_match_interface)
        self.schedule_match_button.grid(row=2, column=0)

        self.record_result_button = tk.Button(self.admin_frame, text="Ghi Kết Quả Trận Đấu", command=self.show_record_result_interface)
        self.record_result_button.grid(row=2, column=1)

        
        self.logout_button = tk.Button(self.admin_frame, text="Đăng Xuất", command=self.logout)
        self.logout_button.grid(row=3, columnspan=2)

 
    def logout(self):
       
        if self.admin_frame:
            self.admin_frame.pack_forget()
        self.login_frame.pack(pady=20)

    def show_register_interface(self):
        self.login_frame.pack_forget()

        self.register_frame = tk.Frame(self.master)
        self.register_frame.pack(pady=20)

        tk.Label(self.register_frame, text="Tên Người Dùng:").grid(row=0, column=0)
        self.new_username_entry = tk.Entry(self.register_frame)
        self.new_username_entry.grid(row=0, column=1)

        tk.Label(self.register_frame, text="Mật Khẩu:").grid(row=1, column=0)
        self.new_password_entry = tk.Entry(self.register_frame, show="*")
        self.new_password_entry.grid(row=1, column=1)

        tk.Button(self.register_frame, text="Đăng Kí", command=self.register_user).grid(row=2, column=0, columnspan=2)

        tk.Button(self.register_frame, text="Quay Lại", command=self.show_login_interface).grid(row=3, column=0, columnspan=2)

    def show_login_interface(self):
        self.register_frame.pack_forget()
        self.login_frame.pack(pady=20)

    def register_user(self):
        new_username = self.new_username_entry.get()
        new_password = self.new_password_entry.get()

        if not new_username or not new_password:
            messagebox.showerror("Lỗi", "Vui lòng nhập tên người dùng và mật khẩu.")
            return

        for user in self.users:
            if user.username == new_username:
                messagebox.showerror("Lỗi", "Tên người dùng đã tồn tại.")
                return

        self.users.append(User(new_username, new_password))
        self.save_users_to_csv()
        messagebox.showinfo("Thành Công", "Đăng kí thành công! Bạn có thể đăng nhập với tài khoản mới.")
        self.show_login_interface()

    def clear_current_function_frame(self):
        if self.current_function_frame:
            self.current_function_frame.pack_forget()
            self.current_function_frame = None

if __name__ == "__main__":
    root = tk.Tk()
    app = SportMatchApp(root)
    root.mainloop()



