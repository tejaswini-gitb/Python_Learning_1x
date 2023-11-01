words=["apple","cherry","banana","jackfruit","almond","fig"]
print(words)
w_len =6

def check_len(word):
    return len(word) > w_len
op=list(filter(check_len,words))
print(op)