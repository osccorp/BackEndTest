import json
import requests

def getUser(aut: str):
    if aut.isdigit():
        url='https://jsonplaceholder.typicode.com/users/'+aut
    ret="User:"
    try:
        req=requests.get(url)
        users = req.json()
        ret=json.dumps(users)
    except:
        ret = f"{aut}: Has no user info"
    return ret

def getComent(post: str):
    if post.isdigit():
        url = f"https://jsonplaceholder.typicode.com/posts/{post}/comments"
    ret = "Post:"
    try:
        req = requests.get(url)
        comments =req.json()
        ret=json.dumps(comments)
    except:
        ret = f"Post [{post}]: Has no comments"
    return ret

def getPosts(start:int = 5, size: int = 10):
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    #start=5
    #size=10
    #Function
    id=0
    user=0
    x ={}
    strJson = ""
    for i in r.json():
        if id >=start and id< start+size:
            user = i["userId"]
            comment = i["id"]
            x[comment]= i
            x[comment]["user"]=getUser(f"{user}")
            x[comment]["comments"]=getComent(f"{comment}")
            strJson = strJson + json.dumps(x[comment])
            print(f"Post: {id} / User:{user} / payload:{x}")
        id=id+1
        if id>start+size:
            break
    return x

#print(strJson)
print("Test")
print(getPosts())