import re

pene = "mi.nombre.es.jorge.lol"

match = re.search("jorge", pene)
print(match.group(0))