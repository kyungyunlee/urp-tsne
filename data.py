import pymongo
import ssl
import numpy as Math
from bson.objectid import ObjectId

client = pymongo.MongoClient(
        'mongodb://beethoven:choral@143.248.249.215:38128/test_db',
        ssl=True,
        ssl_keyfile='/etc/ssl/mongodb.pem',
        ssl_cert_reqs=ssl.CERT_NONE)

print(client)

txtfile = Math.loadtxt("3dpositionsMTT.txt")
txtfile_id = Math.loadtxt("songid.txt", dtype='str')

db = client.test_db
count = db.testcollection.count()

# write the 'song'(=average) values of each of the 50 tags for each song
# for i in range (count):
#   for key in db.testcollection.find()[i]['tags']['MTT']:
#     txtfile.write(str(db.testcollection.find()[i]['tags']['MTT'][key]['song'])+' ')
#   txtfile.write('\n')

# write the id(=label) of each song
# for i in range (count):
#     if(str(db.testcollection.find()[i]['melon_title_id'])==""):
#       txtfile.write('000000'+str(i)+'\n')
#     else:
#       txtfile.write(str(db.testcollection.find()[i]['melon_title_id'])+'\n')

# txtfile.close()

# update db
for i in range(count):
  db.testcollection.update({'_id' : ObjectId(str(txtfile_id[i]))},
    {"$set" :
      {"MTT-TSNE" : [float(txtfile[i][0]), float(txtfile[i][1]), float(txtfile[i][2])]
    }})

print("successfully connected!")