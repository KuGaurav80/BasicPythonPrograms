# python_sort alphabetically the word.py
#
# Created by Shashank Shukla:
__author__ = 'Shashank Shukla'

st= raw_input('Enter String: ')

words= st.split()
words.sort()

for w in words:
    print w