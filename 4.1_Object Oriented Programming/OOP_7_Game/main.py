from player import Player

ali = Player("ali")

print(ali.name)
print(ali.lives)
ali.lives -= 1
print(ali)

ali.lives -= 1
print(ali)

ali.lives -= 1
print(ali)

ali.lives -= 1
print(ali)

ali._lives = 9
print(ali)

ali.level = 2
print(ali)

ali.level += 5
print(ali)

ali.level = 3
print(ali)

ali.score = 500
print(ali)
