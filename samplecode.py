# -*- coding: utf-8 -*-
import traceback

from dataapi import Client
if __name__ == "__main__":
    try:
        client = Client()
        client.init('4b35b6b552ea66ef08186d267e693c86ed4726227979720aac8fb2d42a1c242a')
        url1='/api/market/getMktEqud.json?field=&beginDate=20170801&endDate=&secID=&ticker=000001&tradeDate='
        code, result = client.getData(url1)
        if code==200:
            print(result)
            file_object = open('thefile.csv', 'w')
            file_object.write(result)
            file_object.close()
        else:
            print(code)
            print(result)
    except Exception as e:
        traceback.print_exc()
        raise e
