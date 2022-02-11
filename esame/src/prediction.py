'''
@author: Serio & Nasca
'''

#from src.model_performance import accuracy, MAE, kfold
import pandas as pd
from warnings import simplefilter
from sklearn.model_selection import train_test_split
from sklearn.tree._classes import DecisionTreeClassifier
from src.questions import interaction
from src.prolog import ospedalization

if __name__ == '__main__':
    simplefilter(action='ignore', category=FutureWarning)
    
    data = pd.read_csv(r".\..\dataset\usable.csv")
    
    y = data.Result
    x = data.drop('Result', axis=1)

    y=y.astype('int')
    x=x.astype('int')
    
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
    
    model = DecisionTreeClassifier()
    
    model.fit(x_train, y_train)    
    p_train = model.predict(x_train)
    p_test = model.predict(x_test)

    #accuracy(y_train, y_test, p_train, p_test)
    #MAE(y_train, y_test, p_train, p_test)
    #kfold(model, x, y)
    
    us = interaction()
    ris = us.getValues()
    ospedalization(ris)
    
    for index, row in ris.iterrows():
        if(row[0] == 'Yes'):
            row[0]=1
        else:
            row[0]=0
    ris = ris.T
    
    p = model.predict(ris)
    if(p[0] == 1):
        print("\nSecondo le prestazioni del sistema e le risposta date, l'utente potrebbe essere affetto da Covid-19")
    else:
        print("\nSecondo le prestazioni del sistema e le risposta date, l'utente non e' affetto da Covid-19")
        
pass