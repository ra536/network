""" How to run:
$ sudo mn --custom ~/path/to/python/file --topo rtopo

"""

from mininet.topo import Topo

class RTopo( Topo ):
    "Simple topology example."
    def createSwitchWithHosts ( self, name ):
	newSwitch = self.addSwitch( 's%s' % (name,) )
	for i in range(1,25):
	    newHost = self.addHost( 'h%s_%d' % (name, i) )
	    self.addLink( newHost, newSwitch )
	return newSwitch

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add remote access switches
	r1 = self.createSwitchWithHosts( 'R1' )
	r2 = self.createSwitchWithHosts( 'R2' )
	r3 = self.createSwitchWithHosts( 'R3' )

	# Connect them together (can be removed later...)
	self.addLink( r1, r2 )
	self.addLink( r2, r3 )
	
topos = { 'rtopo': ( lambda: RTopo() ) }

