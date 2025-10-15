import pandas as pd
import matplotlib.pyplot as plt

path='./sample.csv'
df = pd.read_csv(path)
df.head()
print(df)
df['slot_date_time'] = pd.to_datetime(df['slot_date_time'], format='mixed')
df['slot_date_time'] = df['slot_date_time'].dt.month
df.head()
user_count_per_month = df['slot_date_time'].value_counts().sort_index()
print("User Count per Month:")
print(user_count_per_month)
user_name_counts = df['invitee_name'].value_counts()
print("User Name Frequencies:")
print(user_name_counts)

plt.figure(figsize=(10, 6))
user_name_counts.plot(kind='bar', color= 'skyblue')
plt.title('User Name Frequencies ')
plt.xlabel('User Name ')
plt.ylabel('Frequency')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

forms = df['form_name'].value_counts()
plt.figure(figsize=(8, 8))
labels = forms.index
plt.pie(forms, autopct='%1.1f%%', startangle=140)
plt.title('Form')
plt.legend(labels, loc="lower left", bbox_to_anchor=(0.5, 0.5), facecolor='yellow', edgecolor='black')
plt.axis('equal')
plt.savefig("plot1.png", dpi=1000)
plt.show()

plt.figure(figsize=(9, 4))
forms.plot(kind= 'bar', color= 'blue')
plt.title( 'Form created ')
plt.xlabel( 'form name ')
plt.ylabel( 'Frequency')
plt.xticks(rotation=45, ha='right')
plt.savefig("plot2.png", dpi=1000)
plt.show()

best_user = user_name_counts.idxmax()
print(f"The best user is: {best_user}")