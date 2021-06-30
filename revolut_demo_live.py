import revolutAPI_live as rev
import time
import string
import random
length=23

my_account_id = "YOUR ACCOUNT ID"


SAMS_PERSONAL = "TEST-792b-4d86-8229-TEST"


rev1 = rev.Revolut()
rev1.receive_counterparties()
#rev1.accounts()


d_p = {
    "payments": [
        {
        "account_id": my_account_id,
        "receiver": {
            "counterparty_id": SAMS_PERSONAL,
            #"account_id": "449e7a5c-69d3-4b8a-aaaf-5c9b713ebc65"
            },
        "amount": 2,
        "currency": "GBP",
        "reference": "Payment test"
        }
    ]
    }


# create instant payment
rev1.draft_payment(d_p)
