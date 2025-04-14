import pandas as pd
df = pd.read_csv('Exam_Table.csv')

genus_data = df[df['Genus'].str.startswith("St", na=False)] 
print(genus_data)

genus_data.to_csv("b2_output1.csv", index=False)