#!/usr/bin/env python

import wiringpi
import subprocess
import time
import tempita

cool_temp = 35
hot_temp = 37


from subprocess import call
#wiringpi.wiringPiSetup()
wiringpi.wiringPiSetupGpio()
#wiringpi.wiringPiSetupPhys()
wiringpi.pinMode(27 , 1)
wiringpi.digitalWrite(27, 0)
tmpl=tempita.Template.from_filename ("test.mail")
state="start"
while True:
 p=subprocess.Popen(["checktemp"],stdout=subprocess.PIPE)
 (out,rr)=p.communicate()
 if p.returncode !=0:
  print 'error'
  wiringpi.digitalWrite(27, 0)
  if state !='error':
     state="error"
     mail=tmpl.substitute(subject="error",body="Error - temperature is not readable")
     p=subprocess.Popen(["sendmail","yourmail@here.com"],stdin=subprocess.PIPE)
     p.communicate(mail)
  
 else:
  if float(out) == 0:
   print 'error'
   wiringpi.digitalWrite(27, 0)
   if state !='error':
     state="error"
     mail=tmpl.substitute(subject="error",body="Error - null" +out)
     p=subprocess.Popen(["sendmail","yourmail@here.com"],stdin=subprocess.PIPE)
     p.communicate(mail)
  if float(out)  <35 and float(out) !=0:
    print 'ok'
    if state !='ok':
     state="ok"
     mail=tmpl.substitute(subject="ok",body="Back to normal state - temperature is " +out)
     p=subprocess.Popen(["sendmail","yourmail@here.com"],stdin=subprocess.PIPE)
     p.communicate(mail)
    wiringpi.digitalWrite(27, 1)

  if float(out) >37:
    print 'prehrati'
    wiringpi.digitalWrite(27, 0)
    if state !='prehrati':
     state="prehrati"
     mail=tmpl.substitute(subject="overheating",body="NOK - Overheating - temprature is " +out)
     p=subprocess.Popen(["sendmail","yourmail@here.com"],stdin=subprocess.PIPE)
     p.communicate(mail)
  if not (float(out) >37) and not (float(out) <35):
    print 'waiting'
     if state !='waiting':
     state="waiting"
     mail=tmpl.substitute(subject="waiting",body="NOK - Near overheating - temperature is " +out)
     p=subprocess.Popen(["sendmail","yourmail@here.com"],stdin=subprocess.PIPE)
     p.communicate(mail)
  
  print out
  time.sleep (1)
