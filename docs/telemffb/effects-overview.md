# Effects Overview

This reference documents every effect and setting on the Settings tab. The pages mirror the tab itself: one page per section, entries in the same order the application lists them.

## The Settings-tab sections

- **[Basic Settings](effects-basic.md)** - spring modes, force trim, axis control, and per-aircraft basics
- **[Aerodynamics](effects-aerodynamics.md)** - airflow forces, stall buffeting, turbulence, ETL and VRS
- **[Inertial](effects-inertial.md)** - g-force, deceleration, and lateral-force effects
- **[Ground](effects-ground.md)** - runway rumble, touchdown, nosewheel shimmy, ground steering feel
- **[Mechanical\Airframe](effects-mechanical.md)** - engine rumble, moving surfaces and doors, damage, hydraulics
- **[Weapons](effects-weapons.md)** - gunfire, weapon release, countermeasures
- **[Basic FFB Effects](effects-ffb.md)** - damper, inertia, friction, deadzone (not telemetry-driven)
- **[System](effects-system.md)** - per-aircraft VPconf profiles, gain overrides, command runner, pause behavior

## Feel an effect before you fly

Most effects in this reference can be played on your device from the offline editor, at the strength your settings give them, with no simulator running. See [Effect Preview](effect-preview.md) for how it works and which effects have a preview.

## Browse by simulator

A directory of everything available in your sim, linking into the pages above:

[DCS World](effects-sim-dcs.md) · [IL-2 Sturmovik](effects-sim-il2.md) · [Falcon BMS](effects-sim-bms.md) · [Microsoft Flight Simulator](effects-sim-msfs.md) · [X-Plane](effects-sim-xplane.md)

## How to read the entries

Each effect entry opens with a badge line showing which simulators it applies to: <span class="sim-badge sim-dcs">DCS</span> <span class="sim-badge sim-il2">IL2</span> <span class="sim-badge sim-bms">BMS</span> <span class="sim-badge sim-msfs">MSFS</span> <span class="sim-badge sim-xplane">XP</span> - together with which device types can use it. Below the description, a table lists the effect's sub-settings; its **Sims** column shows "—" when a sub-setting matches its parent, and names the sims only where it *differs* - that column is where the per-sim nuances live.

Not every effect exists everywhere, and a shared name does not always mean identical behavior: some effects work from different telemetry per sim and expose different sub-settings (AoA/Stall Buffeting is the classic example). Where behavior differs, the entry says so in a *Per-sim behavior* note, and the [simulator guides](sim-msfs-xplane.md) carry the depth.
