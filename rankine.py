import turbine
import pump
import condenser
import boiler
import iapws


def main():
    condenserExitTemp = 283
    condenserPressure = 0.006
    boilerPressure = 2
    turbineInletTemperature = 560

    condenserExitState = iapws.IAPWS97(T=condenserExitTemp,
                                       P=condenserPressure)
    p = pump.Pump(condenserExitState)
    p.simulate(boilerPressure)
    print "Pump Simulation Completed"
    print p.exitState.P, p.exitState.T, p.exitState.x

    b = boiler.Boiler(p.exitState)
    b.simulate(turbineInletTemperature)
    print "Boiler Simulation Completed"
    print b.exitState.P, b.exitState.T, b.exitState.x

    t = turbine.Turbine(b.exitState)
    t.simulate(condenserPressure)
    print "Turbine Simulation Completed"
    print t.exitState.P, t.exitState.T, t.exitState.x

    c = condenser.Condenser(t.exitState)
    c.simulate(condenserExitState.T)
    print "Condesner Simulation Completed"
    print c.exitState.P, c.exitState.T, c.exitState.x

    efficiency = (t.workExtracted - p.workRequired) / (b.heatAdded)
    print efficiency


if __name__ == '__main__':
    main()
