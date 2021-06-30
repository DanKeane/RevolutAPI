from flask import *
import requests
import json

client_id = "YOUR CLIENT ID"

client_assertion = "YOUR CLIENT ASSERTION" 

access_tokens = []

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/callback")
def callback():
    authorization_token = request.args.get('code')

    headers = {
        "Content-Type" : "application/x-www-form-urlencoded"
    }

    data2 = f"grant_type=authorization_code&client_id={client_id}&code={authorization_token}&client_assertion_type=urn:ietf:params:oauth:client-assertion-type:jwt-bearer&client_assertion={client_assertion}"

    r = requests.post("https://sandbox-b2b.revolut.com/api/1.0/auth/token", data=data2, headers=headers)
    print(r.status_code)
    print(r.text)
    response1 = r.text
    response = json.loads(response1)
    access_token = response["access_token"]
    
    #if len(access_tokens) >= 2:
    #    access_tokens.pop(0)

    data = {}
    data['access_token'] = []
    data['access_token'].append(access_token)

    with open('access_token_list.txt', 'w') as outfile:
        json.dump(data, outfile)

    return render_template("index.html", authorization_token=authorization_token, access_token=access_token)





if __name__ == "__main__":
    app.run()
