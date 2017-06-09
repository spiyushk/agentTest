#!/bin/bash


getLinuxDistro(){

   #filename="/opt/infraguard/etc/linuxDistroInfo.txt" 
   filename="/tmp/linuxDistroInfo.txt" 
   cat /etc/*-release > $filename
   
   while IFS= read -r line; do

      if [[ $line == *"ID_LIKE"* ]]; then
         echo "$line"

          if [[ $line == *"debian"* ]]; then
            os="debian"
            fileAgentController="agent_controller_ubuntu.sh"
         fi

         if [[ $line == *"rhel"* ]]; then
            os="rhel"
         fi

        break;

     fi

  done < "$filename"


}

getLinuxDistro
echo "$os"



