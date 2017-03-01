import pymongo
import ssl


client = pymongo.MongoClient(
        'mongodb://beethoven:choral@143.248.249.215:38128/test_db',
        ssl=True,
        ssl_keyfile='/etc/ssl/mongodb.pem',
        ssl_cert_reqs=ssl.CERT_NONE)

print(client)

txtfile = open("melontitleid.txt", "w")


db = client.test_db
count = db.testcollection.count()

# write the 'song'(=average) values of each of the 50 tags for each song
# for i in range (count):
#   for key in db.testcollection.find()[i]['tags']['MSD']:
#     txtfile.write(str(db.testcollection.find()[i]['tags']['MSD'][key]['song'])+' ')
#   txtfile.write('\n')

# write the id(=label) of each song
for i in range (count):
    if(str(db.testcollection.find()[i]['melon_title_id'])==""):
      txtfile.write('000000'+str(i)+'\n')
    else:
      txtfile.write(str(db.testcollection.find()[i]['melon_title_id'])+'\n')



txtfile.close()

print("successfully connected!")