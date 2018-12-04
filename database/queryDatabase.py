import pandas as pd
from sqlalchemy import create_engine

#engine = create_engine('postgresql://jverhoff:john@localhost:5432/fecInfo')
engine = create_engine('postgresql://databasemaster:Purdue2020!@mydbinstance.cfaohzw41elj.us-east-2.rds.amazonaws.com:5432/databasemaster')


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

def getTopTenOverall():
    df = pd.read_sql_query("SELECT cand_name, total_receipt, cand_office_st, cand_party_affiliation FROM candidate_table ORDER BY total_receipt DESC limit 10;", engine)
    #print(df)
    topTen = []
    for row in df.itertuples():
        topTen.append((row[1],row[2], row[3], row[4]))
   # print(topTen)
    return topTen

def getTopTenState(state):
    df = pd.read_sql_query("SELECT cand_name, total_receipt, cand_party_affiliation FROM candidate_table WHERE cand_office_st='%s' ORDER BY total_receipt DESC limit 10;" % state, engine)
    #print(df)
    topTenState = []
    for row in df.itertuples():
        topTenState.append((row[1], row[2], state, row[3]))
    #print(topTenState)
    return topTenState

def getWarchestOverall():
    df = pd.read_sql_query("SELECT cand_name, cash_on_hand_cop, cand_office_st, cand_party_affiliation FROM candidate_table WHERE cash_on_hand_cop < 10000000000 ORDER BY cash_on_hand_cop DESC limit 10;", engine)
    #print(df)
    topTen = []
    for row in df.itertuples():
        topTen.append((row[1], row[2], row[3], row[4]))
    #print(topTen)
    return(topTen)

def getWarchestState(state):
    df = pd.read_sql_query("SELECT cand_name, cash_on_hand_cop, cand_party_affiliation FROM candidate_table WHERE cash_on_hand_cop < 10000000000000 AND cand_office_st='%s' ORDER BY cash_on_hand_cop DESC limit 10;" % state, engine)
    #print(df)
    topTen = []
    for row in df.itertuples():
        topTen.append((row[1], row[2], state, row[3]))
    #print(topTen)
    return topTen

def listOfContributions():
    df = pd.read_sql_query("SELECT total_receipt FROM candidate_table where total_receipt > 0;", engine)
    lOfCon = []
    for row in df.itertuples():
        lOfCon.append(row[1])
    #print(lOfCon)
    return lOfCon

def listOfWarchests():
    df = pd.read_sql_query("SELECT cash_on_hand_cop FROM candidate_table WHERE cash_on_hand_cop < 100000000000 AND cash_on_hand_cop > 0;", engine)
    lOfWar = []
    for row in df.itertuples():
        lOfWar.append(row[1])
    #print(lOfWar)
    return lOfWar

def getStateData(state):
    tC = state_total(state)
    demP = party_over_state(state, 'DEM', tC)
    repP = party_over_state(state, 'REP', tC)
    otherP = 100 - demP - repP
    return (tC, demP, repP, otherP)



def totDonByParty(state, party):
    df = pd.read_sql_query("SELECT candidate_table.cand_name, contribution_table.transaction_amt FROM contribution_table inner join com_table on contribution_table.cmte_id = com_table.cmte_id inner join candidate_table on com_table.cand_id = candidate_table.cand_id WHERE contribution_table.state='%s' AND candidate_table.cand_party_affiliation='%s' ORDER BY contribution_table.transaction_amt DESC;" %(state, party) , engine)
    print(df)
