from typing import Tuple
import requests

def get_token_response(sandboxNumber: int, credentials: dict) -> Tuple[str,int]:
    url = f"http://titansdevcarrier.clcloud.af.qwest.net:40{sandboxNumber}/login"
    try:
        login_resp = requests.post(url, json=credentials)
        if login_resp.status_code == 200:
            print("recieved token>>", token := login_resp.text)
            return token, 200
        elif login_resp.status_code == 500:  # can be MongoServerSelectionError or invalid username/password
            return str(login_resp.json()["error"]), 400  # will return error message
    except:
        pass
    return "Can't reach the IAP server", 400


def execute_wf(sandboxNumber: int, wf_name: str, payload: dict) -> tuple:
    cred = {"user": {"username": "admin@pronghorn","password": "admin"}}
    token, status = get_token_response(sandboxNumber, cred)  #token will either be a valid token or an error message

    if status == 200:  # in case of a valid token
        start_wf_url = f"http://titansdevcarrier.clcloud.af.qwest.net:40{sandboxNumber}/workflow_engine/startJobWithOptions/{wf_name}?token={token}"
        req_body = {
                "options": {"description": "", "variables": payload},
                "groups": [],
                "type": "automation",
            }
        try:
            execute_wf_resp = requests.post(start_wf_url, json=req_body)
            if execute_wf_resp.status_code == 200 and "application/json" in execute_wf_resp.headers["content-type"]:
                job_id = str(execute_wf_resp.json()["_id"])
                job_url = f"http://titansdevcarrier.clcloud.af.qwest.net:40{sandboxNumber}/workflow_engine/viewer?job_id={job_id}"
                return {"job_id": job_id, "job_url": job_url}, 200
            else:
                print("execute WF resp from IAP>>", execute_wf_resp.text)
                return "Cannot start the workflow", 400
        except:
            return "Cannot start the workflow", 400
    else:
        return token, 400  # it will be an error message
