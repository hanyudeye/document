#!/usr/bin/env bash

for ((i=0;i<4;i++))
do
    touch $i.sh
    echo "#!/usr/bin/env bash" > $i.sh
    chmod 764 $i.sh
done
