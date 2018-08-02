#! python3

# pokemonBattle - battle your pokemon!

# TODO: battle more than one pokemon
# TODO: load pokemon and attacks more dynamically
# TODO: XP
# TODO: defensive moves
# TODO: types
# TODO: STAB
# TODO: Scraggy, Mimikyu, nontrash pokemon

import random

# party and opponent pokemon, stats, attacks

party_pokemon = ["Charmander","Rattata"]
opponent_pokemon = ["Bulbasaur","Pidgey"]

charmander_attacks = [["Scratch",10],["Ember",25]]
charmanderHP = 30
charmanderSpeed = 5

rattata_attacks = [["Tackle",10],["Bite",20]]
rattataHP = 20
rattataSpeed = 10

bulbasaur_attacks = [["Tackle",10],["Vine Whip",25]]
bulbasaurHP = 35
bulbasaurSpeed = 5

pidgey_attacks = [["Tackle",10],["Gust",20]]
pidgeyHP = 15
pidgeySpeed = 10

# choose pokemon

print("Choose your pokemon!")
for i in party_pokemon:
    print("[" + str(party_pokemon.index(i)+1) + "] " + i)
playerChoice = int(input())-1

playerPokemon = party_pokemon[playerChoice]

# loads attacks and stats based on input

if playerPokemon == "Charmander":
    attacks = charmander_attacks
    HP = charmanderHP
    speed = charmanderSpeed
else:
    attacks = rattata_attacks
    HP = rattataHP
    speed = rattataSpeed

# randomly select opponent pokemon, load stats and attacks

opponentChoice = random.randint(0,(len(opponent_pokemon)-1))

opponentPokemon = opponent_pokemon[opponentChoice]

if opponentPokemon == "Bulbasaur":
    opponent_attacks = bulbasaur_attacks
    opponentHP = bulbasaurHP
    opponentSpeed = bulbasaurSpeed
else:
    opponent_attacks = pidgey_attacks
    opponentHP = pidgeyHP
    opponentSpeed = pidgeySpeed

# battle start

print(playerPokemon + " HP: " + str(HP) + " vs. " + opponentPokemon + " HP: " + str(opponentHP))

# start loop for battle

while HP > 0 and opponentHP > 0:

    # if you outspeed opponent then select first
    
    if speed >= opponentSpeed:
        print("You go first!")
        for k in attacks:
            print("[" + str(attacks.index(k)+1) + "] " + k[0])
        attack = int(input("Choose Attack: "))-1

        # calculate opponent HP
        
        opponentHP = opponentHP - attacks[attack][1]

        # if opponent HP gets below 0 set back to 0 and break loop
        
        if opponentHP < 0:
            opponentHP = 0
        if opponentHP == 0:
            break

        # randomly select opponent attack
        
        opponentAttack = random.randint(0,len(opponent_attacks)-1)

        # calculate your HP, reset to zero
        
        HP = HP - opponent_attacks[opponentAttack][1]
        if HP < 0:
            HP = 0
        if HP == 0:
            break

        # print battle status
        
        print(playerPokemon + " HP: " + str(HP) + " vs. " + opponentPokemon + " HP: " + str(opponentHP))      
    else:

        # as above, but reversed
        
        print("Opponent goes first!")
        opponentAttack = random.randint(0,len(opponent_attacks)-1)
        HP = HP - opponent_attacks[opponentAttack][1]
        if HP < 0:
            HP = 0
        if HP == 0:
            break
        for k in attacks:
            print("[" + str(attacks.index(k)+1) + "] " + k[0])
        attack = int(input("Choose Attack: "))-1
        opponentHP = opponentHP - attacks[attack][1]
        if opponentHP < 0:
            opponentHP = 0
        if opponentHP == 0:
            break
        print(playerPokemon + " HP: " + str(HP) + " vs. " + opponentPokemon + " HP: " + str(opponentHP))

# battle outcomes

if opponentHP == 0 and HP != 0:
    print("You win!")
elif opponentHP != 0 and HP == 0:
    print("You lose!")
else:
    print("A draw!")
