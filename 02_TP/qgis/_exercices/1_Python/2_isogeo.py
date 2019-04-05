# -*- coding: UTF-8 -*-

# standard lib


# 3rd party
from isogeo_pysdk import Isogeo, IsogeoUtils, __version__

######### 

print("Working with package version: {}".format(__version__))
utils = IsogeoUtils()

#print(dir(utils))
#print(help(utils))

#######

api_auth = utils.credentials_loader(r"./client_secrets.json")

# authenticate your client application
isogeo = Isogeo(client_id=api_auth.get("client_id"),
                client_secret=api_auth.get("client_secret")
                )

# get the token
token = isogeo.connect()

# add properties as attribute
isogeo.get_app_properties(token)

# set augment option on True
search = isogeo.search(token,
                       query="bar",
                       page_size=0,
                       whole_share=0,
                       augment=1)

print(search.get("total"))
print(search.get("tags"))
print(isogeo.shares_id)
