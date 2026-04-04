import random


class TournamentPlatform:

    def __init__(self):

        self.cards = {}
        self.matches = 0

    def register_card(self, card):

        cid = card.name.lower().replace(" ", "_")

        self.cards[cid] = card

        return cid

    def create_match(self, card1_id, card2_id):

        c1 = self.cards[card1_id]
        c2 = self.cards[card2_id]

        winner = random.choice([c1, c2])
        loser = c2 if winner == c1 else c1

        winner.update_wins(1)
        loser.update_losses(1)

        winner.calculate_rating()
        loser.calculate_rating()

        self.matches += 1

        return {
            "winner": winner.name,
            "loser": loser.name,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating
        }

    def get_leaderboard(self):

        return sorted(
            self.cards.values(),
            key=lambda c: c.rating,
            reverse=True
        )

    def generate_tournament_report(self):

        avg = sum(c.rating for c in self.cards.values()) / len(self.cards)

        return {
            "total_cards": len(self.cards),
            "matches_played": self.matches,
            "avg_rating": int(avg),
            "platform_status": "active"
        }
