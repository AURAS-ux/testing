from API import *

response_snippetT = API("http://localhost:","8081","/get_data","air_pollution",True).getAPIResponse()
response_snippetF = API("http://localhost:","8081","/get_data","air_pollution",False).getAPIResponse()


def test_conn():
    assert response_snippetT.status_code == 200

def test_data():
    assert response_snippetT.text is not None

def test_schema():
    schema = response_snippetT.json()["@context"]["@schema"]
    assert schema == "firebase/air_pollution"

def test_snippetT_size():
    assert len(response_snippetT.json()["@list"]) == 10

def test_snippetF_size():
    assert len(response_snippetF.json()["@list"]) > 10


def test_data_integrity():
    jsonList = response_snippetF.json()["@list"]
    for listItem in jsonList:
        allowdNullValues = 0.3 * len(listItem)
        counter = 0
        for key in listItem:
            if(listItem[key] is None):
                counter+=1

        assert counter < allowdNullValues

