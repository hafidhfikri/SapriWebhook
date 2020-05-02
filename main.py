import requests as req
import json

def webhook(rere):
    #set default response
    response = json.dumps({'fulfillmentMessages':[{'text':{'text':['Internal Error']}}]})
    
    #get request payload
    json_parse = json.loads(rere)

    #dialogflow and telegram validation
    if ('responseId' in json_parse) and (json_parse['originalDetectIntentRequest']['source'] == 'telegram') :
        '''
        try:
            url = ""
            response = req.post(url,request)
        except:
            print("Error Something Happen....")
            response = json.dumps({'fulfillmentMessages':[{'text':{'text':['Internal Error']}}]})
        '''

        response = json.dumps({'fulfillmentMessages':[{'text':{'text':['Sukses']}}]})
    else:
        response = json.dumps({'fulfillmentMessages':[{'text':{'text':['Illegal Action']}}]})
    
    return response  