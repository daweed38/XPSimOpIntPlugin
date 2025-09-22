##################################################
# Sim Open Interface X-Plane Plugin
##################################################
# PI_XPSimOpInt.py REV 1.0
# FarmerSoft © 2025
# By Daweed
##################################################

# System Module Import
# import os
# from datetime import datetime
# import threading

# XPPython3 Module Import
import xp


class PythonInterface:

    ##################################################
    # Plugin Class Initialisation (Required)
    ##################################################

    def __init__(self):
        self.Name = "XPSimOpInt"
        self.Sig = "xpsimopint.xppython3"
        self.Desc = "Sim Open Interface X-Plane plugin"

        self.debug = 0
        self.aircraftdir = xp.extractFileAndPath(xp.getNthAircraftModel(0)[1])[1].removeprefix(xp.getSystemPath())
        self.configdir = self.aircraftdir + '/plugins/PythonPlugins/SimOpInt/Config'

    ##################################################
    # Plugin System Method (Required)
    ##################################################

    def XPluginStart(self):
        # Required by XPPython3
        # Called once by X-Plane on startup (or when plugins are re-starting as part of reload)
        # You need to return three strings
        return self.Name, self.Sig, self.Desc

    def XPluginStop(self):
        # Called once by X-Plane on quit (or when plugins are exiting as part of reload)
        # Return is ignored
        pass

    def XPluginEnable(self):
        # Required by XPPython3
        # Called once by X-Plane, after all plugins have "Started" (including during reload sequence).
        # You need to return an integer 1, if you have successfully enabled, 0 otherwise.
        return 1

    def XPluginDisable(self):
        # Called once by X-Plane, when plugin is requested to be disabled. All plugins
        # are disabled prior to Stop.
        # Return is ignored
        pass

    def XPluginReceiveMessage(self, inFromWho, inMessage, inParam):
        # Called by X-Plane whenever a plugin message is being sent to your
        # plugin. Messages include MSG_PLANE_LOADED, MSG_ENTERED_VR, etc., as
        # described in XPLMPlugin module.
        # Messages may be custom inter-plugin messages, as defined by other plugins.
        # Return is ignored
        pass

    ##################################################
    # Plugin System Method
    ##################################################

    ##################################################
    # Plugin Configuration Method
    ##################################################

    ##################################################
    # Plugin Menu Callback Method
    ##################################################

    ##################################################
    # Plugin Flight Loop Callback Method
    ##################################################

    ##################################################
    # Plugin Interface Method
    ##################################################

    ##################################################
    # DataRef & Command Method
    ##################################################

    ##################################################
    # Plugin Data Method
    ##################################################
