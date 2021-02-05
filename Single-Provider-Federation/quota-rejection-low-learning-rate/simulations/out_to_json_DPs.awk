BEGIN{
	FS="="; 
	print "{ \"x_label\":\"" x_label "\",";
	print "\"y_label\":\"" y_label "\",";
	print " \"results\":["; 
	cnt = 0
	first_data = 1
} 

{
	if(length($0) > 2){
		cnt++; 
		if(cnt == 1){
		       	if (first_data == 0)
				print ","
			print "{ \"x\":" $2","; 
		}
		else if (cnt == 2) 
			print "\"greedy100\":" $2 ",";  
		else if (cnt == 3) 
			print "\"DP_01\":" $2","; 
		else if (cnt == 4) 
			print "\"DP_30\":" $2","; 
		else if (cnt == 5) 
			print "\"DP_60\":" $2","; 
		else if (cnt == 6){
			print "\"DP_99\":" $2 "}"; 
			cnt = 0
			first_data = 0
		}
	}
} 

END{
	print "]}"
}

