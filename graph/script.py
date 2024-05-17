import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

users_df = pd.read_csv('members_data.csv', delimiter='\t')

scatter_data = users_df[['age', 'friends_count']].dropna()

plt.figure(figsize=(10, 6))
sns.scatterplot(x='age', y='friends_count', data=scatter_data, alpha=0.6)
plt.title('Диаграмма рассеяния: Возраст и Количество друзей')
plt.xlabel('Возраст')
plt.ylabel('Количество друзей')
plt.show()