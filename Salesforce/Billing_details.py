import pandas as pd
import numpy as np
import os
import uuid
from datetime import timedelta

# --- 0. 确认所有输入文件名 ---
# 我们现在只需要这3个文件 + 1个用户画像文件
METER_FILENAME = "smart_meter_data.csv"
SUBSCRIPTION_FILENAME = "Customer_Subscriptions.csv"
PRICING_FILENAME = "pricing_plan.csv"
USER_DATA_FILENAME = "user_data.csv" # 包含AccountID, ICP_Number__c, Profile

# --- 1. 加载所有数据 ---
print("正在读取所有源数据文件...")
try:
    meter_df = pd.read_csv(METER_FILENAME)
    subscription_df = pd.read_csv(SUBSCRIPTION_FILENAME)
    pricing_df = pd.read_csv(PRICING_FILENAME)
    user_df = pd.read_csv(USER_DATA_FILENAME) # 这是您的客户主文件
except FileNotFoundError as e:
    print(f"错误：找不到文件 {e.filename}。请确保所有必需的CSV文件都在同一个文件夹中。")
    exit()

# --- 2. 数据预处理 ---
print("正在进行数据预处理...")
meter_df['TimeStamp'] = pd.to_datetime(meter_df['TimeStamp'])
subscription_df['Start_Date'] = pd.to_datetime(subscription_df['Start_Date'], dayfirst=True)
subscription_df['End_date'] = pd.to_datetime(subscription_df['End_date'], dayfirst=True, errors='coerce').fillna(pd.Timestamp('2200-01-01'))
# 确保AccountID列是字符串类型，以便合并
user_df['Id'] = user_df['Id'].astype(str)
subscription_df['AccountID'] = subscription_df['AccountID'].astype(str)
meter_df['AccountID'] = meter_df['AccountID'].astype(str)


# --- 3. 丰富订阅信息 (合并套餐价格) ---
print("正在合并套餐与订阅信息...")
plan_details_df = subscription_df.merge(
    pricing_df,
    left_on="Pricing_Plan_Id__c",
    right_on="Id__c",
    how="left"
)

# --- 4. 将用电记录与正确的套餐匹配 ---
print("正在进行向量化合并，匹配每条用电记录到正确的套餐...")
merged_df = pd.merge(
    meter_df,
    plan_details_df,
    on="AccountID", # 使用AccountID作为共同的钥匙
    how="left"
)
valid_records_df = merged_df[
    (merged_df['TimeStamp'] >= merged_df['Start_Date']) &
    (merged_df['TimeStamp'] < merged_df['End_date'])
].copy()

# --- 5. 计算每小时的可变费用 ---
print("正在向量化计算每小时的可变费用...")
valid_records_df['Variable_Charge'] = np.where(
    valid_records_df['Day/Night'] == 'Day',
    valid_records_df['Usage_KWH'] * valid_records_df['Day_Rate_c__c'],
    valid_records_df['Usage_KWH'] * valid_records_df['Night_Rate_c__c']
)

# --- 6. 一步到位的月度聚合 ---
print("正在按月聚合账单...")
valid_records_df = valid_records_df.set_index('TimeStamp')
monthly_summary = valid_records_df.groupby(
    ['AccountID', pd.Grouper(freq='M')]
).agg(
    Total_Variable_Charge=('Variable_Charge', 'sum'),
    Daily_Charge=('Daily_Charge_c__c', 'first'),
    Days_In_Month=('Day/Night', lambda x: len(np.unique(x.index.day)))
).reset_index()

# --- 7. 计算最终月度账单金额 ---
print("正在计算最终月度账单...")
monthly_summary['Total_Fixed_Charge'] = monthly_summary['Daily_Charge'] * monthly_summary['Days_In_Month']
monthly_summary['Amount__c'] = monthly_summary['Total_Variable_Charge'] + monthly_summary['Total_Fixed_Charge']
monthly_summary['Amount__c'] = monthly_summary['Amount__c'].round(2)

# --- 8. 【关键修正】自动生成“支付画像”并伪造支付行为 ---
print("正在自动生成支付画像并伪造支付行为...")

# 获取所有唯一的AccountID
unique_accounts = monthly_summary[['AccountID']].drop_duplicates()

# 定义画像和它们的分布概率
profiles = ['On-Time', 'Late', 'Risk']
probabilities = [0.6, 0.3, 0.1] # 60%准时, 30%晚交, 10%风险

# 为每个独立客户随机分配一个画像
unique_accounts['Payment_Profile'] = np.random.choice(profiles, size=len(unique_accounts), p=probabilities)

# 将生成的画像信息合并回月度账单中
monthly_summary = monthly_summary.merge(unique_accounts, on='AccountID', how='left')

# 设置到期日
monthly_summary['DueDate__c'] = monthly_summary['TimeStamp'] + pd.DateOffset(months=1, day=20)

# 定义一个函数来根据画像生成支付日期
def generate_paid_date(row):
    due_date = row['DueDate__c']
    profile = row['Payment_Profile']
    billing_month_num = row['TimeStamp'].month

    if profile == 'On-Time':
        return due_date - timedelta(days=np.random.randint(1, 11))
    elif profile == 'Late':
        return due_date + timedelta(days=np.random.randint(15, 31))
    elif profile == 'Risk':
        delay = 10 + (billing_month_num * 5) + np.random.randint(0, 5)
        return due_date + timedelta(days=delay)
    else: # 默认情况
        return due_date - timedelta(days=np.random.randint(1, 11))

monthly_summary['PaidDate__c'] = monthly_summary.apply(generate_paid_date, axis=1)

# --- 9. 整理并输出最终的Billing_History.csv文件 ---
print("正在整理并输出最终文件...")
final_billing_history = monthly_summary.copy()
final_billing_history['Id'] = [str(uuid.uuid4()) for _ in range(len(final_billing_history))]
final_billing_history = final_billing_history.rename(columns={'AccountID': 'Customer__c'})

output_df = final_billing_history[[
    'Id',
    'Customer__c',
    'Amount__c',
    'DueDate__c',
    'PaidDate__c'
]]

output_df['DueDate__c'] = output_df['DueDate__c'].dt.strftime('%Y-%m-%d')
output_df['PaidDate__c'] = output_df['PaidDate__c'].dt.strftime('%Y-%m-%d')

# --- 10. 保存文件 ---
output_filename = 'Billing_History.csv'
print(f"账单历史数据生成完毕! 正在保存到 {output_filename}...")
output_df.to_csv(output_filename, index=False)

print("\n生成Billing_History.csv的前5行预览:")
print(output_df.head())