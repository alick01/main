#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools

def setup():
    #pisitools.dosed("meson.build", "2.33.2", "2.33.1")
    #pisitools.dosed("meson.build", "2.37.1", "2.36.4")
    # pisitools.dosed("meson.build", "webkitgtk-6.0", "webkitgtk-4.1")
    # pisitools.dosed("meson.build", "webkitgtk-web-process-extension-6.0", "webkitgtk-web-process-extension-4.1")
    mesontools.configure("-Dunit_tests=disabled")

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dodoc("COPYING", "README.md", "CONTRIBUTING.md", "HACKING.md")
