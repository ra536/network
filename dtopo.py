""" How to run:
$ sudo mn --custom ~/path/to/python/file --topo dtopo

"""

from mininet.topo import Topo

class DTopo( Topo ):
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

	# Add distribution switches
	d1 = self.addSwitch( 'sD1' )
	d2 = self.addSwitch( 'sD2' )
	d3 = self.addSwitch( 'sD3' )
	
	# Connect distribution for testing (can delete later...)
	self.addLink( d1, d2 )
	self.addLink( d2, d3 )

        # Add access switches
	for name in ["A1", "A2", "A3"]:
	    for i in range(1,4):
	        switchName = '%s_%s' % (name, i)
	        newSwitch = self.createSwitchWithHosts( switchName )
		if switchName[0] == "A":
		    if switchName[1] == "1":
		        self.addLink( newSwitch, d1 )
		    elif switchName[1] == "2":
		        self.addLink( newSwitch, d2 )
		    elif switchName[1] == "3":
			self.addLink( newSwitch, d3 )
	
topos = { 'dtopo': ( lambda: DTopo() ) }

