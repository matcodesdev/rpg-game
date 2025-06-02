'''
Quick test to write a short outline of a game script.
'''

import time

print('Welcome to game!')
time.sleep(1)
username = input('Please create a username: ').lower()

class CharacterClass:
    def __init__ (self, name, health, stamina, ap, ad): 
        self.name = name
        self.health = health
        self.max_hp = health
        self.stamina = stamina
        self.max_stamina = stamina
        self.ap = ap # ability power (magic dmg)
        self.ad = ad # attack damage (physical dmg)

    def __str__ (self): # returns player info when {player_class} called later on
        return (f'''
Class: {self.name.capitalize()}
Health: {self.health}
Stamina: {self.stamina}
Ability Power: {self.ap}
Attack Damage: {self.ad}
''')

    def ad_attack(self):
        self.stamina -= 10
        ad_dmg_dealt = self.ad / 4 
        return ad_dmg_dealt

    def ap_attack(self):
        # doesn't use any stamina
        ap_dmg_dealt = self.ap / 4
        return ap_dmg_dealt
    
    # heal here only handle the math and returns the amount healed
    def heal(self):
        remaining_hp = self.max_hp - self.health
        if self.health == self.max_hp:
            return None
        elif self.health + 20 > self.max_hp:
            self.health += remaining_hp
            return remaining_hp
        else:
            self.health += 20
            return 20

    # elixir here only handle the math and returns the amount recovered
    def elixir(self):
        remaining_stam = self.max_stamina - self.stamina
        if self.stamina == self.max_stamina:
            return None
        elif self.stamina + 10 > self.max_stamina:
            self.stamina += remaining_stam
            return remaining_stam
        else:
            self.stamina += 10
            return 10

#------------------------------------------------------------------------------

class Player(CharacterClass):
    # heal and elixir here only handle the prints
    def heal(self):
        healed = super().heal()
        if healed == None:
            print('\nYou are already at max HP!')
        else:
            print(f'\n You healed for {healed} HP!')

    def elixir(self):
        stamina = super().elixir()
        if stamina == None:
            print('\nYour stamina is full!')
        else:
            print(f'\nYou recovered {stamina} stamina!')

class Enemy(CharacterClass):
    def heal(self):
        healed = super().heal()
        if healed == None:
            print(f'\n{self.name.capitalize()} is already at max HP!')
        else:
            print(f'\n{self.name.capitalize()} healed for {healed} HP!')

    def elixir(self):
        stamina = super().elixir()
        if stamina == None:
            print(f'\n{self.name.capitalize()} stamina is full!')
        else:
            print(f'\n{self.name.capitalize()} recovered {stamina} stamina!')   

    # enemy class to handle prints of heals, attacks, etc.

# -------------------------------------------------------------------------------------

time.sleep(0.5)
print(f'\nWelcome {username}, please choose a class')
time.sleep(1)

# while loop for determining the player's class
while True:
    chosen_class = input('(Knight, Mage, Assassin, Bruiser): ').lower().strip()
    if chosen_class == 'knight':
        player_class = Player('knight', 80, 55, 20, 50)
        break
    elif chosen_class == 'mage':
        player_class = Player('mage', 55, 40, 60, 20)
        break
    elif chosen_class == 'assassin':
        player_class = Player('assassin', 60, 65, 30, 45)
        break
    elif chosen_class == 'bruiser':
        player_class = Player('bruiser', 125, 70, 5, 40)
        break
    else:
        print('\nInvalid class, please choose again')

time.sleep(1)

player_info = (f'''
PLAYER INFO:

Username: {username}
{player_class} _
''')

for word in player_info: # 'animated' printing of player info
    print(word, end= '', flush=True)
    time.sleep(0.01)

time.sleep(2)
print('\nAre you ready to embark on a wild adventure?')
time.sleep(1.5)
print('Let\'s go!')

# -------------------------------------------------------------------------------------

# enemy creation (instantiated from character class)
goblin = Enemy('goblin', 60, 20, 5, 30)
orc = Enemy('orc', 100, 40, 0, 60)
final_boss = Enemy('Gundyr', 300, 100, 50, 100)

enemy_list = [goblin, orc, final_boss]

def win_or_lose(enemy): # checks if player or enemy health is 0 to see if battle is over
    if player_class.health == 0:
        print('You died!')
    elif enemy.health == 0:
        print(f'You defeated the {enemy.name}')

def battle_encounter(): # loop that starts the battle

    for enemy in enemy_list:
        print(f'\nA wild {enemy.name} has appeared!')

        while player_class.health > 0 and enemy.health > 0:
            print(f'\n{username.capitalize()} - HP: {round(player_class.health)}, Stamina: {round(player_class.stamina)}')
            print(f'{enemy.name.capitalize()} - HP: {round(enemy.health)}, Stamina: {round(enemy.stamina)}')
            player_input = input('What do you do? (AD Attack/AP Attack/Heal/Skip/Exit)').lower().strip()
            
            if player_input == 'ad attack':
                damage = player_class.ad_attack()
                enemy.health -= damage
                print(f'\nYou dealt {round(damage)} damage to {enemy.name}')
            elif player_input == 'ap attack':
                damage = player_class.ap_attack()
                enemy.health -= damage
                print(f'\nYou dealt {round(damage)} damage to {enemy.name}')
            elif player_input == 'heal':
                player_class.heal()
            elif player_input == 'skip':
                print('\nYou skip your turn')
                continue
            elif player_input == 'exit':
                break
            else:
                print('Please choose one of the options provided')
                continue
            
            print('-----------------------------------')

        win_or_lose(enemy)

battle_encounter()


"""
🧭 NEXT CHECKLIST – RPG COMBAT SYSTEM

🗡️ COMBAT FUNCTIONALITY
1. Enemy Turn Logic
   - Add basic enemy attack after player turn
   - Optional: healing behavior or conditional decisions

2. Stamina Requirement for Attacks
   - Block ad_attack() if stamina < 10
   - Notify player and skip attack if stamina is insufficient

LOOP / FLOW ENHANCEMENTS
3. Full Turn Loop Feedback
   - Add turn number or divider for visual clarity
   - Clean separation between player and enemy turns

4. Exit Battle Early
   - Ensure 'exit' fully exits both the battle and the enemy loop

POLISH & READABILITY
5. Organize Method Order in Classes
   - Group attacks, healing, and display methods together
   - Move __str__ to the bottom for better structure

6. Combat Log Improvements (optional)
   - Add flavor text: “You miss!”, “Critical hit!”, etc.

7. Victory/Defeat Handling
   - Add final message when last enemy is defeated or player dies
   - Clean exit or option to restart
"""
