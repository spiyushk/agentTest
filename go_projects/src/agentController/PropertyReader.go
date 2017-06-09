package main

import (
    "fmt"
    "stringUtil"
    "fileUtil"
    "strings" 
    
)

func ReadPropertyFile() map[string]string {
  var values, rows []string
  var propertyMap map[string]string
  propertyMap = make(map[string]string)
 
  data := fileUtil.ReadFile("/opt/infraguard/etc/agentConstants.txt", false) 
  data = strings.Replace( data, "\"","",-1) 
  rows = stringUtil.SplitData(data, "\n")
  for _, row := range rows {
    row = strings.TrimSpace(row)
    
    // Ignore row which starts with letter '#'
    if(strings.HasPrefix(row, "#")){
      continue
    }
    if(strings.Contains(row, "=")){
       values = stringUtil.SplitData(row, "=")
       propertyMap[values[0]] = values[1]
    }
  }
  if(propertyMap != nil && len(propertyMap) > 0){
    return propertyMap  
  }
  return nil
  
}

func main() {
    props := ReadPropertyFile()
    for key, val := range props {
    fmt.Println(key +" >> "+val)
    }
fmt.Println(key +" >> "+val)

}

