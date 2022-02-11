'''
@author: Serio & Nasca
'''

from sklearn import metrics
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import cross_val_score
from numpy import mean, std
from sklearn.model_selection._split import KFold

def accuracy(y_train, y_test, p_train, p_test):
    print(f'L\'accuratezza sulle predizioni fatte in fase di apprendimento e\' di {metrics.roc_auc_score(y_train, p_train)}')

    print(f'L\'accuratezza sulle predizioni fatte in fase di test e\' di {metrics.roc_auc_score(y_test, p_test)}\n')

def MAE(y_train, y_test, p_train, p_test):
    print("Mean Absolute Error")
    print(f'MAE train {mean_absolute_error(y_train, p_train)}')
    print(f'MAE test {mean_absolute_error(y_test, p_test)}\n')

def kfold(model,x, y):
    cv = KFold(n_splits=10,  shuffle=True)

    scores = cross_val_score(model, x, y, scoring='roc_auc', cv=cv, n_jobs=-1)

    print(f'Accuratezza media dei k-fold e\': %f con deviazione di +/- (%.3f)\n' % (mean(scores), std(scores)))
    
    
    
    