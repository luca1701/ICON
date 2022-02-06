'''
Created on 5 feb 2022

@author: nasca
'''
 
#Si usa se voglio usare queste funzioni in altri moduli(main o class)
#if __name__ == '__main__':
#    pass
from covid.src.User_class import *

def interaction():
    print("Benvenuto nel sistema per predire se sei affetto dal virus SARS-CoV-2\n\
    Per capire cio' vi faremo una serie di domande su patologie pregresse e sintomi che potreste avere\n\
    Vi preghiamo di rispondere con la massima sincerita'\n\
    Grazie\n")
    print("Le risposte devono essere date nei possibili seguenti modi:\n\
    ->si-s-yes-y\n\
    ->no-n")
    user = User()
    
    while(True):
        print('Hai problemi di respirazione?')
        user.setBreathingProblem(input(''))
        if(user.breathingProblem.__eq__('si') or user.breathingProblem.__eq__('s') or user.breathingProblem.__eq__('y') or user.breathingProblem.__eq__('yes')):
            user.setBreathingProblem('Yes')
            break
        elif(user.breathingProblem.__eq__('no') or user.breathingProblem.__eq__('n')):
            user.setBreathingProblem('No')
            break
        
    while(True): 
        print("Hai febbre?")
        user.setFever(input(''))
        if(user.fever.__eq__('si') or user.fever.__eq__('s') or user.fever.__eq__('y') or user.fever.__eq__('yes')):
            user.setFever('Yes')
            break
        elif(user.fever.__eq__('no') or user.fever.__eq__('n')):
            user.setFever('No')
            break
    
    while(True):
        print("Hai tosse secca?")
        user.setDryCought(input(''))
        if(user.dryCought.__eq__('si') or user.dryCought.__eq__('s') or user.dryCought.__eq__('y') or user.dryCought.__eq__('yes')):
            user.setDryCought('Yes')
            break
        elif(user.dryCought.__eq__('no') or user.dryCought.__eq__('n')):
            user.setDryCought('No')
            break
        
    while(True):
        print("Hai mal di gola?")
        user.setSoreThroat(input(''))
        if(user.soreThroat.__eq__('si') or user.soreThroat.__eq__('s') or user.soreThroat.__eq__('y') or user.soreThroat.__eq__('yes')):
            user.setSoreThroat('Yes')
            break
        elif(user.soreThroat.__eq__('no') or user.soreThroat.__eq__('n')):
            user.setSoreThroat('No')
            break
        
    while(True):    
        print("Hai naso che cola?")
        user.setRunningNose(input(''))
        if(user.runningNose.__eq__('si') or user.runningNose.__eq__('s') or user.runningNose.__eq__('y') or user.runningNose.__eq__('yes')):
            user.setRunningNose('Yes')
            break
        elif(user.runningNose.__eq__('no') or user.runningNose.__eq__('n')):
            user.setRunningNose('No')
            break
        
    while(True):    
        print("Hai asma?")
        user.setAsthma(input(''))
        if(user.asthma.__eq__('si') or user.asthma.__eq__('s') or user.asthma.__eq__('y') or user.asthma.__eq__('yes')):
            user.setAsthma('Yes')
            break
        elif(user.asthma.__eq__('no') or user.asthma.__eq__('n')):
            user.setAsthma('No')
            break
        
    while(True):   
        print("Hai malattia polmonare cronica?")
        user.setChronicLungDisease(input(''))
        if(user.chronicLungDisease.__eq__('si') or user.chronicLungDisease.__eq__('s') or user.chronicLungDisease.__eq__('y') or user.chronicLungDisease.__eq__('yes')):
            user.setChronicLungDisease('Yes')
            break
        elif(user.chronicLungDisease.__eq__('no') or user.chronicLungDisease.__eq__('n')):
            user.setChronicLungDisease('No')
            break
        
    while(True):    
        print("Hai mal di testa?")
        user.setHeadache(input(''))
        if(user.headache.__eq__('si') or user.headache.__eq__('s') or user.headache.__eq__('y') or user.headache.__eq__('yes')):
            user.setHeadache('Yes')
            break
        elif(user.headache.__eq__('no') or user.headache.__eq__('n')):
            user.setHeadache('No')
            break
     
    while(True):    
        print("Hai malattia del cuore?")
        user.setHeartDisease(input(''))
        if(user.heartDisease.__eq__('si') or user.heartDisease.__eq__('s') or user.heartDisease.__eq__('y') or user.heartDisease.__eq__('yes')):
            user.setHeartDisease('Yes')
            break
        elif(user.heartDisease.__eq__('no') or user.heartDisease.__eq__('n')):
            user.setHeartDisease('No')
            break
        
    while(True):
        print("Hai diabete?")
        user.setDiabetes(input(''))
        if(user.diabetes.__eq__('si') or user.diabetes.__eq__('s') or user.diabetes.__eq__('y') or user.diabetes.__eq__('yes')):
            user.setDiabetes('Yes')
            break
        elif(user.diabetes.__eq__('no') or user.diabetes.__eq__('n')):
            user.setDiabetes('No')
            break
        
    while(True):
        print("Hai ipertensione?")
        user.setHyperTension(input(''))
        if(user.hyperTension.__eq__('si') or user.hyperTension.__eq__('s') or user.hyperTension.__eq__('y') or user.hyperTension.__eq__('yes')):
            user.setHyperTension('Yes')
            break
        elif(user.hyperTension.__eq__('no') or user.hyperTension.__eq__('n')):
            user.setHyperTension('No')
            break
        
    while(True):
        print("Hai stanchezza?")
        user.setFatigue(input(''))
        if(user.fatigue.__eq__('si') or user.fatigue.__eq__('s') or user.fatigue.__eq__('y') or user.fatigue.__eq__('yes')):
            user.setFatigue('Yes')
            break
        elif(user.fatigue.__eq__('no') or user.fatigue.__eq__('n')):
            user.setFatigue('No')
            break
        
    while(True):
        print("Hai problemi gastrointestinali?")
        user.setGastrointestinal(input(''))
        if(user.gastrointestinal.__eq__('si') or user.gastrointestinal.__eq__('s') or user.gastrointestinal.__eq__('y') or user.gastrointestinal.__eq__('yes')):
            user.setGastrointestinal('Yes')
            break
        elif(user.gastrointestinal.__eq__('no') or user.gastrointestinal.__eq__('n')):
            user.setGastrointestinal('No')
            break
        
    while(True):
        print("Hai viaggiato all'estero?")
        user.setAbroadTravel(input(''))
        if(user.abroadTravel.__eq__('si') or user.abroadTravel.__eq__('s') or user.abroadTravel.__eq__('y') or user.abroadTravel.__eq__('yes')):
            user.setAbroadTravel('Yes')
            break
        elif(user.abroadTravel.__eq__('no') or user.abroadTravel.__eq__('n')):
            user.setAbroadTravel('No')
            break
         
    while(True):
        print("Hai avuto contatti con pazienti COVID?")
        user.setContactCovidPatient(input(''))
        if(user.contactCovidPatient.__eq__('si') or user.contactCovidPatient.__eq__('s') or user.contactCovidPatient.__eq__('y') or user.contactCovidPatient.__eq__('yes')):
            user.setContactCovidPatient('Yes')
            break
        elif(user.contactCovidPatient.__eq__('no') or user.contactCovidPatient.__eq__('n')):
            user.setContactCovidPatient('No')
            break
        
    while(True):
        print("Hai partecipato ad un grande raduno?")
        user.setAttendedLargeGathering(input(''))
        if(user.attendedLargeGathering.__eq__('si') or user.attendedLargeGathering.__eq__('s') or user.attendedLargeGathering.__eq__('y') or user.attendedLargeGathering.__eq__('yes')):
            user.setAttendedLargeGathering('Yes')
            break
        elif(user.attendedLargeGathering.__eq__('no') or user.attendedLargeGathering.__eq__('n')):
            user.setAttendedLargeGathering('No')
            break
        
    while(True):
        print("Hai visitato posti esposti al pubblico?")
        user.setVisitedPublicPlaces(input(''))
        if(user.visitedPublicPlaces.__eq__('si') or user.visitedPublicPlaces.__eq__('s') or user.visitedPublicPlaces.__eq__('y') or user.visitedPublicPlaces.__eq__('yes')):
            user.setVisitedPublicPlaces('Yes')
            break
        elif(user.visitedPublicPlaces.__eq__('no') or user.visitedPublicPlaces.__eq__('n')):
            user.setVisitedPublicPlaces('No')
            break
        
    while(True):
        print("La tua famiglia lavora in luoghi esposti al pubblico?")
        user.setFamilyPublicPlaces(input(''))
        if(user.familyPublicPlaces.__eq__('si') or user.familyPublicPlaces.__eq__('s') or user.familyPublicPlaces.__eq__('y') or user.familyPublicPlaces.__eq__('yes')):
            user.setFamilyPublicPlaces('Yes')
            break
        elif(user.familyPublicPlaces.__eq__('no') or user.familyPublicPlaces.__eq__('n')):
            user.setFamilyPublicPlaces('No')
            break
        
    while(True):
        print("Indossi sempre la mascherina?")
        user.setWearingMasks(input(''))
        if(user.wearingMasks.__eq__('si') or user.wearingMasks.__eq__('s') or user.wearingMasks.__eq__('y') or user.wearingMasks.__eq__('yes')):
            user.setWearingMasks('Yes')
            break
        elif(user.wearingMasks.__eq__('no') or user.wearingMasks.__eq__('n')):
            user.setWearingMasks('No')
            break
        
    while(True):
        print("Sanifichi tutto cio' che compri al mercato?")
        user.setSanitizationMarket(input(''))
        if(user.sanitizationMarket.__eq__('si') or user.sanitizationMarket.__eq__('s') or user.sanitizationMarket.__eq__('y') or user.sanitizationMarket.__eq__('yes')):
            user.setSanitizationMarket('Yes')
            break
        elif(user.sanitizationMarket.__eq__('no') or user.sanitizationMarket.__eq__('n')):
            user.setSanitizationMarket('No')
            break
        
    #per cambiare possibilmente risposte nel caso in cui siano sbagliate
    #user.viewAnswers()
    return user