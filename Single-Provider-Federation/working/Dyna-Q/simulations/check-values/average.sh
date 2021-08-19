
#!/bin/bash
for i in $(seq 0 1 15)
do
	episode=$((i * 300 + 100))
	cat res.out | grep "QL-20   $episode " | gawk 'BEGIN{FS="("} {print $2}' | gawk 'BEGIN{FS=")"} {print $1}' | gawk 'BEGIN{FS=","} {print $1" "$2" "$3}' | gawk 'BEGIN{c=0; s1=0; s2=0; s3=0} {c++; s1+=$1; s2+=$2; s3+=$3} END{print s1/c" "s2/c" "s3/c}'
done


