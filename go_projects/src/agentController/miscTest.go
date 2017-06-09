package main

import (
     
    "agentUtil"
    "fmt"
    "fileUtil"
)

func main() {
    Handle_RSAKey();
}



func Handle_RSAKey(){
  usrLoginName := "test101" 
  path :=  "/tmp/"+usrLoginName+"_id_rsa"

  agentUtil.ExecComand("rm -rf "+path, "UserHandler.Userdel() L87");
  agentUtil.ExecComand("rm -rf "+path+".pub", "UserHandler.Userdel() L87");



  cmd := "ssh-keygen -t rsa -N \"\" -f /tmp/"+usrLoginName+"_id_rsa"
  agentUtil.ExecComand(cmd, "UserHandler.Userdel() L87");


 // fmt.Println("Status = : ",status)


  privKey := fileUtil.ReadFile(path, false) 
 // fmt.Println("\n----------------------------------------------------------------------\n")
   fmt.Println(privKey)


  pubKey := fileUtil.ReadFile(path+".pub", false) 
  fmt.Println("This is public key = :\n",pubKey)

  to := "piyushcantata@gmail.com"
  cmd = "cat /tmp/test101_id_rsa.pub | mail -s \"Your generated public key\" "+to
  status := agentUtil.ExecComand(cmd, "UserHandler.Userdel() L87");

  msg := "Status of Mail sending to "+to + " is = : "+status
  fmt.Println(msg)

}

