from prefect_email import EmailServerCredentials


def create_email_creds_block():
    credentials = EmailServerCredentials(
        username="asdf123",
        password="asdf",  # must be an app password
    )
    credentials.save("email-taxi-block")
    
if __name__=="__main__":
    create_email_creds_block()