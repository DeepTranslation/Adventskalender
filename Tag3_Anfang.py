print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Willkommen im Winterwunderland.")
print("Finde den Weihnachtsbaum!\n ")

#Schreibe deinen Code unter dieser Zeile 👇

wahl1 = input('Du befindest dich an einer Weggabelung. Nach links geht es in den tief verschneiten Wald und nach rechts'
              ' über das in der tief stehenden Wintersonne vor sich hin glitzernde Feld. Um weiterzugehen, gib "links" '
              'oder "rechts" ein:\n')
if wahl1 == "links":
  wahl2 = input('Du stapfst durch den Schnee und gelangst an einen sich zwischen den Bäumen dahinschlängelnden Bach. '
                'Willst du hinüber "springen" oder nach einer Brücke "suchen"? \n')
  if wahl2 == "suchen":
    wahl3 = input("Hinter der nächsten Biegung wölbt sich eine massive Brücke über den Bach und du gelangst sicher hinüber. "
                  "Du erreichst eine Lichtung, auf der drei mächtige Bäume in den Himmel ragen. Gehst du zu der Eiche, "
                  "der Tanne oder Buche? \n")
    if wahl3 == "Eiche":
      print("Du gerätst in ein Eichenprozessionsspinner-Nest. Game Over.")
    elif wahl3 == "Tanne":
      print("Du hast den Weihnachtsbaum gefunden und darunter ein Weihnachtsgeschenk für dich! Frohe Weihnachten!")
    elif wahl3 == "Buche":
      print("Von einem der Äste stürzt sich ein Luchs auf dich herab. Game Over.")
    else:
      print("Du hast einen Baum gewählt, den es gar nicht gibt. Game Over.")
  else:
    print("Du schaffst es nicht auf die andere Seite, stürzt ins Wasser und wirst von den eisigen Fluten hinweggetragen. Game Over.")
else:
  print("Während du über das Feld wanderst, zieht ein Schneesturm auf und du verlierst die Orientierung. Game Over.")