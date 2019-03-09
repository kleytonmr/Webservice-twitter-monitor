import pandas as pd
import csv
import re


def remove_urls (text):
	text = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', text, flags=re.MULTILINE)
	return(text)

xlsx = pd.ExcelFile('Tweets_Mg.xlsx')
df = pd.read_excel(xlsx, 'sheet')
text = []
classe = []

for i in df.itertuples():
	text.append(remove_urls(i.text))
	classe.append(i.classificacao)


writer = pd.ExcelWriter('out.xlsx')
dff = pd.DataFrame(text, classe)
dff.to_excel(writer,'Sheet1')
writer.save()



print(text)
print(classe)