data_file = open('work_data.txt')
data = data_file.read()
data_file.close()

lines = data.strip().split('\n')

summary = ""

for line in lines:
    parts = line.strip().split(',')
    name = parts[0].strip()
    hours = [int(h.strip()) for h in parts[1:]]
    total = sum(hours)
    average = round(total / len(hours), 1)
    summary += f"{name} - Total: {total} hrs, Average: {average} hrs/day\n"

output_file = open('summary.txt', 'w')
output_file.write(summary)
output_file.close()

print(summary)