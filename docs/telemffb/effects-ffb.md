# Basic FFB Effects

Unlike everything else in this reference, these effects are **not telemetry-driven**. They apply constant device-level forces per aircraft, on top of whatever the active VPforce Configurator profile provides, each expressed as a percentage of the corresponding Configurator slider value. They appear under the **Basic FFB Effects** section of the Settings tab.

The [Low Hydraulic Pressure Effect](effects-mechanical.md#low-hydraulic-pressure-effect-experimental) and [Steering Friction](effects-ground.md#steering-friction-experimental) build on these overrides; they need the relevant override enabled, with headroom left below 100%.

## Damper Override

<!-- telemffb-effect name=enable_damper_ovd part=badges -->

Smooths and resists stick motion: velocity-proportional resistance.

<!-- telemffb-effect name=enable_damper_ovd part=table -->

## Inertia Override

<!-- telemffb-effect name=enable_inertia_ovd part=badges -->

Adds apparent mass to the controls: acceleration-proportional resistance.

<!-- telemffb-effect name=enable_inertia_ovd part=table -->

## Friction Override

<!-- telemffb-effect name=enable_friction_ovd part=badges -->

Constant sliding resistance to stick motion.

<!-- telemffb-effect name=enable_friction_ovd part=table -->

## Enable Configurator Deadzone

<!-- telemffb-effect name=enable_deadzone part=badges -->

An always-on circular deadzone, equivalent to setting a deadzone in the Configurator, but configurable per aircraft.

<!-- telemffb-effect name=enable_deadzone part=table -->
