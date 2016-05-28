import iapws


class Pump():

    """
    Pump class

    Represents a pump in the Rankine cycle
    """

    def __init__(self, inletState):
        """
        Initializes the pump with the previous conditions

        inletState: The state of the steam on the Pump's inlet.
            Must be an IAPWS97 object
        """

        if not isinstance(inletState, iapws.IAPWS97):
            raise TypeError("inletState should be of type iawps.IAWPS97")

        self.inletState = inletState

    def simulate(self, desiredFinalPressure):
        """
        Simulates the pump and tries to have the exit quality
        as desiredOutletQuality. It does so by progressively and
        isentropically extracting work from the pump until
        the desired outlet quality is reached

        desiredOutletQuality: The quality of the pump exit
        """

        self.exitState = iapws.IAPWS97(P=desiredFinalPressure,
                                       s=self.inletState.s)

        self.workRequired = self.exitState.h - self.inletState.h
