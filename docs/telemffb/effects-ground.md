# Ground Effects

Effects for the aircraft's interaction with the surface, in the order they appear under the **Ground** section of the Settings tab. The badge lines and sub-setting tables are generated from the application's settings catalog, so they always match the app.

## Runway Rumble

<!-- telemffb-effect name=runway_rumble_enabled part=badges -->

Rolling vibration while taxiing, taking off, and landing; intensity follows the surface and speed.

<!-- telemffb-effect name=runway_rumble_enabled part=table -->

## Touch-Down Effect

<!-- telemffb-effect name=touchdown_effect_enabled part=badges -->

A single jolt at the moment of touchdown, scaled by how hard you land: the force ramps up to *Max Force* as the landing g reaches *Max G's*. Grease it on and you barely feel it; slam it down and you will.

<!-- telemffb-effect name=touchdown_effect_enabled part=table -->

## Nosewheel Shimmy

<!-- telemffb-effect name=nosewheel_shimmy part=badges -->

Pedal vibration simulating nosewheel shimmy under braking: it triggers only above a minimum speed and beyond a minimum brake application.

<!-- telemffb-effect name=nosewheel_shimmy part=table -->

## Steering Friction (Experimental)

<!-- telemffb-effect name=steering_friction part=badges -->

Ground steering feel for the pedals: friction that is heavy at taxi speed and decays as the aircraft accelerates and the nosewheel unloads, plus a steering-gear centering spring.

!!! note
    Requires the [Friction Override](effects-ffb.md) to be enabled; this effect scales the Configurator friction value.

<!-- telemffb-effect name=steering_friction part=table -->
