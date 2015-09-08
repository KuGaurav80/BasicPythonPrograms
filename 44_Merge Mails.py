# python_Merge Mails.py
#
# Created by Shashank Shukla:
__author__ = 'Shashank Shukla'

with open("name.txt",'r') as file_name:
    with open("body.txt",'r') as file_body:
        body= file_body.read()
        for name in file_name:
            mail= "Hi! "+name+body
            with open(name.strip()+".txt",'w') as file_mail:
                file_mail.write(mail)