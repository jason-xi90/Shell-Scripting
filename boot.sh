#! /bin/bash



function decision_to_play(){
    echo "Would you like to play rock paper scissors? (y/n):"
    read decision
    if [[$decision == "y"]] 
    then
        python3 Rock_paper_scissors.py
    else
        echo "That's too bad, maybe next time"
    fi
}

#Cannot set up the permission with "chmod" as I am using a Windows system.


