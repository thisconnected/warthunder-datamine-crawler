#/usr/bin/env bash

curl -s https://wiki.warthunder.com/aviation?v=l 2>/dev/null > planelist.txt

curl -s https://wiki.warthunder.com/helicopters?v=l 2>/dev/null > helilist.txt

curl -s https://wiki.warthunder.com/ground?v=l 2>/dev/null > groundlist.txt

curl -s https://wiki.warthunder.com/ships?v=l 2>/dev/null > shiplist.txt

curl -s https://wiki.warthunder.com/boats?v=l 2>/dev/null > boatlist.txt


for filename in FILENAMES
do

unit_list=`awk -F"'"  '/WT_UnitList/ {print $2}' $filename`
# combined_list=`echo $unit_list | jq '"\(.[].[0]),\(.[].[1])"'`


fullname_list=`echo $unit_list | jq '.[].[1]'`
name_list=`echo $unit_list | jq -r '.[].[0]'`

for element in $name_list
do
    # element_fullname=`echo $element | awk -F',' '{print $2}'`
    element_id=`curl -s https://wiki.warthunder.com/unit/$element 2>/dev/null | awk -F'"' '/data-feed-unit-id/ {print $8}'`
    echo "$element_id,$element"
done
done
