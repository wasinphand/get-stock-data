import constant
import sys
import helper
from get_data import getData
from store_data import createDelistedEquitiesData, createDividendData

QUERY_SEARCH = constant.QUERY_SEARCH

" INPUT FIELDS "
search = QUERY_SEARCH.DIVIDEND
stockName = "FB"
queryString = {
    "page":3
}

" VALIDATE INPUT FIELDS "
if helper.validateStockName(stockName=stockName) is False:
    sys.exit("Stock not found!!")

" GET DATA "
switchSearch = {
    QUERY_SEARCH.DIVIDEND : lambda: getData(search=search,stockName=stockName),
    QUERY_SEARCH.DELISTED : lambda: getData(search=search,queryString=queryString)
}
responseGetData = switchSearch[search]()
if(responseGetData["status"] != 200) or ("error" in responseGetData.keys()):
    sys.exit("Something on network went wrong !!")

" STORE DATA "
switchStoreData = {
    QUERY_SEARCH.DIVIDEND : lambda: createDividendData(search=search,data = responseGetData["data"]),
    QUERY_SEARCH.DELISTED : lambda: createDelistedEquitiesData(search=search,data = responseGetData["data"])  
}
reponseCreateData  = switchStoreData[search]()
print(reponseCreateData)