# Mechanical & Airframe Effects

Effects driven by the mechanical state of the aircraft (engine vibration, moving surfaces and doors, damage, hydraulics) in the order they appear under the **Mechanical\Airframe** section of the Settings tab. The badge lines and sub-setting tables are generated from the application's settings catalog, so they always match the app.

## Controls Lock

<!-- telemffb-effect name=controls_lock_enable part=badges -->

For aircraft with a control lock (gust lock). While the configured sim variable reports the lock engaged, TelemFFB holds the controls in the locked position. The stick and pedals lock at center, and the collective locks fully down.

When the lock engages, a centering spring pulls the control to the locked position. Once the control is there, TelemFFB holds it with detents and stops the spring. On a device without detent support, the spring stays on and holds the control by itself. A damper also runs for as long as the lock is engaged. When the lock releases, TelemFFB returns the controls to their normal forces.

- **Controls Lock Force** sets the strength of the detents and the centering spring.
- **Controls Lock Damper** adds damping while the controls are locked. Very strong detents can make the stick bounce or oscillate; the damper settles it.

Changes to either setting apply at once, even while the controls are locked. The **Monitor** tab lists the lock's effects as **Controls Lock Spring**, **Controls Lock Lower Bound**, **Controls Lock Upper Bound** and **Controls Lock Damper**.

The variable can be an `L:Var`, a SimVar, or an MSFS 2024 input event written as `B:EVENT_NAME`. See [Input events](telem-overrides.md#input-events-b-variables) for how to find the name of a cockpit control.

The built-in profiles for these MSFS aircraft include a control lock: the Saab 340, A2A Piper PA-24, Black Square A36 and B36TP Bonanza, Baron 58, Duke, Grand Duke, Turbine Duke and Commander 114TC, Flysimware C414AW, Pilatus PC-6, Wilga, and Taog's Hangar H500C and OH-6A.

<!-- telemffb-effect name=controls_lock_enable part=table -->

## Heli Engine/Rotor Rumble { #heli-engine-rotor-rumble }

<!-- telemffb-effect name=engine_rotor_rumble_enabled part=badges -->

Helicopter engine and rotor vibration, driven by rotor RPM and blade count.

<!-- telemffb-effect name=engine_rotor_rumble_enabled part=table -->

## Afterburner Rumble

<!-- telemffb-effect name=afterburner_effect_enabled part=badges -->

Rumble while the afterburner is lit, scaled by afterburner stage where the telemetry provides it.

<!-- telemffb-effect name=afterburner_effect_enabled part=table -->

## Engine Rumble - Shake Telemetry (IL-2)

<!-- telemffb-effect name=il2_prop_eng_shake_enabled part=badges -->

IL-2 exports its physics engine's own computed engine-shake amplitude and frequency. These effects (one for props, one for jets) render that telemetry directly: startup lope, roughness, and damage arrive in the shake automatically. They are an alternative to the RPM-based rumble effects below: enable one or the other, not both.

<!-- telemffb-effect name=il2_prop_eng_shake_enabled part=table -->

<!-- telemffb-effect name=il2_jet_eng_shake_enabled part=table -->

## Propeller Rumble

<!-- telemffb-effect name=engine_prop_rumble_enabled part=badges -->

RPM-driven piston-engine and propeller vibration. The two RPM/intensity pairs work together: at the *Low RPM* value the effect plays at *Low Intensity*, ramping toward *High Intensity* at the *High RPM* value. These are not floor values: below *Low RPM* (engine start, shutdown) the intensity keeps increasing above *Low Intensity*.

!!! tip
    High-frequency vibration feels stronger than low-frequency vibration at equal intensity, so the *High RPM* intensity should be set **lower** than the *Low RPM* intensity.

<!-- telemffb-effect name=engine_prop_rumble_enabled part=table -->

## Jet Engine Rumble

<!-- telemffb-effect name=engine_jet_rumble_enabled part=badges -->

Turbine rumble scaled by engine power, at a configurable base frequency.

<!-- telemffb-effect name=engine_jet_rumble_enabled part=table -->

## Canopy Motion

<!-- telemffb-effect name=canopy_motion_effect_enabled part=badges -->

Vibration while the canopy is opening or closing.

<!-- telemffb-effect name=canopy_motion_effect_enabled part=table -->

## Damage Effect

<!-- telemffb-effect name=damage_effect_enabled part=badges -->

A short bump in a random direction, at randomized intensity, each time the aircraft takes damage; some hits land harder than others by design.

<!-- telemffb-effect name=damage_effect_enabled part=table -->

## Flaps Motion

<!-- telemffb-effect name=flaps_motion_effect_enabled part=badges -->

Vibration while the flaps are in motion.

<!-- telemffb-effect name=flaps_motion_effect_enabled part=table -->

## Fuel Boom/Door Motion { #fuel-boom-door-motion }

<!-- telemffb-effect name=fuelboom_motion_effect_enabled part=badges -->

Vibration while the refueling boom receptacle or door is deploying or retracting.

<!-- telemffb-effect name=fuelboom_motion_effect_enabled part=table -->

## Gear Buffet

<!-- telemffb-effect name=gear_buffet_effect_enabled part=badges -->

Aerodynamic buffet from extended landing gear, growing with airspeed between the low- and high-intensity speeds.

<!-- telemffb-effect name=gear_buffet_effect_enabled part=table -->

## Gear Motion

<!-- telemffb-effect name=gear_motion_effect_enabled part=badges -->

Vibration while the gear is in transit, with clunks at the ends of travel.

<!-- telemffb-effect name=gear_motion_effect_enabled part=table -->

## Speedbrake Buffet / Speedbrake Motion

<!-- telemffb-effect name=speedbrake_buffet_effect_enabled part=badges -->

Buffet while the speed brake is deployed, and vibration while it is moving.

<!-- telemffb-effect name=speedbrake_buffet_effect_enabled part=table -->

<!-- telemffb-effect name=speedbrake_motion_effect_enabled part=table -->

## Spoiler Buffet / Spoiler Motion

<!-- telemffb-effect name=spoiler_buffet_effect_enabled part=badges -->

Buffet while spoilers are deployed, and vibration while they move (motion effect currently F-14 only).

<!-- telemffb-effect name=spoiler_buffet_effect_enabled part=table -->

<!-- telemffb-effect name=spoiler_motion_effect_enabled part=table -->

## Stick Shaker

<!-- telemffb-effect name=enable_stick_shaker part=badges -->

A stall-warning stick shaker: the distinct high-frequency square-wave shake of the real device, separate from the aerodynamic [AoA/Stall Buffeting](effects-aerodynamics.md#aoa-stall-buffeting). In MSFS it triggers from the sim's stall warning; DCS/BMS use the configurable AoA threshold.

<!-- telemffb-effect name=enable_stick_shaker part=table -->

## Tailhook Motion / Wing Fold Motion

<!-- telemffb-effect name=tailhook_motion_effect_enabled part=badges -->

Vibration while the tailhook or wing-fold mechanism is deploying or retracting.

<!-- telemffb-effect name=tailhook_motion_effect_enabled part=table -->

<!-- telemffb-effect name=wingfold_motion_effect_enabled part=table -->

## Low Hydraulic Pressure Effect (Experimental)

<!-- telemffb-effect name=enable_hydraulic_loss_effect part=badges -->

Simulates the heavy, sluggish controls of a failing hydraulic system: as the aircraft's hydraulic state falls from the configured threshold toward zero, the damper and friction forces ramp from their normal values toward the levels configured here.

<!-- telemffb-effect name=enable_hydraulic_loss_effect part=table -->

!!! note
    Requires the damper and friction [overrides](effects-ffb.md) to be enabled, and headroom left in them; if your base forces already sit at 100%, there is no room to increase them. To set the threshold for a new aircraft, observe the normal *HydSys* value in the Monitor tab and set the threshold below it.

!!! warning
    Increase these forces carefully; too much damper or friction can cause motor instability and a protective shutdown.

### Custom Hydraulic Variable (MSFS)

TelemFFB reads the aircraft's hydraulic state from **HYDRAULIC SYSTEM INTEGRITY**. Some aircraft model their hydraulics in their own variables and never change it. For those, enable **Custom Hydraulic Variable** and enter the variable that shows the hydraulic state: a SimVar, an L:Var or an input event (`B:`).

The effect needs a value from 0 (no hydraulics) to 1 (normal). A switch, or a value that already reads 0 to 1, works as it is. For anything else, enter a **Transform to 0-1**, with `x` standing for the variable's value. The syntax is the same as the Scale field in the [overrides editor](telem-overrides.md):

| The variable reads | Transform |
|---|---|
| A pressure, 3000 when normal | `x/3000` |
| A percentage | `x/100` |
| A failure flag, 1 when failed | `1-x` |

The Monitor tab shows the raw value as *HydSys* and the result as *_hyd_health*. A transform TelemFFB cannot read is reported as a configuration error. The built-in profiles for the FlyInside Bell 206 and the CowanSim R66 already set this variable.

## Vibration from Telemetry (FlyInside)

<!-- telemffb-effect name=FI_vibration_enable part=badges -->

For FlyInside helicopters in MSFS: renders the vibration data exported by the FlyInside flight model directly. See [FlyInside Helicopters](msfs-xp-helicopters.md#flyinside-helicopters-msfs-only).

<!-- telemffb-effect name=FI_vibration_enable part=table -->
