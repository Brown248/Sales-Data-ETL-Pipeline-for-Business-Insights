import pandas as pd
import os

RAW_DATA_PATH = os.path.join('data', 'raw', 'SampleSuperstore.csv')
PROCESSED_DATA_PATH = os.path.join('data', 'processed', 'cleaned_sales.csv')

df = pd.read_csv(RAW_DATA_PATH)
print("---------- ข้อมูลทั้งหมด ----------")
print(df.shape)
print("---------- Columns ----------")
print(df.head())

# 3. Clean ข้อมูล
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
print("---------- Columns หลังแปลง ----------")
print(df.columns.tolist())

# ลบ row ที่ sales หรือ profit เป็นค่าว่าง
df = df.dropna(subset=['sales', 'profit'])

# แปลง sales, profit, quantity, discount เป็น numeric
df['sales'] = pd.to_numeric(df['sales'], errors='coerce')
df['profit'] = pd.to_numeric(df['profit'], errors='coerce')
df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
df['discount'] = pd.to_numeric(df['discount'], errors='coerce')

df = df.dropna(subset=['sales', 'profit', 'quantity', 'discount']) 

# 4. ตรวจสอบข้อมูลหลัง clean
print("---------- ข้อมูลหลัง clean ----------")
print(df.shape)
print("---------- Columns หลัง Clean----------")
print(df.head())

# 5. บันทึกไฟล์ cleaned
os.makedirs(os.path.join('data', 'processed'), exist_ok=True)
df.to_csv(PROCESSED_DATA_PATH, index=False)
print(f"บันทึกไฟล์ cleaned ที่: {PROCESSED_DATA_PATH}")




