import pandas as pd
df = pd.read_csv('candidate_summary_2018.csv')
df.columns = [c.lower() for c in df.columns]

from sqlalchemy import create_engine
engine = create_engine('postgresql://jverhoff:john@localhost:5432/fecInfo')

df.to_sql("candidate_table", engine)
