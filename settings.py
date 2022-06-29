import os
import dotenv
import intrinio_sdk as intrinio

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

_INTRINIO_API_KEY = os.getenv("INTRINIO_API_KEY")
intrinio.ApiClient().set_api_key(_INTRINIO_API_KEY)
intrinio.ApiClient().allow_retries(True)
