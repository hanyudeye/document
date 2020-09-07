spin () {
    rotations=3
    delay=0.1
    for i in `seq 0 $rotations`; do
        for char in '|' '/' '-' '\'; do
            #'# inserted to correct broken syntax highlighting
            echo -n $char
            sleep $delay
            printf "\b"
        done
    done
}

spin
