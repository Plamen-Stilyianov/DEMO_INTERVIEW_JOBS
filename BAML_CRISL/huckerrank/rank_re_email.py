import email.utils, re


def validate_email(mail):
    line = email.utils.parseaddr(mail)
    if re.match(r'[a-zA-Z](\w|-|\.)*@[a-zA-Z]*\.[a-zA-Z]{0,3}$', line[1]):
        print(email.utils.formataddr(line))


[validate_email(input()) for _ in range(int(input()))]

data = """9
vin <vineet@>
vineet <vineet@gmail.com>
vineet <vineet@gma.il.co.m>
vineet <vineet@gma-il.co-m>
vineet <vineet@gma,il.co@m>
vineet <vineet@gmail,com>
vineet <.vin@gmail.com>
vineet <vin-nii@gmail.com>
vineet <v__i_n-n_ii@gmail.com>"""
