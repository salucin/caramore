"""
Characters

Characters are (by default) Objects setup to be puppeted by Accounts.
They are what you "see" in game. The Character class in this module
is setup to be the "default" character type created by the default
creation commands.

"""
from evennia import DefaultCharacter


class Character(DefaultCharacter):
    """
    The Character defaults to reimplementing some of base Object's hook methods with the
    following functionality:

    at_basetype_setup - always assigns the DefaultCmdSet to this object type
                    (important!)sets locks so character cannot be picked up
                    and its commands only be called by itself, not anyone else.
                    (to change things, use at_object_creation() instead).
    at_after_move(source_location) - Launches the "look" command after every move.
    at_post_unpuppet(account) -  when Account disconnects from the Character, we
                    store the current location in the pre_logout_location Attribute and
                    move it to a None-location so the "unpuppeted" character
                    object does not need to stay on grid. Echoes "Account has disconnected"
                    to the room.
    at_pre_puppet - Just before Account re-connects, retrieves the character's
                    pre_logout_location Attribute and move it back on the grid.
    at_post_puppet - Echoes "AccountName has entered the game" to the room.

    """
    def at_object_creation(self):
        # I will have to fix these stats later.  We don't updating character defaults to reset rolled stats.
        self.db.strength = 0
        self.db.agility = 0
        self.db.intelligence = 0
        self.db.charisma = 0
        self.db.constitution = 0
        self.db.spirit = 0
        # Xp and leveling based values.
        self.db.chlevel = 1
        self.db.xpmulti = .10
        # The base amount of exp.  Xp progress is based around this value.
        self.db.xpbase = 1000
        self.db.exp = 0
        self.ndb.xplvl = (self.db.xpbase * self.db.xpmulti) + self.db.xpbase

    def get_stats(self):

        return self.db.strength, self.db.agility, self.db.intelligence, self.db.charisma, self.db.constitution, self.db.spirit, self.db.chlevel, self.ndb.xplvl
