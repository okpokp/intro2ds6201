from collections import Counter
import sys

def show_help():
    print()
    print(f"Count words and show most common N words in a text file.")
    print(f"\tpython {sys.argv[0]} INPUT_FILENAME NUM_TOPN")
    print()

try:
    filename = sys.argv[1]
    N = int(sys.argv[2])         # how many top-N words needed?
except IndexError:
    show_help()
    sys.exit(1)

CHUNKSIZE = 128              # size_hint for readlines
num_words = 0
word_counter = Counter()

with open(filename, 'r') as f:  
    # read multiple lines at a time, with siz_hint CHUNKSIZE 
    # and transform it to iterable, 
    #   stop when f.readlines(CHUNKSIZE)  returns an empty string
    for chunk in iter(lambda: f.readlines(CHUNKSIZE), ''):
        if len(chunk) == 0:
            break
        # ''.join(chunk)  transform list of lines into a string
        #    .strip()     remove newline
        #    .split()     split into word (delimited by a space ' ' character
        words = ''.join(chunk).strip().split()
        num_words += len(words)
        word_counter.update(words)
        
print(f"total number of words in message.txt: {num_words}")
print(f"total number of distinct words: {len(word_counter.keys())}")
print(f"top-{N} most commonly used words: {', '.join([x[0] for x in word_counter.most_common(N)])}")

