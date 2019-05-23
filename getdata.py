from flask import Flask,jsonify,request
import requests
import json

app = Flask(__name__)

@app.route('/data')
def getData():
    
   #return requests.get("https://api.github.com").content
    url = "https://api.github.com"
    try :

        status=requests.get(url).status_code
        print(status)
        
        
        return requests.get(url).content
    except ConnectionError as e:
        print(e)

@app.route('/choice',methods=['POST'])
def userChoice():

    #choicedata = request.json
    #print(choicedata)
    #dataDict = json.loads(data)
    #return json.dumps(request.json)
    '''
    notify = request.json['notifications_url']
    url = "https://api.github.com"
    #info = requests.get(url).content
    if notify == 'https://api.github.com/notifications':
        print("Authenticated User")
        return requests.get(url).content

    elif KeyError :
        print('Not Found')
        return jsonify({
            "notifications_url" : "Wrong value"

        }
                    

                    
                )
       '''
    try :

        notify = request.json['notifications_url']
        url = "https://api.github.com"
        #info = requests.get(url).content
        if notify == 'https://api.github.com/notifications':

            print("Authenticated User")
            return requests.get(url).content

        #this will run if value of notify is wrong
        else :
            print ('Not Found')
            return jsonify({
                "Value" :"Wrong"
            })

    except Exception as e:
        print(e)
        return jsonify({
            "Property" : "Wrong "

        })



if __name__ == '__main__':
    app.run()

    