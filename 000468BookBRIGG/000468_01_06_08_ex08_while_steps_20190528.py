found_coins = 20
magic_coins = 70
stolen_coins = 3
coins = found_coins
for week in range(1, 53):
	coins = coins + magic_coins -  stolen_coins
	print('Неделя %s = %s coins' % (week, coins))
input()