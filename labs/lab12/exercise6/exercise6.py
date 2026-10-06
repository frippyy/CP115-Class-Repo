a = int(input())

overtake_round = 0
distance_a = 0
distance_b = 0
i = 0
round = 0
while a != -1:
    i += 1
    if i % 2 != 0:
        distance_a = a
    else:
        distance_b = a
    if i == 2:
        round += 1
        if distance_b > distance_a:
            overtake_round = round
            break
        i = 0
    a = int(input())
    

print(overtake_round)
