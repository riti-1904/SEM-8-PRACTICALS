import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load transformed data
df = pd.read_csv("output/transformed_data.csv")

# Bar Chart: Average Salary per Department
plt.figure(figsize=(8, 5))
sns.barplot(x='Department', y='Salary', data=df, palette='Blues_d')
plt.title('Average Salary by Department')
plt.xlabel('Department')
plt.ylabel('Average Salary')
plt.tight_layout()
plt.savefig("output/bar_chart_salary_by_department.png")
plt.show()

# Line Chart: Experience Distribution
df_sorted = df.sort_values("Experience_Years")
plt.figure(figsize=(8, 5))
plt.plot(df_sorted['Name'], df_sorted['Experience_Years'], marker='o')
plt.title("Employee Experience (Years)")
plt.xlabel("Employee")
plt.ylabel("Years of Experience")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("output/line_chart_experience.png")
plt.show()

# Pie Chart: Department Count
dept_counts = df['Department'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(dept_counts, labels=dept_counts.index, autopct='%1.1f%%', startangle=140)
plt.title("Department Distribution")
plt.savefig("output/pie_chart_department.png")
plt.show()

# Interactive Scatter Plot: Salary vs Experience
fig = px.scatter(df, x="Experience_Years", y="Salary", color="Department",
                 hover_data=['Name'], title="Salary vs Experience (Interactive)")
fig.write_html("output/scatter_salary_experience.html")
fig.show()
