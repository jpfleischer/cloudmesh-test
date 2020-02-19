from __future__ import print_function

import platform

from cloudmesh.shell.command import PluginCommand
from cloudmesh.shell.command import command
from cloudmesh.windows.Windows import Windows


class WindowsCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_windows(self, args, arguments):
        """
        ::

          Usage:
                windows check

          This command is intended to check if your windows set up is
          correctly done.

          Bugs:
              This program is supposed to be implemented. It is at this
              time just a template

          Description:

          Checks we do

             1. are you running python 3.8.1
             2. are you having the newest version of pip
             3. is cl installed
             4. is nmake installed
             5. is the username without spaces


          Checks that are missing or need implemented

             6. are you running in a vnenv
             7. is the default mongo port used
             8. do you have docker installed
             9. do you have vbox installed
            10. is hyperv switched on or off
            11. how much memory do you have
            12. do you have free diskspace
            13. are containers running
            14. .... other tyings that can help us debug your environment

        """

        w = Windows()

        #
        # Python setup
        #
        w.check_venv()
        w.check_command("python --version", test="3.8.1")
        w.check_python()
        w.check_command("pip --version", test="20.0.2")

        #
        # command tool setup
        #

        if platform.system() == "Windows":
            w.check_command("cl")
            w.check_command("nmake")
        w.check_command("git --version", test="git version")
        w.check_command("ssh", test="usage", show=False)
        w.check_command("ssh-keygen --help", test="usage", show=False)

        w.is_user_name_valid()
        w.check_mongo()
        w.check_command("docker --version", test="Docker version")
        w.check_command("VirtualBox --help", test="Oracle VM VirtualBox VM Selector", show=False)

        w.usage()
        w.check_command("yamllint", test="usage: yamllint", show=False)
        w.check_yaml()
        return ""
