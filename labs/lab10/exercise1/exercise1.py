num_rounds = int(input())

final_score = 0

for rounds_processed in range(num_rounds):
    score = int(input())
    if score > 100:
        score *= 1.2
    final_score += score

rounds_processed = num_rounds

print(f"{final_score:.1f}")
print(rounds_processed)
