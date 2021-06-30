import requests
import json
import revolut_at as rev_at


with open('access_token_list.txt') as json_file:
    data = json.load(json_file)
    for at in data['access_token']:
        access_token = at


access_token_list = rev_at.access_tokens

client_id = "YOUR CLIENT ID"

base_url_live = "https://b2b.revolut.com/api/1.0"

print(access_token)

base_url_sandbox = "https://sandbox-b2b.revolut.com/api/1.0"

headers = {
    "Authorization" : f"Bearer {access_token}",
    #"Content-Type" : "application/json"
}


account_ids = []
counterparty_ids = []

class Revolut:

    def accounts(self):
        '''
        Get request to receive my accounts // Needed for my id
        '''
        accounts_endpoint = "/accounts"

        get_accounts = f"{base_url_sandbox}{accounts_endpoint}"

        #when get requests.get
        r = requests.get(get_accounts, headers=headers)


        print(r.status_code)
        print(r.text)


    def receive_counterparties(self):
        '''
        Use this to get all of my counterparties added previously. This will be used to check if i need to add the new customer to my counterparty list.
        If they are on this list i can just pass over the next step.
        '''

        receive_counterparties_endpoint = "/counterparties"

        receive_counterparties = f"{base_url_sandbox}{receive_counterparties_endpoint}"

        r = requests.post(receive_counterparties, headers=headers)

        print(r.status_code)
        print(r.text)





    def create_counterparty_rev(self, data):
        '''
        Making a counterparty to make the payment
        '''

        counterparty_endpoint = "/counterparty"

        create_counterparty = f"{base_url_sandbox}{counterparty_endpoint}"

        r = requests.post(create_counterparty, json=data, headers=headers)

        print(r.status_code)
        print(r.text)

            
    def create_counterparty_uk(self, data):
        counterparty_endpoint = "/counterparty"

        create_counterparty = f"{base_url_sandbox}{counterparty_endpoint}"

        r = requests.post(create_counterparty, json=data, headers=headers)

        print(r.status_code)
        print(r.text)
        text = r.text
        json_txt = json.loads(text)
        counterparty_id = json_txt["id"]
        counterparty_ids.append(counterparty_id)
        accounts = json_txt["accounts"]
        accounts_json = accounts[0]
        account_id = accounts_json["id"]
        account_ids.append(account_id)

    def create_counterparty_international(self, data):
        counterparty_endpoint = "/counterparty"

        create_counterparty = f"{base_url_sandbox}{counterparty_endpoint}"

        r = requests.post(create_counterparty, json=data, headers=headers)

        print(r.status_code)
        print(r.text)

    def instant_payment(self, data):
        '''
        This is to create an instant payment. This is used if the rental is less than 3 days
        '''
        instant_payment_endpoint = "/pay"

        create_instant_payment = f"{base_url_sandbox}{instant_payment_endpoint}"

        r = requests.post(create_instant_payment, json=data, headers=headers)

        print(r.status_code)
        print(r.text)


    def schedule_payment(self):
        '''
        This is used to create a schedule payment. This is if the rental is longer than 3 days
        '''
        sp_data = {
            "request_id": "e0cbf84637264ee082a848b",
            "account_id": "bdab1c20-8d8c-430d-b967-87ac01af060c",
            "receiver": {
                "counterparty_id": "5138z40d1-05bb-49c0-b130-75e8cf2f7693",
                "account_id": "db7c73d3-b0df-4e0e-8a9a-f42aa99f52ab"
            },
            "amount": 123.11,
            "currency": "EUR",
            "reference": "Invoice payment #123",
            "schedule_for": "2017-10-10"
            }

        schedule_payment_endpoint = "/pay"

        create_schedule_payment = f"{base_url_sandbox}{schedule_payment_endpoint}"

        r = requests.post(create_schedule_payment, json=sp_data, headers=headers)

        print(r.status_code)
        print(r.text)

    def receive_all_transactions(self):
        '''
        receive all transactions from the past 90 days
        ''' 
        receive_all_transactions_endpoint = "/transactions"

        receive_all_transactions = f"{base_url_sandbox}{receive_all_transactions_endpoint}"

        r = requests.get(receive_all_transactions, headers=headers)

        print(r.status_code)
        print(r.text)

    def receive_a_transaction(self, data):
        '''
        receive a transaction
        ''' 
        receive_a_transaction_endpoint = f"/transactions/{data}"

        receive_a_transaction = f"{base_url_sandbox}{receive_a_transaction_endpoint}"

        r = requests.get(receive_a_transaction, headers=headers)

        print(r.status_code)
        print(r.text)


    def webhook(self):
        '''
        This is to receive webhooks.
        '''
        webhook_data = {
            "url": "https://example.com/example/path" #my url
            }
        
        webhook_endpoint = "/webhook"

        create_webhook = f"{base_url_sandbox}{webhook_endpoint}"

        r = requests.post(create_webhook, json=webhook_data, headers=headers)

        print(r.status_code)
        print(r.text)

rev = Revolut()
