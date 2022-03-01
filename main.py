from flask import Flask, Response, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def get_root():
    print('sending root')
    return render_template('index.html')

@app.route('/docs')
def get_docs():
    print('sending swagger docs')
    return render_template('swaggerui.html')

@app.route('/auth')
def get_api():
    print('json recieved from swagger>>', cred := request.args.to_dict())   #recieved credentials
    SNDBX = cred.pop('sandboxNumber')
    print('json sent to IAP login>>', toIAP := {'user': cred})

    try:
        login_resp = requests.post(f'http://titansdevcarrier.clcloud.af.qwest.net:40{SNDBX}/login',json=toIAP)
        
        if login_resp.status_code == 200:
            return Response(login_resp.text, status=200)
        elif login_resp.status_code == 500:   #can be MongoServerSelectionError or invalid username/password
            return Response(login_resp.json()['error'],status=400)  #will return error message
    except:
        pass
    return Response("Can't reach the IAP server",status=400)

app.run(use_reloader=True, debug=False)