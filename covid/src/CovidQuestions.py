'''
Created on 5 feb 2022

@author: nasca
'''
 
#Si usa se voglio usare queste funzioni in altri moduli(main o class)
#if __name__ == '__main__':
#    pass
import User as User

print("Benvenuto nel sistema per predire se sei affetto dal virus SARS-CoV-2\n\
Per capire cio' vi faremo una serie di domande sui sintomi che potreste avere\n\
Vi preghiamo di rispondere con la massima sincerita'\n\
Grazie\n")

user = User.User()

print('Hai problemi di respirazione? ')
user.setBreathingProblem(input(''))

print("Hai febbre?")
user.setFever(input(''))

print("Hai tosse secca?")
user.setDryCought(input(''))

print("Hai mal di gola?")
user.setSoreThroat(input(''))

print("Hai naso che cola?")
user.setRunningNose(input(''))

print("Hai asma?")
user.setAsthma(input(''))

print("Hai malattia polmonare cronica?")
user.setChronicLungDisease(input(''))

print("Hai mal di testa?")
user.setHeadache(input(''))

print("Hai malattia del cuore?")
user.setHeartDisease(input(''))

print("Hai diabete?")
user.setDiabetes(input(''))

print("Hai ipertensione?")
user.setHyperTension(input(''))

print("Hai stanchezza?")
user.setFatigue(input(''))

print("Hai problemi gastrointestinali?")
user.setGastrointestinal(input(''))

print("Hai viaggiato all'estero?")
user.setAbroadTravel(input(''))

print("Hai avuto contatti con pazienti COVID?")
user.setContactCovidPatient(input(''))

print("Hai partecipato ad un grande raduno?")
user.setAttendedLargeGathering(input(''))

print("Hai visitato posti esposti al pubblico?")
user.setVisitedPublicPlaces(input(''))

print("La tua famiglia lavora in luoghi esposti al pubblico?")
user.setFamilyPublicPlaces(input(''))

print("Indossi sempre la mascherina?")
user.setWearingMasks(input(''))

print("Sanifichi tutto cio' che compri al mercato?")
user.setSanitizationMarket(input(''))

#per cambiare possibilmente risposte nel caso in cui siano sbagliate
user.viewAnswers()
