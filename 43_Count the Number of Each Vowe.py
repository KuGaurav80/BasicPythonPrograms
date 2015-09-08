# python_count the number of each vowel in a string.py
#
# Created by Shashank Shukla:
__author__ = 'Shashank Shukla'

vowels= 'aeiou'
st= raw_input('enter string: ')
st= st.lower()
count= {}.fromkeys(vowels,0)

for ch in st:
    if ch in count:
        count[ch] += 1
print count