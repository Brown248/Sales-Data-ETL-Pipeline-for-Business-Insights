from extract import extract_data
import pandas as pd
import os
import sqlite3

# Transform Function
def transform_data(df):
    if df.empty:
        print("DataFrame ว่าง! Transform ไม่ทำงาน")
        return df

    # แปลงชื่อ column เป็น snake_case
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    print("Columns หลังแปลง:", df.columns.tolist())  # debug

    # ลบ row ที่ sales หรือ profit เป็นค่าว่าง
    # ต้องใช้ชื่อ column หลังแปลงแล้ว
    df = df.dropna(subset=['sales', 'profit'])

    # แปลง numeric
    df['sales'] = pd.to_numeric(df['sales'], errors='coerce')
    df['profit'] = pd.to_numeric(df['profit'], errors='coerce')
    df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
    df['discount'] = pd.to_numeric(df['discount'], errors='coerce')

    # ลบ row ที่เกิด NaN หลังแปลง numeric
    df = df.dropna(subset=['sales', 'profit', 'quantity', 'discount'])
    print("Columns ก่อน dropna:", df.columns.tolist())

    return df

# Load Function
DB_PATH = os.path.join("database", "sales.db")
os.makedirs("database", exist_ok=True)

def load_to_db(df, table_name='sales'):
    if df.empty:
        print("DataFrame ว่าง ไม่มีข้อมูลโหลดลง Database")
        return
    try:
        conn = sqlite3.connect(DB_PATH)
        df.to_sql(table_name, conn, if_exists="replace", index=False)
        print(f"โหลดข้อมูลลง table '{table_name}' เรียบร้อย! DB: {DB_PATH}")

    except Exception as e:
        print("เกิดข้อผิดพลาดในการโหลดข้อมูล:", e)
    finally:
        conn.close()

# Main ETL Pipeline
def run_etl():
    print("ETL Pipeline...")

    # Extract
    print("\n[1] Extract Data")
    df = extract_data()
    print(f"Shape หลัง Extract: {df.shape}")

    # Transform
    print("\n[2] Transform Data")
    df_clean = transform_data(df)
    print(f"Shape หลัง Transform: {df_clean.shape}")

    # Load
    print("\n[3] Load Data to Database")
    load_to_db(df_clean, table_name="sales")
    print("\nETL Pipeline เสร็จเรียบร้อย")

# รัน Pipeline ถ้าเรียกไฟล์ตรงๆ
if __name__ == "__main__":
    run_etl()