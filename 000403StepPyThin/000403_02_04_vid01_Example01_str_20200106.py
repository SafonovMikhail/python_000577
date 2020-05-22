# вариант 1
# genome = input()
genome = 'CCAT'
cnt = 0
for nucl in genome:
    if nucl == 'C':
        cnt += 1
print(cnt)
# вариант 2
# genome = input()
genome = 'CCAT'
print(genome.count('C'))