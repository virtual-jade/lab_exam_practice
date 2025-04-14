with open("Exam_Table.csv", "r") as file:
    csvreader = file.readlines()
csvreader = csvreader[1:]

Genus_Po = []

for row in csvreader:
    parts = row.strip().split(",")
    if len(parts) > 1:
        name = parts[9].strip()
        if name.startswith(str("St")):
            Genus_Po.append(row.strip())

with open("b2_output1.csv", "w") as outfile:
    for item in Genus_Po:
        outfile.write(item + "\n")

print()

with open ("b2_output1.csv", "r") as file:
    csvreader = file.readlines()
for row in csvreader:
    print(row)