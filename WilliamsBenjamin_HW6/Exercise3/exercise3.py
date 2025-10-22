import pandas as pd

temps = {'Mon': [68, 89], 'Tue': [71, 93], 'Wed': [66, 82], 'Thu': [75, 97], 'Fri': [62, 79]}

df = pd.DataFrame(temps, index=['low', 'high'])
print(df)


print('\n -------------Temps For Mon-Wed-------------')

MtoW = df.loc[:, ['Mon', 'Tue', 'Wed']]
print(MtoW)


print('\n -------------Lows For the Week-------------')
lows = df.loc['low', :]
print(lows)

print('\nAnalysis of Temps for The Week')
print('Average High: ', df.loc['high', :].mean())
print('Average Low: ', df.loc['low', :].mean())