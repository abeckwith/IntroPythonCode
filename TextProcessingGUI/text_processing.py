# this is your code, so put shebang, etc. here...

def concat(a, b, c):
    '''returns a combination of three strings'''
    return a + b + c

def switchy(first_word, last_word):
    '''switches two words'''
    return last_word + " " + first_word

def square(num):
    '''returns the square of the number'''
    if num.isdigit():
        num = int(num)
        return num * num
    else:
        return "not able to be calculated.  Enter a positive integer"
    
def vowels(text):
    '''returns the number of vowels in the text'''
    count = 0
    for c in text:
        if c in "aeiou":
            count += 1
    return count
                