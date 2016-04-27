__author__ = 'Juan Tellez'

from API import *



while 1:
    showMenu()
    choice = int(raw_input())

    if choice is -1:
        print" Bye..."
        break
    elif choice is 1:
        print "Your options are: Barber, Hair Stylist, Receptionist"
        val= raw_input()
        getStaffByPosition(val)
    elif choice is 2:
        print "Your options are:\n 1: Christine Rielly\n 2: Jonatan Reyes"
        val = raw_input()
        getStaffByOwner(val)
    elif choice is 3:
        print "Please enter an Appointment time (10-19) and a staff id (20-23) ex: 13:00:00, 20"
        val= raw_input()
        getClientInfo(val.split(',')[0],val.split(',')[1])
    elif choice is 4:
        print"Please enter a Hair Product Brand ex: Pantene"
        val= raw_input()
        getProductCount(val)
    elif choice is 5:
        print" Pleae enter an Appointment time (10-19) and an amount of appointments ex: 15:00:00, 3"
        val= raw_input()
        getStaffByAppointments(val.split(',')[0],int(val.split(',')[1]))
    elif choice is 6:
        print" Please enter two Appointment times, one where staff is free and other where staff is busy ex: 13:00:00, 17:00:00"
        val= raw_input()
        getStaffForEval(val.split(',')[0],val.split(',')[1])