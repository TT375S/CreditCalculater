#!/usr/bin/python
# -*- coding: utf-8 -*-
import cgi
import sys

args = sys.argv

output_file = "creditsSheet.txt"
f_o = open(output_file, 'w')


if len(args) > 1:
#標準入力から読み込み
	if args[1] == "-l":
		print "成績照会のページのhtmlソースを貼り付けてください。入力終了はctrl+Dです。(Windowsではctrl+Z?)"
		input_file ="htmlsource.txt"
		form = sys.stdin.readlines()
		f_i = open(input_file, 'w')
		for line in form:
			f_i.write(line)
		#開き直さないと、f_i.readline()で一行目から読み込まれない。書き込んだ最後からの読み込みになってしまう。
		f_i = open(input_file)
#webからダウンロード
	elif args[1] == "-w":
		input_file ="htmlsource.txt"
		form = cgi.FieldStorage()
		f_i = open(input_file, 'w')
		f_i.write(form['htmlsource'])
		f_i = open(input_file)
#ファイルからHTMLを読み込み
	elif args[1] == "-f":
		input_file = args[2]
		f_i = open(input_file)
	else :
		print "オプションを指定してください"
else :
	print "オプションを指定してください"

line = f_i.readline()
credit = {"A+":0, "A":0, "B":0, "C":0, "F":0, "G":0, "H":0 }
#credit = {}
group = {}
currentGroup = "NONEGROUP"
GPA = 0
classNum = 0
while line:
	if line.find("◎") != -1:
		group[line] = 0
		currentGroup = line
	elif line.find("operationboxf") != -1 and currentGroup != "NONEGROUP":
		group[currentGroup] += 1
		line = f_i.readline()
		line = f_i.readline()
		line = f_i.readline()
		line = f_i.readline()
		
		creditNum =int(line.strip().replace("<TD>","").replace("</TD>","").replace("<BR>", "0").replace("＊", "0"))
		line = f_i.readline()
		grade = line.strip().replace("<TD>","").replace("</TD>","") 	
#		print grade
		line = f_i.readline()
		score = int(line.strip().replace("<TD>","").replace("</TD>","").replace("<BR>", "0").replace("＊", "0"))
		GPA += score
		print classNum
		if grade in credit:
			credit[grade] += 1
		else:
			credit[grade] = 1
	line = f_i.readline()	

print "受講している授業名の、htmlからの抽出が終了しました。"
for key in credit.keys():
	print key + " " + str(credit[key])
	classNum += credit[key]
classNum -= credit["<BR>"]	
print "scoreSum " + str(GPA)
print "classNum" + str(classNum)
print "GPA" + str(float(GPA)/(classNum-credit["＊"]))

