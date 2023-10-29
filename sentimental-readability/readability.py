from cs50 import get_string

text=get_string("Text that should be tested: ")

num_s=0
num_words=0

for i in range(len(text)):
    if ("?" == text[i] or "!" == text[i] or "." == text[i]):
        num_s+=1

    if (" " == text[i]):
        num_words+=1

num_letter= len(text)- num_words - num_s
num_words+=1

faktor= 100/num_words

s= num_s*faktor
l=num_letter*faktor

grade = 0.0588 * l - 0.296 * s - 15.8
grade=round(grade, 1)
if grade>16:
    print("Grade 16+")
elif grade <1:
    print("Before Grade 1")
else:
    print(f"Grade: {grade}")


