import json
from typing import Optional
import requests
from fastapi import FastAPI

app = FastAPI()

def gtallposts(idx: int):
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    pst = r.json()
    return r.json()
def getUser(aut: str):
    # si el parametro es numérico intentará obtener el usuario relacionado al post agregando el id a la URL
    if aut.isdigit():
        url='https://jsonplaceholder.typicode.com/users/'+aut
    ret="User:"
    try:
        req=requests.get(url)
        users = req.json()
        ret=str(users)
    except:
        ret = f"{aut}: Has no user info"
    return ret

def getComent(post: str):
    if post.isdigit():
        # si el parametro es numérico intentará obtener los comentarios relacionados al post agregando el id a la URL
        url = f"https://jsonplaceholder.typicode.com/posts/{post}/comments"
    ret = "Post:"
    try:
        req = requests.get(url)
        comments =req.json()
        ret=str(comments)
    except:
        ret = f"Post [{post}]: Has no comments"
    return ret

def getPosts(start:int = 5, size: int = 10):
    try:
        #Obtener la lista de publicaciones
        r = requests.get('https://jsonplaceholder.typicode.com/posts')
        id=0
        user=0
        x ={}
        strJson = ""
        #Tomar el request y convertirlo en objeto json e iteramos en los componentes
        for i in r.json():
            if id >=start and id< start+size:
                # obtenemos el user id
                user = i["userId"]
                # obtenemos el id del post para obtener los comentarios
                comment = i["id"]
                #complementamos el json del post
                x[comment]= i
                #agregamos los datos del usuario que publico el post relacionandolo con el userId
                x[comment]["user"]=getUser(f"{user}")
                #agregamos los comentarios relacionados al post relacionandolo con el id del post
                x[comment]["comments"]=getComent(f"{comment}")
                strJson = strJson + str(x[comment])
                #print(f"Post: {id} / User:{user} / payload:{x[comment]}")
            id=id+1
            # mientras haya posts disponibles seguirá generando el json
            if id>start+size:
                break
    except:
        strJson = {"error"}
    return strJson


@app.get("/")
def read_root():
    p = gtallposts(10)
    return {"posts":p}

@app.get("/posts/{start}")
def read_item(start: Optional[int] = 1, size: Optional[int] = 10):
    strJson = getPosts(start,size)
    return {strJson}


