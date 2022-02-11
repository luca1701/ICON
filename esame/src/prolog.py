'''
@author: Serio & Nasca
'''

import pytholog as pl

def ospedalization(ris):
    kb = pl.KnowledgeBase('ospedalization')
    
    kb([f"symp(asma,{ris[0][4].lower()})",
        f"symp(breathproblem,{ris[0][0].lower()})",
        f"symp(sorethroat,{ris[0][3].lower()})",
        f"symp(drycough,{ris[0][2].lower()})",
        "several(S) :- symp(asma, S), symp(breathproblem, S), symp(drycough, S)",
        "several(S) :- symp(asma, S), symp(breathproblem, S), symp(sorethroat, S)",
        ])

    if(kb.query(pl.Expr(f"several(yes)"))[0] == 'Yes'):
        print("\nSi consiglia la visita da uno specialista!")