'''
Created on 9 feb 2022

@author: serio
'''
import pytholog as pl

def ospedalization(ris):
    kb = pl.KnowledgeBase('ospedalization')
    kb([f"symp(asma,{ris[0][4].lower()})",
        f"symp(breathproblem,{ris[0][0].lower()})",
        f"symp(sorethroat,{ris[0][3].lower()})",
        f"symp(drycough,{ris[0][2].lower()})",
        f"affect1(S) :- symp(asma, S)",
        f"affect2(S) :- symp(breathproblem, S)",
        f"affect3(S) :- symp(sorethroat, S)",
        f"affect4(S) :- symp(drycough, S)",        
        f"several(S1) :- affect1(asma,S1), affect2(breathproblem,S1) , affect4(drycough, S1)",
        f"several2(S2) :- affect1(asma,S2), affect2(breathproblem,S2), affect3(sorethroat,S2)"
        ])
    #several1 e several2 non funzionano e non capisco perchè, leho provate tutte!
    #perciò uso le affect per capire se hanno dei sintomi. Sono più generali rispetto ai symptoms perchè-
    #includono l'uso di variabili!
    if((kb.query(pl.Expr(f"affect1(yes)"))[0] == 'Yes' and
    kb.query(pl.Expr(f"affect2(yes)"))[0] == 'Yes') and
    (kb.query(pl.Expr(f"affect3(yes)"))[0] == 'Yes' or
    kb.query(pl.Expr(f"affect4(yes)"))[0] == 'Yes')):
        print("Si consiglia la va visita da uno specialista!")
