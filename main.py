from flask import Flask, Response, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def root():
    print('sending root')
    return render_template('index.html')

@app.route('/docs')
def swagger_docs():
    print('sending swagger docs')
    return render_template('swaggerui.html')

@app.route('/auth')
def login():
    
    print('json recieved from swagger>>',data_from_swagger := request.args.to_dict())   #recieved credentials
    sandboxNum = data_from_swagger.pop('sandboxNumber')
    print('json data for IAP login>>', data_to_IAP := {'user': data_from_swagger})

    try:
        login_resp = requests.post(f'http://titansdevcarrier.clcloud.af.qwest.net:40{sandboxNum}/login',json=data_to_IAP)
        if login_resp.status_code == 200:
            print('recieved token>>', token := login_resp.text)
            return Response(token, status=200)
        elif login_resp.status_code == 500:   #can be MongoServerSelectionError or invalid username/password
            return Response(login_resp.json()['error'],status=400)  #will return error message
    except:
        pass
    return Response("Can't reach the IAP server",status=400)

app.run(use_reloader=True, debug=False)