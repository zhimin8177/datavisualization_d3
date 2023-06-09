'''
从原数据生成graph6需要用到的数据
'''

import pandas as pd
chemistry = pd.read_csv("dataverse_files/Chemistry publication record.csv",parse_dates=['Prize year','Pub year'])
medicine = pd.read_csv("dataverse_files/Medicine publication record.csv",parse_dates=['Prize year','Pub year'])
physics = pd.read_csv("dataverse_files/Physics publication record.csv",parse_dates=['Prize year','Pub year'])
prize = pd.read_csv("dataverse_files/Prize-winning paper record.csv",parse_dates=['Prize year','Pub year'])

chemistry['subject'] = "chemistry"
medicine['subject'] = "medicine"
physics['subject'] = "physics"

fulldata = pd.concat([chemistry,medicine,physics])

chemistry['Prize year'] = chemistry['Prize year'].dt.year
chemistry['Pub year'] = chemistry['Pub year'].dt.year
medicine['Prize year'] = medicine['Prize year'].dt.year
medicine['Pub year'] = medicine['Pub year'].dt.year
physics['Prize year'] = physics['Prize year'].dt.year
physics['Pub year'] = physics['Pub year'].dt.year
prize['Prize year'] = prize['Prize year'].dt.year
prize['Pub year'] = prize['Pub year'].dt.year

prize.loc[prize['Title']=='xxxvii on the constitution of atoms and molecules','Pub year'] = 1913
prize.loc[prize['Title']=="Wien's displacement law",'Pub year'] = 1893
prize.loc[prize['Title']=="researches with the dropping mercury cathode part ii the polarograph",'Pub year'] = 1923

#计算正确的年份差距
prize['prize_pub_year'] = prize['Prize year'] - prize['Pub year']

prize_pub_year_field = prize.groupby(['Field','prize_pub_year']).nunique().Title.to_frame().reset_index().rename(columns={'Title':'paper_count'})
prize_pub_year_all = prize.groupby(['prize_pub_year']).nunique().Title.to_frame().reset_index().rename(columns={'Title':'paper_count'})
prize_pub_year_all.to_csv("prize_pub_year_all.csv",index=False)
prize_pub_year_field.to_csv("prize_pub_year_field.csv",index=False)
