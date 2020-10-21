BEGIN{
	FS="="; 
	print "{ \"x_label\":\"" x_label "\",";
	print "\"y_label\":\"" y_label "\",";
	print "\"results\":["; 
	cnt = 0
} 

{
	if(length($0) > 2){
		cnt++; 
		if(cnt == 1) 
			print "{ \"x\":" $2","; 
		else if (cnt == 2) 
			print "\"DP_05\":" $2 ","; 
		else if (cnt == 3) 
			print "\"DP_30\":" $2 ","; 
		else if (cnt == 4) 
			print "\"DP_60\":" $2 ","; 
		else if (cnt == 5) 
			print "\"DP_95\":" $2 ","; 
		else if (cnt == 6) 
			print "\"QL-Dynamic\":" $2 ","; 
		else if (cnt == 7) {
			print "\"QL-Static\":" $2 "},"; 
			cnt = 0
		}
	}
} 

END{
	print "]}"
}

