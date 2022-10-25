import email
import logging
from datetime import datetime, timedelta
from imaplib import IMAP4_SSL, IMAP4

LOGGER = logging.getLogger(__name__)

class GmailClient:
    SERVER = "imap.google.com"
    PORT = 993

    def __init__(self, email_addr, password):
        LOGGER.info("setting up gmail client")
        self.email_address = email_addr
        self.password = password
        self.client = None
        self.connect()

    def connect(self):
        LOGGER.info("Connecting with Gmail server...")
        self.client = IMAP4_SSL(host=self.SERVER)
        self.client.login(self.email_address, self.password)
        self.client.select("inbox")

    @staticmethod
    def _check_response(resp: str):
        LOGGER.debug("IMAP response: %s", resp)
        assert resp == "OK", "IMAP client error: command unknown or arguments invalid"

    def get_message_ids(self, search_criteria):
        LOGGER.info("Getting message ids...")
        self.client.noop()
        res, data = self.client.search(None, search_criteria)
        self._check_response(res)
        msg_ids = data[0].decode().split()
        LOGGER.debug("Got message ids: %s", msg_ids)
        return msg_ids

    def fetch_emails(self, message_ids, current_utc_time, date_format):
        email_messages = []
        for i in message_ids:
            res, data = self.client.fetch(i, '(RFC822)')
            self._check_response(res)
            for response_part in data:
                if not isinstance(response_part, tuple):
                    continue
                msg = email.message_from_string(tuple(response_part)[1].decode())
                LOGGER.info("Found the following msg '{}':")#надо дописать
                msg_date = datetime.strptime(msg["date"], date_format)#.astimezone(tz=tz.tzlocal()).replace(tzinfo=None)
                if (msg_date - current_utc_time).total_seconds() >= 0:
                    email_messages.append(msg)
        return email_messages

    def get_messages(self, to_email, from_email=None, search_in_all_folders = True, is_new_email = True,  find_before = 20):
        current_utc_time = datetime.now() - timedelta(seconds=find_before)
        date_format = "%a, %d %b %Y %H:%M:%S %z"
        search_criteria = ""

        if search_in_all_folders:
            search_criteria += ' ALL'
        if from_email:
            search_criteria += ' FROM "{}"'.format(from_email)
        if to_email:
            search_criteria += ' TO "{}"'.format(to_email)
        if is_new_email:
            search_criteria += ' UNSEEN'
        search_criteria = search_criteria.strip()

        def get_emails_list() -> list:
            LOGGER.info("Retrieving emails...")
            email_messages = self.fetch_emails(message_ids=self.get_message_ids(search_criteria),
                                               current_utc_time=current_utc_time, date_format=date_format)
            assert email_messages, "Not found at least one email message to following filters '{}' and"\
                                    "since '{}'".format(search_criteria, current_utc_time)
            return email_messages

    def logout(self):
        LOGGER.info("Closing the Gmail connecting...")
        try:
            self.client.logout()
        except IMAP4.abort:
            LOGGER.warning("The CMAIL connection was closed...")


# email testeriko123@gmail.com
# password Testeriko123.
if __name__ == "__main__":
    gmail_client = GmailClient(email_addr="testeriko123@gmail.com", password="Testeriko123.")
    LOGGER.info("Getting messages...")
    messages = gmail_client.get_messages(to_email="testeriko123@gmail.com", find_before=2000)
    LOGGER.info("Done.")