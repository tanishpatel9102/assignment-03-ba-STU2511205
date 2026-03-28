raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]
cleaned_students= []
for students in raw_students:

# Task 1.1

    name = students["name"]
    name = name.strip()
    name = name.title()

    roll = int(students["roll"])

    marks = list(map(int, students["marks_str"].split(", ")))

# Task 1.2

    is_valid = all(word.isalpha() for word in name.split())

    if is_valid:
        print(name, "→ ✓ Valid name")
    else:
        print(name, "→ ✗ Invalid name")

# Task 1.3

    cleaned_students.append({"name": name, "roll": roll, "marks": marks})

    print("=" * 40)
    print(f"Student : {name}")
    print(f"Roll No : {roll}")
    print(f"Marks : {marks}")
    print("=" * 40)

# Task 1.4

for student in cleaned_students:
    if student["roll"] == 103:
        print(student["name"].upper()) 
        print(student["name"].lower())

# Task 2.1
student_name = "Ayesha Sharma"
subjects     = ["Math", "Physics", "CS", "English", "Chemistry"]
marks        = [88, 72, 95, 60, 78]

for i in range(len(subjects)):
    m = marks[i]

    if 90 <= m <= 100:
        grade = "A+"
    elif 80 <= m <= 89:
        grade = "A"
    elif 70 <= m <= 79:
        grade = "B"
    elif 60 <= m <= 69:
        grade = "C"
    else:
        grade = "F"

    print(subjects[i], ":", m, "----", grade) 

# Task 2.2

print("Total Marks: ",sum(marks))

print(f"Average Marks: {sum(marks) / len(marks):.2f}")

max_marks = max(marks)
index = marks.index(max_marks)

print("Highest scoring subject: ", subjects[index], max_marks)

min_marks = min(marks)
index = marks.index(min_marks)

print("Lowest scoring subject: ", subjects[index], min_marks)

# Task 2.3

new_count = 0

while True:
    subject = input("Enter subject name (or type 'done' to stop): ")
    if subject.lower() == "done":
        break
    marks_input = input("Enter marks (0–100): ")
    if not marks_input.isdigit():
        print("Invalid marks")
        continue
    m = int(marks_input)
    if m < 0 or m > 100:
        print("Marks must be between 0-100")
        continue
    subjects.append(subject)
    marks.append(m)
    new_count += 1

print("New subjects added:", new_count)
print(f"Updated Average: {sum(marks)/len(marks):.2f}")

# Task 3.1
class_data = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]

for name, marks in class_data:
    avg = sum(marks) / len(marks)

    if avg >=60:
        status = "Pass"
    else:
        status = "Fail"
    print(f"{name} = Average: {avg:.2f} = {status}")

# Task 3.2

print(f"{'Name':<18} | {'Average':^7} | {'Status'}")
print("-" * 60)

for name, marks in class_data:
    avg = sum(marks) / len(marks)
    print(f"{name:<18} | {avg:>7.2f} | {'Pass' if avg>= 60 else 'Fail'}")

# Task 3.3

pass_count = fail_count = 0
topper_name, topper_avg = "", 0
total_avg = 0

for name, marks in class_data:
    avg = sum(marks) / len(marks)
    total_avg += avg

    if avg>=60:
        pass_count +=1    
    else:
        fail_count += 1

    if avg > topper_avg:
        topper_name, topper_avg = name, avg
    

print("Passed:", pass_count)
print("Failed:", fail_count)
print(f"Topper: {topper_name} ({topper_avg:.2f})")
print(f"Class Average: {total_avg/len(class_data):.2f}")

essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "
# 4.1 Strip
clean_essay = essay.strip()
print("Clean essay: ", clean_essay)
# 4.2 Convert
print("Title Case: ", clean_essay.title())
# 4.3 Count
count = clean_essay.count("python")
print("'python' Count: ", count)
# 4.4 Replace
replaced = clean_essay.replace("python", "Python 🐍")
print("Replaced Essay: ", replaced)
# 4.5 Split
sentences = clean_essay.split(". ")
print("Sentences List: ", sentences)
# 4.6 Numbered Sentence
print("Numbered Sentence: ")
for i, sentence in enumerate(sentences, 1):
    if not sentence.endswith("."):
        sentence += "."
    print(f"{i}. {sentence}")

