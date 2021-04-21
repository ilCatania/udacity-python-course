import collections


def count_unique_words(filename):
    c = collections.Counter()
    with open(filename, 'r') as f:
        for l in f.readlines():
            c.update(l.split())
    return c


if __name__ == '__main__':
    c = count_unique_words('hamlet.txt')
    top_ten = sorted(c.items(), key=lambda e: -e[1])[:10]
    for k, v in top_ten:
        print(k, " ", v)
