import requests as req
import json

def webhook(request):
    #set default response
    response = json.dumps({'fulfillmentMessages':[{'text':{'text':['Internal Error']}}]})
    
    #get request payload
    json_parse = request.get_json() #jadi dictionary
    print(type(json_parse)) 
    print(type(request))
    print(json_parse.get('originalDetectIntentRequest', {}).get('source') is 'telegram')
    print(json_parse.get('originalDetectIntentRequest', {}).get('source') == 'telegram')
    
    #dialogflow and telegram validation
    if ('responseId' in json_parse) and (json_parse.get('originalDetectIntentRequest', {}).get('source') == 'telegram') :
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