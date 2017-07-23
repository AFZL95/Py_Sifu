from player import Player

ali = Player("ali")

print(ali.name)
print(ali.lives)
ali.lives -= 1
print(ali)

ali.lives = 20
print(ali.lives)

ali._set_lives(50)
print(ali.lives)


"""
ali.lives -= 1
print(ali)

ali.lives -= 1
print(ali)

ali.lives -= 1
print(ali)
"""