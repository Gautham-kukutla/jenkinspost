#!/bin/bash
echo "entered shell script"
if [ -e "changes.txt" ]
then
  echo "changes done"
  rm changes.txt
  git push https://${GIT_USERNAME}:${GIT_PASSWORD}@github.com/Gautham-kukutla/pythongit2.git
 #git push 'https://github.com/Gautham-kukutla/pythongit2.git'
#git push origin main
#git push 'git@github.com:Gautham-kukutla/pythongit2.git'
fi
