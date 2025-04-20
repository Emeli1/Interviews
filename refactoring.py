# Мы устроились на новую работу. Бывший сотрудник начал разрабатывать модуль для работы с почтой, но не успел доделать его.
# Код рабочий. Нужно только провести рефакторинг кода.
#
# Создать класс для работы с почтой;
# Создать методы для отправки и получения писем;
# Убрать "захардкоженный" код. Все значения должны определяться как аттрибуты класса, либо аргументы методов;
# Переменные должны быть названы по стандарту PEP8;
# Весь остальной код должен соответствовать стандарту PEP8;
# Класс должен инициализироваться в конструкции.
# if __name__ == '__main__':
# Скрипт для работы с почтой.

import email
import smtplib
import imaplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Email:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    def send_email(self, gmail_smtp, port, recipients, subject, message):
        try:
            message_form = MIMEMultipart()
            message_form['From'] = self.login
            message_form['To'] = ', '.join(recipients)
            message_form['Subject'] = subject
            message_form.attach(MIMEText(message))
            sending_mail = smtplib.SMTP(gmail_smtp, port)
            sending_mail.ehlo()
            sending_mail.starttls()
            sending_mail.ehlo()
            sending_mail.login(self.login, self.password)
            result = sending_mail.sendmail(message_form['From'], message_form['To'], message_form.as_string())
            sending_mail.quit()
            return result
        except Exception as ex:
            return f'Ошибка отправки почты: {ex}'

    def recieve_email(self, gmail_imap, mailbox, header=None):
        recieving_mail = imaplib.IMAP4_SSL(gmail_imap)
        try:
            recieving_mail.login(self.login, self.password)
            recieving_mail.list()
            recieving_mail.select(mailbox)
            criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
            result, data = recieving_mail.uid('search', None, criterion)
            assert data[0], 'There are no letters with current header'
            latest_email_uid = data[0].split()[-1]
            print(latest_email_uid.decode('utf-8'))
            result, data = recieving_mail.uid('fetch', latest_email_uid, '(RFC822)')
            raw_email = data[0][1]
            email_message = email.message_from_string(raw_email.decode('utf-8'))
            recieving_mail.logout()
            return email_message
        except Exception as ex:
            return f'Ошибка получения почты: {ex}'


if __name__ == '__main__':
    mail = Email('login@gmail.com', 'qwerty')
    print(mail.send_email("smtp.gmail.com", 587, ['vasya@email.com', 'petya@email.com'],
                          'Message', 'Text'))

