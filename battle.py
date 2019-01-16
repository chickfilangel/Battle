import time
import random

print()
print('-' * 60)
print('A wild Jigglypuff appears!')
time.sleep(0.2)
print('You only have one Pokemon, Snorlax.')
time.sleep(0.2)
print('I choose you Snorlax!')
print()
time.sleep(0.2)

# Starting HPs
snorlax_hp = 200
jiggly_hp = 125

# Starting HP
print('Updated HP!')
print('-Snorlax HP:' + str(snorlax_hp))
time.sleep(0.2)
print('-Jigglypuff HP:' + str(jiggly_hp))
time.sleep(0.2)
print()
time.sleep(0.2)
while snorlax_hp > 0 and jiggly_hp > 0:
	print('Battle Options:')
	time.sleep(0.2)
	print('[1] Sleep Heal')
	time.sleep(0.2)
	print('[2] Comet Punch')
	time.sleep(0.2)
	print('[3] Sonic Boom')
	time.sleep(0.2)
	print('[4] Hyper Beam')
	time.sleep(0.2)
	print('[5] Capture')
	your_move = input('Choose a move using the corresponding number: ')
	print()
	if your_move == '1':
		snorlax_hp = snorlax_hp + 50
		print('Snorlax uses Sleep Heal, his HP increases to ' + str(snorlax_hp))
		time.sleep(0.2)
	elif your_move == '2':
		jiggly_hp = jiggly_hp - 10
		print('Snorlax uses tackle and deals 10 damage to Jigglypuff!')
		time.sleep(0.2)
	elif your_move == '3':
		snorlax_hp == jiggly_hp - 30
		print('Snorlax uses Roundhouse Kick and deals 30 damage to Jigglypuff!')
		time.sleep(0.2)
	elif your_move == '4':
		snorlax_hp == jiggly_hp - 40
		print('Snorlax uses Hyperbeam and deals 40 damage to Jigglypuff!')
		time.sleep(0.2)
	elif your_move == '5':
		capture_roll = random.randint(0,125)
		if capture_roll > jiggly_hp:
			print('You have captured jigglypuff!')
			break
		else:
			print('You tried to capture jigglypuff, but it escaped!')
			break
	print()

	# jigglypuff attacks
	enemy_move = random.randint(1,2)
	enemy_move = str(enemy_move)
	if enemy_move == '1':
		snorlax_hp = snorlax_hp - 30
		jiggly_hp = jiggly_hp + 30
		print('Jigglypuff uses Drink Blood and deals 30 HP of damage while recovering 30 health.')
		time.sleep(0.2)
	elif enemy_move == '2':
		snorlax_hp = snorlax_hp - 50
		print('Jigglypuff uses Breathe Fire and deals 50 HP of damage.')
		time.sleep(0.2)
		print()

	if snorlax_hp < 0:
		snorlax_hp = 0
	if jiggly_hp < 0:
		jiggly_hp = 0

	print('Updated HP!')
	print('-Snorlax HP:' + str(snorlax_hp))
	time.sleep(0.2)
	print('-Jigglypuff HP:' + str(jiggly_hp))
	time.sleep(0.2)
	print()
	time.sleep(0.2)

if snorlax_hp == 0:
	print('Snorlax has been defeated! The winner is jigglypuff!')
elif jiggly_hp == 0:
	print('Jigglypuff has been defeated! The winner is Snorlax!')

print('-' * 65)




