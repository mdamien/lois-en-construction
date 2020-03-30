titres = open('titres').read().strip().split('\n')

for i, titre in enumerate(titres):
	titre = titre.strip()
	print("cp texte_0%s.md ../lois-en-construction-données/texte" % (i,))
	print("git -C ../lois-en-construction-données add texte")
	print("git -C ../lois-en-construction-données commit -m '%s'" % (titre,))
