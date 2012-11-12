import sqlite3
import BeautifulSoup
import re

recipe_db = "muffinki.txt"

conn = sqlite3.connect(recipe_db)
cursor = conn.cursor()

recipes_html = cursor.execute("SELECT * FROM django_flatpage").fetchall()

ingredient_candidates = set()

for recipe_html in recipes_html:
    soup = BeautifulSoup.BeautifulSoup(recipe_html[3])
    ings = str(soup.find("p", { "class" : "ingredients" }))
    ings = ings.replace('<br />', '').decode('utf-8')

    matching = re.findall(r'([^\W0-9_]+)', ings, flags=re.U)
    matching = [m.lower() for m in matching]
    matching = [m for m in matching if len(m) > 2]
    for w in matching:
        ingredient_candidates.add(w)

ingredient_candidates = list(ingredient_candidates)
for w in ingredient_candidates:
    print w.encode('utf-8')
