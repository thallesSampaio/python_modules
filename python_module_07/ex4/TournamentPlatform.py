from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self):
        self.cards = []
        self.matches = 0

    def register_card(self, card: TournamentCard) -> str:
        if card.__class__ != TournamentCard:
            raise ValueError("Only TournamentCard instances can be registered")
        self.cards.append(card)
        return f"{card.name} (ID: {card.card_id}):" \
            f"\n- Interfaces: [Card, Combatable, Rankable]" \
            f"\n- Rating: {card.rating}\n" \
            f"- Record: {card.record['wins']}-{card.record['losses']}"

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        card1, card2 = None, None
        for c in self.cards:
            if c.card_id == card1_id:
                card1 = c
            if c.card_id == card2_id:
                card2 = c
        if not card1 or not card2:
            raise ValueError("Both cards must be registered in the platform")
        res = {}
        while True:
            res_atk = card1.attack(card2)
            if res_atk["defender_health"] <= 0:
                card1.update_wins(1)
                card2.update_losses(1)
                res["winner"] = card1.card_id
                res["loser"] = card2.card_id
                break
            else:
                res_atk2 = card2.attack(card1)
                if res_atk2["defender_health"] <= 0:
                    card2.update_wins(1)
                    card1.update_losses(1)
                    res["winner"] = card2.card_id
                    res["loser"] = card1.card_id
                    break
        if res["winner"] == card1.card_id:
            res["winner_rating"] = card1.calculate_rating()
            res["loser_rating"] = card2.calculate_rating()
        else:
            res["winner_rating"] = card2.calculate_rating()
            res["loser_rating"] = card1.calculate_rating()

        self.matches += 1
        return res

    def get_leaderboard(self) -> list:
        r = []
        for c in self.cards:
            lb = c.get_rank_info()
            r.append(lb)
        r = sorted(r, key=lambda x: x["rating"], reverse=True)
        return r

    def generate_tournament_report(self) -> dict:
        total_rating = sum(c.rating for c in self.cards)
        avg = total_rating / len(self.cards) if self.cards else 0
        avg = int(avg)
        return {
            "total_cards": len(self.cards),
            "matches_played": self.matches,
            "avg_rating": avg,
            "platform_status": "active"
        }
