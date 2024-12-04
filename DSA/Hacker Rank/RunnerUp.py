arr = [3,4,6,2,3,5,7]
unique_scores = list(set(arr))
unique_scores.sort(reverse=True)
runner_up_score = unique_scores[1]
print(runner_up_score)