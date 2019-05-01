import os
import sys
import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

projectpath='/Users/daelsaid/Documents/scsnl_2019/met/'
participation_tracker=os.path.join(projectpath,'MET_Participation_Tracker.xlsx')
datatracker=os.path.join(projectpath,'MET_Data_Tracker.xlsx')

datatracker_df=pd.read_excel(datatracker,sheet_name='Assessment_Tracker',skiprows=1)

participation_tracker_df=pd.read_excel(participation_tracker,sheet_name='Participation Progress',skiprows=1)

merged_df=pd.DataFrame()

merged_df=pd.merge(participation_tracker_df,datatracker_df,on='PID',how='outer',suffixes=('_master','_np'))

merged_df.to_csv(os.path.join(projectpath,'merged_np_and_participation_tracker.csv'))
