import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from datetime import datetime
import csv
import pandas as pd

danh_sach_nhan_vien = []

def luu_vao_csv():
    try:
        with open('nhan_vien.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Mã', 'Tên', 'Đơn vị', 'Chức danh', 'Ngày sinh', 'Giới tính', 'Số CMND', 'Ngày cấp', 'Nơi cấp'])
            writer.writerows(danh_sach_nhan_vien)
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể lưu dữ liệu: {e}")

def luu_nhan_vien():
    nhan_vien = [entry_ma.get(),entry_ten.get(),don_vi_var.get(),chuc_danh_var.get(),entry_ngay_sinh.get(),gioi_tinh_var.get(),entry_cmnd.get(),entry_ngay_cap.get(),entry_noi_cap.get()]

    if not nhan_vien[0] or not nhan_vien[1] or not nhan_vien[2]:
        messagebox.showwarning("Cảnh báo", "Các mục Mã, Tên, và Đơn vị là bắt buộc!")
        return
    danh_sach_nhan_vien.append(nhan_vien)
    luu_vao_csv()
    messagebox.showinfo("Thông báo", "Lưu thông tin thành công!")

    for entry in entries:
        entry.delete(0, tk.END)
    entry_ngay_sinh.set_date(datetime.now())
    entry_ngay_cap.set_date(datetime.now())

def hien_thi_sinh_nhat_hom_nay():
    today = datetime.now().strftime('%d/%m')
    sinh_nhat_hom_nay = [emp for emp in danh_sach_nhan_vien if emp[4][0:5] == today]

    if sinh_nhat_hom_nay:
        messagebox.showinfo(
            "Nhân viên sinh nhật hôm nay",
            "\n".join([f"{emp[1]} ({emp[0]})" for emp in sinh_nhat_hom_nay])
        )
    else:
        messagebox.showinfo("Thông báo", "Không có nhân viên nào sinh nhật hôm nay.")

def xuat_ra_excel():
    try:
        df = pd.DataFrame(danh_sach_nhan_vien, columns=['Mã', 'Tên', 'Đơn vị', 'Chức danh', 'Ngày sinh', 'Giới tính', 'Số CMND', 'Ngày cấp', 'Nơi cấp'])
        df['Ngày sinh'] = pd.to_datetime(df['Ngày sinh'], format='%d/%m/%Y', errors='coerce')
        df = df.sort_values(by='Ngày sinh', ascending=False)
        df.to_excel('nhan_vien.xlsx', index=False, engine='openpyxl')
        messagebox.showinfo("Thông báo", "Xuất file Excel thành công!")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể xuất file Excel: {e}")

root = tk.Tk()
root.title("Quản lý thông tin nhân viên")
root.geometry("600x280")

khung_nhap_lieu = ttk.LabelFrame(root, text="Thông tin nhân viên", padding=10)
khung_nhap_lieu.pack(padx=10, pady=10, fill="x")

entries = []
#Dòng1
tk.Label(khung_nhap_lieu, text="Mã:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
tk.Label(khung_nhap_lieu, text="*", fg="red").grid(row=0, column=1, padx=0, pady=5, sticky=tk.W)
entry_ma = ttk.Entry(khung_nhap_lieu, width=20)
entry_ma.grid(row=0, column=2, padx=5, pady=5)
entries.append(entry_ma)

tk.Label(khung_nhap_lieu, text="Tên:").grid(row=0, column=3, padx=5, pady=5, sticky=tk.W)
tk.Label(khung_nhap_lieu, text="*", fg="red").grid(row=0, column=4, padx=0, pady=5, sticky=tk.W)
entry_ten = ttk.Entry(khung_nhap_lieu, width=20)
entry_ten.grid(row=0, column=5, padx=5, pady=5)
entries.append(entry_ten)
#Dòng 2
tk.Label(khung_nhap_lieu, text="Đơn vị:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
tk.Label(khung_nhap_lieu, text="*", fg="red").grid(row=1, column=1, padx=0, pady=5, sticky=tk.W)
don_vi_var = tk.StringVar()
entry_don_vi = ttk.Combobox(khung_nhap_lieu, textvariable=don_vi_var, values=["Phân xưởng A", "Phân xưởng B"], width=18)
entry_don_vi.grid(row=1, column=2, padx=5, pady=5)

chuc_danh_var = tk.StringVar()
ttk.Label(khung_nhap_lieu, text="Chức danh:").grid(row=1, column=3, padx=5, pady=5, sticky=tk.W)
entry_chuc_danh = ttk.Combobox(khung_nhap_lieu, textvariable=chuc_danh_var, values=["Nhân viên", "Quản lý"], width=18)
entry_chuc_danh.grid(row=1, column=5, padx=5, pady=5)
#Dòng 3
ttk.Label(khung_nhap_lieu, text="Ngày sinh:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
entry_ngay_sinh = DateEntry(khung_nhap_lieu, date_pattern='dd/MM/yyyy', width=17)
entry_ngay_sinh.grid(row=2, column=2, padx=5, pady=5)

gioi_tinh_var = tk.StringVar(value="Nam")
ttk.Label(khung_nhap_lieu, text="Giới tính:").grid(row=2, column=3, padx=5, pady=5, sticky=tk.W)
ttk.Radiobutton(khung_nhap_lieu, text="Nam", variable=gioi_tinh_var, value="Nam").grid(row=2, column=5, sticky=tk.W)
ttk.Radiobutton(khung_nhap_lieu, text="Nữ", variable=gioi_tinh_var, value="Nữ").grid(row=2, column=5, padx=70, sticky=tk.W)
#Dòng 4
ttk.Label(khung_nhap_lieu, text="Số CMND:").grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
entry_cmnd = ttk.Entry(khung_nhap_lieu, width=20)
entry_cmnd.grid(row=3, column=2, padx=5, pady=5)
entries.append(entry_cmnd)

ttk.Label(khung_nhap_lieu, text="Ngày cấp:").grid(row=3, column=3, padx=5, pady=5, sticky=tk.W)
entry_ngay_cap = DateEntry(khung_nhap_lieu, date_pattern='dd/MM/yyyy', width=17)
entry_ngay_cap.grid(row=3, column=5, padx=5, pady=5)
#Dòng 5
ttk.Label(khung_nhap_lieu, text="Nơi cấp:").grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
entry_noi_cap = ttk.Entry(khung_nhap_lieu, width=20)
entry_noi_cap.grid(row=4, column=2, padx=5, pady=5)
entries.append(entry_noi_cap)

khung_nut_chuc_nang = ttk.Frame(root, padding=10)
khung_nut_chuc_nang.pack(fill="x")

btn_luu = ttk.Button(khung_nut_chuc_nang, text="Lưu thông tin", command=luu_nhan_vien)
btn_luu.pack(side="left", padx=5)

btn_sinh_nhat = ttk.Button(khung_nut_chuc_nang, text="Sinh nhật hôm nay", command=hien_thi_sinh_nhat_hom_nay)
btn_sinh_nhat.pack(side="left", padx=5)

btn_xuat = ttk.Button(khung_nut_chuc_nang, text="Xuất danh sách", command=xuat_ra_excel)
btn_xuat.pack(side="left", padx=5)

root.mainloop()


