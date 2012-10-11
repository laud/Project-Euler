def problem_sixty_seven():
    tree = []
    with open('problem_files/problem67.txt') as f:
        for l in f:
            tree.append(l.split())

    for i in xrange(len(tree)-2, -1, -1):
        for j in xrange(0, len(tree[i])):
            tree[i][j] = int(tree[i][j]) + int(max(tree[i+1][j], tree[i+1][j+1]))

    return tree[0][0]