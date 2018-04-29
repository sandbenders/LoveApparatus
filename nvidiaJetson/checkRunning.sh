#!/bin/bash
SERVICE='love_apparatus.py'
 
if ps ax | grep -v grep | grep $SERVICE > /dev/null
then
    echo "$SERVICE service running, everything is fine"
else
    echo "$SERVICE is not running"
    cd ~/Documents/loveapparatus/
    python3 love_apparatus.py
fi
