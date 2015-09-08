# python_Check_string_is palindrome or not.py
#
# Created by Shashank Shukla:
__author__ = 'Shashank Shukla'

st= raw_input("Enter String: ")
st= st.lower()
rv_st= reversed(st)

if list(st) == list(rv_st):
    print 'PALINDROME'
else:
    print 'not PALINDROME'