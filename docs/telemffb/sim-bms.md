# Falcon BMS

!!! info inline end ""
    [All settings available in BMS](effects-sim-bms.md)

TelemFFB supports Falcon BMS 4.38 and later as a **beta** integration.

## Setup

Enable BMS on the **Simulator Setup** tab ([Connecting Your Simulator](sim-setup.md#bms-beta-support)). No export script or plugin is required; TelemFFB reads the BMS shared-memory telemetry directly, so BMS and TelemFFB must run on the same PC.

## How TelemFFB fits with BMS

BMS sits between the sim categories. The game supports native FFB with a limited set of effects, and the primary F-16 is fly-by-wire, so its side-stick has no traditional force-feel to model in the first place. TelemFFB's role is therefore mostly **haptic augmentation**: gunfire, buffeting, touchdown, and similar event and state effects layered on top, the same way it supplements DCS.

Internally, BMS uses the same aircraft effect implementations as DCS, driven by the shared-memory telemetry. The [BMS settings directory](effects-sim-bms.md) lists everything available.

BMS's own native FFB effects can also be captured and rendered through TelemFFB with the [DirectInput Tap](dinput-tap.md), which adds a per-type enable and gain for each of the game's effects.

## Notes and limitations

- **Afterburner detection is estimated** - BMS does not export afterburner state directly, so TelemFFB infers it from nozzle position and fuel flow.
- Some effect settings may not behave as expected where the shared-memory telemetry is limited or absent for a given value.
- The integration has had comparatively little field testing. If something does not work or feels wrong, feedback genuinely improves it; report on the **[#TelemFFB-User](https://discord.com/channels/965234441511383080/968208779084701716)** channel on the VPforce Discord.

For connection problems, see the [Falcon BMS troubleshooting section](../rhino/game-specific-troubleshooting.md#falcon-bms).
