import turbine
import pump
import condenser
import boiler
import iapws
from tabulate import tabulate


def main():
    condenserOverCool = 0.1
    condenserPressure = 0.006

    desiredQuality = 0.9

    table = []

    for boilerPressure in [1, 1.5, 2]:
        turbineEntropy = iapws.IAPWS97(P=condenserPressure, x=desiredQuality).s

        turbineInletTemperature = iapws.IAPWS97(P=boilerPressure,
                                                s=turbineEntropy).T

        condenserExitState = iapws.IAPWS97(x=0,
                                           P=condenserPressure)
        condenserExitState = iapws.IAPWS97(h=condenserExitState.h -
                                           condenserOverCool,
                                           P=condenserPressure)

        p = pump.Pump(condenserExitState)
        p.simulate(boilerPressure)

        b = boiler.Boiler(p.exitState)
        b.simulate(turbineInletTemperature)

        boilerSaturationTemp = iapws.IAPWS97(P=boilerPressure, x=0.5).T
        degreeOfSuperheat = turbineInletTemperature - boilerSaturationTemp

        t = turbine.Turbine(b.exitState)
        t.simulate(condenserPressure)

        c = condenser.Condenser(t.exitState)
        c.simulate(condenserExitState.T)

        efficiency = (t.workExtracted - p.workRequired) / (b.heatAdded)

        table.append([boilerPressure, degreeOfSuperheat, efficiency])

    print tabulate(table, headers=["Boiler Pressure",
                                   "Degree of Superheat",
                                   "Efficiency"])


if __name__ == '__main__':
    main()
