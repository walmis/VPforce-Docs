# TheAmazinGreat's '86 Motor FFB Base

This project is a modification of Gadroc's FFB joystick base, designed to accommodate larger 86BLF03 or 86BLF04 series motors for stronger force feedback. The design uses the same gimbal as other community builds but features larger panels to fit the bigger motors. Panels are not interchangeable with standard builds due to the increased motor size.

**GitHub Repository:** [https://github.com/TheAmazinGreat/86-Motor-VPF-FFB-Base](https://github.com/TheAmazinGreat/86-Motor-VPF-FFB-Base)

## Overview

This modified FFB base accepts the larger 86 series motors from VPForce, providing significantly increased torque output compared to standard Rhino builds. Panels should be printable on any 3D printer with a bed size equivalent to an Ender3 or larger.

!!! note "Gimbal Compatibility"

    This project does not include gimbal files to avoid confusion. Any of the community gimbals (Protomaker, Gadroc, mrusk, mabo, etc.) will work with this base. The Protomaker gimbal is recommended and the BOM has been cross-referenced with that design.

## Why Choose 86 Motors Over 57 Motors?

The 86 series motors provide two key advantages over standard 57 series motors found in typical Rhino builds: superior thermal management and higher sustained torque output.

### Thermal Performance

The larger 86 motors have significantly better thermal characteristics than 57 series motors, but this advantage only matters during high-intensity use.

**Heat generation follows the $P = I^2R$ relationship**, meaning thermal buildup increases with the square of current (and torque demand). During level flight or gentle maneuvering, both motor sizes produce minimal heat. The thermal advantage of 86 motors becomes apparent only during sustained high-force scenarios.

The 86 motors' larger physical size provides:

- Greater thermal mass to absorb heat during high-load transients
- Larger surface area for more effective passive cooling
- Improved heat dissipation from motor windings to the case
- Higher continuous torque rating before thermal throttling occurs

### Sustained Performance in Extended Dogfights

The thermal advantage of 86 motors is specifically relevant during prolonged aggressive maneuvering. During routine flight operations, neither motor size generates significant heat. However, during extended dogfights with sustained high forces, 57 motors will reach thermal limits faster and begin reducing available torque to maintain safe operating temperatures.

**When thermal advantages matter:**

- Back-to-back dogfights with minimal cooldown between engagements
- Prolonged defensive maneuvering under sustained G-loads
- Extended air-to-ground attack runs with continuous stick deflection
- High-intensity multiplayer sorties with continuous combat action

**Practical benefits:**

- 86 motors maintain full torque output longer during intensive combat sequences
- Less thermal throttling during aggressive maneuvering scenarios
- More headroom for sustained high-force effects without performance degradation
- Better suited for continuous high-intensity action without cooldown periods

### Peak Torque Comparison

With appropriate gear ratios, 86 motor builds deliver 1.7x to 2.0x the peak torque of standard Rhino configurations. This increased output, combined with superior thermal management, means the system can sustain higher forces throughout your entire flight session rather than backing off when temperatures rise.

!!! tip "Thermal Management"

    While all Rhino builds include active cooling systems, the 86 motors' inherent thermal advantages mean the cooling fans are more effective at maintaining optimal operating temperatures, allowing you to push harder for longer without experiencing force reduction.

## Required Components

### Motor Kits

You will need to purchase one of the following motor kits from VPForce:

*   **2x86BLF03 + USBkit** - High torque option
*   **2x86BLF04 + USBkit** - Strongest option available

### Gear Ratio Options

Choose one of the two gear ratios below. Both options require different belt lengths.

*   **60T/15T Ratio:** 1.7x standard Rhino peak torque

    - Uses 465mm belt (pitch axis)
    - Uses 380mm belt (roll axis)

*   **72T/15T Ratio:** 2.0x standard Rhino peak torque

    - Uses 500mm belt (pitch axis)
    - Uses 420mm belt (roll axis)

## CAD Files

Fusion 360 files are available in the CAD folder of the repository. The 57 series design is also included as a reference in a subfolder.

!!! note "Development Status"

    Step files are planned for future release. The 15-degree throw limiter is optional and available in the CAD file. The boot clamp design is included but has not been tested yet.

## 3D Printed Parts

All STLs should be checked for optimal orientation in your slicer to minimize supports. Placing the long edge of case plates in the X direction works best for most setups.

!!! tip "Print Settings"

    Parts have been successfully printed in eSUN PLA+ with a 0.6mm nozzle and 0.3mm layer height. Adjust settings as necessary for your printer and filament.

### Required Parts (All Gimbal Types)

Print these parts regardless of gear ratio choice:

| Part | Quantity | Supports | Description |
|------|----------|----------|-------------|
| ext_bearing_retainer_x3 | 3 | None | Exterior bearing retainers |
| int_bearing_retainer_x8 | 8 | None | Interior bearing retainers |
| control_mount_retainer | 1 | None | Control mount / bearing retainer |
| 86 Rear Plate | 1 | None | Rear case plate (roll drive) |
| 86 Right Plate | 1 | None | Right case plate (pitch drive) |
| 86 Mid Plate | 1 | None | Mid case plate (roll bearing / control mount) |
| 86 Front Plate | 1 | None | Front case plate (fan mount) |
| 86 Left Plate | 1 | None | Left case plate (pitch bearing) |
| 86 Top Plate | 1 | None | Case top plate |
| 86 Base Plate | 1 | None | Bottom case plate |
| USB Bracket | 1 | None | USB panel mount bracket |

### Gear Ratio Specific Parts

Choose one pair based on your selected gear ratio:

| Part | Quantity | Supports | Gear Ratio | Description |
|------|----------|----------|------------|-------------|
| HTD-5M-60 Pulley | 2 | None | 60T (1.7x) | 60 tooth gimbal pulleys |
| HTD-5M-72 Pulley | 2 | None | 72T (2.0x) | 72 tooth gimbal pulleys |

### Gimbal Parts

Print and assemble the Protomaker gimbal or another community gimbal design of your choice.

## Bill of Materials

This BOM has been cross-referenced with the Protomaker gimbal assembly. Due to bulk quantities from linked sources, you may have hardware remaining for future projects.

!!! important "Motor Mounting Hardware"

    The BOM below includes correct specifications for 86 series motors. Belt sizes, pulleys, and motor mounting screws differ from standard builds.

### Bearings

| Quantity | Part | Link | Notes |
|----------|------|------|-------|
| 4 | 6808-2RS Bearings | [Amazon](https://www.amazon.com/dp/B0CGM2PG3Z) | Large pulley bearings |
| 8 | 6802-2RS Bearings | [Amazon](https://www.amazon.com/dp/B0CGM2CHB8) | Gimbal bearings |
| 2 | F625ZZ Bearings | [Amazon](https://www.amazon.com/dp/B07Z3DXF14) | Stick adapter bearings |

### Fasteners and Hardware

| Quantity | Part | Notes |
|----------|------|-------|
| 120 | [M4 Threaded Inserts](https://a.co/d/13tdMM1) | Various locations (not all will be used) |
| 12 | M4 x 35 Button Head Screw | Pulley mounting screws |
| 12 | M4 Nut | Pulley mounting nuts |
| 24 | M4 Washer | Pulley mounting washers |
| 4 | M4 x 19mm Washer | Gimbal washers |
| 3 | M5 Washer (Stock) | Gimbal core joint / stick adapter |
| 2 | M5 Nut (Stock) | Gimbal core joint / stick adapter |
| 1 | M5 x 60 Socket Head Screw (Stock) | Gimbal core joint |
| 4 | M4 x 10 Button Head Screw (Stock) | 6802 bearing retainer with 19mm washers |
| 8 | M5 x 10 Button Head Screw (Stock) | Pillow block to gimbal arm screws |
| 120 | [M3 Threaded Inserts](https://a.co/d/bVtzw0D) | Case, brackets, mounts (not all will be used) |
| 80 | [M3 x 12 Flat Head Screw](https://a.co/d/5OQshW6) | Case assembly screws (not all will be used) |
| 2 | M3 x 12 Button Head Screw (Stock) | USB bracket screws |
| 12 | M3 x 15 Button Head Screw (Stock) | Pulley bearing retainer screws |
| 12 | M3 Nut (Stock) | Pulley bearing retainer nuts |
| 4 | M3 x 5 Button Head Screw (Stock) | Control board screws |
| 8 | M6 x 20 Socket Head Screw | Motor mounting screws (86 series specific) |

### Drive Components

| Quantity | Part | Link | Notes |
|----------|------|------|-------|
| 2 | 5M-15T-20W Pulley | [Amazon](https://a.co/d/b9yMcuO) | Motor pulleys |

### Belt Options

!!! important "Choose One Pair"

    Select belt pair A or B based on your chosen gimbal pulley size.

**Pair A - For 60T Gimbal Pulleys (1.7x torque)**

| Quantity | Part | Axis |
|----------|------|------|
| 1 | 465mm HTD 5M-15W Belt | Pitch |
| 1 | 380mm HTD 5M-15W Belt | Roll |

**Pair B - For 72T Gimbal Pulleys (2.0x torque)**

| Quantity | Part | Axis |
|----------|------|------|
| 1 | 500mm HTD 5M-15W Belt | Pitch |
| 1 | 420mm HTD 5M-15W Belt | Roll |

### Electronics and Connectors

| Quantity | Part | Link | Notes |
|----------|------|------|-------|
| 1 | [80mm Case Fan](https://a.co/d/6VjeeIf) | Includes mounting screws |
| 1 | [E-Stop Switch](https://a.co/d/37DwknT) | 10A rated for larger motors |
| 2 | [10k Type B Linear Potentiometer](https://a.co/d/jhRPIQb) | |
| 1 | [XT60E-M Connector](https://a.co/d/5N06VCB) | Panel mount, includes screws |
| 1 | [XT60-F Connector](https://a.co/d/5WA5z3b) | Optional if power supply lacks connector |
| 1 | 5 Pin Mini Din Connector (Stock) | Stick connector (source from Digi-Key) |

## Assembly

This project is a close derivative of Protomaker's work. Follow the Protomaker assembly guide for complete build instructions. The assembly process is similar, with the primary differences being the larger motor mounting points and modified case dimensions.

## Credits

*   **walmis:** Electronics, firmware, and original base design
*   **mabo:** Expanded base design including full gimbal
*   **protomaker:** 3D printing modification and refinements
*   **Gadroc:** Basis for modifications and previous design iterations
