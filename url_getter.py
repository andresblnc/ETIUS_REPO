# https://youtu.be/-H9yN_jl4FQ
# https://serpapi.com/dashboard

import os
import serpapi

from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("SERPAPI_KEY")
client = serpapi.Client(api_key=api_key)

result = client.search(
    engine="google",
    q="Coffee",
    location="Austin, Texas",
    hl="en",
    gl="us",
    num=10,
    start=0,
    tbm="isch"
)