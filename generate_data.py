import pandas as pd
import random
from datetime import datetime, timedelta

# ตั้งค่าการสุ่ม
users = ['User_Alpha', 'User_Beta', 'User_Gamma', 'User_Delta', 'User_Omega']
channels = ['General', 'Gaming', 'Music', 'Memes', 'Announcements']
start_date = datetime(2026, 1, 1)
data = []

# สุ่มข้อมูล 500 แถว
for _ in range(500):
    # สุ่มวันที่ภายใน 60 วันล่าสุด
    random_date = start_date + timedelta(days=random.randint(0, 60))
    
    # สุ่มข้อมูลอื่นๆ
    user = random.choice(users)
    channel = random.choice(channels)
    
    # สุ่มประเภทกิจกรรม (70% Text, 30% Voice)
    if random.random() > 0.3:
        activity_type = 'Text'
        value = random.randint(1, 50)  # จำนวนข้อความ
        unit = 'messages'
    else:
        activity_type = 'Voice'
        value = random.randint(10, 120) # จำนวนนาที
        unit = 'minutes'

    data.append([random_date.date(), user, channel, activity_type, value, unit])

# สร้าง DataFrame และบันทึกเป็น CSV
df = pd.DataFrame(data, columns=['Date', 'User', 'Channel', 'Activity_Type', 'Value', 'Unit'])
df.to_csv('discord_data.csv', index=False)

print("สร้างไฟล์ discord_data.csv เรียบร้อยแล้ว! (Commit ไฟล์นี้ลง Git ได้เลย)")