import iapws

class Condenser:
    """
    The condenser class
    """

    def __init__(self, inletState):
        """
        Initializes the condenser with the previous conditions

        inletState: The state of the steam on the Condenser's inlet.
            Must be an IAPWS97 object
        """

        if not isinstance(inletState, iapws.IAPWS97):
            raise TypeError("inletState should be of type iawps.IAWPS97")

        self.inletState = inletState

    def simulate(self, desiredOutletTemp):
        """
        Simulates the Condenser and tries to get the exit temperature down
        to the desiredOutletTemp. This is done by continuously extracting h 
        while keeping the P constant.
        """

        exitState = self.inletState

        hDecrement = 1

        while exitState.T >= desiredOutletTemp:
            exitState = iapws.IAPWS97(h=exitState.h - hDecrement, P=exitState.P)
            print exitState.h

        self.exitState = exitState

        self.heatExtracted = self.inletState.h - self.exitState.h
