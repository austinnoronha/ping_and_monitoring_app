"""Common Functions."""

import json


def json_response(message: str = "success", status_code: int = 200, data=None):
    """Common API Response."""
    dataparams = {"message": message, "status_code": status_code}
    dataparams["data"] = data
    return json.dump(dataparams)
