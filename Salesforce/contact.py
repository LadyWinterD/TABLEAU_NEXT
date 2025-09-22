import csv
import random
from datetime import datetime, timedelta

# 你的100个Account ID
account_ids = [
    "001NS00001uEHLB", "001NS00001uEHLC", "001NS00001uEHLD", "001NS00001uEHLE",
    "001NS00001uEHLF", "001NS00001uEHLG", "001NS00001uEHLH", "001NS00001uEHLI",
    "001NS00001uEHLJ", "001NS00001uEHLK", "001NS00001uEHLL", "001NS00001uEHLM",
    "001NS00001uEHLN", "001NS00001uEHLO", "001NS00001uEHLP", "001NS00001uEHLQ",
    "001NS00001uEHLR", "001NS00001uEHLS", "001NS00001uEHLT", "001NS00001uEHLU",
    "001NS00001uEHLV", "001NS00001uEHLW", "001NS00001uEHLX", "001NS00001uEHLY",
    "001NS00001uEHLZ", "001NS00001uEHLa", "001NS00001uEHLb", "001NS00001uEHLc",
    "001NS00001uEHLd", "001NS00001uEHLe", "001NS00001uEHLf", "001NS00001uEHLg",
    "001NS00001uEHLh", "001NS00001uEHLi", "001NS00001uEHLj", "001NS00001uEHLk",
    "001NS00001uEHLl", "001NS00001uEHLm", "001NS00001uEHLn", "001NS00001uEHLo",
    "001NS00001uEHLp", "001NS00001uEHLq", "001NS00001uEHLr", "001NS00001uEHLs",
    "001NS00001uEHLt", "001NS00001uEHLu", "001NS00001uEHLv", "001NS00001uEHLw",
    "001NS00001uEHLx", "001NS00001uEHLy", "001NS00001uEHLz", "001NS00001uEHM0",
    "001NS00001uEHM1", "001NS00001uEHM2", "001NS00001uEHM3", "001NS00001uEHM4",
    "001NS00001uEHM5", "001NS00001uEHM6", "001NS00001uEHM7", "001NS00001uEHM8",
    "001NS00001uEHM9", "001NS00001uEHMA", "001NS00001uEHMB", "001NS00001uEHMC",
    "001NS00001uEHMD", "001NS00001uEHME", "001NS00001uEHMF", "001NS00001uEHMG",
    "001NS00001uEHMH", "001NS00001uEHMI", "001NS00001uEHMJ", "001NS00001uEHMK",
    "001NS00001uEHML", "001NS00001uEHMM", "001NS00001uEHMN", "001NS00001uEHMO",
    "001NS00001uEHMP", "001NS00001uEHMQ", "001NS00001uEHMR", "001NS00001uEHMS",
    "001NS00001uEHMT", "001NS00001uEHMU", "001NS00001uEHMV", "001NS00001uEHMW",
    "001NS00001uEHMX", "001NS00001uEHMY", "001NS00001uEHMZ", "001NS00001uEHMa",
    "001NS00001uEHMb", "001NS00001uEHMc", "001NS00001uEHMd", "001NS00001uEHMe",
    "001NS00001uEHMf", "001NS00001uEHMg", "001NS00001uEHMh", "001NS00001uEHMi",
    "001NS00001uEHMj", "001NS00001uEHMk", "001NS00001uEHMl", "001NS00001uEHMm"
]

# 随机数据选项
first_names = ['Alice', 'Bob', 'Carol', 'David', 'Emma', 'Frank', 'Grace', 'Henry', 'Isabella', 'James']
last_names = ['Smith', 'Brown', 'Johnson', 'Lee', 'Wilson', 'Davis', 'Clark', 'Lewis', 'Taylor', 'Walker']
departments = ['Sales', 'Marketing', 'IT', 'HR', 'Finance']
genders = ['Male', 'Female', 'Non-Binary']
cities = ['New York', 'San Francisco', 'Chicago', 'Boston', 'Seattle', 'Austin', 'Denver', 'Miami', 'Portland', 'Atlanta']
states = ['NY', 'CA', 'IL', 'MA', 'WA', 'TX', 'CO', 'FL', 'OR', 'GA']
income_brackets = ['Low', 'Medium', 'High']
title_types = ['Manager', 'Director', 'Analyst', 'Coordinator']

# 生成98条Contact数据
contacts = []
account_indices = random.sample(range(len(account_ids)), 98)  # 随机选择98个Account
for i, idx in enumerate(account_indices[:98]):
    account_id = account_ids[idx]
    num_contacts = 2 if i < 49 else 1  # 前49个Account各2条，第50个1条，总计98
    for _ in range(num_contacts):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        age = random.randint(18, 80)
        birthdate = (datetime.now() - timedelta(days=age*365)).strftime('%Y-%m-%d')
        city = random.choice(cities)
        state = random.choice(states)
        contacts.append({
            'AccountId__c': account_id,
            'Age__c': age,
            'Birthdate__c': birthdate,
            'Department__c': random.choice(departments),
            'Description__c': 'Test Contact',
            'DoNotCall__c': random.choice(['TRUE', 'FALSE']),
            'EmailBouncedDate__c': '',
            'EmailBouncedReason__c': '',
            'Email__c': f"{first_name.lower()}.{last_name.lower()}@test.com",
            'Fax__c': '',
            'FirstName__c': first_name,
            'GenderIdentity__c': random.choice(genders),
            'HomePhone__c': f"+1-555-01{random.randint(10, 99)}",
            'Income_Bracket__c': random.choice(income_brackets),
            'IndividualId__c': '',
            'MailingCity__c': city,
            'MailingCountry__c': 'USA',
            'MailingGeocodeAccuracy__c': '',
            'MailingLatitude__c': '',
            'MailingLongitude__c': '',
            'MailingPostalCode__c': f"{random.randint(10000, 99999)}",
            'MailingState__c': state,
            'MailingStreet__c': f"{random.randint(100, 999)} {city} St",
            'MobilePhone__c': f"+1-555-02{random.randint(10, 99)}",
            'Name__c': f"{first_name} {last_name}",
            'OtherCity__c': '',
            'OtherCountry__c': '',
            'OtherGeocodeAccuracy__c': '',
            'OtherLatitude__c': '',
            'OtherLongitude__c': '',
            'OtherPhone__c': '',
            'OtherPostalCode__c': '',
            'OtherState__c': '',
            'OtherStreet__c': '',
            'Phone__c': f"+1-555-03{random.randint(10, 99)}",
            'TitleType__c': random.choice(title_types),
            'Title__c': random.choice(title_types),
            'LastName__c': last_name
        })

# 写入CSV
with open('fake_contacts_98.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['AccountId__c', 'Age__c', 'Birthdate__c', 'Department__c', 'Description__c', 'DoNotCall__c', 'EmailBouncedDate__c', 'EmailBouncedReason__c', 'Email__c', 'Fax__c', 'FirstName__c', 'GenderIdentity__c', 'HomePhone__c', 'Income_Bracket__c', 'IndividualId__c', 'MailingCity__c', 'MailingCountry__c', 'MailingGeocodeAccuracy__c', 'MailingLatitude__c', 'MailingLongitude__c', 'MailingPostalCode__c', 'MailingState__c', 'MailingStreet__c', 'MobilePhone__c', 'Name__c', 'OtherCity__c', 'OtherCountry__c', 'OtherGeocodeAccuracy__c', 'OtherLatitude__c', 'OtherLongitude__c', 'OtherPhone__c', 'OtherPostalCode__c', 'OtherState__c', 'OtherStreet__c', 'Phone__c', 'TitleType__c', 'Title__c', 'LastName__c'])
    writer.writeheader()
    writer.writerows(contacts)

print(f"Generated {len(contacts)} Contact records in fake_contacts_98.csv")