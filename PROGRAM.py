new_dict={"userinfo1":{"first_name":"Ruzeena","last_name":"Bashir","address":{"city":"abc","state":"jandk"}},
"userinfo2":{"first_name":"Heeba","last_name":"Kawoosa","address":{"city":"def","state":"Delhi"}},
"userinfo3":{"first_name":"Rumaya","last_name":"Rashid","address":{"city":"ghi","state":"Banglore"}}}

for i,r in enumerate(new_dict):
    print i,r
    #print "state=%s" %new_dict[r]['address']['state']

#for i in new_dict:
 #   print new_dict[i]

for i,r in sorted(new_dict.iteritems(), key=lambda (x, y): y['address']['state']):
    print i,r
 #   print s[1]['address']






                    
  




