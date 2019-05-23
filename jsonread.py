import json

try:

    #read file
    with open('gitlab.json', 'r') as myfile:

        data = myfile.read()
        print("Read Successful")
    
        #parse file
        obj = json.loads(data)
        print("current user url "+ str(obj["current_user_url"]))
        print("hub url " + str(obj["hub_url"]))
        print("organization url "+ str(obj["organization_url"]))


except IOError as e:
    print("couldn't read file")