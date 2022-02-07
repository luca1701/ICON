'''
Created on 4 feb 2022

@author: serio
'''
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors._classification import KNeighborsClassifier
from sklearn.metrics import mean_absolute_error;
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from numpy import mean
from numpy import std
from sklearn import metrics
from src.complete import interaction

if __name__ == '__main__':
    
    data = pd.read_csv(r".\..\dataset\usable.csv")
    
    corr=data.corr()
    corr.style.background_gradient(cmap='coolwarm',axis=None)
    print(corr)
    #for index, row in data.iterrows():
    #    for i in range(len(data.columns)):
    #        if(row[i]== 'Yes'):
    #            row[i]=1
    #        else:
    #            row[i]=0
    #print (data.head())
    
    #data.to_csv(r'.\..\dataset\usable.csv', index=False)
    
    #divido il dataset in dati da usare per addestarre(x), e dati da predire(y)
    y = data.Result
    x = data.drop('Result', axis=1)
    #definisco che sia x che y sono interi
    y=y.astype('int')
    x=x.astype('int')
    
    #prepare the cross-validation procedure
    cv = KFold(n_splits=10, random_state=1, shuffle=True)
    # create model
    model = KNeighborsClassifier(10)
    # evaluate model
    scores = cross_val_score(model, x, y, scoring='accuracy', cv=cv, n_jobs=-1)
    # report performance
    print('Accuratezza: %f con deviazione di +/- (%.3f)' % (mean(scores), std(scores)))
    
    #divido x e y in modo da avere una parte per il training e una per il test
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)
    
    #qui il modello apprende da solo
    #model = KNeighborsClassifier(10)
    model.fit(x_train, y_train)
    #effettuo predizione sui dati
    p_train = model.predict(x_train)#p_train contiene le predizioni(y) sui dati x di training
    p_test = model.predict(x_test)#p_test contiene le predizioni(y) sui dati x di test
      
    #calcolo accuratezza del sistema
    print(f'L\'accuratezza reale sulle predizioni fatte e\' di {metrics.balanced_accuracy_score(y_test, p_test)}')
    
    #calcolo errori
    mae_train = mean_absolute_error(y_train, p_train)
    mae_test = mean_absolute_error(y_test, p_test)
    
    print('MAE test', mae_test)
    print('MAE train', mae_train)
    
    us = interaction()
    ris = us.getValues(data.columns)
            
    for index, row in ris.iterrows():
        if(row[0]== 'Yes'):
            row[0]=1
        else:
            row[0]=0
    ris = ris.T
    ris=ris.astype('int')   
    p = model.predict(ris)
    print(f'prediction->{p[0]}')
pass