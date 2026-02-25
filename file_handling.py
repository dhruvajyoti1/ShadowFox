import csv

# Open file
file = open("student_marks.csv", "r")
reader = csv.reader(file)

header = next(reader)

students = {}

for row in reader:
    name = row[0]   
    
    math = int(row[-3])
    reading = int(row[-2])
    writing = int(row[-1])
    
    students[name] = [math, reading, writing]

file.close()

# Calculate total and average
new_data = []

for name, marks in students.items():
    total = sum(marks)
    average = total / 3
    
    new_row = [name] + marks + [total, round(average, 2)]
    new_data.append(new_row)

# Create new CSV file
new_file = open("new_student_marks.csv", "w", newline="")
writer = csv.writer(new_file)

# Write header
new_header = ["Identifier", "Math", "Reading", "Writing", "Total_Marks", "Average"]
writer.writerow(new_header)

writer.writerows(new_data)

new_file.close()

print("New CSV file created successfully!")
