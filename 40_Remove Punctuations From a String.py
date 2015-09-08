# python_Remove Punctuations From a String.py
#
# Created by Shashank Shukla:
__author__ = 'Shashank Shukla'

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

st= raw_input('Enter string: ')
rm_pun= ''
for ch in st:
    if ch not in punctuations:
        rm_pun= rm_pun + ch

print rm_pun
