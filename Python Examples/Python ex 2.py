Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:54:40) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> user = "Tuna McFish"
>>> user[5]
'M'
>>> user[7]
'F'
>>> user[-1]
'h'
>>> user[2:7]
'na Mc'
>>> Type "copyright", "credits" or "license()" for more information.
SyntaxError: invalid syntax
>>> 
>>> user[:7]
'Tuna Mc'
>>> user[1:]
'una McFish'
>>> user[:]
'Tuna McFish'
>>> print ("deadfish")
deadfish
>>> len("how many characters" )
19
>>> len (user)
11
>>> -----------------------------------------
SyntaxError: invalid syntax
>>> //k
SyntaxError: invalid syntax
>>> ##Practice with lists
>>> #-----------------------------------------------------------------
>>> players = [29,58,77,45,69]
>>> players[2]
77
>>> players[2]=33
>>> players
[29, 58, 33, 45, 69]
>>> players + [1,2,3]
[29, 58, 33, 45, 69, 1, 2, 3]
>>> players
[29, 58, 33, 45, 69]
>>> #as you can see the addition of 1,2,3 was only temporary
>>> #ie the list wasnt changed
>>> players.append(120)
>>> players
[29, 58, 33, 45, 69, 120]
>>> #append permentatly changes the list and + is temporal
>>> players{:2}
SyntaxError: invalid syntax
>>> players[:2]
[29, 58]
>>> players[:2]=[0,0]
>>> players
[0, 0, 33, 45, 69, 120]
>>> players[:2] = [];
>>> players
[33, 45, 69, 120]
>>> players[:]= []
>>> players
[]
>>> #about start using jgrasp
>>> 
