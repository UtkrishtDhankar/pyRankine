import iapws


class Boiler:
    """
    The boiler class
    """

    def __init__(self, inletState):
        """
        Initializes the boiler with the previous conditions

        inletState: The state of the steam on the Boiler's inlet.
            Must be an IAPWS97 object
        """

        if not isinstance(inletState, iapws.IAPWS97):
            raise TypeError("inletState should be of type iawps.IAWPS97")

        self.inletState = inletState

    def simulate(self, desiredOutletTemp):
        """
        Simulates the Boiler and tries to get the exit temperature down
        to the desiredOutletTemp. This is done by continuously adding h
        while keeping the P constant.
        """

        exitState = self.inletState

        hIncrement = 1

        while exitState.T <= desiredOutletTemp:
            exitState = iapws.IAPWS97(h=exitState.h + hIncrement,
                                      P=exitState.P)

        self.exitState = exitState

        self.heatAdded = self.exitState.h - self.inletState.h
