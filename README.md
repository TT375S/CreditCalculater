# CreditCalculater
Calculate a number of Credit granted and, GPA( Grade Point Average).

大学の成績照会のページから、どの群の科目の単位をどれだけとったかと、GPAを算出するプログラムです。

##前提となるもの
Python2.xさえ使えれば、特に用意するものはありません。

##使い方
適当なフォルダで、  
`$ git clone https://github.com/TT375S/CreditCalculater.git`   
としてクローンします。  
次に、ファイルのあるディレクトリに移動します。  
`$ cd TestScheduleGetter/files`   
実行します。  
`$ python digestHTML.py -l`  
  
すると、入力待ちになりますので、  
後は、大学の成績照会ページ<https://iaidp.ia.waseda.jp/idp/profile/SAML2/Redirect/SSO;jsessionid=C1C4CD947A9D52B605515638EA7D720C?execution=e1s1>に行って、成績が表示されているページのHTMLソースコードをコピーして、ターミナルに貼り付けます。   

##出力例  
	受講している授業名の、htmlからの抽出が終了しました。
	---群別の単位数(カッコ内は履修はしているもののまだ成績が決定されていないもの)---
	Ｃ群(専門教育科目): 21 (16)
	Ｂ群: 33 (0)
	Ａ群: 18 (4)
	Ｄ群(保健体育・自主挑戦科目): 2 (0)
	合計: 74 (20) 単位

	---評価別の数(＊は未評価)---
	A 17
	C 2
	B 13
	G 0
	F 0
	H 0
	A+ 3
	＊ 11

	---成績計算---
	scoreSum 91
	class 46
	finishedClass 35
	GPA 2.6


