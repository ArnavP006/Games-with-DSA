q = {
    "Which data structure uses FIFO? ": "queue",
    "Which sorting algorithm is fastest on average? ": "quicksort",
    "Which data structure uses LIFO? ": "stack"
}

score = 0
for i in q:
    ans = input(i).lower()
    if ans == q[i]:
        score += 1
        print("Correct!")
    else:
        print("Wrong! Answer:", q[i])

print(f"\nYour score: {score}/{len(q)}")
