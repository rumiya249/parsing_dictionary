new_list=[{"first_name":"Ruzeena","last_name":"Bashir","address":["abc","jandk"]},
{"first_name":"Heeba","last_name":"Kawoosa","address":["def","Delhi"]},
{"first_name":"Rumaya","last_name":"Rashid","address":["ghi","Banglore"]}]

#for i,r in enumerate(new_list):
 #   print "state=%s" %r['address'][1]
for i,r in enumerate(sorted(new_list, key=lambda r: r['address'][1])):
    print i,r 
    #print i,r












