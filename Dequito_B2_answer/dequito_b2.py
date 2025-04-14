import pandas as pd
df = pd.read_csv('Exam_Table.csv')

genus_data = df[df['Genus'].str.startswith("St", na=False)] 
print(genus_data)

genus_data.to_csv("b1_output1_copy.csv", index=False)