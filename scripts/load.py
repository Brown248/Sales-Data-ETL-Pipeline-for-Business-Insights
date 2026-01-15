import pandas as pd
import os
import sqlite3

DB_PATH = os.path.join('sale', 'sales.db')

# สร้าง folder database 
os.makedirs("database", exist_ok=True)

# ฟังก์ชันโหลด DataFrame ลง SQLite

def load_to_db(df, table_name="sales"):
    if df.empty:
        print("DataFrame ว่าง ไม่มีข้อมูลให้ลง Database")
        return
    try:
        conn = sqlite3.connect(DB_PATH)
        df.to_sql(table_name, conn, if_exists="replace", index=False)

    except Exception as e:
        print("เกิดข้อผิดพลาดในการโหลดข้อมูล:", e)
    
    finally:
        conn.close()