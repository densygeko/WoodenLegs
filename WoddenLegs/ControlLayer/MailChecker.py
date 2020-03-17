import re

class MailChecker:
    
    def checkMail(text):
        emails = re.findall('\S+@\S+\.[a-zA-Z]{2,4}', text)
        print(emails)
        return emails

    def checkPhone(text):
        phones = re.search('(\+?(45){1})?([-.\s]?\d{1}){8}', text)
        print(phones)
