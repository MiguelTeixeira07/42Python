from ex3.CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class FantasyCardFactory(CardFactory):

    def create_creature(self, name_or_power=None):

        return CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

    def create_spell(self, name_or_power=None):

        return SpellCard("Lightning Bolt", 3, "Common", "damage")

    def create_artifact(self, name_or_power=None):

        return ArtifactCard("Mana Ring", 2, "Rare", 5, "+1 mana")

    def create_themed_deck(self, size: int):

        return {
            "creature": self.create_creature(),
            "spell": self.create_spell(),
            "artifact": self.create_artifact()
        }

    def get_supported_types(self):

        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball"],
            "artifacts": ["mana_ring"]
        }
