
import datetime              
import pingdomlib


username = 'gms@rightcloud.asia'
password = 'D~ia=7*Fm{Bz'
apikey = '2cn29ljjlmrnk92tirhkf6ux8uzyg8qv'
accountemail = 'pingdom@rightcloud.asia'
api = pingdomlib.Pingdom( username = "", password = "", apikey = "")


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

def main():
   # get_actions_alerts(request)
   print "Going to hit api..."
   username = 'gms@rightcloud.asia'
   password = 'D~ia=7*Fm{Bz'
   apikey = '2cn29ljjlmrnk92tirhkf6ux8uzyg8qv'
   accountemail = 'pingdom@rightcloud.asia'
   api = pingdomlib.Pingdom( username = "", password = "", apikey = "")
   print "Return from api..."
   print api



# difference between pingdomlib and pyngdom

#pip install pingdomlib
# sudo pip install requests 

# sudo python setup.py install

# http://stackoverflow.com/questions/17771723/pingdom-get-actions-alerts-method-returns-empty-list

#r = request.get(‘https://github.com/timeline.json’)