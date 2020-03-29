from bs4 import BeautifulSoup as Soup

html = open('tableau.html').read()

html = html.replace('text-decoration: line-through;', '')
html = html.replace('border-bottom: 3px double;', '')
html = html.replace('▫', '')

soupe = Soup(html, 'lxml')

for num_colonne, colonne in enumerate(soupe.select('table colgroup col')):

    if 'texte-col-pastille' in colonne.attrs['class']:
        break

    fichier = 'texte_%s.md' % (str(num_colonne).rjust(2, '0'))

    titre = soupe.select('table #head-fixed .texte-col')[num_colonne].text.strip()
    print(titre)

    print(fichier)

    with open(fichier, 'w') as f:
        for article in soupe.select('table'):
            for ligne in article.select('.texte-ligne'):
                cellule = ligne.select('.texte-col')[num_colonne]
                for dispositif in cellule.select('.dispositif'):
                    texte = dispositif.text.strip().replace('\n', '')

                    if not texte:
                        continue

                    if '/amendements/' in str(dispositif):
                        continue

                    classes = dispositif.attrs['class']

                    if 'TCTexte' in classes:
                        print(texte, file=f)
                        print(file=f)
                    else:
                        print('##', texte, file=f)
                        print(file=f)