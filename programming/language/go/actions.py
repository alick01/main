#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

NoStrip=["/"]

def build():
    
    shelltools.export("GOROOT", "%s/go-go1.6.2" % get.workDIR()) #0
    shelltools.export("GOBIN", "$GOROOT/bin") #1
    shelltools.export("GOPATH", "%s" % get.workDIR())
    #shelltools.export("GOROOT_FINAL", "/usr/lib/go")
    shelltools.export("GOROOT_BOOTSTRAP", "%s/go-go1.6.2/go-linux-amd64-bootstrap" % get.workDIR())  #2

    shelltools.export("GOOS","linux")
    shelltools.export("GOARCH","amd64")
    
    shelltools.cd("src")

    shelltools.system("./make.bash")

    #shelltools.cd("%s/go-go1.6.2" % get.workDIR())

    #shelltools.system("$GOROOT/bin/go get -d golang.org/x/tools/cmd/godoc")
    #shelltools.system("$GOROOT/bin/go build -o $GOPATH/godoc golang.org/x/tools/cmd/godoc")

    #for tool in ["godex", "godoc", "goimports", "gomvpkg", "gorename", "gotype", "benchcmp", "bundle", "callgraph", "digraph", "eg", "fiximports", "html2article", "oracle", #"present", "ssadump", "stress", "stringer"]:
    #    shelltools.system("$GOROOT/bin/go get -d golang.org/x/tools/cmd/%s" % tool)
    #    shelltools.system("$GOROOT/bin/go build -v -x -o $GOROOT/pkg/tool/$GOOS\_$GOARCH/%s golang.org/x/tools/cmd/%s" % (tool, tool))


def install():  
    shelltools.cd("%s/go-go1.6.2" % get.workDIR())

    pisitools.dodir("/usr/lib/go")
    shelltools.system("cp -rp api bin doc lib pkg src  %s/usr/lib/go" % get.installDIR())
        
    pisitools.dosym("/usr/lib/go/bin/go", "/usr/bin/go")
    pisitools.dosym("/usr/lib/go/bin/gofmt", "/usr/bin/gofmt")
    
    shelltools.system("cp -R doc  %s/usr/lib/go" % get.installDIR())
    shelltools.system("cp -R lib  %s/usr/lib/go" % get.installDIR())
    shelltools.system("cp -R pkg  %s/usr/lib/go" % get.installDIR())
    shelltools.system("cp -R src  %s/usr/lib/go" % get.installDIR())
    
#    shelltools.chmod("%s/usr/lib/go/bin" % get.installDIR(), 0755)
#    shelltools.chmod("%s/usr/lib/go/pkg/tool" % get.installDIR(), 0755)

    shelltools.system("cp -a misc  %s/usr/lib/go" % get.installDIR())
    
    pisitools.removeDir("/usr/lib/go/pkg/bootstrap")
 
    pisitools.dodoc("VERSION", "LICENSE", "PATENTS", "README*", "AUTHORS", "CONTRIBUTORS")
