# ../bomb_security/bomb_security.py

"""Allows CTs to pick up the bomb."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Source.Python
from entities.entity import Entity
from entities.hooks import EntityCondition, EntityPostHook, EntityPreHook
from memory import make_object


# =============================================================================
# >> GLOBAL VARIABLES
# =============================================================================
_bump_player = None


# =============================================================================
# >> ENTITY HOOKS
# =============================================================================
@EntityPreHook(EntityCondition.is_human_player, 'bump_weapon')
@EntityPreHook(EntityCondition.is_bot_player, 'bump_weapon')
def _pre_bump_weapon(stack_data):
    """Switch the player's team if they are a CT picking up the bomb."""
    global _bump_player
    if make_object(Entity, stack_data[1]).classname != 'weapon_c4':
        return
    _bump_player = make_object(Entity, stack_data[0])
    if _bump_player.team == 3:
        _bump_player.team = 2
    else:
        _bump_player = None


@EntityPostHook(EntityCondition.is_human_player, 'bump_weapon')
@EntityPostHook(EntityCondition.is_bot_player, 'bump_weapon')
def _post_bump_weapon(stack_data, return_value):
    """Switch the player's team back to CT if they just picked up the bomb."""
    global _bump_player
    if _bump_player is None:
        return
    _bump_player.team = 3
    _bump_player = None
