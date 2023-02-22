import platform
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests


class PyPINotifier:
    def __init__(self, email, password, recipient_email):
        self.email = email
        self.password = password
        self.recipient_email = recipient_email

    def get_new_packages(self):
        """Get the list of new packages available on PyPI"""
        response = requests.get('https://pypi.org/rss/packages.xml')
        new_packages = []
        if response.status_code == 200:
            content = response.text
            package_start_index = content.find('<title>') + len('<title>')
            package_end_index = content.find('</title>')
            while package_start_index > 0 and package_end_index > package_start_index:
                package_name = content[package_start_index:package_end_index].strip()
                new_packages.append(package_name)
                content = content[package_end_index+1:]
                package_start_index = content.find('<title>') + len('<title>')
                package_end_index = content.find('</title>')
        return new_packages

    def send_email_notification(self, new_packages):
        """Send an email notification to the recipient with the list of new packages"""
        if not new_packages:
            return
        subject = 'New PyPI packages available'
        body = '\n'.join(new_packages)
        message = MIMEMultipart()
        message['From'] = self.email
        message['To'] = self.recipient_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
            server.login(self.email, self.password)
            server.sendmail(self.email, self.recipient_email, message.as_string())

    def run(self):
        """Check for new packages and send an email notification if any are found"""
        new_packages = self.get_new_packages()
        self.send_email_notification(new_packages)


if __name__ == '__main__':
    email = 'sender_email@gmail.com'
    password = 'sender_password'
    recipient_email = 'recipient_email@example.com'
    notifier = PyPINotifier(email, password, recipient_email)
    notifier.run()
