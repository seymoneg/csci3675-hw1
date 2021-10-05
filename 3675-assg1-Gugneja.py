/*
Seymone Gugneja

3675 assignment 1

9/14/2021
*/

#import modules
from abc import ABC, abstractmethod
import datetime

class Contact:
    
    """
    CONTACT CLASS
    * Initialize first name, last name, and telephone number
    * get_name returns name
    * get_phone returns phone number
    * toString() returns the information as a string
    """
    
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        
    def get_name(self):
        return self.name
    
    def get_phone(self):
        return self.phone
    
    def toString(self):
        return "Person name: " + self.get_name() + " " + str(self.get_phone())
        
class Event(ABC):
    """
    EVENT ABSTRACT CLASS
    * Create abstract class event with 2 subclasses appointment and meeting
    * toString() returns the information as a string
    """

    def __init__(self, contact, mtgDateTime):
        self.contact = contact
        self.mtgDateTime = mtgDateTime
  
    def toString(self):
        return "Contact: " + self.contact.toString() + ' ' + str(self.mtgDateTime)
        
class Appointment(Event):
    """
    APPOINTMENT SUBCLASS
    * Create subclass for appointment that specifies the type of appointment
    * get_type returns the type of appointment
    * toString() returns the information as a string
    """
    
    def __init__(self, contact, mtgDateTime, apptType): 
        super().__init__(contact, mtgDateTime)
        self.apptType = apptType
            
    def get_type(self):
        return self.apptType
    
    def toString(self):
        return super().toString() + '' + self.get_type()
        
class Meeting(Event):
    """
    MEETING SUBCLASS
    * Create subclass for meeting that maintains the name of attendees
    * provide toString() method, addAttendee method, and get_attendees method
    * addAttendee method adds given name to meeting's list of attendees
    * get_attendees returns list of attendee names
    * toString() returns the information as a string
    """
    
    def __init__(self, contact, mtgDateTime, apptType, attendeeNames): 
        super().__init__(contact, mtgDateTime)
        self.apptType = apptType
        self.attendeeNames = attendeeNames
        
    def addAttendee(self, person):
        self.attendeeNames.append(person)
    
    def get_attendees(self):
        return self.attendeeNames
    
    def toString(self):
        return super().toString() + '' + self.get_attendees()
    
class AppointmentBook:
    
    """
    APPOINTMENT BOOK
    * Maintain attribute that stores the list of events
    * add_event adds given event to appointment book
    * get_events_for_date returns a list of events for a given date
    """
    
    def __init__(self, eventList): 
        self.eventList = eventList
        
    def add_event(self, newEvent): 
        eventOnDate = self.get_events_for_date(newEvent.mtgDateTime)
        for i in eventOnDate:
            if newEvent.mtgDateTime == i.mtgDateTime:
                return
            
        self.eventList.append(newEvent)
    
    def get_events_for_date(self, date): 
        return [j for j in self.eventList if date.date() == j.mtgDateTime.date()]
        
def main():
    contact1 = Contact("Ashley Wilson", 7777777777)
    print(contact1.toString()+"\n")
    contact2 = Contact("Davis Black", 5555555555)
    print(contact2.toString()+"\n")

    event1 = Event(contact1, datetime.datetime(2021, 5, 12, 8, 34, 52))
    print(event1.toString()+"\n")
    event2 = Event(contact2, datetime.datetime(2021, 10, 11, 4, 20, 0))
    print(event2.toString()+"\n")

    appointment1 = Appointment(contact1, datetime.datetime(2021, 5, 12, 8, 34, 52), " Tattoo appointment\n")
    print(appointment1.toString())
    appointment2 = Appointment(contact2, datetime.datetime(2021, 7, 14, 9, 40, 10), " Movies\n")
    print(appointment2.toString())


    meeting1 = Meeting(contact1, datetime.datetime(2021, 3, 9, 8, 17, 0), " Grocery trip", " Bill Nye\n")
    print(meeting1.toString())
    meeting2 = Meeting(contact2, datetime.datetime(2021, 12, 12, 12, 20, 0), " Work", " Sarah Jane\n")
    print(meeting2.toString())

    appointmentBook = AppointmentBook([meeting1, meeting2])
    dt = datetime.datetime(2021, 12, 12, 12, 20, 0)
    efd = appointmentBook.get_events_for_date(dt)
    for x in efd:
      print(x.toString())
    
main()
