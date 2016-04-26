#########################################################
#author: ata fatahi baarzi                              #
#mailto: afbcesh91@gmail.com                            #            
#########################################################
import smtplib
import datetime
import unicodedata
from urllib2 import urlopen as up
from time import  gmtime, strftime
from bs4 import BeautifulSoup as BS


course_url = "http://ce.sharif.edu/courses/94-95/2/ce221-3/"
last_time = ''
def read_page(url):
    return up(url).read()
def num_apperances_of_tag(tag_name, html):
    soup = BS(html)
    return soup.findAll("td")[-1].get_text()


def prompt(prompt):
    return raw_input(prompt).strip()

last_time_str = unicodedata.normalize('NFKD', num_apperances_of_tag("tr",read_page(course_url))).encode('ascii','ignore')
last_time_update =  str(str(last_time_str).split()[-2] + " " + str(last_time_str).split()[-1])
last_time  = datetime.datetime.strptime(last_time_update,'%Y-%m-%d %H:%M')




def check_is_updated(last_date):    
    last_update_str = unicodedata.normalize('NFKD', num_apperances_of_tag("tr",read_page(course_url))).encode('ascii','ignore')
    last_update =  str(str(last_update_str).split()[-2] + " " + str(last_update_str).split()[-1])
    luobj = datetime.datetime.strptime(last_update,'%Y-%m-%d %H:%M')
    if luobj > last_date:
        global last_time
        last_time = luobj
        print last_time
        return (True,last_time)
    return (False,str(last_time))


def send_email(recipient, subject, body):    

    gmail_user = user    
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login('YOUR@EMAIL', "YOUREMAILPASSWORD")
        server.sendmail(FROM, TO, message)
        server.close()
        print 'successfully sent the mail'
    

    except Exception,e: print str(e)
    

while True:
    isUpdated,tm = check_is_updated(last_time)
    if isUpdated:
        send_email('afbcesh91@gmail.com', "CE REMINSER", "course updated! see here:"+course_url)
    
