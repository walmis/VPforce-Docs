# Basic Settings

The settings that define how your controls fundamentally feel (the spring model, force trim, axis control, and per-aircraft basics) in the order they appear under the **Basic Settings** section of the Settings tab. The badge lines and sub-setting tables are generated from the application's settings catalog, so they always match the app.

## Class

<!-- telemffb-effect name=type -->

The aircraft class: PropellerAircraft, TurbopropAircraft, JetAircraft, GliderAircraft, Helicopter, or a special class such as HPGHelicopter (choices depend on the simulator). The class decides which class defaults apply and which spring modes and effects are offered; see [How Settings Work](settings-model.md).

## Spring Mode

<!-- telemffb-effect name=spring_mode part=badges -->

The master selector for how the centering spring behaves. The available modes depend on the simulator, aircraft class, and device; an MSFS fixed-wing joystick offers different modes than DCS helicopter pedals or a collective. Each mode reveals its own sub-settings, listed below by mode.

- For **MSFS/X-Plane**, the spring modes are the core of the FFB implementation; see [Axis Control & Spring Modes](msfs-xp-axis-spring.md).
- For **DCS**, the default is the game-managed spring; the override modes are described in the [DCS guide](sim-dcs.md#joystick-spring-mode), including the [pedal modes](sim-dcs.md#pedal-spring-mode).
- For a **collective**, the modes are *No Spring* and *Hardware Force Trim*; see [Collective Spring Mode](msfs-xp-helicopters.md#collective-spring-mode).
- **Advanced Dynamic** is configured through its own curve editor; see [Advanced Spring & G-Force Curves](spring-curves.md).
- **Force Trim** (helicopters and gliders) holds the stick where you release the trim button; see [Helicopter Force Trim](msfs-xp-helicopters.md#helicopter-force-trim). Many gliders have a lever-actuated trim system that works the same way, which is why the aileron/elevator force-trim options exist for gliders too.

<!-- telemffb-effect name=spring_mode part=table -->

## Disable Collective Spring

<!-- telemffb-effect name=force_disable_collective_gain -->

When flying a fixed-wing aircraft with a collective connected, TelemFFB normally zeroes the collective's spring gain (a fixed-wing throttle has no centering spring). This option disables that behavior.

## Trim Wheel Buttons

<!-- telemffb-effect name=trimwheel_use_master_buttons -->

<!-- telemffb-effect name=trimwheel_elev_dn_button -->

<!-- telemffb-effect name=trimwheel_elev_up_button -->

For a VPforce trim wheel device: use button inputs from the master device (or the wheel itself), and bind the nose-down / nose-up trim buttons.

## Trim Workaround

<!-- telemffb-effect name=trim_workaround -->

Some DCS modules (AV-8B, MiG-19) do not implement native FFB trim following. This workaround mimics it by moving the physical joystick with the trim.

## Pedal Force Trim

<!-- telemffb-effect name=pedal_force_trim_enabled -->

Enables a static spring on the pedals with a force-trim release button: hold the button, position the pedals, release to lock the new center.

## IL2 Shake Master

<!-- telemffb-effect name=il2_shake_master part=badges -->

IL-2 implements its own basic FFB shake effects in-game. The Shake Master group replaces them with TelemFFB's more configurable versions: buffeting, runway rumble, and weapons effects, each individually adjustable. When using these, set the in-game "Shaking" intensity to 0; see the [IL-2 guide](sim-il2.md).

<!-- telemffb-effect name=il2_shake_master part=table -->

!!! note
    IL-2 provides a single combined buffeting channel (stall, gear, and so on share one intensity), a limitation of the IL-2 telemetry, not of TelemFFB. The *Dynamic Gunfire Mode* reads shell mass and velocity from telemetry, so lighter, faster-firing guns feel quicker and sharper than heavy cannon.

## Axis Control

<!-- telemffb-effect name=telemffb_controls_axes part=badges -->

MSFS/X-Plane only: TelemFFB becomes the source of the axis positions the simulator receives, the foundation for the spring modes, trim following, and autopilot following. The family includes the axis scales, hands-on detection, custom axis variables, and the entire Trim/AP Following tree.

!!! important
    When Axis Control is enabled in MSFS, you must **unbind the affected axes in MSFS** (or SPAD.neXt). See [Axis Control & Spring Modes](msfs-xp-axis-spring.md).

- Trim following and its gains: [Trim & Autopilot Following](msfs-xp-trim-following.md)
- The calibrated trim curve: [Automatic Trim Calibration](msfs-xp-trim-calibration.md)
- Hands-on detection and Force Mode: [Helicopters - Force Mode](msfs-xp-helicopters.md#force-mode-experimental)

<!-- telemffb-effect name=telemffb_controls_axes part=table -->

## Collective AP Spring Gain / Dampening

<!-- telemffb-effect name=collective_ap_spring_gain -->

HPG helicopters: the spring strength applied to the collective while the AFCS/autopilot commands it. See [HPG Airbus Helicopters](msfs-xp-helicopters.md#hpg-airbus-helicopters-msfs-only).

## HPG Pedal Spring Gain

<!-- telemffb-effect name=hpg_pedal_spring_gain -->

HPG helicopters: the pedal spring gain used by the AFCS integration, as a percent of the Configurator spring value.

## Co-Pilot/RIO Spring Override

<!-- telemffb-effect name=cp_spr_override_enabled part=badges -->

DCS multi-crew: temporarily overrides the joystick spring gain when you occupy a seat other than the pilot's, so the stick is not fighting you while you work the back seat. Optionally active only while a configured button is held.

<!-- telemffb-effect name=cp_spr_override_enabled part=table -->

## Autopilot Deadzone

<!-- telemffb-effect name=ap_active_deadzone_enabled part=badges -->

DCS: applies a device deadzone while the autopilot is engaged, preventing small FFB stick movements from feeding back into the AP control loop and causing false disconnects or oscillation. Supported on a limited set of modules; see [Autopilot Oscillation with FFB](sim-dcs.md#autopilot-oscillation-with-ffb).

<!-- telemffb-effect name=ap_active_deadzone_enabled part=table -->
