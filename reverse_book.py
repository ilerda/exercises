# x is a string representing a book of text. The pages are separatd by \b. The lines by \n. 

# Write a function that reverses the
# - order of pages
# - order of lines in each page
# - order of words in each line
# - don't reverse the characters in each word

# Sample string:
x="the brown fox jumped over the fence\nthe brown bear fell down the hill\n\bThe big lion chased the deer\nThe monkey ate the bananas\n\b"

def book_reverse(x):
    res = []
    pages = x.split("\b")
    nlines = []
    for page in pages:
        lines = page.split("\n")
        nwords = []
        for line in lines:
            words = line.split(" ")
            nwords.append(" ".join(words[::-1]))
        nlines.append("\n".join(nwords[::-1]))
    res.append("\\b".join(nlines[::-1]))
    return res
    
print(book_reverse(x))
