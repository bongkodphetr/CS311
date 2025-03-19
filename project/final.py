import tkinter as tk
from tkinter import messagebox, filedialog, ttk
from PIL import Image, ImageTk
import os
import sqlite3
import shutil

class TravelApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Travel Thailand")
        self.root.geometry("800x600")
        
        # หาตำแหน่งของไฟล์ Python และสร้างพาธไปยังโฟลเดอร์ images
        self.base_path = os.path.dirname(os.path.abspath(__file__))
        self.image_dir = os.path.join(self.base_path, "images")
        if not os.path.exists(self.image_dir):
            os.makedirs(self.image_dir)
        
        # เชื่อมต่อฐานข้อมูล SQLite
        self.db_path = os.path.join(self.base_path, "travel.db")
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        
        # สร้างตาราง
        self.create_tables()
        
        # เพิ่มข้อมูลเริ่มต้นถ้าตารางว่าง
        self.initialize_data()
        
        self.current_province = None
        self.current_province_id = None
        self.current_user = None  # เก็บผู้ใช้ที่ล็อกอิน
        self.show_login_page()

    def create_tables(self):
        # ตาราง users
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
        ''')
        
        # ตาราง provinces
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS provinces (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                image TEXT NOT NULL
            )
        ''')
        
        # ตาราง places
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS places (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                province_id INTEGER NOT NULL,
                name TEXT NOT NULL,
                image TEXT NOT NULL,
                days TEXT NOT NULL,
                hours TEXT NOT NULL,
                info TEXT NOT NULL,
                FOREIGN KEY (province_id) REFERENCES provinces(id)
            )
        ''')
        self.conn.commit()

    def initialize_data(self):
        # ตรวจสอบว่ามีผู้ใช้เริ่มต้นหรือไม่
        self.cursor.execute("SELECT COUNT(*) FROM users")
        if self.cursor.fetchone()[0] == 0:
            self.cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("admin", "1234"))
        
        # ตรวจสอบว่ามีข้อมูลจังหวัดหรือไม่
        self.cursor.execute("SELECT COUNT(*) FROM provinces")
        if self.cursor.fetchone()[0] == 0:
            provinces_data = [
                ("กรุงเทพฯ", os.path.join(self.image_dir, "phrakaew.jpg")),
                ("เชียงใหม่", os.path.join(self.image_dir, "chiangmai.jpg")),
                ("ภูเก็ต", os.path.join(self.image_dir, "phuket.jpg")),
                ("อยุธยา", os.path.join(self.image_dir, "ayutthaya.jpg"))
            ]
            
            for name, image in provinces_data:
                self.cursor.execute("INSERT INTO provinces (name, image) VALUES (?, ?)", (name, image))
            self.conn.commit()
            
            places_data = [
                (1, "วัดพระแก้ว", os.path.join(self.image_dir, "phrakaew.jpg"), "ทุกวัน", "08:30-15:30", "วัดพระแก้วเป็นวัดที่สำคัญที่สุดในประเทศไทย ตั้งอยู่ในพระบรมมหาราชวัง"),
                (1, "พระบรมมหาราชวัง", os.path.join(self.image_dir, "grand_palace.jpg"), "ทุกวัน", "08:00-17:00", "พระบรมมหาราชวังเป็นที่ประทับของกษัตริย์ไทยในอดีต"),
                (1, "วัดอรุณ", os.path.join(self.image_dir, "wat_arun.jpg"), "ทุกวัน", "08:00-18:00", "วัดอรุณหรือวัดแจ้ง มีเจดีย์ที่งดงามริมแม่น้ำเจ้าพระยา"),
                (2, "ดอยสุเทพ", os.path.join(self.image_dir, "doi_suthep.jpg"), "ทุกวัน", "06:00-18:00", "ดอยสุเทพเป็นที่ตั้งของวัดพระธาตุดอยสุเทพ วิวสวยงาม"),
                (2, "วัดพระสิงห์", os.path.join(self.image_dir, "wat_phra_singh.jpg"), "ทุกวัน", "06:00-18:00", "วัดพระสิงห์เป็นวัดสำคัญในตัวเมืองเชียงใหม่"),
                (2, "ถนนคนเดิน", os.path.join(self.image_dir, "walking_street.jpg"), "วันเสาร์-อาทิตย์", "17:00-22:00", "ถนนคนเดินท่าแพ มีของกินและของฝากมากมาย"),
                (3, "หาดป่าตอง", os.path.join(self.image_dir, "patong.jpg"), "ทุกวัน", "24 ชั่วโมง", "หาดป่าตองเป็นชายหาดที่มีชีวิตชีวา เหมาะสำหรับนักท่องเที่ยว"),
                (3, "แหลมพรหมเทพ", os.path.join(self.image_dir, "promthep.jpg"), "ทุกวัน", "06:00-18:00", "แหลมพรหมเทพเป็นจุดชมวิวพระอาทิตย์ตกที่สวยงาม"),
                (3, "เกาะพีพี", os.path.join(self.image_dir, "phiphi.jpg"), "ทุกวัน", "08:00-17:00", "เกาะพีพีมีน้ำทะเลใสและแนวปะการังที่สวยงาม"),
                (4, "วัดมหาธาตุ", os.path.join(self.image_dir, "mahatat.jpg"), "ทุกวัน", "08:00-17:00", "วัดมหาธาตุมีพระพุทธรูปในรากไม้ที่มีชื่อเสียง"),
                (4, "วัดไชยวัฒนาราม", os.path.join(self.image_dir, "chaiwatthanaram.jpg"), "ทุกวัน", "08:00-17:00", "วัดไชยวัฒนารามเป็นวัดที่มีสถาปัตยกรรมสวยงาม"),
                (4, "วัดพระศรีสรรเพชญ์", os.path.join(self.image_dir, "srisanphet.jpg"), "ทุกวัน", "08:00-17:00", "วัดพระศรีสรรเพชญ์เป็นวัดสำคัญในสมัยอยุธยา")
            ]
            
            for province_id, name, image, days, hours, info in places_data:
                self.cursor.execute("INSERT INTO places (province_id, name, image, days, hours, info) VALUES (?, ?, ?, ?, ?, ?)",
                                  (province_id, name, image, days, hours, info))
            self.conn.commit()

    def show_login_page(self):
        self.clear_window()
        login_frame = tk.Frame(self.root)
        login_frame.pack(pady=50)
        tk.Label(login_frame, text="Login", font=("Arial", 20)).pack(pady=10)
        tk.Label(login_frame, text="Username:").pack()
        self.username_entry = tk.Entry(login_frame)
        self.username_entry.pack(pady=5)
        tk.Label(login_frame, text="Password:").pack()
        self.password_entry = tk.Entry(login_frame, show="*")
        self.password_entry.pack(pady=5)
        tk.Button(login_frame, text="Login", command=self.login).pack(pady=5)
        tk.Button(login_frame, text="Register", command=self.show_register_page).pack(pady=5)

    def show_register_page(self):
        self.clear_window()
        register_frame = tk.Frame(self.root)
        register_frame.pack(pady=50)
        tk.Label(register_frame, text="Register", font=("Arial", 20)).pack(pady=10)
        tk.Label(register_frame, text="Username:").pack()
        self.reg_username = tk.Entry(register_frame)
        self.reg_username.pack(pady=5)
        tk.Label(register_frame, text="Password:").pack()
        self.reg_password = tk.Entry(register_frame, show="*")
        self.reg_password.pack(pady=5)
        tk.Button(register_frame, text="Register", command=self.register).pack(pady=5)
        tk.Button(register_frame, text="Back to Login", command=self.show_login_page).pack(pady=5)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        self.cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = self.cursor.fetchone()
        if user:
            self.current_user = username
            messagebox.showinfo("Success", "Login successful!")
            self.show_province_list()
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def register(self):
        username = self.reg_username.get()
        password = self.reg_password.get()
        if not (username and password):
            messagebox.showerror("Error", "Please fill in all fields")
            return
        
        try:
            self.cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            self.conn.commit()
            messagebox.showinfo("Success", "Registration successful!")
            self.show_login_page()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Username already exists")

    def resize_image(self, img, target_width, target_height):
        """ปรับขนาดและตัดรูปภาพให้พอดีกับขนาดเป้าหมาย"""
        img.thumbnail((target_width, target_height), Image.Resampling.LANCZOS)
        width, height = img.size
        left = (width - target_width) // 2 if width > target_width else 0
        top = (height - target_height) // 2 if height > target_height else 0
        right = left + target_width if width > target_width else width
        bottom = top + target_height if height > target_height else height
        img_cropped = img.crop((left, top, right, bottom))
        if img_cropped.size != (target_width, target_height):
            img_cropped = img_cropped.resize((target_width, target_height), Image.Resampling.LANCZOS)
        return img_cropped

    def show_province_list(self):
        if not self.current_user:
            messagebox.showwarning("Warning", "Please login first!")
            self.show_login_page()
            return
        
        self.clear_window()
        list_frame = tk.Frame(self.root)
        list_frame.pack(fill="both", expand=True, pady=20)
        tk.Label(list_frame, text=f"ยินดีต้อนรับ {self.current_user} | เลือกจังหวัด", font=("Arial", 20)).pack(pady=10)
        
        grid_frame = tk.Frame(list_frame)
        grid_frame.pack(fill="both", expand=True)
        
        col = 0
        row = 0
        
        self.cursor.execute("SELECT id, name, image FROM provinces")
        provinces = self.cursor.fetchall()
        
        for province_id, province_name, province_image in provinces:
            frame = tk.Frame(grid_frame)
            frame.grid(row=row, column=col, padx=20, pady=10, sticky="n")
            
            try:
                if not os.path.exists(province_image):
                    raise FileNotFoundError(f"File not found: {province_image}")
                img = Image.open(province_image)
                img_resized = self.resize_image(img, 250, 200)
                photo = ImageTk.PhotoImage(img_resized)
                lbl = tk.Label(frame, image=photo)
                lbl.image = photo
                lbl.pack()
            except Exception as e:
                print(f"Error loading image {province_image}: {e}")
                tk.Label(frame, text="[No Image]").pack()
            
            btn = tk.Button(frame, text=province_name, command=lambda p=province_name, pid=province_id: self.show_province_detail(p, pid))
            btn.pack(pady=5)
            
            col += 1
            if col > 1:
                col = 0
                row += 1

    def show_province_detail(self, province_name, province_id):
        if not self.current_user:
            messagebox.showwarning("Warning", "Please login first!")
            self.show_login_page()
            return
        
        self.clear_window()
        self.current_province = province_name
        self.current_province_id = province_id
        
        detail_frame = tk.Frame(self.root)
        detail_frame.pack(fill="both", expand=True, pady=20)
        tk.Label(detail_frame, text=province_name, font=("Arial", 20)).pack(pady=10)
        
        canvas = tk.Canvas(detail_frame)
        scrollbar = tk.Scrollbar(detail_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        self.cursor.execute("SELECT name, image, days, hours, info FROM places WHERE province_id = ?", (province_id,))
        places = self.cursor.fetchall()
        
        for place_name, place_image, days, hours, info in places:
            place_frame = tk.Frame(scrollable_frame, borderwidth=2, relief="groove")
            place_frame.pack(fill="x", pady=5, padx=10)
            
            try:
                if not os.path.exists(place_image):
                    raise FileNotFoundError(f"File not found: {place_image}")
                img = Image.open(place_image)
                img_resized = self.resize_image(img, 150, 150)
                photo = ImageTk.PhotoImage(img_resized)
                lbl = tk.Label(place_frame, image=photo)
                lbl.image = photo
                lbl.pack(side="left", padx=10)
            except Exception as e:
                print(f"Error loading image {place_image}: {e}")
                tk.Label(place_frame, text="[No Image]").pack(side="left", padx=10)
            
            text_frame = tk.Frame(place_frame)
            text_frame.pack(side="left", fill="x", expand=True)
            
            tk.Label(text_frame, text=place_name, font=("Arial", 14, "bold")).pack(anchor="w")
            tk.Label(text_frame, text=f"วันเปิด: {days}", font=("Arial", 12)).pack(anchor="w")
            tk.Label(text_frame, text=f"เวลา: {hours}", font=("Arial", 12)).pack(anchor="w")
            tk.Label(text_frame, text=f"รายละเอียด: {info}", font=("Arial", 12), wraplength=400, justify="left").pack(anchor="w")
        
        tk.Button(detail_frame, text="เพิ่มสถานที่", command=self.show_add_place_page).pack(pady=5)
        tk.Button(detail_frame, text="กลับ", command=self.show_province_list).pack(pady=5)
        tk.Button(detail_frame, text="Logout", command=self.logout).pack(pady=5)

    def show_add_place_page(self):
        if not self.current_user:
            messagebox.showwarning("Warning", "Please login first!")
            self.show_login_page()
            return
        
        self.clear_window()
        add_frame = tk.Frame(self.root)
        add_frame.pack(pady=20)
        
        tk.Label(add_frame, text="เพิ่มสถานที่ใหม่", font=("Arial", 20)).pack(pady=10)
        
        tk.Label(add_frame, text="เลือกจังหวัด:").pack()
        province_var = tk.StringVar(value=self.current_province)
        tk.Label(add_frame, text=self.current_province, font=("Arial", 12)).pack()
        
        tk.Label(add_frame, text="ชื่อสถานที่:").pack()
        self.place_name_entry = tk.Entry(add_frame)
        self.place_name_entry.pack(pady=5)
        
        tk.Label(add_frame, text="รูปภาพ:").pack()
        self.image_path_entry = tk.Entry(add_frame)
        self.image_path_entry.pack(pady=5)
        tk.Button(add_frame, text="เลือกไฟล์", command=self.select_image_file).pack(pady=5)
        
        tk.Label(add_frame, text="วันเปิด-ปิด:").pack()
        days_options = ["ทุกวัน", "จันทร์-ศุกร์", "เสาร์-อาทิตย์", "เฉพาะวันหยุด", "ปิดตลอด"]
        self.days_var = tk.StringVar(value=days_options[0])
        days_combo = ttk.Combobox(add_frame, textvariable=self.days_var, values=days_options)
        days_combo.pack(pady=5)
        
        tk.Label(add_frame, text="เวลาเปิด-ปิด:").pack()
        hours_options = ["06:00-18:00", "08:00-17:00", "08:30-15:30", "17:00-22:00", "24 ชั่วโมง"]
        self.hours_var = tk.StringVar(value=hours_options[0])
        hours_combo = ttk.Combobox(add_frame, textvariable=self.hours_var, values=hours_options)
        hours_combo.pack(pady=5)
        
        tk.Label(add_frame, text="รายละเอียด:").pack()
        self.info_entry = tk.Text(add_frame, height=4, width=40)
        self.info_entry.pack(pady=5)
        
        tk.Button(add_frame, text="เพิ่ม", command=self.add_place).pack(pady=5)
        tk.Button(add_frame, text="กลับ", command=lambda: self.show_province_detail(self.current_province, self.current_province_id)).pack(pady=5)

    def select_image_file(self):
        file_path = filedialog.askopenfilename(
            title="เลือกไฟล์รูปภาพ",
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif")]
        )
        if file_path:
            file_name = os.path.basename(file_path)
            dest_path = os.path.join(self.image_dir, file_name)
            if not os.path.exists(dest_path):
                shutil.copy(file_path, dest_path)
            self.image_path_entry.delete(0, tk.END)
            self.image_path_entry.insert(0, dest_path)

    def add_place(self):
        if not self.current_user:
            messagebox.showwarning("Warning", "Please login first!")
            self.show_login_page()
            return
        
        place_name = self.place_name_entry.get()
        image_path = self.image_path_entry.get()
        days = self.days_var.get()
        hours = self.hours_var.get()
        info = self.info_entry.get("1.0", tk.END).strip()
        
        if not (place_name and image_path and days and hours and info):
            messagebox.showerror("Error", "กรุณากรอกข้อมูลให้ครบ")
            return
        
        self.cursor.execute("INSERT INTO places (province_id, name, image, days, hours, info) VALUES (?, ?, ?, ?, ?, ?)",
                           (self.current_province_id, place_name, image_path, days, hours, info))
        self.conn.commit()
        
        messagebox.showinfo("Success", f"เพิ่มสถานที่ {place_name} ใน {self.current_province} สำเร็จ!")
        self.show_province_detail(self.current_province, self.current_province_id)

    def logout(self):
        self.current_user = None
        messagebox.showinfo("Logout", "Logged out successfully!")
        self.show_login_page()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def __del__(self):
        # ปิดการเชื่อมต่อฐานข้อมูลเมื่อปิดโปรแกรม
        self.conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = TravelApp(root)
    root.mainloop()