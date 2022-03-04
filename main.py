from flask import Flask, render_template, request
from sandbox_apis import get_token_response, execute_wf
import json

app = Flask(__name__)

@app.route("/")
def root():
    print("sending root")
    return render_template("index.html")


@app.route("/docs")
def swagger_docs():
    print("sending swagger docs")
    return render_template("swaggerui.html")


@app.route("/auth")
def login():
    print("json recieved from swagger>>", data_from_swagger := request.args.to_dict())  # recieved credentials
    sandboxNum = int(data_from_swagger.pop("sandboxNumber"))
    print("json data for IAP login>>", data_to_IAP := {"user": data_from_swagger})

    return get_token_response(sandboxNum, data_to_IAP)


@app.route("/start_wf/LNAAS_CREATE_UNI_SL_V1", methods=["POST"])
def start_wf_lnaas_create_uni_sl_v1():
    print("sandbox number>>", sandboxNum := request.args.to_dict()['sandboxNumber'])
    print(
        "payload recieved from swagger>>",
        json.dumps(payload_from_swagger := request.json, indent=4)
    )

    return execute_wf(sandboxNum, "LNAAS_CREATE_UNI_SL_V1", payload_from_swagger)


app.run(host="0.0.0.0",use_reloader=True, debug=True)
