student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
grades = {
    'Outstanding':[91,100],
    'Exceeds Expectations':[81,90],
    'Acceptable':[71,80],
    'Fail':[0,70]
}


def get_grade(score, grades):
    matching_key = next((key for key,(start,end) in grades.items() if start <= score <=end), None)
    return matching_key
        
    
    
student_grades = {key: get_grade(value,grades) for key,value in student_scores.items()}

print(student_grades)