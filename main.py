'''
Created on 30 dic 2021

@author: serio
'''
import csv
import pandas as pd
from _io import open
from tabulate import tabulate
from wsgiref import headers
import warnings

if __name__ == '__main__':
    warnings.filterwarnings("ignore")

    #csv = csv.reader(open('Dataset_1.csv'), delimiter=',')
    csv = pd.read_csv('Dataset_1.csv', delimiter=',')
    
    sesso_csv = open("sesso.txt","r").read().split("\n")
    sesso_mod = []
    for element in sesso_csv:
        sesso_mod.append(element.split(":"))
        
    scuole_csv = open("scuole.txt","r").read().split("\n")
    scuole_mod = []
    for element in scuole_csv:
        scuole_mod.append(element.split(":"))
        
    interessi_csv = open("interessi.txt","r").read().split("\n")
    interessi_mod = []
    for element in interessi_csv:
        interessi_mod.append(element.split(":"))
    
    corsi_csv = open("corsi.txt", "r").read().split("\n")
    corsi_mod = []
    for element in corsi_csv:
        corsi_mod.append(element.split(":"))
    '''
    questo va bene ma per dataset come lista di elementi
    line = 0
    dataset = []
    for row in csv:
        if(line == 0):
            line +=1
            columns = row
        else:
            dataset.append(row)
    

    for row in printable:
        print(row)
        for line in sesso_mod:
            if(row[0]==line[0]):
                row[0]=line[1]
        for line in scuole_mod:
            if(row[2]==line[0]):
                row[2]=line[1]     
        for line in interessi_mod:
            if(row[4]==line[0]):
                row[4]=line[1]    
            if(row[5]==line[0]):
                row[5]=line[1]     
        for line in corsi_mod:
            if(row[6]==line[0]):
                row[6]=line[1]

    #print(tabulate(printable, headers=columns))
    '''
    y = csv['corso_laurea']
    x = csv.drop('corso_laurea', axis=1)
    from sklearn.model_selection import train_test_split
    x_train,x_test,y_train,y_test=train_test_split(x,y)
    
    from sklearn.naive_bayes import GaussianNB
    gnb = GaussianNB()
    gnb.fit(x_train,y_train)
    
    print("Naive Bayes Classifier")
    y_pred=gnb.predict(x_test)
    from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
    from sklearn.metrics import r2_score
    from sklearn.metrics import mean_squared_error
    print("Classification Report is:\n",classification_report(y_test,y_pred))
    print("Confusion Matrix:\n",confusion_matrix(y_test,y_pred))
    print("Training Score:\n",gnb.score(x_train,y_train)*100)
    
    pass