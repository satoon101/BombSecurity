# ../bomb_security/info.py

"""Provides/stores information about the plugin."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Source.Python Imports
#   Cvars
from cvars.public import PublicConVar
#   Plugins
from plugins.info import PluginInfo


# =============================================================================
# >> PLUGIN INFO
# =============================================================================
info = PluginInfo()
info.name = 'Bomb Security'
info.author = 'Satoon101'
info.version = '1.0'
info.basename = 'bomb_security'
info.variable = info.basename + '_version'
info.url = 'http://forums.sourcepython.com/showthread.php?1104'
info.convar = PublicConVar(info.variable, info.version, info.name + ' Version')
