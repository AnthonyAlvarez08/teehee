#!/usr/bin/bash
output=outputfile.txt
# early experiment in the computer breaking game, will make a million files
b="why hello there my dude"
mkdir ~/desktop/thing
cd ~/desktop/thing

# write stuff to file
echo $b >> $output
cat $output
for ((i = 0; i < 1000000; i++)); do
    ha=file$i.txt
    echo $i >> $ha
done

read n
