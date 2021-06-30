from flask import *
import requests
import json
import time
import revolutAPI_live as rev

client_id = "YOUR CLIENT ID "


access_tokens = []

refresh_tokens = []

app = Flask(__name__)

client_assertion = "Long String"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/callback")
def callback():
    authorization_token = request.args.get('code')

    headers = {
        "Content-Type" : "application/x-www-form-urlencoded"
    }

    data = f"grant_type=authorization_code&client_id={client_id}&code={authorization_token}&client_assertion_type=urn:ietf:params:oauth:client-assertion-type:jwt-bearer&client_assertion={client_assertion}"

    r = requests.post("https://b2b.revolut.com/api/1.0/auth/token", data=data, headers=headers)
    print(r.status_code)
    print(r.text)
    named_tuple = time.localtime() # get struct_time
    time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)

    print("start time:" + time_string)
    response1 = r.text
    response = json.loads(response1)
    access_token = response["access_token"]
    refresh_token = response["refresh_token"]
    refresh_tokens.append(refresh_token)

    #if len(access_tokens) >= 2:
    #    access_tokens.pop(0)

    data = {}
    data['access_token'] = []
    data['access_token'].append(access_token)

    with open('your_txt.txt', 'w') as outfile:
        json.dump(data, outfile)

    rev1 = rev.Revolut()
    rev1.receive_counterparties()
    print(r.status_code)
    print(r.text)

    time.sleep(2380)
    rev1 = rev.Revolut()
    rev1.receive_counterparties()
    print(r.status_code)
    print(r.text)

    time.sleep(30)
    rev1 = rev.Revolut()
    rev1.receive_counterparties()
    print(r.status_code)
    print(r.text)












    return render_template("index.html", authorization_token=authorization_token, access_token=access_token)



if __name__ == "__main__":
    app.run()
