import requests
import os
import dotenv
import helper


dotenv.load_dotenv()
BASE_URL = "https://financialmodelingprep.com/api/v3/"
API_KEY = os.getenv("API_KEYS") or ""

def getData(search:str,stockName:str="",queryString:dict={}):
    errorMessage = helper.validateInput(search,stockName)
    if(errorMessage["error"]) is True:
        return errorMessage

    query = ""
    for q in query:
        query += str(q)+"="+str(queryString[q])+"&"
    
    url = "{base}{search}{stockName}?{query}apikey={key}".format(base=BASE_URL,search=search,query=query,stockName=stockName,key=API_KEY)
    res = requests.get(url)
    return {
        "status": res.status_code,
        "data": res.json()
    }
