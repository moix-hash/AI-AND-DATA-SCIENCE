Scores_list = [40, 89, 90, 89, 23, 90, 50]

unique_scores = list(set(Scores_list))  # remove duplicates
unique_scores.sort(reverse=True)

print("Best Score:", unique_scores[0])
print("Second Best Score:", unique_scores[1])
