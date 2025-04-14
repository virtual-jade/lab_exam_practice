import pandas as pd
df = pd.read_csv("Exam_Table.csv")

interval_30_0 = df[df['Interval']=="30-0"] 
print(interval_30_0)

interval_30_0.to_csv("b1_output1.csv", index=False)