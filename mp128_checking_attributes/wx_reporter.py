import wx_observer

def show_summary(obs):
    print("\nObservation summary:")
    print(f"  Precipitation: {obs.precip}cm")
    print(f"  Temp:          {obs.temp}C")

show_summary(wx_observer.wx_obs)