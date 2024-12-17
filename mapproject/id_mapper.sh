#/usr/bin/env bash

curl -s https://wiki.warthunder.com/aviation?v=l 2>/dev/null > planelist.txt

unit_list=`awk -F"'"  '/WT_UnitList/ {print $2}' planelist.txt`
# combined_list=`echo $unit_list | jq '"\(.[].[0]),\(.[].[1])"'`


fullname_list=`echo $unit_list | jq '.[].[1]'`
name_list=`echo $unit_list | jq -r '.[].[0]'`

for element in $name_list
do
    # element_fullname=`echo $element | awk -F',' '{print $2}'`
    element_id=`curl -s https://wiki.warthunder.com/unit/$element 2>/dev/null | awk -F'"' '/data-feed-unit-id/ {print $8}'`
    echo "$element_id,$element"
done
