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
