import os
import requests

def get_droplets():
    url = 'https://reqres.in/api/users?page=2'
    r = requests.get(url)
    print(r.json())
    # r = requests.get(url, headers={'Authorization':'Bearer %s' % 'access_token'})
    # droplets = r.json()
    # droplet_list = []
    # for i in range(len(droplets['droplets'])):
    #     droplet_list.append(droplets['droplets'][i])
    # return droplet_list

get_droplets()