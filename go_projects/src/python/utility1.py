#!/usr/bin/python3
from subprocess import call

import datetime              
import pingdomlib

   
class PythonUtility1:

  "This class is used to test all Python Utility Program"
  globalVariable = 15;
  app = {'passwd' : 'piyush'}
  app = ('abc')
  list = [4,5,54, 7, 'a', 'xyx', "This is a sentence"]  # instance Variable

  def __init__(self): 
    print "self.globalVariable = : ", self.globalVariable

# ---------------- Table Printing -------------------
  def printTable(self):
   self.no = 1000
   call(["clear", ""])
   "This method used to print table"
   print "\n\n ------------------------- Table Test ------------------"
   for x in range(1,5):
    val = x * self.globalVariable
    print "Table of %d is %d"%(self.globalVariable, val) 
   
   print "self.no = : %d"%(self.no) 

   print "Going to hit api..."
   username = 'gms@rightcloud.asia'
   password = 'D~ia=7*Fm{Bz'
   apikey = '2cn29ljjlmrnk92tirhkf6ux8uzyg8qv'
   accountemail = 'pingdom@rightcloud.asia'
   #api = pingdomlib.Pingdom( username = "", password = "", apikey = "")
   api = pingdomlib.Pingdom( username, password, apikey)
   print "Return from api..."
   print api

   pingdomactions=api.actions()
   print "pingdomactions=",  pingdomactions 

   return
# ---------------- List Testing -------------------
  def listTest(self):
   cntr = 0
   print "\n\n ------------------------- List Test ------------------"
   self.list[2] = 300
   for entry in self.list:
    print "list[%d] = : %s" %(cntr, entry)
    cntr += 1;

   return



  def tupleTest(self):
   "This method is for Tuple Test"
   tup1 = ('xyz', 'abc', 'c', 'd');
   cntr = 0;
   print "\n\n ------------------------- Tuple Test ------------------"
   for i in tup1:
    print "tup1[%d] = : %s >> i = : %s" %(cntr, tup1[cntr], i);
    #tup1[1] = 'ffffffffff'; Unmodifiable Tuple
    cntr += 1
   return;
 

  

  def hitApi(self):
   print "Going to hit api..."
   username = 'gms@rightcloud.asia'
   password = 'D~ia=7*Fm{Bz'
   apikey = '2cn29ljjlmrnk92tirhkf6ux8uzyg8qv'
   accountemail = 'pingdom@rightcloud.asia'
   #api = pingdomlib.Pingdom( username = "", password = "", apikey = "")
   api = pingdomlib.Pingdom( username, password, apikey)
   print "Return from api..."
   print api

   pingdomactions=api.actions()
   print "pingdomactions=",  pingdomactions

   for alert in api.alerts(limit=10):
        time = datetime.datetime.fromtimestamp(alert['time'])
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        print timestamp
        print "[%s] %s is %s" % (time, alert['name'], alert['status'])


   return

  
  def get_actions_alerts(request):

    pingdomactions=api.actions()
    print "pingdomactions=",  pingdomactions 

    for alert in api.alerts(limit=10):
        time = datetime.datetime.fromtimestamp(alert['time'])
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        print timestamp
        print "[%s] %s is %s" % (time, alert['name'], alert['status'])

    return render_to_response("base_audit_template.html") #need to render data to this page


def get_checks(request):
    pingdomchecks = api.getChecks()
    print "pingdomchecks" , pingdomchecks
    for check in pingdomchecks:
    # See pingdomlib.check documentation for information on PingdomCheck class
        if check.status != 'up':
            print check
        else :
            print "status up:" , check
    return render_to_response("base_audit_template.html")
 



#PythonUtility1().printTable()
obj = PythonUtility1()

obj.hitApi()
#obj.listTest()
#obj.tupleTest()
#obj.vermaTest()
#print "list[0] = : ", list[0], list[1],list[2],list[3], list[4], list[5], list[6];


# difference between pingdomlib and pyngdom

#pip install pingdomlib
# sudo pip install requests 

# sudo python setup.py install

# http://stackoverflow.com/questions/17771723/pingdom-get-actions-alerts-method-returns-empty-list

#r = request.get(‘https://github.com/timeline.json’)



