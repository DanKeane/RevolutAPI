import requests
import json
import revolut_at as rev_at


with open('access_token_list_real.txt') as json_file:
    data = json.load(json_file)
    for at in data['access_token']:
        access_token = at


access_token_list = rev_at.access_tokens

client_id = "YOUR CLIENT ID HERE"

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

        get_accounts = f"{base_url_live}{accounts_endpoint}"

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

        receive_counterparties = f"{base_url_live}{receive_counterparties_endpoint}"

        r = requests.get(receive_counterparties, headers=headers)

        print(r.status_code)
        print(r.text)





    def create_counterparty_rev(self, data):
        '''
        Making a counterparty to make the payment
        '''

        counterparty_endpoint = "/counterparty"

        create_counterparty = f"{base_url_live}{counterparty_endpoint}"

        r = requests.post(create_counterparty, json=data, headers=headers)

        print(r.status_code)
        print(r.text)
        text = r.text
        json_txt = json.loads(text)
        counterparty_id = json_txt["id"]
        counterparty_ids.append(counterparty_id)

            
    def create_counterparty_uk(self, data):
        counterparty_endpoint = "/counterparty"

        create_counterparty = f"{base_url_live}{counterparty_endpoint}"

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

        create_counterparty = f"{base_url_live}{counterparty_endpoint}"

        r = requests.post(create_counterparty, json=data, headers=headers)

        print(r.status_code)
        print(r.text)

    def instant_payment(self, data):
        '''
        This is to create an instant payment. This is used if the rental is less than 3 days
        '''
        instant_payment_endpoint = "/pay"

        create_instant_payment = f"{base_url_live}{instant_payment_endpoint}"

        r = requests.post(create_instant_payment, json=data, headers=headers)

        print(r.status_code)
        print(r.text)


    def schedule_payment(self, data):
        '''
        This is used to create a schedule payment. This is if the rental is longer than 3 days
        '''

        schedule_payment_endpoint = "/pay"

        create_schedule_payment = f"{base_url_live}{schedule_payment_endpoint}"

        r = requests.post(create_schedule_payment, json=data, headers=headers)

        print(r.status_code)
        print(r.text)

    def draft_payment(self, data):
        '''
        Used for draft payments. Draft payments have to be manually accepted by the revolut owner.
        '''
        draft_payment_endpoint = "/payment-drafts"

        create_draft_payment = "https://b2b.revolut.com/api/1.0/payment-drafts"

        r = requests.post(create_draft_payment, json=data, headers=headers)

        print(r.status_code)
        print(r.text)



    def receive_all_transactions(self):
        '''
        receive all transactions from the past 90 days
        ''' 
        receive_all_transactions_endpoint = "/transactions"

        receive_all_transactions = f"{base_url_live}{receive_all_transactions_endpoint}"

        r = requests.get(receive_all_transactions, headers=headers)

        print(r.status_code)
        print(r.text)

    def receive_a_transaction(self, data):
        '''
        receive a transaction
        ''' 
        receive_a_transaction_endpoint = f"/transactions/{data}"

        receive_a_transaction = f"{base_url_live}{receive_a_transaction_endpoint}"

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

        create_webhook = f"{base_url_live}{webhook_endpoint}"

        r = requests.post(create_webhook, json=webhook_data, headers=headers)

        print(r.status_code)
        print(r.text)

rev = Revolut()
