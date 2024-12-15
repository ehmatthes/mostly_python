import wx_observer
import wx_observer_wind

def show_summary(obs):
    print("\nObservation summary:")
    print(f"  Precipitation: {obs.precip}cm")
    print(f"  Temp:          {obs.temp}C")

    try:
        print(f"  Wind:          {obs.wind}kph")
    except AttributeError:
        pass

show_summary(wx_observer.wx_obs)
show_summary(wx_observer_wind.wx_obs)
