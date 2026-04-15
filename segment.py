import pandas as pd
import matplotlib.pyplot as plt

# ---- Load Data ----
df = pd.read_csv("train.csv")

# ---- Cleaning ----
num_cols = df.select_dtypes(include=['int64', 'float64']).columns
df[num_cols] = df[num_cols].fillna(df[num_cols].mean())

cat_cols = df.select_dtypes(include=['object', 'string']).columns
df[cat_cols] = df[cat_cols].fillna(df[cat_cols].mode().iloc[0])

df['Postal Code'] = df['Postal Code'].fillna(df['Postal Code'].mode()[0])

# ---- Data for Segment ----
segment_data = df['Segment'].value_counts().reset_index()
segment_data.columns = ['Segment', 'Count']
segment_data['Percentage'] = (segment_data['Count'] / segment_data['Count'].sum() * 100).round(2)
segment_data['Percentage'] = segment_data['Percentage'].astype(str) + '%'

# ---- Layout: Graph + Table side by side ----
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
plt.style.use('seaborn-v0_8')

# ---- Bar Chart ----
colors = ['#4CAF50', '#2196F3', '#FF9800']
bars = ax1.bar(segment_data['Segment'], segment_data['Count'], color=colors)

ax1.set_title("Customer Segment Distribution", fontsize=16, fontweight='bold')
ax1.set_xlabel("Segment")
ax1.set_ylabel("Number of Orders")
ax1.grid(axis='y', linestyle='--', alpha=0.7)

for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, yval + 50, int(yval), ha='center', fontsize=12)

# ---- Table ----
ax2.axis('off')

rows = ['Count', 'Percentage']
cols = segment_data['Segment'].tolist()

table = ax2.table(
    cellText=[segment_data['Count'].tolist(), segment_data['Percentage'].tolist()],
    rowLabels=rows,
    colLabels=cols,
    cellLoc='center',
    loc='center',
    bbox=[0.05, 0.3, 0.9, 0.4]
)

table.auto_set_font_size(False)
table.set_fontsize(12)

# Header row styling
for j, col in enumerate(cols):
    table[0, j].set_facecolor(colors[j])
    table[0, j].set_text_props(color='white', fontweight='bold')

# Row label styling
for i in range(1, len(rows) + 1):
    table[i, -1].set_facecolor('#f0f0f0')
    table[i, -1].set_text_props(fontweight='bold')

ax2.set_title("Segment Summary Table", fontsize=16, fontweight='bold', pad=20)

plt.tight_layout()
plt.savefig("segment_analysis.png", dpi=150, bbox_inches='tight')
plt.show()

print("\nSegment Summary:")
print(segment_data.to_string(index=False))