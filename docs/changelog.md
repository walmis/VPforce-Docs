# Changelog
- **September 17, 2026:**

    - Rewrote **[Aircraft Profiles](telemffb/aircraft-profiles.md)** for the new profile matching: [how an aircraft is matched](telemffb/aircraft-profiles.md#how-telemffb-matches-an-aircraft), the [Multiple matching profiles](telemffb/aircraft-profiles.md#when-your-profile-and-a-built-in-both-match) prompt and merge, and the [split button](telemffb/aircraft-profiles.md#giving-the-loaded-aircraft-its-own-profile). Updated the New Aircraft Wizard steps and screenshots.
    - Updated **[Telemetry Overrides](telemffb/telem-overrides.md)** with the [Class, Default and User tiers](telemffb/telem-overrides.md#where-an-aircrafts-overrides-come-from), the editor's Source column, and [input events](telemffb/telem-overrides.md#input-events-b-variables) (`B:` variables).
    - Corrected the cloning guidance in **[Aircraft with Special Treatment](telemffb/msfs-xp-special-aircraft.md)**: only some of these aircraft need a cloned profile, and the roster now says which.
    - Added **[Device recovery](telemffb/devices-instances.md#device-recovery)** and updated the [device status indications](telemffb/ui-overview.md#deviceinstance-status-indications).
    - Added **Device problems** and **[Reading the log](telemffb/troubleshooting.md#reading-the-log)** to Troubleshooting.
    - Updated [UI Overview](telemffb/ui-overview.md), [How Settings Work](telemffb/settings-model.md) and the [helicopter force trim](telemffb/msfs-xp-helicopters.md#helicopter-force-trim) notes to match.

- **September 13, 2026:**

    - Added **[Effect Preview](telemffb/effect-preview.md)** - a new page on playing an effect on the device from the offline editor with no simulator running: the two ways into the editor (the Profiles menu and the **Offline/Preview Mode** button for a loaded aircraft), the **▶** and **▶▶** buttons, the tooltip that states what each preview represents, the confirmation for constant-force previews, and a table of every effect that can be previewed with what its preview plays
    - Updated the [Profiles menu](telemffb/ui-overview.md#profiles-menu) and [Settings tab](telemffb/ui-overview.md#settings-tab) descriptions and the [offline editor](telemffb/settings-model.md#offlineglobal-simclass-configuration) section for the renamed **Offline Editor/Effect Preview** entry and the new corner button
    - Restored the missing **AoA/Stall Buffeting** heading in the [Aerodynamics](telemffb/effects-aerodynamics.md#aoastall-buffeting) reference, so the entry no longer appears under Blade Slap and links to it resolve

- **September 9, 2026:**

    - Added **[Black Box Not Reading the Grip](products/grip-adapters.md#black-box-not-reading-the-grip)** to the [Grip Adapters](products/grip-adapters.md) page - community-sourced fixes for when a VKB grip is not detected or its buttons do not reach the Rhino: flashing the correct Black Box firmware and pressing Default, running the Black Box in standalone mode, the Gunfighter Mk4 firmware-before-v2.20 requirement, and a continuity check of the connector's three contacts (with a pinout photo) to isolate wiring faults

- **August 27, 2026:**

    - Added **[The DirectInput Tap](telemffb/dinput-tap.md)** - a new page covering the game-side capture wrapper for DCS, IL-2, and Falcon BMS: what it does, per-sim setup from System Settings, the **Game Managed (DirectInput Tap)** spring modes (including IL-2 Korea's FFB pedals), per-effect-type toggles and gains for the game's own effects, the start-order rule, misconfiguration warnings, the configuration file, and updates/removal
    - Documented **[multiple joysticks and per-aircraft device selection](telemffb/devices-instances.md#multiple-joysticks-msfs-x-plane)** for MSFS and X-Plane: alternate device rows on the joystick card, the primary marker, live switching at save, and the per-aircraft **Device** section
    - Updated [System Settings](telemffb/configuration.md) for the reduced restart requirements (most changes now apply live; a restart is prompted only for master-device, auto-launch, or theme changes) and the DirectLink integration toggle with its status line
    - Added DirectInput Tap cross-references and the tap spring mode to the [DCS](telemffb/sim-dcs.md), [IL-2](telemffb/sim-il2.md) (including Korea pedal FFB), and [BMS](telemffb/sim-bms.md) guides
    - Documented the System Settings [File menu](telemffb/configuration.md#import-export-and-reset) - settings export/import for backup and machine migration, and Reset to Defaults, none of which commit until Save
    - Rewrote [System Settings](telemffb/configuration.md) for the reorganized dialog - three tabs (Devices / System / Simulator Setup), the per-device Device Settings panels that replace the retired Startup Behavior page, the now-global update prompt setting, and the master-only dialog that configures every instance - with matching updates to [Devices & Instances](telemffb/devices-instances.md) (device cards carry the launch controls), the Quick Start, and [Connecting Your Simulator](telemffb/sim-setup.md)

- **August 16, 2026:**

    - Added **[Blade Slap](telemffb/effects-aerodynamics.md#blade-slap)** to the Aerodynamic Effects reference - the new helicopter blade-vortex interaction effect (MSFS, X-Plane, DCS): sharp blade-passage kicks in descents, flares, and loaded turns, with X-Plane's native slap signal (and the *Use Native Slap Telemetry* toggle) or the inferred flight-state method with *Band Center* and *G-Induced Slap Factor* tuning
    - Re-vendored the settings reference data so the new Blade Slap settings appear in the generated tables
    - Added **[X-Trident AW109](telemffb/msfs-xp-helicopters.md#x-trident-aw109-x-plane-only)** setup guide to the Helicopters chapter: the aircraft's required Configurations-page settings (servo motors, per-axis toggles, non-centering options, force-trim release modes, recommended input gains) with an annotated screenshot, and the pedal-following AFCS Threshold / Response Rate tuning notes
    - Updated the [Aircraft with Special Treatment](telemffb/msfs-xp-special-aircraft.md#x-trident-aw109sp) AW109SP entry: the pedals now actively track the anti-torque requirement (the "pedal AFCS less active than the real aircraft" known issue is resolved)

- **August 15, 2026:**

    - Added **[Aircraft with Special Treatment](telemffb/msfs-xp-special-aircraft.md)** - a dedicated page cataloguing every MSFS/X-Plane addon aircraft with a dedicated class or curated default profile (HPG H145/H160, FlyInside B206/B47, the ten-model CowanSim fleet, Taog's Hangar H500C/OH6A and UH-1H/205-A1B, Simfocus Bell 407, A2A Comanche, X-Trident AW109SP), what each integration does, and why additional profiles for these aircraft must be cloned from the default rather than created from scratch
    - Renamed the SimConnect/Dataref Overrides page to **[Telemetry Overrides](telemffb/telem-overrides.md)** to match the application, and documented the status-area **Telem Ovd** indicator with its Default/User tier counts
    - Added **[How the Axis Positions Reach the Sim](telemffb/msfs-xp-axis-spring.md#how-the-axis-positions-reach-the-sim)** to Axis Control & Spring Modes - the default SimConnect axis events per aircraft class, the input range and sensitivity notes, and the X-Plane plugin's override and position datarefs (including the sim's designated prop-ratio collective mapping)
    - Added **[Exception Tracking & Reporting](telemffb/troubleshooting.md#exception-tracking-reporting)** - the status-bar Errors counter, the Logged Exceptions viewer with deduplication and child-instance forwarding, and the Report Exceptions upload flow - plus a [Status Bar](telemffb/ui-overview.md#status-bar) section in the UI overview
    - Updated **[Exception Tracking & Reporting](telemffb/troubleshooting.md#exception-tracking-reporting)** for the new report dialog: the optional Discord username (session-only, shown in the uploaded file name) and the additional-information field, with a refreshed screenshot

- **August 8, 2026 (later):**

    - Added a **[Troubleshooting & Getting Help](telemffb/troubleshooting.md)** page for the TelemFFB Manual: status-area triage, links to the per-sim troubleshooting checklists, log and support-bundle locations, and a short FAQ
    - Added a **[Falcon BMS guide](telemffb/sim-bms.md)** covering setup, how TelemFFB augments the F-16's fly-by-wire stick, and the beta integration's limitations
    - Documented **device auto-assignment** and the per-role device selector pulldowns in [Devices & Instances](telemffb/devices-instances.md), and updated the Quick Start and Troubleshooting pages to match
    - Documented **[Profile Notes](telemffb/ui-overview.md#profile-notes)** - curated notes on shipped profiles, adding your own notes, and the flashing notes icon
    - Rewrote **[VPforce Configurator Integration](telemffb/vpconf-profiles.md)** around a four-rule model of how TelemFFB manages device gains, with a precedence table and the worked examples reformatted as state timelines
    - Documented **[Telemetry Overrides](telemffb/telem-overrides.md)** - re-sourcing telemetry items from an addon's custom variables (the autopilot-indication case), overriding individual list elements, transform expressions, and subscribing to additional telemetry, with a worked A2A example

- **August 8, 2026:**

    - Reorganized the **[TelemFFB](telemffb/index.md)** section into task-focused groups: Setup, Core Concepts, Simulator Guides, and Reference
    - Added **[Connecting Your Simulator](telemffb/sim-setup.md)** page collecting the per-simulator enable and auto-setup steps in one place
    - Added **[Devices & Instances](telemffb/devices-instances.md)** page combining multi-device setup with the instance launch options
    - Added **[How Settings Work](telemffb/settings-model.md)** page explaining where settings are stored and how the delta-based configuration model resolves defaults
    - Moved **Understanding Native DCS FFB, TelemFFB, and VPforce Configurator** from the overview into the **[DCS guide](telemffb/sim-dcs.md)**, keeping the overview focused on what TelemFFB does per simulator
    - Repaired heading hierarchy on the simulator guide pages so section numbering and the table of contents render correctly
    - Clarified in **[Running TelemFFB from Source](telemffb/installation.md#running-telemffb-from-source)** that Python 3.12 is required - newer versions are incompatible with the pinned numpy release
    - Updated **[IL-2 setup](telemffb/sim-setup.md#il-2-sturmovik)** for the current System Settings layout: discrete configuration groups for IL-2 Great Battles and IL-2 Korea, the telemetry port setting, and the new Telemetry Forwarding feature for sending Telemetry/Motion/FFB streams to additional destinations; removed the retired "Pause IL-2 Effects on Focus Loss" setting
    - Added a **[Quick Start](telemffb/quick-start.md)** walkthrough covering install, first launch, simulator connection, verifying telemetry, and live tuning
    - Rewrote **[How Settings Work](telemffb/settings-model.md)** to explain the layered defaults model - application defaults, class defaults, shipped aircraft profiles, and user overrides - and how the Settings tab shows where each value comes from
    - Split the **[MSFS & X-Plane guide](telemffb/sim-msfs-xplane.md)** into ordered chapters: [Axis Control & Spring Modes](telemffb/msfs-xp-axis-spring.md), [Trim & Autopilot Following](telemffb/msfs-xp-trim-following.md), [Automatic Trim Calibration](telemffb/msfs-xp-trim-calibration.md), and [Helicopters](telemffb/msfs-xp-helicopters.md)
    - Automatic Trim Calibration is now the headlined way to set the trim-following gains; the hand-tuning procedure moved to **[Manual Trim Tuning (Legacy)](telemffb/msfs-xp-trim-manual.md)**
    - Documented the **[Collective Spring Mode](telemffb/msfs-xp-helicopters.md#collective-spring-mode)** (No Spring / Hardware Force Trim) for MSFS, X-Plane, and DCS, including the trim release, reset, and trim up/down button behavior
    - Documented **[Cyclic Trim Following](telemffb/msfs-xp-helicopters.md#cyclic-trim-following)** for helicopters, including how its rotor-trim data source and simpler model differ from the fixed-wing implementation
    - Redesigned the entire Effects Reference around per-effect entries in the same order as the Settings tab - simulator badges, a written explanation of every effect, its sub-settings (grouped by spring/g-force mode where applicable), and per-sim behavior notes - across all eight section pages: [Basic Settings](telemffb/effects-basic.md), [Aerodynamics](telemffb/effects-aerodynamics.md), [Inertial](telemffb/effects-inertial.md), [Ground](telemffb/effects-ground.md), [Mechanical & Airframe](telemffb/effects-mechanical.md), [Weapons](telemffb/effects-weapons.md), [Basic FFB Effects](telemffb/effects-ffb.md), and [System](telemffb/effects-system.md)
    - Added per-simulator settings directories - [DCS](telemffb/effects-sim-dcs.md), [IL-2](telemffb/effects-sim-il2.md), [BMS](telemffb/effects-sim-bms.md), [MSFS](telemffb/effects-sim-msfs.md), [X-Plane](telemffb/effects-sim-xplane.md) - listing everything available in each sim with links to the full documentation
    - Fixed the "Overpeed Shake" typo (now Overspeed Shake) in the application's setting labels
    - Retired the "What's New in 2.0" page - version history lives in the Release Notes
    - Moved the **[Advanced Curve Editor](telemffb/spring-curves.md)** into the Effects Reference (it documents the editor behind the Advanced Dynamic spring and G-force curve options) and **[VPforce Configurator Integration](telemffb/vpconf-profiles.md)** into Core Concepts
    - Expanded **[Devices & Instances](telemffb/devices-instances.md)** with an explanation of the master/child instance model and how to work with child instances
    - Added a connection-verification note to **[Connecting Your Simulator](telemffb/sim-setup.md)**
    - Rebuilt the Effects Reference as categorized pages with setting tables generated directly from the application's settings catalog: **[Overview](telemffb/effects-overview.md)** (including how effects differ between simulators), **[Basic & Spring](telemffb/effects-basic.md)**, **[Aerodynamic](telemffb/effects-aerodynamics.md)**, **[Inertial](telemffb/effects-inertial.md)**, **[Ground](telemffb/effects-ground.md)**, **[Mechanical & Airframe](telemffb/effects-mechanical.md)**, **[Weapons](telemffb/effects-weapons.md)**, **[Basic FFB Effects](telemffb/effects-ffb.md)**, and **[System](telemffb/effects-system.md)**; the legacy A-Z page now redirects to the new overview, with its remaining unique content migrated into the category pages (G-force effect deep-dive, propeller rumble tuning, glider force trim, DCS pedal spring V-speed behavior, SimConnect axis events) and its troubleshooting content consolidated into [Game-Specific Troubleshooting](rhino/game-specific-troubleshooting.md)
    - Moved the Turbulence and Low Hydraulic Pressure effect documentation from the MSFS & X-Plane overview into their effects-reference categories, keeping the overview focused on the guide chapters

- **August 7, 2026:**

    - Added a **[TelemFFB Release Notes](telemffb/release-notes.md)** page - full version history (newest first) in collapsible sections, with a stable `/telemffb/latest/` link that always points to the most recent release for the in-app update notification

- **June 28, 2026:**

    - Added **Running TelemFFB from Source** section to the **[Installation](telemffb/installation.md)** page, covering Python setup, cloning the repository, checking out a specific branch, installing dependencies, and launching the app

- **June 13, 2026:**

    - Added missing image depicting axis rescale example
    - Clarified procedure for re-centering motors after belt slippage/removal
    - Refactor "Apply/Save Config" throughout documentation to "Apply/Save Settings" to match button text in Configurator

- **May 1, 2026:**

    - Split **[Game Specific Troubleshooting](rhino/game-specific-troubleshooting.md)** into its own dedicated page, separated from the hardware **[Troubleshooting](rhino/troubleshooting-maintenance.md)** page
    - Expanded game-specific troubleshooting with new sections for DCS telemetry setup, DCS joystick Y-axis offset, MSFS SimConnect limitations, IL-2 and X-Plane telemetry setup, and Falcon BMS beta status

- **April 21, 2026:**

    - Refined the **[Grip Adapters](products/grip-adapters.md)** page for improved clarity and consistency

- **April 19, 2026:**

    - Restructured **[TelemFFB Application Guide](telemffb/index.md)** into separate focused pages: [Installation](telemffb/installation.md), [UI Overview](telemffb/ui-overview.md), [Configuration](telemffb/configuration.md), [Aircraft Profiles](telemffb/aircraft-profiles.md), [Effects Reference](telemffb/effects-reference.md), [Spring Curves](telemffb/spring-curves.md), [VPconf Profiles](telemffb/vpconf-profiles.md), [Multi-Device](telemffb/multi-device.md), [What's New](telemffb/whats-new.md), and sim-specific pages for [DCS](telemffb/sim-dcs.md), [IL-2](telemffb/sim-il2.md), and [MSFS/X-Plane](telemffb/sim-msfs-xplane.md)
    - Added **[Virpil ACE Pedal FFB Mod by Number481](community-projects/VirpilACE_FFB_Mod_Guide.md)** community project - belt-driven 6:1 ratio FFB conversion for Virpil ACE rudder pedals using the 86BLF-03 motor kit, fully reversible with no permanent modifications required

- **April 17, 2026:**

    - Added **[CAD Files](community-projects/index.md#cad-files)** section to the Community Projects index with downloadable STEP files for Rhino PCB, 57BLF01, 57BLF03, 86BLF04, PLG060, and PLG090 motors and gearboxes

- **April 8, 2026:**

    - Clarified **[Monster Rhino](third-party-vendors/winger-kits/monster-rhino.md)** torque comparisons by distinguishing official Rhino published torque from theoretical calculated stick-side values
    - Corrected the official Rhino comparison ratio to **75T/12T** in **[Monster Rhino](third-party-vendors/winger-kits/monster-rhino.md)** and **[TheAmazinGreat 86 Motor FFB Base](community-projects/theamazingreat-rhino.md)**, while noting that many DIY Rhino variants use a 74T pulley
    - Tightened **[Monster Rhino](third-party-vendors/winger-kits/monster-rhino.md)** wording around ratio selection, thermal performance, and US shipping guidance for accuracy and consistency
    - Replaced unresolved assembly figure placeholders in **[Monster Rhino](third-party-vendors/winger-kits/monster-rhino.md)** and added a short troubleshooting section for common assembly checks

- **April 7, 2026:**

    - Added and refined **[Leaving the RHINO Idle](rhino/using-the-rhino.md#leaving-the-rhino-idle)** guidance covering USB power-save behavior, the **USB suspend** requirement for automatic sleep, E-stop use, full PSU power-off, and practical recommendations for how to leave the unit between sessions
    - Refactored **[Using the RHINO](rhino/using-the-rhino.md)** to fix broken references, remove a missing image, clarify calibration save steps, and tighten several setup explanations
    - Standardized **Apply Settings** terminology across Rhino setup, usage, and maintenance pages to distinguish temporary activation from **Store Settings** permanent saves

- **March 31, 2026:**

    - Strengthened **[USB Isolator Recommendation](rhino/troubleshooting-maintenance.md#usb-isolator-recommendation)** with ground-loop damage warning and ground connection best practices
    - Added **[Powering Multiple FFB Devices from a Single PSU](community-projects/tips-and-tricks.md#powering-multiple-ffb-devices-from-a-single-psu)** section in Tips and Tricks
    - Added **[Throw Limiters](products/throw-limiters.md)** product page with Onshape CAD model link for parametric 3D printing
    - Updated throw limiter sections in Getting Started and Maintenance with VPforce ordering and Onshape links
    - Added **DCS "set spring autocenter failed"** to [Known Issues](rhino/appendix-a-known-issues.md) with USB troubleshooting guidance
    - Added simulator-specific issues note in [General Troubleshooting](rhino/troubleshooting-maintenance.md#general-troubleshooting-steps) with links to known issues and game-specific sections
    - Streamlined **[How to Get Effective Support](rhino/troubleshooting-maintenance.md#how-to-get-effective-support)** section for clarity and readability

- **March 27, 2026:**

    - Added **[Kit Diagram](products/diy-kits.md#kit-comparison)** to DIY Motor Kits page with clickable link to the technical drawing PDF
    - Added **Alpha Prime** to supported Virpil grips in [Grip Adapters](products/grip-adapters.md) and [Getting Started](rhino/getting-started.md)
    - Added **FC Technologies** to natively supported grip brands in [Grip Adapters](products/grip-adapters.md)
    - Added **Custom Grips (Shift-Register)** section to [Grip Adapters](products/grip-adapters.md) for community-designed grips
    - Expanded **[Rhino FFB Base](products/rhino-ffb-base.md)** specifications with weight, dimensions, PSU rating, cooling, motors, transmission ratio, and encoder resolution
    - Added direct **Configurator download link** to the [Rhino FFB Base](products/rhino-ffb-base.md) page
    - Fixed **86BLF03 single kit price** from 299 to 229 EUR in [DIY Motor Kits](products/diy-kits.md)
    - Standardized brand name to **VPforce** (lowercase f) across all product pages
    - Updated all documentation links from `vpforcecontrols.com` to `vpforce.eu`
    - Fixed **WinWing** capitalization across Rhino manual pages

- **March 16, 2026:**

    - Added **[Autopilot Oscillation with FFB](telemffb/sim-dcs.md#autopilot-oscillation-with-ffb)** section documenting DCS autopilot pitch/roll oscillation caused by the simulator's autopilot-FFB feedback loop, with diagnostic steps and workarounds

- **February 27, 2026:**

    - Added **Technical Specifications** section to the [Monster Rhino Kitbase](third-party-vendors/winger-kits/monster-rhino.md) page with motor torque constant (Kt), drive current limit, computed motor shaft torque, and per-gear-ratio peak torque at the stick (~15.2 N·m at 60T/15T, ~18.3 N·m at 72T/15T)
    - Updated **[TheAmazinGreat 86 Motor FFB Base](community-projects/theamazingreat-rhino.md)** torque section with a full per-motor, per-gear-ratio table including 86BLF03 (Kt 0.110 N·m/A, ~13-16 N·m) and 86BLF04 (Kt 0.127 N·m/A, ~15-18 N·m) calculated from motor specs

- **February 24, 2026:**

    - Added **[DCS Force Feedback Fix (dinput8 wrapper)][dcs-force-feedback-fix-dinput8-wrapper]** section in troubleshooting documenting the community dinput8 wrapper that fixes FFB being sent to wrong devices (vJoy, pedals, collective) and FFB effects dying after a USB reconnect mid-mission

- **February 7, 2026:**

    - Updated **[RHINO Maintenance][rhino-maintenance]** with warnings about fragile Molex Picoblade contacts, added gimbal stem screws as a potential source of clicking noise, and included an introduction for the grip mount head replacement section

- **December 3, 2025:**

    - Added comprehensive **[Power Issues][power-issues]** troubleshooting section with separate diagnostics for USB power path failures and DC motor power failures
    - Added **[Spring Gain Mapping Tab][spring-gain-mapping-tab]** documentation explaining force-versus-displacement mapping and game gain remapping for customizing spring force behavior
    - Added **[Autopilot Misbehaving or Disengaging Unexpectedly][autopilot-misbehaving-or-disengaging-unexpectedly]** troubleshooting for aircraft autopilot systems interpreting trim offset as hands-on override
    - Added **[How to Get Effective Support][how-to-get-effective-support]** guide with bad/good request examples, required information checklist, and common pitfalls to avoid
    - Completely rewrote **[Re-tightening the Belts][re-tightening-the-belts]** maintenance section with detailed step-by-step procedures, troubleshooting, and belt realignment instructions

- **November 25, 2025:**

    - Added **[Understanding Configuration Profiles and Personalization][understanding-configuration-profiles-and-personalization]** section explaining why profile sharing is uncommon in the Rhino community and providing recommended approach for building custom baseline configurations
    - Reformatted **[Technical Specifications][technical-specifications]** in Getting Started guide with organized subsections (Physical, Motors, Power & Cooling, Safety & Controls, Grip Compatibility)
    - Expanded **[WinUSB / WebUSB Firmware Update Issues][winusb-webusb-firmware-update-issues]** troubleshooting with comprehensive driver cleanup procedures for resolving Zadig and driver store conflicts
    - Added **[VPforce Motor Kit Discount][ordering-shipping]** information for Monster Rhino Kitbase customers (10% off 2x86BLF04+USB kit)

- **November 13, 2025:**

    - Updated **[Kaltokri DIY FFB Kits availability](third-party-vendors/kaltokri-kits/index.md)** - kits now generally in stock with 2-3 working day dispatch after payment
    - Added **[General Troubleshooting Steps](rhino/troubleshooting-maintenance.md#general-troubleshooting-steps)** section with factory reset procedure as first troubleshooting step

- **November 12, 2025:**

    - Added **[FFB Yoke by YuchenYan](community-projects/ffb-yoke.md)** comprehensive project reference documentation
    - Added **[FFB Axes Setup][ffb-axes-setup-tab]** section documenting main axis calibration, force compensation, axis control options, and verification procedures

- **November 11, 2025:**

    - Added **[Kaltokri DIY FFB Kits](third-party-vendors/kaltokri-kits/index.md)** comprehensive documentation suite covering 8 DIY conversion kits
        - Documented **[RhinoJoystick](third-party-vendors/kaltokri-kits/rhinojoystick.md)** complete DIY FFB joystick base kit with dual 57BLF03 motors
        - Added **[RhinoMFG](third-party-vendors/kaltokri-kits/rhinomfg.md)** MFG Crosswind FFB conversion kit documentation (57BLF03 motor)
        - Added **[RhinoMFG86](third-party-vendors/kaltokri-kits/rhinomfg86.md)** high-torque MFG Crosswind conversion with 86BLF03 motor
        - Documented **[RhinoTPR Inside](third-party-vendors/kaltokri-kits/rhinotpr-inside.md)** Thrustmaster TPR conversion (motor-inside, drilled variant)
        - Documented **[RhinoTPR Outside](third-party-vendors/kaltokri-kits/rhinotpr-outside.md)** Thrustmaster TPR conversion (motor-outside, non-drilled variant)
        - Added **[RhinoACE](third-party-vendors/kaltokri-kits/rhinoace.md)** Virpil ACE pedals FFB conversion documentation
        - Added **[RhinoOrion](third-party-vendors/kaltokri-kits/rhinoorion.md)** WinWing Orion pedals FFB conversion documentation
        - Added **[RhinoR1](third-party-vendors/kaltokri-kits/rhinor1.md)** Virpil R1 pedals FFB conversion documentation
        - Created **[General FAQ](third-party-vendors/kaltokri-kits/general-faq.md)** with centralized pricing, PSU requirements, shipping, payment, assembly guidance, and warranty information

- **November 9, 2025:**

    - Added **[DIY Tips and Tricks](community-projects/tips-and-tricks.md)** documenting multi-turn encoder ambiguity and other challenges in custom FFB configurations
    - Expanded **[Known Issues](rhino/appendix-a-known-issues.md)** with DCS axis curve incompatibility explanation and FFB best practices
    - Documented IL-2 8-device USB limit and devreorder workaround solution
    - Added **[Community Projects](community-projects/index.md)** section featuring DIY FFB builds and modifications
    - Documented **[TheAmazinGreat 86 Motor FFB Base](community-projects/theamazingreat-rhino.md)** with thermal management advantages for extended high-intensity use
    - Added **[Tiger TPR FFB Mod Guide](community-projects/Tiger_TPR_FFB_Mod_Guide.md)** for Thrustmaster TPR pedal FFB conversion
    - Added **[TPR FFB Project Documentation](community-projects/TPR_FFB_Project_Documentation.md)** with complete assembly procedures and troubleshooting FAQ
    - Added **[MFG Crosswind FFB Mod Guide](community-projects/MFG_Crosswind_FFB_Mod_Guide.md)** for MFG Crosswind pedal FFB conversion
    - Documented **[Planetary Gearbox DIY][planetary-gearboxes-for-diy-projects]** options for increased torque output with reduced motor speed
    - Added **[Community Rhino Builds](community-projects/community-rhino-builds.md)** overview linking protomaker, mabo, and other community base designs
    - Created **[Third-Party Vendors](third-party-vendors/index.md)** section for commercial FFB kit offerings
    - Added **[SR-F Winger Monster Rhino Kitbase](third-party-vendors/winger-kits/monster-rhino.md)** documentation for 86BLF04-based commercial kit
    - Documented **FAULT_UNDERVOLTAGE** motor fault in **[Troubleshooting & Maintenance](rhino/troubleshooting-maintenance.md)** with voltage threshold details, under-load vs idle diagnostic guidance, and resolution procedures for power supply and connection issues

- **November 6, 2025:**

    - Added new community project page for the [Tiger TPR FFB Mod](community-projects/Tiger_TPR_FFB_Mod_Guide.md)
    - Added comprehensive documentation for the [Force-Feedback TPR Pedal Mod](community-projects/TPR_FFB_Project_Documentation.md) with assembly steps and FAQ
    - Added guide for the [MFG Crosswind FFB Mod](community-projects/MFG_Crosswind_FFB_Mod_Guide.md)

- **November 5, 2025:**

    - Added comprehensive section explaining Native DCS FFB, TelemFFB, and VPforce Configurator interactions (TelemFFB Application Guide)
    - Documented effect source identification using Configurator debug tab badges (`configurator`, `game`, `telemFFB`)
    - Added testing procedures for observing native DCS FFB behavior
    - Expanded USB troubleshooting with systematic diagnostic steps (hub, port, cable, power checks)
    - Added ground loop documentation for poor DC connections
    - Added USB isolator recommendation with AduM3160 product guidance
    - Clarified relationship between device-level gains and all FFB effects
    - Added signal flow diagram explaining DCS → Device → Motor output

