import requests

def status_decorator(func):
    def status_and_data_check(*args,**kwargs):
        r=func(*args,**kwargs)
        if "errorMessage" in r.keys():
            r={"status" :"error raised during data acquisition"}
        elif r["data"]["data"] == []:
            r={"status" : "no data to present"}
        return r
    return status_and_data_check


class electricity_prices:
    def __init__(self):
        self.headers =  { "Accept": "application/json" }
        self.basic_endpoint="https://odegdcpnma.execute-api.eu-west-2.amazonaws.com/development/prices?"

    @status_decorator
    def get_prices(self,dno,voltage,start_date,end_date):
        #dates accepted format: DD-MM-YYYY
        req_url=self.basic_endpoint+f"dno={dno}&voltage={voltage}&start={start_date}&end={end_date}"
        r = requests.get(req_url, headers = self.headers)

        return(r.json())



ele=electricity_prices()
prices=ele.get_prices(12,"HVE","10-11-2022","12-11-2022")
