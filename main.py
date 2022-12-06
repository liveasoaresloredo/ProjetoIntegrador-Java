import requests
from bs4 import BeautifulSoup
import pandas as pd

lista = []
listatitulos = []
listaprecos = []
listadesc = []

r = requests.get("http://127.0.0.1:5500/produtos.html")
soup = BeautifulSoup(r.content, "html.parser")

s = soup.find('div', class_="re1")
tituloproduto = s.find_all("h5")
for c in tituloproduto:
    listatitulos.append(c.text)
valor = s.find_all('div', class_="preco")
for c in valor:
    listaprecos.append(c.text)
categoria = s.find_all('div', class_="desc")
for c in categoria:
    listadesc.append(c.text)

print(listatitulos)
print(listaprecos)
print(listadesc)


s = soup.find('div', class_="re2")
tituloproduto = s.find_all("h5")
for c in tituloproduto:
    listatitulos.append(c.text)
valor = s.find_all('div', class_="preco")
for c in valor:
    listaprecos.append(c.text)
categoria = s.find_all('div', class_="desc")
for c in categoria:
    listadesc.append(c.text)

print(listatitulos)
print(listaprecos)
print(listadesc)


s = soup.find('div', class_="re3")
tituloproduto = s.find_all("h5")
for c in tituloproduto:
    listatitulos.append(c.text)
valor = s.find_all('div', class_="preco")
for c in valor:
    listaprecos.append(c.text)
categoria = s.find_all('div', class_="desc")
for c in categoria:
    listadesc.append(c.text)

print(listatitulos)
print(listaprecos)
print(listadesc)

s = soup.find('div', class_="re4")
tituloproduto = s.find_all("h5")
for c in tituloproduto:
    listatitulos.append(c.text)
valor = s.find_all('div', class_="preco")
for c in valor:
    listaprecos.append(c.text)
categoria = s.find_all('div', class_="desc")
for c in categoria:
    listadesc.append(c.text)

print(listatitulos)
print(listaprecos)
print(listadesc)

s = soup.find('div', class_="re5")
tituloproduto = s.find_all("h5")
for c in tituloproduto:
    listatitulos.append(c.text)
valor = s.find_all('div', class_="preco")
for c in valor:
    listaprecos.append(c.text)
categoria = s.find_all('div', class_="desc")
for c in categoria:
    listadesc.append(c.text)

print(listatitulos)
print(listaprecos)
print(listadesc)


listalegal = {"Nome produto": listatitulos,
              "Preço produto": listaprecos,
              "Categoria": listadesc}
listateste = pd.DataFrame(listalegal
)
listateste.to_excel("pi.xls")