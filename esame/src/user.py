'''
@author: Serio & Nasca
'''

import pandas as pd

class User(object):

    def __init__(self):
        self.breathingProblem = "No"
        self.fever = "No"
        self.dryCought = "No"
        self.soreThroat = "No"
        self.asthma = "No"
        self.heartDisease = "No"
        self.diabetes = "No"
        self.hyperTension = "No"
        self.abroadTravel = "No"
        self.contactCovidPatient = "No"
        self.attendedLargeGathering = "No"
        self.visitedPublicPlaces = "No"
        self.familyPublicPlaces = "No"
        
    def getValues(self):
        df = pd.DataFrame.from_dict(vars(self), orient='index', dtype='string')
        return df

    def setBreathingProblem(self, val):
        self.breathingProblem = val
     
    def setFever(self, val):
        self.fever =val   
      
    def setAbroadTravel(self, val):
        self.abroadTravel =val 
        
    def setAsthma(self, val):
        self.asthma =val     
        
    def setAttendedLargeGathering(self, val):
        self.attendedLargeGathering =val 
        
    def setContactCovidPatient(self, val):
        self.contactCovidPatient =val 
        
    def setDiabetes(self, val):
        self.diabetes =val 
        
    def setDryCought(self, val):
        self.dryCought =val 
        
    def setFamilyPublicPlaces(self, val):
        self.familyPublicPlaces =val 
        
    def setHeartDisease(self, val):
        self.heartDisease =val 
        
    def setHyperTension(self, val):
        self.hyperTension =val 
       
    def setSoreThroat(self, val):
        self.soreThroat =val  
        
    def setVisitedPublicPlaces(self, val):
        self.visitedPublicPlaces =val