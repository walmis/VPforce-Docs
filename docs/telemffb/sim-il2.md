# IL-2

!!! info inline end ""
    [All settings available in IL-2](effects-sim-il2.md)

## The DirectInput Tap

Both IL-2 titles compute their own force feedback: dynamic stick forces and shake effects. The [DirectInput Tap](dinput-tap.md) captures those effects and renders them through TelemFFB, where each effect type gets an enable toggle and a gain, and the game's spring gets per-axis corrections. To render the captured spring, select the **Game Managed (DirectInput Tap)** joystick spring mode.

### FFB pedals in IL-2 Korea

IL-2 Korea is the only supported simulator that renders force feedback to pedals. With the tap capturing the pedals, the pedals instance offers the **Game Managed (DirectInput Tap, Korea Only)** pedal spring mode, the game's own pedal forces rendered by TelemFFB. The label notes Korea because IL-2 Great Battles has no pedal FFB.

## Duplicate 'Shake' effects

IL2 implements FFB for dynamic stick forces and some very basic shake effects. TelemFFB implements duplicate (but far more configurable) effects which overlap with those that are implemented by IL2. To enable these specific settings, enable the "IL-2 Shake Master" setting in TelemFFB.

!!! note
    It is recommended to set the "Shaking" intensity in the IL-2 FFB control settings to 0 if you enable these settings in TelemFFB.

This can be found in Settings→Input Devices within the IL2 configuration

![](images/sim-il2/il2-input-shaking.png){ width="445px" height="126px" }

The IL2 Shake Master settings

![](images/sim-il2/il2-shake-master.png){ width="423px" height="204px" }

Each setting individually controls the intensity of that effect type:

- **Buffeting** - Controls the intensity of AoA Stall Buffeting

- **Runway Rumble** - Controls the intensity of bumping induced while taxiing

- **Weapons Effects (Master Toggle)**

    - **Dynamic Gunfire Mode**

        - When Enabled, the shell size and weight are used to calculate a dynamic effect frequency. In general, smaller lighter rounds will produce a higher frequency effect than larger, slower rounds.

            - Direct "rounds per second" telemetry is not available from the sim

    - **Gunfire** - Controls the intensity of the gunfire/canon effect
    - **Bombs** - Controls the intensity of the bomb-drop effect
    - **Rockets** - Controls the intensity of the rocket firing effect
