"""
Un palindromo es un una palabra o frase que se lee igua de izquierdta a derecta que de seretta aizq er da
ejemplo Ojo, Oso, Ana, Anna, Ott..,
Su misión es, realizar un algortmo que me permita conocer dada una palabra por el usuario si es
palindroms o no
"""

word = input("Ingrese una palabra: ")
word = word.lower().replace(" ", "") 
if  word == word[::-1]: 
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")