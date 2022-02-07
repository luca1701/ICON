'''
Created on 5 feb 2022

@author: nasca
'''
 
#Si usa se voglio usare queste funzioni in altri moduli(main o class)
#if __name__ == '__main__':
#    pass
from src.user import User

def interaction():
    print("Benvenuto nel sistema per predire se sei affetto dal virus SARS-CoV-2\n\
    Per capire cio' vi faremo una serie di domande su patologie pregresse e sintomi che potreste avere\n\
    Vi preghiamo di rispondere con la massima sincerita'\n\
    Grazie\n")
    print("Le risposte devono essere date nei possibili seguenti modi:\n\
    ->si-s-yes-y\n\
    ->no-n")
    utente = User()
    
    while(True):
        print('Hai problemi di respirazione?')
        utente.setBreathingProblem(input(''))
        if(utente.breathingProblem.__eq__('si') or utente.breathingProblem.__eq__('s') or utente.breathingProblem.__eq__('y') or utente.breathingProblem.__eq__('yes')):
            utente.setBreathingProblem('Yes')
            break
        elif(utente.breathingProblem.__eq__('no') or utente.breathingProblem.__eq__('n')):
            utente.setBreathingProblem('No')
            break
        
    while(True): 
        print("Hai febbre?")
        utente.setFever(input(''))
        if(utente.fever.__eq__('si') or utente.fever.__eq__('s') or utente.fever.__eq__('y') or utente.fever.__eq__('yes')):
            utente.setFever('Yes')
            break
        elif(utente.fever.__eq__('no') or utente.fever.__eq__('n')):
            utente.setFever('No')
            break
    
    while(True):
        print("Hai tosse secca?")
        utente.setDryCought(input(''))
        if(utente.dryCought.__eq__('si') or utente.dryCought.__eq__('s') or utente.dryCought.__eq__('y') or utente.dryCought.__eq__('yes')):
            utente.setDryCought('Yes')
            break
        elif(utente.dryCought.__eq__('no') or utente.dryCought.__eq__('n')):
            utente.setDryCought('No')
            break
        
    while(True):
        print("Hai mal di gola?")
        utente.setSoreThroat(input(''))
        if(utente.soreThroat.__eq__('si') or utente.soreThroat.__eq__('s') or utente.soreThroat.__eq__('y') or utente.soreThroat.__eq__('yes')):
            utente.setSoreThroat('Yes')
            break
        elif(utente.soreThroat.__eq__('no') or utente.soreThroat.__eq__('n')):
            utente.setSoreThroat('No')
            break
        
    while(True):    
        print("Hai naso che cola?")
        utente.setRunningNose(input(''))
        if(utente.runningNose.__eq__('si') or utente.runningNose.__eq__('s') or utente.runningNose.__eq__('y') or utente.runningNose.__eq__('yes')):
            utente.setRunningNose('Yes')
            break
        elif(utente.runningNose.__eq__('no') or utente.runningNose.__eq__('n')):
            utente.setRunningNose('No')
            break
        
    while(True):    
        print("Hai asma?")
        utente.setAsthma(input(''))
        if(utente.asthma.__eq__('si') or utente.asthma.__eq__('s') or utente.asthma.__eq__('y') or utente.asthma.__eq__('yes')):
            utente.setAsthma('Yes')
            break
        elif(utente.asthma.__eq__('no') or utente.asthma.__eq__('n')):
            utente.setAsthma('No')
            break
        
    while(True):   
        print("Hai malattia polmonare cronica?")
        utente.setChronicLungDisease(input(''))
        if(utente.chronicLungDisease.__eq__('si') or utente.chronicLungDisease.__eq__('s') or utente.chronicLungDisease.__eq__('y') or utente.chronicLungDisease.__eq__('yes')):
            utente.setChronicLungDisease('Yes')
            break
        elif(utente.chronicLungDisease.__eq__('no') or utente.chronicLungDisease.__eq__('n')):
            utente.setChronicLungDisease('No')
            break
        
    while(True):    
        print("Hai mal di testa?")
        utente.setHeadache(input(''))
        if(utente.headache.__eq__('si') or utente.headache.__eq__('s') or utente.headache.__eq__('y') or utente.headache.__eq__('yes')):
            utente.setHeadache('Yes')
            break
        elif(utente.headache.__eq__('no') or utente.headache.__eq__('n')):
            utente.setHeadache('No')
            break
     
    while(True):    
        print("Hai malattia del cuore?")
        utente.setHeartDisease(input(''))
        if(utente.heartDisease.__eq__('si') or utente.heartDisease.__eq__('s') or utente.heartDisease.__eq__('y') or utente.heartDisease.__eq__('yes')):
            utente.setHeartDisease('Yes')
            break
        elif(utente.heartDisease.__eq__('no') or utente.heartDisease.__eq__('n')):
            utente.setHeartDisease('No')
            break
        
    while(True):
        print("Hai diabete?")
        utente.setDiabetes(input(''))
        if(utente.diabetes.__eq__('si') or utente.diabetes.__eq__('s') or utente.diabetes.__eq__('y') or utente.diabetes.__eq__('yes')):
            utente.setDiabetes('Yes')
            break
        elif(utente.diabetes.__eq__('no') or utente.diabetes.__eq__('n')):
            utente.setDiabetes('No')
            break
        
    while(True):
        print("Hai ipertensione?")
        utente.setHyperTension(input(''))
        if(utente.hyperTension.__eq__('si') or utente.hyperTension.__eq__('s') or utente.hyperTension.__eq__('y') or utente.hyperTension.__eq__('yes')):
            utente.setHyperTension('Yes')
            break
        elif(utente.hyperTension.__eq__('no') or utente.hyperTension.__eq__('n')):
            utente.setHyperTension('No')
            break
        
    while(True):
        print("Hai stanchezza?")
        utente.setFatigue(input(''))
        if(utente.fatigue.__eq__('si') or utente.fatigue.__eq__('s') or utente.fatigue.__eq__('y') or utente.fatigue.__eq__('yes')):
            utente.setFatigue('Yes')
            break
        elif(utente.fatigue.__eq__('no') or utente.fatigue.__eq__('n')):
            utente.setFatigue('No')
            break
        
    while(True):
        print("Hai problemi gastrointestinali?")
        utente.setGastrointestinal(input(''))
        if(utente.gastrointestinal.__eq__('si') or utente.gastrointestinal.__eq__('s') or utente.gastrointestinal.__eq__('y') or utente.gastrointestinal.__eq__('yes')):
            utente.setGastrointestinal('Yes')
            break
        elif(utente.gastrointestinal.__eq__('no') or utente.gastrointestinal.__eq__('n')):
            utente.setGastrointestinal('No')
            break
        
    while(True):
        print("Hai viaggiato all'estero?")
        utente.setAbroadTravel(input(''))
        if(utente.abroadTravel.__eq__('si') or utente.abroadTravel.__eq__('s') or utente.abroadTravel.__eq__('y') or utente.abroadTravel.__eq__('yes')):
            utente.setAbroadTravel('Yes')
            break
        elif(utente.abroadTravel.__eq__('no') or utente.abroadTravel.__eq__('n')):
            utente.setAbroadTravel('No')
            break
         
    while(True):
        print("Hai avuto contatti con pazienti COVID?")
        utente.setContactCovidPatient(input(''))
        if(utente.contactCovidPatient.__eq__('si') or utente.contactCovidPatient.__eq__('s') or utente.contactCovidPatient.__eq__('y') or utente.contactCovidPatient.__eq__('yes')):
            utente.setContactCovidPatient('Yes')
            break
        elif(utente.contactCovidPatient.__eq__('no') or utente.contactCovidPatient.__eq__('n')):
            utente.setContactCovidPatient('No')
            break
        
    while(True):
        print("Hai partecipato ad un grande raduno?")
        utente.setAttendedLargeGathering(input(''))
        if(utente.attendedLargeGathering.__eq__('si') or utente.attendedLargeGathering.__eq__('s') or utente.attendedLargeGathering.__eq__('y') or utente.attendedLargeGathering.__eq__('yes')):
            utente.setAttendedLargeGathering('Yes')
            break
        elif(utente.attendedLargeGathering.__eq__('no') or utente.attendedLargeGathering.__eq__('n')):
            utente.setAttendedLargeGathering('No')
            break
        
    while(True):
        print("Hai visitato posti esposti al pubblico?")
        utente.setVisitedPublicPlaces(input(''))
        if(utente.visitedPublicPlaces.__eq__('si') or utente.visitedPublicPlaces.__eq__('s') or utente.visitedPublicPlaces.__eq__('y') or utente.visitedPublicPlaces.__eq__('yes')):
            utente.setVisitedPublicPlaces('Yes')
            break
        elif(utente.visitedPublicPlaces.__eq__('no') or utente.visitedPublicPlaces.__eq__('n')):
            utente.setVisitedPublicPlaces('No')
            break
        
    while(True):
        print("La tua famiglia lavora in luoghi esposti al pubblico?")
        utente.setFamilyPublicPlaces(input(''))
        if(utente.familyPublicPlaces.__eq__('si') or utente.familyPublicPlaces.__eq__('s') or utente.familyPublicPlaces.__eq__('y') or utente.familyPublicPlaces.__eq__('yes')):
            utente.setFamilyPublicPlaces('Yes')
            break
        elif(utente.familyPublicPlaces.__eq__('no') or utente.familyPublicPlaces.__eq__('n')):
            utente.setFamilyPublicPlaces('No')
            break
        
    while(True):
        print("Indossi sempre la mascherina?")
        utente.setWearingMasks(input(''))
        if(utente.wearingMasks.__eq__('si') or utente.wearingMasks.__eq__('s') or utente.wearingMasks.__eq__('y') or utente.wearingMasks.__eq__('yes')):
            utente.setWearingMasks('Yes')
            break
        elif(utente.wearingMasks.__eq__('no') or utente.wearingMasks.__eq__('n')):
            utente.setWearingMasks('No')
            break
        
    while(True):
        print("Sanifichi tutto cio' che compri al mercato?")
        utente.setSanitizationMarket(input(''))
        if(utente.sanitizationMarket.__eq__('si') or utente.sanitizationMarket.__eq__('s') or utente.sanitizationMarket.__eq__('y') or utente.sanitizationMarket.__eq__('yes')):
            utente.setSanitizationMarket('Yes')
            break
        elif(utente.sanitizationMarket.__eq__('no') or utente.sanitizationMarket.__eq__('n')):
            utente.setSanitizationMarket('No')
            break
        
    #per cambiare possibilmente risposte nel caso in cui siano sbagliate
    #utente.viewAnswers()
    return utente