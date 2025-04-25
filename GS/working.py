from collections import Counter
def run(students):
    student_mark = {}
    for student in students:
        student_mark[student[0]] = sum(student[1])/len(student[1])
    l_sort_students = sorted(student_mark.items(), key=lambda x: x[1], reverse=True)
    return l_sort_students[0]

if __name__ == '__main__':
    students = [
                ['KALA', (5,4,6,3,5)],
                ['ENI', (5, 3, 4, 3, 4)],
                ['PANO', (5, 3, 3, 3, 4)],
                ['SERGE', (4, 4, 6, 4, 4)],
                ]
    print(run(students))
