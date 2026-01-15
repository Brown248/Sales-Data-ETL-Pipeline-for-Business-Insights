# Sales Data ETL & Analysis Project

โปรเจคนี้เป็นตัวอย่าง **Data Engineering & Analysis Workflow** สำหรับข้อมูลยอดขาย Superstore (Dataset ตัวอย่าง)  

เราทำ **ETL Pipeline + Analysis + Visualization** แบบครบวงจร

---

## 🗂 โครงสร้างโปรเจค

sales-etl-project/
├── data/
│ ├── raw/ # ข้อมูลดิบ CSV
│ └── processed/ # ข้อมูลสรุป CSV หลังวิเคราะห์
├── database/
│ └── sales.db # SQLite database
├── notebooks/
│ └── analysis_th.ipynb # Notebook วิเคราะห์ + Plot ภาษาไทย
├── scripts/
│ ├── extract.py
│ ├── transform.py
│ ├── load.py
│ └── etl_pipeline.py # ETL pipeline รวม 3 ขั้นตอน
├── sql/
│ └── analysis_queries.sql # ตัวอย่าง SQL queries
└── README.md


---

## ⚡ Workflow

1. **Extract** – โหลดข้อมูล CSV ดิบจาก `data/raw/`  
2. **Transform** – Clean data, ลบค่า null, แปลงชื่อ column  
3. **Load** – เก็บข้อมูลลง SQLite Database (`sales.db`)  
4. **Analysis** – อ่าน DB, ทำ groupby, aggregation, plot graph  
5. **Visualization** – Bar chart / Pie chart / Top 5 Sub-Category / Region / Segment  
6. **Export** – สรุปผลเป็น CSV ใน `data/processed/`  

---

## 📊 Insights ตัวอย่าง

- ยอดขายรวมแต่ละ Category  
- Top 5 Sub-Category ที่มีกำไรสูงสุด  
- ยอดขายรวมแต่ละ Region  
- จำนวน Order / ยอดขาย / กำไรแต่ละ Segment  

**กราฟและสรุปข้อมูลทั้งหมดอยู่ใน Notebook `analysis_th.ipynb`**  

---

## 🛠 Tools & Libraries

- Python 3.x  
- Pandas  
- SQLite3  
- Matplotlib & Seaborn  

---

## ✅ วิธีรัน

1. รัน ETL Pipeline:
```bash
python scripts/etl_pipeline.py

2. เปิด Notebook วิเคราะห์:
jupyter notebook notebooks/analysis_th.ipynb
