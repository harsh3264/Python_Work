# Program 1 reverse the digits
def digit_sum(n):
    x = len(str(n))
    sums = 0
    while x>0:
        y = int(n/(10 ** (x-1)))
        n = n - (y * (10 ** (x-1)))
        sums += y
        x -= 1
    return sums
        
        
print digit_sum(456436346)

# Program 2 reverse the string
def reversey(text):
    y = len(text)
    l = []
    for each in range(y):
        z = y - each - 1
        l.append(text[z])
    print "".join(l)
    
def reverse(text):
    result = ""
    index = len(text) - 1
    for i in range(0,len(text)):
        result = result + text[index]
        index = index - 1
    return result
        
        
    
print reverse("Python!")

# P 3 Vowel remove
def anti_vowel(text):
    l = []
    for i in text:
        if i.lower() not in "aeiou":
            l.append(i)
    print "".join(l)

print anti_vowel("Hey You!")

def anti_vowel(text):
    vowel = ['a', 'e', 'i', 'o', 'u',"A","E","I","O","U"]
    new = []
    for char in text:
        if char not in vowel:
            new.append(char)
    return "".join(new)

  # P 4 scrabble
  score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
         
def scrabble_score(word):
    s = 0
    
        
    for i in word:
        if i.lower() == ' ':
            s += 0
        else:
            s += score[i.lower()]
    print s
    
print scrabble_score("pie A c")

# Censor the word
def censor(text, word):
    x = text.split()
    for i in range(len(x)):
        if x[i] == word:
            x[i] = len(x[i]) * "*"
    return " ".join(x)


# Removing duplicates from list
def remove_duplicates(List):
    newList = []
    for item in List:
        if item not in newList:
            newList.append(item)
    return newList
                
                
print remove_duplicates([1,2,3,1,2,1,2,1,1,4,2,1,5])

# grades exercise
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print grade

def grades_sum(grades):
    total = 0
    for grade in grades: 
        total += grade
    return total
    
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average
    
def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance += (average - score) ** 2
    variance = variance/float(len(scores))
    return variance
    
def grades_std_deviation(variance):
    std = variance ** 0.5
    return std
    
variance = grades_variance(grades)
std = grades_std_deviation(variance)
print std
    
print print_grades(grades)
print grades_sum(grades)
print grades_average(grades)
print grades_variance(grades)
print grades_std_deviation(variance)    

        

# printing even numbers between 1 to 50 
evens_to_50 = [i for i in range(51) if i % 2 == 0]
print evens_to_50

# printing strides
x - [ i**2 for i in range(1,101) if (i**2) % 4 == 0]
print x[3:81:4]

# printing lambda functions
my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list)

# fnmatch and lambda uses
import fnmatch
languages = ["HTML", "JavaScript", "Python", "Ruby"]
print filter(lambda x: x == 'Python',languages)
print fnmatch.filter(languages,'R*')

# combine both
import fnmatch
l = ["HTML", "JavaScript", "Python", "Ruby"]
print filter(lambda x: x == "".join(fnmatch.filter(l,'P*')),l)
