if __name__ == '__main__':
    alist = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        alist.append([name, score])
second_highest = sorted(set([score for name, score in alist]))[1]
print('\n'.join(sorted([name for name, score in alist if score == second_highest])))