print("hem inglizcede hemde turkcede olan sozcukler")




meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "NOOB": "ezik veya bir konuda kotu olan birine denir",
            "OK": "kabul etmek",
            "NOPE": "bir seyi reddetmek icin kullanilir
            "PRO": "her iste yada belirli bir iste cok iyi olan birine denir",
            }
            
            
for i in range(5):
    word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("Sözlükte bu kelime bulunmuyor")
