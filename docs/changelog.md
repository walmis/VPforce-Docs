# Changelog
- **May 1, 2026:**

    - Split **[Game Specific Troubleshooting](rhino/game-specific-troubleshooting.md)** into its own dedicated page, separated from the hardware **[Troubleshooting](rhino/troubleshooting-maintenance.md)** page
    - Expanded game-specific troubleshooting with new sections for DCS telemetry setup, DCS joystick Y-axis offset, MSFS SimConnect limitations, IL-2 and X-Plane telemetry setup, and Falcon BMS beta status

- **April 21, 2026:**

    - Refined the **[Grip Adapters](products/grip-adapters.md)** page for improved clarity and consistency

- **April 19, 2026:**

    - Restructured **[TelemFFB Application Guide](telemffb/index.md)** into separate focused pages: [Installation](telemffb/installation.md), [UI Overview](telemffb/ui-overview.md), [Configuration](telemffb/configuration.md), [Aircraft Profiles](telemffb/aircraft-profiles.md), [Effects Reference](telemffb/effects-reference.md), [Spring Curves](telemffb/spring-curves.md), [VPconf Profiles](telemffb/vpconf-profiles.md), [Multi-Device](telemffb/multi-device.md), [What's New](telemffb/whats-new.md), and sim-specific pages for [DCS](telemffb/sim-dcs.md), [IL-2](telemffb/sim-il2.md), and [MSFS/X-Plane](telemffb/sim-msfs-xplane.md)
    - Added **[Virpil ACE Pedal FFB Mod by Number481](community-projects/VirpilACE_FFB_Mod_Guide.md)** community project — belt-driven 6:1 ratio FFB conversion for Virpil ACE rudder pedals using the 86BLF-03 motor kit, fully reversible with no permanent modifications required

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
    - Standardized **Apply Config** terminology across Rhino setup, usage, and maintenance pages to distinguish temporary activation from **Store Config** permanent saves

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

    - Added **[Autopilot Oscillation with FFB](telemffb/index.md#autopilot-oscillation-with-ffb)** section documenting DCS autopilot pitch/roll oscillation caused by the simulator's autopilot-FFB feedback loop, with diagnostic steps and workarounds

- **February 27, 2026:**

    - Added **Technical Specifications** section to the [Monster Rhino Kitbase](third-party-vendors/winger-kits/monster-rhino.md) page with motor torque constant (Kt), drive current limit, computed motor shaft torque, and per-gear-ratio peak torque at the stick (~15.2 N·m at 60T/15T, ~18.3 N·m at 72T/15T)
    - Updated **[TheAmazinGreat 86 Motor FFB Base](community-projects/theamazingreat-rhino.md)** torque section with a full per-motor, per-gear-ratio table including 86BLF03 (Kt 0.110 N·m/A, ~13–16 N·m) and 86BLF04 (Kt 0.127 N·m/A, ~15–18 N·m) calculated from motor specs

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

