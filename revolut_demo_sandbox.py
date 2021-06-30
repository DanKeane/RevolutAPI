import revolutAPI as rev
import time
import string
import random
length=23

my_account_id = "YOUR ACCOUNT ID"

rev1 = rev.Revolut()


#rev1.receive_all_transactions()

'''

PLAN 

Do step "For counterparties" in the dashbaord and save counterparty_id and account_id to db

'''


################################################################################### For counterparties #################################################################################

#use this if they have a revolut account
r_cp_data = {
    "profile_type": "personal",
    "name": "sab Smith",
    "phone": "+44753456789"
    }
#use this if they dont have a revolut account but from the UK
uk_cp_data = {
    "company_name": "John Kella Co.",
    "profile_type": "personal",
    "bank_country": "GB",
    "currency": "GBP",
    "account_no": "14345628",
    "sort_code": "213734",
    "email": "john@smith.com",
    "phone": "+447771434455",
    "address": {
        "street_line1": "1 Canada Square",
        "street_line2": "Canary Wharf",
        "region": "East End",
        "postcode": "E115AB",
        "city": "London",
        "country": "GB"
    }
    }
#use this if they dont have a revolut account and outside the uk
i_cp_data = {
    "company_name": "John Smith Co.",
    "bank_country": "FR",
    "currency": "EUR",
    "iban": "FR1420041010050500013M02606",
    "bic": "0500013M026",
    "email": "john@smith.co",
    "phone": "+447771234455",
    "address": {
        "street_line1": "20 Central Paris",
        "street_line2": "Champ de Mars",
        "region": "Paris",
        "postcode": "75007",
        "city": "Paris",
        "country": "FR"
    }
    }


# create counterparty
create_counterparty = rev1.create_counterparty_uk(uk_cp_data)

counterparty_id = rev.counterparty_ids[0]
# only need account_id for buisness requests
account_id = rev.account_ids[0]


########################################################################################################################################################################################




################################################################################## Create instant transfer #############################################################################

request_id = ''.join(random.choices(string.ascii_letters+string.digits,k=length))

ip_data = {
    "request_id": request_id, #u can make this up
    "account_id": my_account_id,
    "receiver": {
        "counterparty_id": counterparty_id,
    },
    "amount": 2,
    "currency": "GBP",
    "reference": "Test Payment 2"
    }

ip_business_data = {
    "request_id": "e0cbf84637264ee082a848b",
    "account_id": "my_account_id",
    "receiver": {
        "counterparty_id": "counterparty_id",
        "account_id": "f4b6b464-59d0-477a-9377-90b5c2565e2a"
    },
    "amount": 123.11,
    "currency": "EUR",
    "reference": "Invoice payment #123"
    }

# create instant payment
create_intant_payment = rev1.instant_payment(ip_data)

########################################################################################################################################################################################

