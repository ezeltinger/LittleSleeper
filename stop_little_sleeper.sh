pids=$(cat pid.log)
for pid in $pids
do
   echo "Stopping $pid"
   kill -15 $pid
done
rm pid.log
