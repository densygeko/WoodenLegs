import re

class MailChecker:
    
    def checkMail(text):
        emails = re.findall('\S+@\S+\.[a-zA-Z]{2,4}\s', text)
        print(emails)
        return emails

    def checkPhone(text):
        phones = re.search('(\+?(45){1})?([-.\s]?\d{1}){8}', text)
        print(phones)

mailCheck = MailChecker
mailCheck.checkPhone("4524233211")
#mailCheck.checkMail("this is my email psavage1995@gmail.com and this is another one peop@babi.come s   hje@hotmail.cos.uk  abc@ads.co.ssdds")