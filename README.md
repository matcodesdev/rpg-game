# Text-Based RPG Game

A terminal-based RPG prototype built in Python. Choose your class, face enemies in turn-based combat, manage your health and stamina, and survive each battle!

---

## Structure Overview

- `CharacterClass`: Base class handling stats, attack logic, healing, and stamina.
- `Player`: Subclass with enhanced healing and custom feedback.
- `Enemy`: Subclass for enemy behavior and printed messages.
- `battle_encounter()`: Main game loop handling enemy encounters.

---

### Coming Soon

- Enemy AI turns (`attack`, `heal` decisions)
- Stamina checks before attacks
- Limited inventory count for heals and elixirs
- Boss-specific logic and encounter intros
- Game over and victory end states

---

#### How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/matcodesdev/rpg-game.git
   cd rpg-game
