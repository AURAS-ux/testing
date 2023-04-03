import requests

class API:
    endpoint:str
    port:str
    resource:str
    dataType:str
    snippet:bool

    def __init__(self,endpoint:str,port:str,resource:str,dataTye:str,snippet:bool):
        self.endpoint = endpoint
        self.port = port
        self.resource = resource
        self.dataType = dataTye
        self.snippet = snippet

    def __buildQuery(self):
        if(self.dataType is not None and self.snippet is not None):
            return f"?data_type={self.dataType}&snippet={str(self.snippet).lower()}"
        else:
            return ""

    def getApi(self):
        return self.endpoint+self.port+self.resource+self.__buildQuery()

    def getAPIResponse(self):
        return requests.get(self.getApi())