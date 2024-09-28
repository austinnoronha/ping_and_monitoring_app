"""Config File."""

import os
import sys

from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()


# ------------------------
# Common
# ------------------------
APP_PATH = os.path.abspath(os.path.join(__file__, "../.."))
OS_IS_WINDOWS = False
if sys.platform == "win32":
    OS_IS_WINDOWS = True

ERROR_MESSAGES = {
    "ERR_SERVER_CON_1": "A server connection error has occurred. \
    We are working to resolve the issue. Please try again later."
}

# Ensure that all necessary environment variables are loaded
assert APP_PATH, "APP_PATH environment variable is not set."
