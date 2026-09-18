# System Settings (Per-Aircraft)

Non-effect settings that can be configured per aircraft, in the order they appear under the **System** section of the Settings tab. The badge lines and sub-setting tables are generated from the application's settings catalog, so they always match the app.

## TelemFFB Profile

<!-- telemffb-effect name=telemffb_profile -->

Selects a named TelemFFB settings profile to activate for this aircraft; see [Aircraft Profiles](aircraft-profiles.md).

## Configurator File

<!-- telemffb-effect name=vpconf -->

Pushes a specific `.vpconf` file (created with VPforce Configurator) to the device when this aircraft loads. The pushed profile stays active until another sim, class, or model setting pushes a different one. See [VPconf Profiles & Gain Overrides](vpconf-profiles.md).

## Override Configurator Sliders

<!-- telemffb-effect name=configurator_override_enabled part=badges -->

Directly modifies the per-effect-type gain sliders on the device when this aircraft loads, a lighter-weight alternative to pushing a whole `.vpconf` file. See [VPconf Profiles & Gain Overrides](vpconf-profiles.md#dynamic-configurator-gain-overrides).

<!-- telemffb-effect name=configurator_override_enabled part=table -->

## Command Runner

<!-- telemffb-effect name=command_runner_enabled part=badges -->

Executes a shell command when the aircraft loads: start a companion utility, run a batch script, or any other action executable from a command line.

!!! warning
    The command runs exactly as entered, with no validation. Treat it with the same care as anything you would type into a terminal.

<!-- telemffb-effect name=command_runner_enabled part=table -->

## Center on Pause/Slew

<!-- telemffb-effect name=center_spring_on_pause -->

Forces spring centering while the simulator is paused or in slew mode. When disabled, you will need to bring the axis close to center to re-establish axis control after unpausing.

## Keep Forces on Pause/Slew

<!-- telemffb-effect name=keep_forces_on_pause -->

Keeps the damper/inertia/friction forces active while the simulator is paused, instead of letting the stick go slack.
