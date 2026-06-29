if __name__ == '__main__':

    students = []

    # Step 1: Store all students in a nested list
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    # Step 2: Store all scores separately
    scores = []

    for student in students:
        scores.append(student[1])

    # Step 3: Sort the scores
    scores.sort()

    # Step 4: Find the second lowest score
    lowest = scores[0]

    for score in scores:
        if score > lowest:
            second_lowest = score
            break

    # Step 5: Find students having the second lowest score
    names = []

    for student in students:
        if student[1] == second_lowest:
            names.append(student[0])

    # Step 6: Sort the names alphabetically
    names.sort()

    # Step 7: Print the names
    for name in names:
        print(name)