import pandas as pd
import os

RAW_DATA_PATH = os.path.join("data", "raw", "SampleSuperstore.csv")

# โหลด CSV
try:
    df = pd.read_csv(RAW_DATA_PATH)
    print(f"โหลดข้อมูลเสร็จสิ้น Shape: {df.shape}")
except FileExistsError:
    print(f"ไม่พบไฟล์: {RAW_DATA_PATH}")
    df = pd.DataFrame()

# ดูข้อมูลเบื้องต้น
if not df.empty:
    print("Columns ในไฟล์ CSV:", df.columns.tolist())
    print("ตัวอย่างข้อมูล 5 แถวแรก:")
    print(df.head())

# คืนค่า DataFrame สำหรับขั้นตอนถัดไป
def extract_data():
    return df