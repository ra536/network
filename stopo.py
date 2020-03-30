""" How to run:
$ sudo mn --custom ~/path/to/python/file --topo stopo

"""

from mininet.topo import Topo

class STopo( Topo ):
    "Simple topology example."
    def createSwitchWithHosts ( self, name ):
	newSwitch = self.addSwitch( 's%s' % (name,) )
	for i in range(1,4):
	    newHost = self.addHost( 'h%s_%d' % (name, i) )
	    self.addLink( newHost, newSwitch )
	return newSwitch

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add remote access switches
	d1 = self.createSwitchWithHosts( 'D1' )
	
topos = { 'stopo': ( lambda: STopo() ) }

