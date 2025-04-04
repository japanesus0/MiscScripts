#!/usr/bin/python3
from readability import Readability
import glob
import re
import nltk

nltk.download('punkt')
#nltk.download('gutenberg')
#nltk.download('brown')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('universal_tagset')

#data_dir="/home/japanesus/scripts/gov/data/"
data_dir="data/"
data=[]
speech=[]

name=["elon", "mm", "aoc", "ken", "nmace", "ddavis", "trump_tw", "trump_ts", "charli", "mcd"]

for derp in name:
	counter=0
	wc=0
	for each_file in glob.glob(data_dir + str(derp) + '*.txt'):
		counter+=1
		with open(each_file, 'r', encoding='utf-8') as f:
			for line in f:
				if re.match('[^\.\!\?]$',line):   #probably useless
					line = line + "."
				data.append(line)
	r = Readability(' '.join(data))

	print("\nName: " + derp + "\tNum Tweets:" + str(counter) + '\tWord Counter:' + str(len(re.findall('[A-Za-z]+',str(data)))))

	fk = r.flesch_kincaid()
	fe = r.flesch()
	dc = r.dale_chall()
	gf = r.gunning_fog()
	ari = r.ari()
	sp = r.spache()
	cl = r.coleman_liau()
#	sm = r.smog(all_sentences=True)
	lw = r.linsear_write()
	
	print("F-K Ease:\t" + str(round(fe.score,2)) + "\tF-K Grade:\t" + str(round(fk.score,2)) + "\tDale Chall:\t" + str(round(dc.score,2)) + "\tGunning Fog:\t" + str(round(gf.score,2)) + "\tARI:\t" + str(round(ari.score,2)) + "\tColeman-Liau: " + str(round(cl.score,2)) + "\tSpache:\t" + str(round(sp.score,2)) + "\tLinsear Write:\t" + str(round(lw.score,2)) )
#	print("Grade:\nF-K Kincaid:\t" + str(fk.grade_level)+ "\tDale Chall:\t" + str(dc.grade_levels) + "\tGunning Fog:\t" + str(gf.grade_level) + "\tARI:\t" + str(ari.grade_levels))

	print("_" * 150)

	data.clear()

s_input="speech_mlk.txt"

with open(data_dir + s_input,'r') as f:
	for line in f:
		speech.append(line)

r1 = Readability(' '.join(speech))

#print(' '.join(speech))	#debug the input

print("\n\n" + s_input + "  :\n" +' \tWord Counter:' + str(len(re.findall('[A-Za-z]+',str(speech)))))
fe = r1.flesch()
fk = r1.flesch_kincaid()
dc = r1.dale_chall()
gf = r1.gunning_fog()
ari = r1.ari()
lw = r1.linsear_write()
#print("Flesch Kincaid Ease:\n" + str(round(fe.score,2)))
#print("Flesch Kincaid Grade:\n" + str(round(fk.score,2)))
print("Flesch Kincaid Ease:\n" + str(fe))
print("Flesch Kincaid Grade:\n" + str(fk))

print("\nDale Chall:\t" + str(round(dc.score,2)) + "\tGunning Fog:\t" + str(round(gf.score,2)) + "\tAutomated Readability Index:\t" + str(round(ari.score,2)) + "\tColeman-Liau:\t" + str(round(cl.score,2)) + "\tSpache:\t" + str(round(sp.score,2)) + "\tLinsear Write:\t" + str(round(lw.score,2)))

