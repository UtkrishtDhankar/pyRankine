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

        self.exitState = iapws.IAPWS97(P=self.inletState.P,
                                       T=desiredOutletTemp)

        self.heatExtracted = self.inletState.h - self.exitState.h
