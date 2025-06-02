# ../bomb_security/bomb_security.py

"""Allows CTs to pick up the bomb."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Source.Python
from entities.entity import Entity
from entities.hooks import EntityCondition, EntityPostHook, EntityPreHook
from memory import make_object
from players.teams import teams_by_name


# =============================================================================
# >> CLASSES
# =============================================================================
class _BumpManager:
    bump_player = None

    def pre_bump_weapon(self, stack_data):
        """Switch the player's team if they are a CT picking up the bomb."""
        if make_object(Entity, stack_data[1]).classname != "weapon_c4":
            return
        self.bump_player = make_object(Entity, stack_data[0])
        if self.bump_player.team_index == teams_by_name["ct"]:
            self.bump_player.team_index = teams_by_name["t"]
        else:
            self.bump_player = None

    def post_bump_weapon(self):
        """Switch the player back to CT if they just picked up the bomb."""
        if self.bump_player is None:
            return
        self.bump_player.team_index = teams_by_name["ct"]
        self.bump_player = None


_bump_manager = _BumpManager()


# =============================================================================
# >> ENTITY HOOKS
# =============================================================================
@EntityPreHook(EntityCondition.is_human_player, "bump_weapon")
@EntityPreHook(EntityCondition.is_bot_player, "bump_weapon")
def _pre_bump_weapon(stack_data):
    _bump_manager.pre_bump_weapon(stack_data)


@EntityPostHook(EntityCondition.is_human_player, "bump_weapon")
@EntityPostHook(EntityCondition.is_bot_player, "bump_weapon")
def _post_bump_weapon(stack_data, return_value):
    _bump_manager.post_bump_weapon()
