# wordfreq.py

import string

def compareItems((w1, c1), (w2, c2)):
    if c1 > c2:
        return -1
    elif c1 == c2:
        return cmp(w1, w2)
    else:
        return 1

def main():
    print "This program analyzes word frequency in a file"
    print "and prints a report on the n most frequent words.\n"
    
    # get the sequence of words from a file
    fname = raw_input("File to analyze: ")
    text = open(fname, 'r').read()
    text = string.lower(text)
    # replace each punctuation character with a space
    for ch in '!"#$%&()*+,-./:;<=>?@[\]^_|~':
        text = string.replace(text, ch, ' ')
    # split string at whitespace to form a list of words
    words = string.split(text)
    
    # construct a dictionary of the word counts
    counts = {}
    for w in words:
        counts[w] = counts.get(w,0) + 1
    
    # output analysis of n most frequent words
    n = input("Output analysis of how many words? ")
    items = counts.items()
    items.sort(compareItems)
    for i in range(n):
        print "%-10s%d" % items[i]

if __name__ == '__main__': main()