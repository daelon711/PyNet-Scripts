import re
import datetime
from email.message import EmailMessage
from email.parser import Parser


class EmailObject:
    def __init__(self, from_email, to_email, subject, body):
        self.msg = EmailMessage()
        self.msg['From'] = from_email
        self.msg['To'] = to_email
        self.msg['Subject'] = subject
        self.msg.set_content(body)
        # parse message to extract headers
        self.parsed = Parser().parsestr(self.msg.as_string())

    def get_body(self):
        # email body
        return self.msg.get_content()

    def as_string(self):
        # formatted email as a string
        return self.msg.as_string()


def is_valid_email(email):
    pattern = r'^[\w\.-]+@([\w-]+\.)+[\w-]{2,4}$'
    match = re.match(pattern, email)
    if match is not None:
        return True
    else:
        return False


def log_email_check(email):
    now = datetime.datetime.now()
    print(f"\nChecking '{email}' at {now.strftime('%Y-%m-%d %H:%M:%S')}")
    if is_valid_email(email):
        print("valid email")
        return True
    else:
        print("invalid email")
        return False


def interactive_email_builder():
    try:
        from_email = input("sender email: ").strip()
        to_email = input("recipient email: ").strip()
        # Check both emails and stop if either is invalid
        if not log_email_check(from_email) or not log_email_check(to_email):
            print("One of the emails is invalid.")
            return

        subject = input("subject: ").strip()
        body = input("email body:\n")

        email_obj = EmailObject(from_email, to_email, subject, body)
        print("\n---------")
        print(email_obj.as_string())
    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == '__main__':
    interactive_email_builder()
