import iapws


class Turbine():

    """
    Turbine class

    Represents a turbine in the Rankine cycle
    """

    def __init__(self, inletState):
        """
        Initializes the turbine with the previous conditions

        inletState: The state of the steam on the Turbine's inlet.
            Must be an IAPWS97 object
        """

        if not isinstance(inletState, iapws.IAPWS97):
            raise TypeError("inletState should be of type iawps.IAWPS97")

        self.inletState = inletState

    def simulate(self, desiredOutletPressure):
        """
        Simulates the turbine and tries to have the exit quality
        as desiredOutletQuality. It does so by progressively and
        isentropically extracting work from the turbine until
        the desired outlet quality is reached

        desiredOutletQuality: The quality of the turbine exit
        """

        self.exitState = iapws.IAPWS97(P=desiredOutletPressure,
                                       s=self.inletState.s)

        self.workExtracted = - self.exitState.h + self.inletState.h
