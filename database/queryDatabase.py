import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://databasemaster:Purdue2020!@mydbinstance.cfaohzw41elj.us-east-2.rds.amazonaws.com:5432/databasemaster')

def getNR():
    df = pd.read_sql_query("SELECT cand_name, total_receipt FROM candidate_table ORDER BY total_receipt DESC;", engine)
    print(df)

def getTopInState(state):
    df = pd.read_sql_query("SELECT cand_name, total_receipt, cand_party_affiliation FROM candidate_table WHERE cand_office_st='%s' ORDER BY total_receipt DESC;" % state, engine)
    print(df)

def state_total(state):
    df = pd.read_sql_query("SELECT total_receipt FROM candidate_table WHERE cand_office_st='%s';" % state, engine)
    stateTotal = df['total_receipt'].sum()
    #print(stateTotal)
    return stateTotal

def nationwide_total():
    df = pd.read_sql_query("SELECT total_receipt FROM candidate_table;", engine)
    nationalTotal = df['total_receipt'].sum()
    print(nationalTotal)
    return nationalTotal

def party_over_state(state, party, stateTotal):
    df = pd.read_sql_query("SELECT total_receipt FROM candidate_table WHERE cand_office_st='%s' AND cand_party_affiliation='%s';" %(state, party), engine)
    pt = df['total_receipt'].sum()
    return (100*(pt/stateTotal))

def getStateData(state):
    tC = state_total(state)
    demP = party_over_state(state, 'DEM', tC)
    repP = party_over_state(state, 'REP', tC)
    otherP = 100 - demP - repP
    return (tC, demP, repP, otherP)
