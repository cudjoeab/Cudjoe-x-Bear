# word = ['a', 'b', 'c','c','b', 'a']

# Test out palindromes! 
# Words inlude:
#       madam 
#       racecar 
#       redivider 
# Sentences include:
#    "Mr Owl ate my metal worm"
#    "Do geese see God?"
#    "Was it a car or a cat I saw?"
#    "Murder for a jar of red rum" 
#    "Go hang a salami I'm a lasagna hog"

# NB: some challenges to modify the code:
# 1. needed to make the user input non case sensitive 
# 2. needed to remove the spaces from the sentences 

userInput = input('Please enter your palindrome test word or phrase: ').lower()
print(userInput)
userInputMod = userInput.replace(" ", "")
print(userInputMod)
testPal = list(userInputMod) 
print(testPal)

def test():
    left = 0 
    right = len(testPal) - 1
    while left < right: 
        print(testPal[left]) 
        print(testPal[right])
        if testPal[left] != testPal[right]: 
            return False
        right = right - 1 
        left = left + 1 
    return True 
        

result = test() 

print(result)








