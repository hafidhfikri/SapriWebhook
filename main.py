import requests as req
import json

def webhook(request):
    #set default response
    response = json.dumps({'fulfillmentMessages':[{'text':{'text':['Internal Error']}}]})
    
    #get request payload
    json_parse = request.get_json()

    #dialogflow and telegram validation
    if ('responseId' in json_parse) and (json_parse.get('originalDetectIntentRequest', {}).get('source') == 'telegram') :    
        
        try:
            url = "https://us-central1-newagent-mnsmjh.cloudfunctions.net/ChatGateway"
            header = {"Content-Type":"application/json"}
            print(json_parse)
            result = req.post(url,json=json.dumps(json_parse),header=header)
            response = result.text
        except Exception as e:
            print("Error Something Happen....")
            print(e)
            response = json.dumps({'fulfillmentMessages':[{'text':{'text':['Request Error']}}]})

    else:
        response = json.dumps({'fulfillmentMessages':[{'text':{'text':['Illegal Action']}}]})
    
    return response  