from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        targets = self.prioritize_targets(battlefield)
        played = []
        total_mana = 0
        total_damage = 0
        for card in hand:
            if card.name == "Fire Dragon":
                continue
            played.append(card.name)
            total_mana += card.cost
            if hasattr(card, 'attack'):
                total_damage += card.attack
            elif hasattr(card, 'effect_type') and card.effect_type == 'damage':
                total_damage += 3

        return {
            'cards_played': played,
            'mana_used': total_mana,
            'targets_attacked': [targets[0]] if targets else [],
            'damage_dealt': total_damage
        }

    def get_strategy_name(self) -> str:
        return 'AggressiveStrategy'

    def prioritize_targets(self, available_targets: list) -> list:
        targets = []
        for t in available_targets:
            if 'Player' in t:
                targets.append(t)
            elif 'Creature' in t:
                targets.append(t)
        return targets
