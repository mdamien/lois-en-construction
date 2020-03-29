titres = """Texte du projet de loi
Texte adopté par la commission de l’Assemblée nationale en première lecture
Texte adopté par l’Assemblée nationale en première lecture
Texte adopté par la commission du Sénat en première lecture
Texte adopté par le Sénat en première lecture
Texte adopté en commission mixte paritaire
Texte définitif établi au Sénat
Texte promulgué""".split('\n')

for i, titre in enumerate(titres):
	titre = titre.strip()
	print("cp texte_0%s.md ../lois-en-construction-données/texte" % (i,))
	print("git -C ../lois-en-construction-données add texte")
	print("git -C ../lois-en-construction-données commit -m '%s'" % (titre,))
