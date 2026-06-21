#1/bin/sh

check_server()
{
name=$1
status=$2
if [ $status = "running" ]; then
    echo "$1 is $2 ✅ "
else 
    echo " $1 is $2 ❌ "
fi    
}

for line in $(cat servers.txt); do
    name=$(echo $line | cut -d',' -f1)
    status=$(echo $line | cut -d',' -f2)
    check_server $name $status
done