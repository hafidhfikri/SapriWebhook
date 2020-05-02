import requests as req
import json

def webhook(request):
    #set default response
    print("START")
    response = json.dumps({'fulfillmentMessages':[{'text':{'text':['Internal Error']}}]})
    '''
    #get request payload
    request_json = request.get_json()
    json_parse = json.loads(request_json)

    #dialogflow and telegram validation
    if ("responseId" in json_parse) and (json_parse["originalDetectIntentRequest"]["source"] == "telegram") :
        print("ACCEPTED!!!")
        
        try:
            url = ""
            response = req.post(url,request_json)
        except:
            print("Error Something Happen....")
            response = json.dumps({"fulfillmentMessages":[{"text":{"text":["Internal Error"]}}]})
        
        print("Sukses")
        response = json.dumps({"fulfillmentMessages":[{"text":{"text":["Sukses"]}}]})
    else:
        print("Illegal Request")
        response = json.dumps({"fulfillmentMessages":[{"text":{"text":["Illegal Request"]}}]})
    '''
    return response