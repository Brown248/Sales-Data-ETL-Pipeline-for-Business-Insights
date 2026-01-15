import pandas as pd
import os

RAW_DATA_PATH = os.path.join('data', 'raw', 'SampleSuperstore.csv')
PROCESSED_DATA_PATH = os.path.join('data', 'processed', 'cleaned_sales.csv')

df = pd.read_csv(RAW_DATA_PATH)
print("---------- ข้อมูลทั้งหมด ----------")
print(df.shape)
print("---------- Columns ----------")
print(df.head)

df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

df['']