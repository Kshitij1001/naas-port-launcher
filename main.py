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
    sandboxNum = data_from_swagger.pop("sandboxNumber")
    data_to_IAP = {"user": data_from_swagger}
    app.logger.info('json data for IAP login>> %s', data_to_IAP)
    return get_token_response(sandboxNum, data_to_IAP)


@app.route("/start_wf", methods=["POST"])
def start_workflow():
    print("URL parameters from swagger>>", url_parameters := request.args.to_dict())
    sandboxNum, wf_name = url_parameters["sandboxNumber"], url_parameters["workflowName"]
    print(
        "payload recieved from swagger>>",
        json.dumps(payload_from_swagger := request.json, indent=4)
    )

    return execute_wf(sandboxNum, wf_name, payload_from_swagger)


app.run(use_reloader=True, debug=True)
