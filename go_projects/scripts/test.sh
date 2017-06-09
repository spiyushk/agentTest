#!/bin/bash




getLinuxType(){

   filename="/tmp/linuxDistroInfo.txt" 
   cat /etc/*-release > $filename
   
   while IFS= read -r line; do

      if [[ $line == *"ID_LIKE"* ]]; then
         echo "$line"
         
     

         # Extract string after "=" i.e ID_LIKE="fedora"
         osType=${line/ID_LIKE=/""}

         osType="${osType%\"}"
         osType="${osType#\"}"
         
         echo "osType = : $osType"
         osType=$osType | tr -d ' ' # Remove space if any
         echo "osType at 22 = : $osType"
         osType=${osType,,} # Convert into lower case to isnore case insensitive comparison
         echo "osType at 24 = : $osType"

         


         
          if [[ $osType == "debian" ]]; then
             os="debian"
             fileAgentController="agent_controller_ubuntu.sh"
          fi


          if [[ $osType == "fedora" ]]; then
             os="fedora"
             fileAgentController="agent_controller.service"
          fi

        # break;

      fi

  done < "$filename"


}



os="rhel fedora"
fileAgentController="agent_controller.sh"
getLinuxType

echo "fileAgentController = : $fileAgentController"
echo "OS = : $os"

