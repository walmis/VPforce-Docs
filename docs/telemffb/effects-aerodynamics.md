# Aerodynamic Effects

The effects driven by airflow and angle-of-attack telemetry, in the order they appear under the **Aerodynamics** section of the Settings tab. Each entry shows which simulators and devices the effect applies to, what it does, and its sub-settings; the badge line and sub-setting tables are generated from the application's settings catalog, so they always match the app.

## Prop Diameter

<!-- telemffb-effect name=prop_diameter -->

Not an effect - a reference value. The propeller diameter feeds the dynamic airflow calculations for the prop-flow effects below. Shipped aircraft profiles set it; set it yourself when building a profile for a new propeller aircraft.

## AoA Reduction

<!-- telemffb-effect name=aoa_reduction_effect_enabled part=badges -->

Simulates the increased *forward* stick pressure some fighter aircraft apply when a critical angle of attack is exceeded. The effect monitors AoA and applies a linear force, starting at the *Critical AoA Start* angle and reaching *Max Force* at the *Critical AoA Max* angle. The force is a percentage of the constant-force value in VPforce Configurator.

<!-- telemffb-effect name=aoa_reduction_effect_enabled part=table -->

## Elevator Droop

<!-- telemffb-effect name=elevator_droop_enabled part=badges -->

At very low speeds (below ~20 kt) there is not enough airflow over the tail to hold the elevator up, and the stick slumps forward under the elevator's weight. This effect simulates that droop force for the sims with native FFB.

<!-- telemffb-effect name=elevator_droop_enabled part=table -->

## Elevator Droop Moment

<!-- telemffb-effect name=elevator_droop_moment -->

The MSFS/X-Plane counterpart of Elevator Droop: sets the strength of the forward stick force at rest, fading out as airspeed builds and the airflow takes the elevator's weight.

## Elevator Prop Flow / Rudder Prop Flow

<!-- telemffb-effect name=elevator_prop_flow_ratio -->

On propeller aircraft, the prop blows air over the tail, so the elevator and rudder feel firmer than airspeed alone would explain, especially at high power and low speed. These two ratios scale how much of that propwash contributes to the dynamic forces on each axis. *Prop Diameter* (above) feeds the same calculation.

<!-- telemffb-effect name=rudder_prop_flow_ratio -->

## AoA Effect

<!-- telemffb-effect name=aoa_effect_enabled part=badges -->

A constant force that builds with angle of attack: back pressure grows as the aircraft flies at higher AoA.

<!-- telemffb-effect name=aoa_effect_enabled part=table -->

!!! note "Per-sim behavior"
    The exposed settings differ per sim, as the Sims column shows: MSFS uses the enable toggle and gain, while DCS/BMS configure the effect through its max-force value.

## ETL Effect

<!-- telemffb-effect name=etl_effect_enable part=badges -->

Helicopters: the shudder as the rotor transitions through Effective Translational Lift. The effect plays while airspeed is between the start and stop speeds, shaking hardest in the middle of the band, matching the ETL vibration felt when accelerating through roughly 10-25 kt.

<!-- telemffb-effect name=etl_effect_enable part=table -->

## VRS Effect

<!-- telemffb-effect name=vrs_effect_enable part=badges -->

Helicopters: Vortex Ring State rumble. The effect arms only below the *Airspeed Threshold* (VRS cannot occur with forward airspeed), then ramps with sink rate, starting at the *Onset Vertical Speed* and reaching full intensity at the *Full Vertical Speed*.

<!-- telemffb-effect name=vrs_effect_enable part=table -->

## Blade Slap

<!-- telemffb-effect name=blade_slap_enable part=badges -->

Helicopters: the signature 'wop-wop' of blade-vortex interaction, rendered as sharp kicks through the controls at blade-passage rate (rotor RPM x blade count). The effect fires where you hear blade slap in the sim: shallow descents at moderate speed, decelerating approaches, flares, and loaded turns. It stays silent in level cruise, climbs, and on the ground. Two-bladed teetering rotors slap hardest; higher blade counts produce a faster, softer texture.

<!-- telemffb-effect name=blade_slap_enable part=table -->

!!! note "Per-sim behavior"
    **X-Plane** computes blade slap natively, and by default the effect is driven exclusively by that signal (including tail rotor slap). Disabling *Use Native Slap Telemetry* switches to the inferred method and activates the tuning sliders. **MSFS** and **DCS** have no native signal, so the effect infers slap from flight state: an airspeed band centered on *Blade Slap Band Center* (higher for heavily disc-loaded helicopters, lower for light rotors), a descent-gradient gate that matches wake re-entry geometry, and a G-loading term weighted by the *G-Induced Slap Factor* (set it to 0 for slap from descent geometry only). Per-model tuning ships for the default helicopter profiles.

## AoA/Stall Buffeting

<!-- telemffb-effect name=aoa_buffeting_enabled part=badges -->

Shakes the stick as the aircraft approaches the stall. Intensity builds from the buffet-onset angle of attack to the stall AoA, and scales with dynamic pressure relative to the aircraft's *own* stall speed, so a slow trainer buffets as fully at its stall as a jet does at its, and an accelerated stall at higher speed buffets harder.

<!-- telemffb-effect name=aoa_buffeting_enabled part=table -->

!!! note "Per-sim behavior"
    The AoA thresholds come from different places per sim. **MSFS** reads the aircraft's stall AoA directly from telemetry. **X-Plane** reports the aircraft's stall-warning threshold, and TelemFFB estimates the band around it. **DCS/BMS** provide neither, so the manual *Buffet Onset AoA* and *Stall AoA* settings define the band.

**Buffet Style** (MSFS/X-Plane): *Classic* is a steady single-frequency shake, the original effect. *Dynamic* is irregular and gusty, surging and ebbing like real separated-flow buffet and growing heavier and slower as the stall deepens. The *Buffeting Frequency* slider applies in both styles; in Dynamic it anchors the character sweep.

## Overspeed Shake

<!-- telemffb-effect name=overspeed_effect_enable part=badges -->

Airframe shake when the aircraft exceeds safe speed: the effect ramps up from the *Start Speed* toward maximum intensity as speed continues to build.

<!-- telemffb-effect name=overspeed_effect_enable part=table -->

## Turbulence Effect (Experimental)

<!-- telemffb-effect name=turbulence_effect_enable part=badges -->

Simulates the small, rapid wind disturbances of turbulent air. The simulator's relative-wind telemetry is analyzed for short-term fluctuations; rapid wind shifts are isolated through a high-pass filter and converted into randomized force impulses on the stick, a tactile "gusty air" feel. In calm weather the effect is minimal by design, since it works from real wind data.

<!-- telemffb-effect name=turbulence_effect_enable part=table -->

!!! tip
    Start with moderate values: Gust Memory 70%, Attack Speed 40%, Sensitivity 50%, Intensity 30%. Raising **Intensity** without balancing **Sensitivity** makes turbulence feel harsh and random.

## Wind Effect

<!-- telemffb-effect name=wind_effect_enabled part=badges -->

Wind-driven forces on the controls for the native-FFB sims, scaled between the overall scaling factor and the maximum intensity cap.

<!-- telemffb-effect name=wind_effect_enabled part=table -->
