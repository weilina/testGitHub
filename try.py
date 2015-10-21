vertice_list = []

for line in bk_pmi:
uniItem = line.decode("utf-8")
	lst = uniItem.split(" ")	

	if lst[0] in wordlist == True:
		new_tp = (lst[0],lst[1])
		vertice_list.append(new_tp)
		print "Appending %s" %(lst[0].encode('utf-8'), lst[1].encode('utf-8'))
	else:
		new_tp = (lst[1],lst[0])
		vertice_list.append(new_tp)
		print "Appending %s" %(lst[1].encode('utf-8'),lst[0].encode('utf-8'))
