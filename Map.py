words = 'Data Science Academy offers the best data analysis courses in Brazil'.split()
results = map(lambda w: [w.upper(), w.lower(), len(w)], words)
for i in results:
    print(i)