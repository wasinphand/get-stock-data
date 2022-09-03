import constant

STOCK_LIST = constant.STOCKS.STOCK_LIST
QUERY_SEARCH = constant.QUERY_SEARCH

def getAttributeFromClass(obj:type): 
    return [getattr(obj,attr) for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]

def validateStockName(stockName:str):
    return stockName in STOCK_LIST

def validateInput(search:str,stockName:str):
    if validateStockName(stockName) is False and search == QUERY_SEARCH.DIVIDEND:
        return {
            "error": True,
            "message":"Stock quote not found"
        }
    if search not in getAttributeFromClass(QUERY_SEARCH):
        return {
            "error": True,
            "message":"Wrong query parameter, please recheck search parameter or add new parameter in constant.py"
        }     
    return {
        "error": False,
        "message":None
    }