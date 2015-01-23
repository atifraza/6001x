s = 'azcbobobegghakl'
vowelCount = 0
vowels = ['a', 'e', 'i', 'o', 'u']
for char in vowels:
    vowelCount = vowelCount + s.count(char)
    
print('Number of vowels: ' + str(vowelCount))