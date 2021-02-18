import httplib
import smtplib
from email.MIMEText import MIMEText
from email.Header import Header
from email.Utils import formatdate

myURL = raw_input('URL Please:')
httpconnection = httplib.HTTPConnection(myURL)
httpconnection.request('GET', '/')
res = httpconnection.getresponse()
data = res.read()
#allheaders = res.getheaders()
print data

f = open('text.html', 'w')
f.write(data)
f.close()

from_address = "myaddress@exmaple.com"
to_address = "friend@example.com"
charset = "ISO-2022-JP"
subject = "test"
text = data
msg = MIMEText(text.encode(charset),"plain",charset)
msg["Subject"] = Header(subject,charset)
msg["From"] = from_address
msg["To"] = to_address
msg["Date"] = formatdate(localtime=True)
smtp = smtplib.SMTP("cupost.chiba-u.jp")
smtp.sendmail(from_address,to_address,msg.as_string())
smtp.close()
