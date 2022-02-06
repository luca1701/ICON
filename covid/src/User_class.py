'''
Created on 5 feb 2022

@author: nasca
'''
import pandas as pd

class User(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.breathingProblem = "No"
        self.fever = "No"
        self.dryCought = "No"
        self.soreThroat = "No"
        self.runningNose = "No"
        self.asthma = "no"
        self.chronicLungDisease = "No"
        self.headache = "No"
        self.heartDisease = "No"
        self.diabetes = "No"
        self.hyperTension = "No"
        self.fatigue = "No"
        self.gastrointestinal = "No"
        self.abroadTravel = "No"
        self.contactCovidPatient = "No"
        self.attendedLargeGathering = "No"
        self.visitedPublicPlaces = "No"
        self.familyPublicPlaces = "No"
        self.wearingMasks = "No"
        self.sanitizationMarket = "No"
        #self.prediction = "No"
        #self.result = "No"
        
        
    def viewAnswers(self):
        print("\n1.Hai problemi di respirazione?", self.breathingProblem,"\n2.Hai febbre? ", self.fever, "\n\
        3.Hai tosse secca? ", self.dryCought, "\n4.Hai mal di gola? ", self.soreThroat, "\n\
        5.Hai naso che cola? ", self.runningNose, "\n6.Hai asma? ", self.asthma, "\n7.Hai malattia polmonare cronica? ",
        self.chronicLungDisease, "\n8.Hai mal di testa? ", self.headache, "\n9.Hai malattia del cuore? ", self.heartDisease,
        "\n10.Hai diabete? ", self.diabetes, "\n11.Hai ipertensione? ", self.hyperTension,
        "\n12.Hai stanchezza? ", self.fatigue, "\n13.Hai problemi gastrointestinali? ", self.gastrointestinal,
        "\n14.Hai viaggiato all'estero? ", self.abroadTravel, "\n15.Hai avuto contatti con pazienti COVID?",
        self.contactCovidPatient, "\n16.Hai partecipato ad un grande raduno? ", self.attendedLargeGathering,
        "\n17.Hai visitato posti esposti al pubblico? ", self.visitedPublicPlaces, "\n18.La tua famiglia \
        lavora in luoghi esposti al pubblico?", self.familyPublicPlaces, "\n19.Indossi sempre la mascherina? ",
        self.wearingMasks, "\n20.Sanifichi tutto cio' che compri al mercato? ", self.sanitizationMarket)
    
    def getValues(self, col):
        '''
        array = []
        
        for i in dict.keys():
            array.append(dict.get(i))
        '''
        dict = vars(self)
        #df = pd.DataFrame.from_dict(dict, orient='columns')
        df = pd.DataFrame.from_dict(dict, orient='index', dtype='string')
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
        
    def setChronicLungDisease(self, val):
        self.chronicLungDisease =val 
        
    def setContactCovidPatient(self, val):
        self.contactCovidPatient =val 
        
    def setDiabetes(self, val):
        self.diabetes =val 
        
    def setDryCought(self, val):
        self.dryCought =val 
        
    def setFamilyPublicPlaces(self, val):
        self.familyPublicPlaces =val 
        
    def setFatigue(self, val):
        self.fatigue =val 
        
    def setGastrointestinal(self, val):
        self.gastrointestinal =val 
        
    def setHeadache(self, val):
        self.headache =val 
        
    def setHeartDisease(self, val):
        self.heartDisease =val 
        
    def setHyperTension(self, val):
        self.hyperTension =val 
        
    def setPrediction(self, val):
        self.prediction =val 
        
    def setResult(self, val):
        self.result =val 
        
    def setRunningNose(self, val):
        self.runningNose =val 
        
    def setSanitizationMarket(self, val):
        self.sanitizationMarket =val 
       
    def setSoreThroat(self, val):
        self.soreThroat =val  
        
    def setWearingMasks(self, val):
        self.wearingMasks =val  
        
    def setVisitedPublicPlaces(self, val):
        self.visitedPublicPlaces =val