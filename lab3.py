import sqlite3

conn = sqlite3.connect("lab3.db")
cursor = conn.cursor()

# Xóa bảng cũ nếu tồn tại
cursor.execute("DROP TABLE IF EXISTS khach_hang")
cursor.execute("DROP TABLE IF EXISTS san_pham")

# Tạo bảng khách hàng
cursor.execute("""
CREATE TABLE khach_hang (
    ma_khach_hang INTEGER PRIMARY KEY,
    ho_ten TEXT,
    so_dien_thoai TEXT,
    dia_chi TEXT
)
""")

# Tạo bảng sản phẩm
cursor.execute("""
CREATE TABLE san_pham (
    ma_san_pham INTEGER PRIMARY KEY,
    ten_san_pham TEXT,
    gia_tien REAL
)
""")

# Thêm dữ liệu mẫu
cursor.execute("""
INSERT INTO khach_hang VALUES
(1, 'Nguyen Van Anh', '0123456789', 'Ha Noi')
""")

conn.commit()
conn.close()

print("Chạy OK!")