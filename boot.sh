#! /bin/bash



function decision_to_play(){
    echo "Would you like to play rock paper scissors? (y/n):"
    read decision
    while [[$decision == "y"]] 
    do
        python3 Rock_paper_scissors.py
    done
    
    echo "That's too bad, maybe next time"
    
    fi
}



