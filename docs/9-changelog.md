# Changelog

- **November 12, 2025:**

    - Added **[FFB Yoke by YuchenYan](2-community-projects/ffb-yoke.md)** comprehensive project reference documentation
    - Added **[FFB Axes Setup][ffb-axes-setup-tab]** section documenting main axis calibration, force compensation, axis control options, and verification procedures

- **November 11, 2025:**

    - Added **[Kaltokri DIY FFB Kits](3-third-party-vendors/kaltokri-kits/index.md)** comprehensive documentation suite covering 8 DIY conversion kits
        - Documented **[RhinoJoystick](3-third-party-vendors/kaltokri-kits/rhinojoystick.md)** complete DIY FFB joystick base kit with dual 57BLF03 motors
        - Added **[RhinoMFG](3-third-party-vendors/kaltokri-kits/rhinomfg.md)** MFG Crosswind FFB conversion kit documentation (57BLF03 motor)
        - Added **[RhinoMFG86](3-third-party-vendors/kaltokri-kits/rhinomfg86.md)** high-torque MFG Crosswind conversion with 86BLF03 motor
        - Documented **[RhinoTPR Inside](3-third-party-vendors/kaltokri-kits/rhinotpr-inside.md)** Thrustmaster TPR conversion (motor-inside, drilled variant)
        - Documented **[RhinoTPR Outside](3-third-party-vendors/kaltokri-kits/rhinotpr-outside.md)** Thrustmaster TPR conversion (motor-outside, non-drilled variant)
        - Added **[RhinoACE](3-third-party-vendors/kaltokri-kits/rhinoace.md)** Virpil ACE pedals FFB conversion documentation
        - Added **[RhinoOrion](3-third-party-vendors/kaltokri-kits/rhinoorion.md)** WinWing Orion pedals FFB conversion documentation
        - Added **[RhinoR1](3-third-party-vendors/kaltokri-kits/rhinor1.md)** Virpil R1 pedals FFB conversion documentation
        - Created **[General FAQ](3-third-party-vendors/kaltokri-kits/general-faq.md)** with centralized pricing, PSU requirements, shipping, payment, assembly guidance, and warranty information

- **November 9, 2025:**

    - Added **[DIY Tips and Tricks](2-community-projects/1-tips-and-tricks.md)** documenting multi-turn encoder ambiguity and other challenges in custom FFB configurations
    - Expanded **[Known Issues](1-rhino/7-appendix-a-known-issues.md)** with DCS axis curve incompatibility explanation and FFB best practices
    - Documented IL-2 8-device USB limit and devreorder workaround solution
    - Added **[Community Projects](2-community-projects/index.md)** section featuring DIY FFB builds and modifications
    - Documented **[TheAmazingGreat's 86 Motor FFB Base](2-community-projects/theamazingreat-rhino.md)** with thermal management advantages for extended high-intensity use
    - Added **[Tiger TPR FFB Mod Guide](2-community-projects/Tiger_TPR_FFB_Mod_Guide.md)** for Thrustmaster TPR pedal FFB conversion
    - Added **[TPR FFB Project Documentation](2-community-projects/TPR_FFB_Project_Documentation.md)** with complete assembly procedures and troubleshooting FAQ
    - Added **[MFG Crosswind FFB Mod Guide](2-community-projects/MFG_Crosswind_FFB_Mod_Guide.md)** for MFG Crosswind pedal FFB conversion
    - Documented **[Planetary Gearbox DIY](2-community-projects/Planetary_Gearboxes_DIY.md)** options for increased torque output with reduced motor speed
    - Added **[Community Rhino Builds](2-community-projects/community-rhino-builds.md)** overview linking protomaker, mabo, and other community base designs
    - Created **[Third-Party Vendors](3-third-party-vendors/index.md)** section for commercial FFB kit offerings
    - Added **[SR-F Winger Monster Rhino Kitbase](3-third-party-vendors/SR-F_Winger.md)** documentation for 86BLF04-based commercial kit
    - Documented **FAULT_UNDERVOLTAGE** motor fault in **[Troubleshooting & Maintenance](1-rhino/6-troubleshooting-maintenance.md)** with voltage threshold details, under-load vs idle diagnostic guidance, and resolution procedures for power supply and connection issues

- **November 6, 2025:**

    - Added new community project page for the [Tiger TPR FFB Mod](2-community-projects/Tiger_TPR_FFB_Mod_Guide.md)
    - Added comprehensive documentation for the [Force-Feedback TPR Pedal Mod](2-community-projects/TPR_FFB_Project_Documentation.md) with assembly steps and FAQ
    - Added guide for the [MFG Crosswind FFB Mod](2-community-projects/MFG_Crosswind_FFB_Mod_Guide.md)

- **November 5, 2025:**

    - Added comprehensive section explaining Native DCS FFB, TelemFFB, and VPforce Configurator interactions (TelemFFB Application Guide)
    - Documented effect source identification using Configurator debug tab badges (`configurator`, `game`, `telemFFB`)
    - Added testing procedures for observing native DCS FFB behavior
    - Expanded USB troubleshooting with systematic diagnostic steps (hub, port, cable, power checks)
    - Added ground loop documentation for poor DC connections
    - Added USB isolator recommendation with AduM3160 product guidance
    - Clarified relationship between device-level gains and all FFB effects
    - Added signal flow diagram explaining DCS → Device → Motor output

