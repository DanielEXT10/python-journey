student_scores = [150,142,120,182,171,184,149,24,59,68, 199]


total_exam_score = sum(student_scores)

sum = 0

for score in student_scores:

    sum += score

print(sum)

#get the max value

def max(arr):
    max = 0
    for i in arr:
        if i > max:
            max = i
    print(max)
    

max(student_scores)