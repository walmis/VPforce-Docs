# Mechanical & Airframe Effects

Effects driven by the mechanical state of the aircraft (engine vibration, moving surfaces and doors, damage, hydraulics) in the order they appear under the **Mechanical\Airframe** section of the Settings tab. The badge lines and sub-setting tables are generated from the application's settings catalog, so they always match the app.

## Controls Lock

<!-- telemffb-effect name=controls_lock_enable part=badges -->

For aircraft with a control lock (gust lock): while the configured sim variable reports the lock engaged, TelemFFB holds the controls firmly in place.

The variable can be an `L:Var`, a SimVar, or an MSFS 2024 input event written as `B:EVENT_NAME`. See [Input events](telem-overrides.md#input-events-b-variables) for how to find the name of a cockpit control.

<!-- telemffb-effect name=controls_lock_enable part=table -->

## Heli Engine/Rotor Rumble

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

## Fuel Boom/Door Motion

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

A stall-warning stick shaker: the distinct high-frequency square-wave shake of the real device, separate from the aerodynamic [AoA/Stall Buffeting](effects-aerodynamics.md#aoastall-buffeting). In MSFS it triggers from the sim's stall warning; DCS/BMS use the configurable AoA threshold.

<!-- telemffb-effect name=enable_stick_shaker part=table -->

## Tailhook Motion / Wing Fold Motion

<!-- telemffb-effect name=tailhook_motion_effect_enabled part=badges -->

Vibration while the tailhook or wing-fold mechanism is deploying or retracting.

<!-- telemffb-effect name=tailhook_motion_effect_enabled part=table -->

<!-- telemffb-effect name=wingfold_motion_effect_enabled part=table -->

## Low Hydraulic Pressure Effect (Experimental)

<!-- telemffb-effect name=enable_hydraulic_loss_effect part=badges -->

Simulates the heavy, sluggish controls of a failing hydraulic system: as the *HydSys* telemetry value falls from the configured threshold toward zero, the damper, inertia, and friction forces ramp from their normal values toward the levels configured here.

<!-- telemffb-effect name=enable_hydraulic_loss_effect part=table -->

!!! note
    Requires the damper/inertia/friction [overrides](effects-ffb.md) to be enabled, and headroom left in them; if your base forces already sit at 100%, there is no room to increase them. To set the threshold for a new aircraft, observe the normal *HydSys* value in the Monitor tab and set the threshold below it.

!!! warning
    Increase these forces carefully; too much inertia or friction can cause motor instability and a protective shutdown.

## Vibration from Telemetry (FlyInside)

<!-- telemffb-effect name=FI_vibration_enable part=badges -->

For FlyInside helicopters in MSFS: renders the vibration data exported by the FlyInside flight model directly. See [FlyInside Helicopters](msfs-xp-helicopters.md#flyinside-helicopters-msfs-only).

<!-- telemffb-effect name=FI_vibration_enable part=table -->
