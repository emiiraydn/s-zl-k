meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "Bro: İngilizce "brother" kelimesinin kısaltılmış hâlidir.",
            "gg: Good game kelimelerinin kısaltılmasıdır, iyi oyunlar anlamına gelir.",
            "nt: Nice try yani güzel deneme anlamında bir şeyin denenmesini takdir etmek anlamında kullanılmaktadır.",
            "Bug: İngilizcedeki karşılığı olan böcek kelimesinden türetilmiştir, en yakın anlamıyla bir sistemin açığı anlamına gelir.",
            }

word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
   print("Böyle bir kelime bulunamadı!")
