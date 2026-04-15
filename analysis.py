import pandas as pd
df=pd.read_csv("train.csv")
print(df.head())
print(df.info())
print(df.isnull().sum())

#Numeric columns - mean se fill
num_clos = df.select_dtypes(include=['int64', 'float64']).columns
df[num_clos] = df[num_clos].fillna(df[num_clos].mean())

#Fill categorical
cat_cols= df.select_dtypes(include=['object', 'string']).columns
df[cat_cols]= df[cat_cols].fillna(df[cat_cols].mode().iloc[0])

#Special case
df['Postal Code']= df['Postal Code'].fillna(df['Postal Code'].mode()[0])

# City-Wise count
print(df['City'].value_counts())

#Segment-wise distribution
print(df['Segment'].value_counts())

#Visulaization
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("train.csv")

# ---- Cleaning ----
num_cols = df.select_dtypes(include=['int64', 'float64']).columns
df[num_cols] = df[num_cols].fillna(df[num_cols].mean())

cat_cols = df.select_dtypes(include=['object', 'string']).columns
df[cat_cols] = df[cat_cols].fillna(df[cat_cols].mode().iloc[0])

df['Postal Code'] = df['Postal Code'].fillna(df['Postal Code'].mode()[0])

# ---- Visualization ----
plt.figure(figsize=(8,5))

data = df['Segment'].value_counts()

bars = plt.bar(data.index, data.values)

plt.title("Customer Segment Distribution", fontsize=16, fontweight='bold')
plt.xlabel("Segment")
plt.ylabel("Number of Customers")

# Value labels
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 50, int(yval), ha='center')

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.style.use('seaborn-v0_8')
bars = plt.bar(data.index, data.values, color=['#4CAF50','#2196F3','#FF9800'])

plt.show()