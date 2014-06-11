#!/usr/bin/python
# Import modules for CGI handling 
import cgi, cgitb
#import mail api's for GAE
from google.appengine.api import mail
import webapp2
# Create instance of FieldStorage 
form = cgi.FieldStorage() 
# Get data from fields
name  = form.getvalue('name')
email  = form.getvalue('email')
subject_e  = form.getvalue('subject')
message = form.getvalue('message')

email_body="\nFrom :\t"+name+" <"+email+">\n\n"+message+"\n"
mail.send_mail(sender="GarryOrGKS <gks2703@gmail.com>",to="Gaurav Singh <gauravsingh@lnmiit.ac.in>",subject=subject_e,body=email_body)
print "<html>"
print "<head>"
print "<title>Sending Mail</title>"
print "</head>"
print "<body>"
print "<br><br><br><h4>Your message has been sent.</h4>"
print "</body>"
print "</html>"



