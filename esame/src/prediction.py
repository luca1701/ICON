'''
Created on 4 feb 2022

@author: serio
'''
from src.model_performance import accuracy, MAE, kfold
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree._classes import DecisionTreeClassifier
from src.complete import interaction
import seaborn as sns
import matplotlib.pyplot as plt
from src.prolog import ospedalization

if __name__ == '__main__':
    
    data = pd.read_csv(r".\..\dataset\usable.csv")
        
    data=data.drop('Wearing Masks',axis=1)
    data=data.drop('Sanitization from Market',axis=1)
    
    
    data=data.drop('Running Nose',axis=1)
    data=data.drop('Chronic Lung Disease',axis=1)
    data=data.drop('Headache',axis=1)
    data=data.drop('Fatigue ',axis=1)
    data=data.drop('Gastrointestinal ',axis=1)
    #data.to_csv(r".\..\dataset\usable.csv", index=False)

    #corr=data.corr().round(2)
    #corr.style.background_gradient(cmap='coolwarm',axis=None)
    #sns.heatmap(corr, annot=True, vmax=1, vmin=-1, center=0, cmap='vlag')
    #plt.show()
    
    
    
    #for index, row in data.iterrows():
    #    for i in range(len(data.columns)):
    #        if(row[i]== 'Yes'):
    #            row[i]=1
    #        else:
    #            row[i]=0
    
    #data.to_csv(r'.\..\dataset\usable.csv', index=False)
    
    #divido il dataset in dati da usare per addestarre(x), e dati da predire(y)
    y = data.Result
    x = data.drop('Result', axis=1)

    #definisco che sia x che y sono interi
    y=y.astype('int')
    x=x.astype('int')
    
    #divido x e y in modo da avere una parte per il training e una per il test
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)
    
    #qui il modello apprende da solo
    model = DecisionTreeClassifier()
    #effettuo predizione sui dati
    model.fit(x_train, y_train)    
    #p_train contiene le predizioni(y) sui dati x di training
    p_train = model.predict(x_train)
    #p_test contiene le predizioni(y) sui dati x di test
    p_test = model.predict(x_test)
    
    #accuracy(y_train, y_test, p_train, p_test)
    #MAE(y_train, y_test, p_train, p_test)
    #kfold(model, x, y)
    
    us = interaction()
    ris = us.getValues()
    print("\n\n")
    ospedalization(ris)
    
    for index, row in ris.iterrows():
        if(row[0] == 'Yes'):
            row[0]=1
        else:
            row[0]=0
    ris = ris.T
    ris=ris.astype('int')   
    p = model.predict(ris)
    if(p[0] == 1):
        print("Secondo le prestazioni del sistema e le risposta date, l'utente e' affetto da Covid-19")
    else:
        print("Secondo le prestazioni del sistema e le risposta date, l'utente non e' affetto da Covid-19")
    print(f'prediction->{round(p[0])}')

pass
