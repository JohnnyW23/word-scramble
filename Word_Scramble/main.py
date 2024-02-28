from codes import title, generateWord, game, playAgain, exit
title()
v = d = c = 0
ccl = True
while ccl:
    c += 1
    secret, scrambled = generateWord(6)
    v, d, = game(secret, scrambled, v, d)
    ccl = playAgain()
exit(c, v, d)
