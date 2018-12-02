import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://jverhoff:john@localhost:5432/fecInfo')

def getNR():
    df = pd.read_sql_query("SELECT cand_name, total_receipt FROM candidate_table ORDER BY total_receipt DESC;", engine)
    print(df)

def getTopInState(state):
    df = pd.read_sql_query("SELECT cand_name, total_receipt, cand_party_affiliation FROM candidate_table WHERE cand_office_st='%s' ORDER BY total_receipt DESC;" % state, engine)
    print(df)
