with open("Exam_Table.csv", "r") as file:
    csvreader = file.readlines()
csvreader = csvreader[1:]

interval_30_0 = []

for row in csvreader:
    parts = row.strip().split(",")
    if len(parts) > 1:
        interval = parts[8].strip()
        if interval == str("30-0"):
            interval_30_0.append(row.strip())

with open("b1_output1.csv", "w") as outfile:
    for item in interval_30_0:
        outfile.write(item + "\n")

print()

with open("b1_output1.csv", "r") as file:
    csvreader = file.readlines()
for row in csvreader:
    print(row)