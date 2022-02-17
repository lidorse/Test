import requests
import json

class Post():
    def __init__(self,d):
        self.__dict__ = d

    def __str__(self):
        result = ''
        for k,v in self.__dict__.items():
            result += f'{(k)} = {(v)}, '
        return result

def postId(ID):
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{ID}')
    response = json.loads(response.content)
    getPostById = Post(response)
    return getPostById
