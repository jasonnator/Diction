#-------------------------------------------------------------------------------
# Name:        os_emulator
# Purpose:
#
# Author:      Jason Decastro
#
# Created:     07/09/2013
# Copyright:   (c) Jason Decastro 2013
# Licence:     GNU/Diction 3.0.0-12-generic i686
#-------------------------------------------------------------------------------

import getpass, time, subprocess, sqlite3
from controllers.operator import *

def main():
    obj = Login()
    obj.login()

if __name__ == '__main__':
    main()