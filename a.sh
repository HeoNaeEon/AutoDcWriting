while true; do
 python dc.py
 value=`cat b.txt`
 if [ "$value" = "0" ]
 then
  break
 fi
 sleep 1 
done
