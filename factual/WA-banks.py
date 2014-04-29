#!/usr/bin/python

#
#  simple python script to READ data from Factual API
#
#
#

from factual import Factual


KEY = "nW0WeB8bzGHuuk9cZ8F0wHDFEnzENtSclFqiwoez"
SECRET = "BUYSzUSKNsMrgM5dc6lB9C8DQdpBGMRn9trbLduj"

#
# http://api.v3.factual.com/t/places?filters={"name":"Stand"}&geo={"$circle":{"$center":[34.06018, -118.41835],"$meters": 5000}}
#

#
# http://www.factual.com/data/t/places#filters={"$and":[{"country":{"$eq":"US"}},{"region":{"$eq":"WA"}},{"category_labels":{"$eq":"[%5C"SERVICES+AND+SUPPLIES%5C",%5C"FINANCIAL%5C",%5C"BANKING+AND+FINANCE%5C"]"}}]}
#

def main():
    factual = Factual(KEY, SECRET)
    
    table = factual.table('places')
    
    # q1 = table.search("sushi Santa Monica")
    # print q1.data()[1]
    # print q1.get_url()
    
    q2 = table.select("longitude,latitude,website").filters({'category_ids':{'$includes':218}, 'region': "WA", 'locality': "SEATTLE"}).limit(50)
    print q2.data()
  
if __name__ == '__main__':
  main()