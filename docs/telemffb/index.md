# VPforce TelemFFB Application

TelemFFB is an open source community-driven Python/Qt based application which takes telemetry from a simulator and uses that telemetry to produce various effects.

The latest version can always be downloaded from the repository release page here:
[https://github.com/walmis/VPforce-TelemFFB/releases](https://github.com/walmis/VPforce-TelemFFB/releases)

Supported simulators:

-   DCS World
-   Microsoft Flight Simulator
-   IL-2 Sturmovik
-   X-Plane 11/12
-   Beta support for Falcon BMS (4.38+)

For **DCS** and **IL-2**, which support native FFB, the TelemFFB app is primarily leveraged to implement certain effects like gunfire, engine rumble and helicopter ETL shaking (among many others). However, there are some additional 'FFB type' effects which are implemented such as deceleration force and g-loading effect.

For **MSFS** and **X-Plane**, which ***do not*** have native FFB support, TelemFFB also implements dynamic axis FFB in addition to most of the effects previously mentioned for DCS.

**Falcon BMS** sits somewhere in between. While the game does support native FFB with limited native effects, the primary F-16 aircraft is fly-by-wire and as such does not have any traditional "force feedback" on its flight stick. TelemFFB implements several haptic style effects (gunfire, buffeting, etc) to augment immersion.

## How it works

TelemFFB started out its life as not much more than a haptic effect generator driven by telemetry, originally only for DCS. It started out by adding supplemental effects such as engine rumble and gunfire on top of the native force feedback effects supported directly by the simulator.

It has grown since then into a highly configurable, feature rich application supporting not only supplemental haptic effects but also full dynamic FFB modeling for simulators such as Microsoft Flight Simulator (20/24) and X-Plane that do not have **any **native FFB support.

TelemFFB leverages telemetry that is available from a given simulator and uses that telemetry to create various types of effects based on real-time analysis of said telemetry.

In practice, it is more complicated and depends largely on the simulator. However, it can be mostly broken down into two categories: Simulators ***with ***native FFB support and those ***without***.

**Sims with native FFB**

-   This includes **DCS**, **IL-2** and, to some extent, **BMS**. For these simulators, TelemFFB is primarily a haptics and supplemental effects generator. While there are overrides that a user can implement to use TelemFFB to manage the dynamic spring effect, the native game-supplied spring effect is typically used most of the time. This means that the game is managing the spring effect, while TelemFFB would be adding additional effects on top.

-   For these simulators, by default, the spring effect, including trim/autopilot following is managed wholly by the game itself.

**Sims without native FFB**

-   This includes both **Microsoft Flight Simulator** as well as **X-Plane**. Fortunately both of these titles have much more rich telemetry than the others and have sufficient data to implement not just simple speed based dynamic spring, but spring loading that is based on calculated dynamic pressure throughout the aircraft speed envelope as defined by the telemetry data.
-   For these simulators, the **entire** FFB implementation is handled by the TelemFFB application

### Understanding Native DCS FFB, TelemFFB, and VPforce Configurator

To effectively use TelemFFB, it is important to understand how native simulator FFB effects, TelemFFB effects, and VPforce Configurator device settings interact with one another.

#### Native DCS FFB Effects

DCS sends native force feedback effects directly to your FFB device without any involvement from TelemFFB. These effects vary by aircraft module and typically include:

- **Aerodynamic buffeting** - Stall buffet, AoA buffeting, and other aerodynamic shaking
- **Dynamic stick forces** - Changes in control resistance based on airspeed and flight conditions (Typically warbirds, Mig-21, etc.)
- **Overspeed buffeting** - Shaking when aircraft exceeds safe speeds (Su-25T)

!!! important
    DCS native FFB effects will work even if TelemFFB is not running, provided your device driver and VPforce Configurator are properly installed.

Module-specific FFB implementation varies. Eagle Dynamics does not publish a comprehensive list of native FFB effects per-module, so discovery typically requires testing in the aircraft itself or consulting module-specific community resources and forums.

#### TelemFFB Effects: Supplemental vs. Override

TelemFFB operates in one of two ways relative to native DCS FFB:

**Supplemental Mode (Default)**

- TelemFFB adds additional effects on top of native DCS FFB effects
- Native DCS effects (spring, buffeting, etc.) continue unmodified from the simulator
- TelemFFB contributes new effects like engine rumble customization, gunfire enhancement, helicopter ETL shaking, and other telemetry-driven effects
- Both the simulator and TelemFFB are generating forces simultaneously on the device

**Override Mode (Optional)**

- TelemFFB can be configured to take control of certain effects, particularly spring management
- When override is enabled for an effect, TelemFFB's implementation replaces the native DCS effect
- This is useful when you want to customize how forces feel beyond what DCS provides by default
- Overrides are configured on a per-aircraft basis in TelemFFB's settings

#### VPforce Configurator Device Settings

VPforce Configurator controls how your physical device responds to **all** incoming FFB commands, whether they originate from DCS or TelemFFB. These device-level settings include:

- **Spring Gain** - Overall strength of spring/centering forces
- **Damper** - Resistance and smoothing of stick movement
- **Inertia** - Rotational inertia of the stick
- **Friction** - Static friction when the stick is moving
- **Master Gain** - Overall FFB intensity multiplier

!!! important "Critical Point"
    Adjusting VPforce Configurator gains affects **all** FFB effects equally. If you increase spring gain in Configurator, both native DCS spring forces and any TelemFFB-generated spring forces become proportionally stronger or weaker.

#### Signal Flow: From Simulator to Device

```
DCS Simulator
    ↓ (native FFB effects)
    +─→ FFB Device (via OS/driver)
        └─→ VPforce Configurator settings applied
                ↓
                Physical motor output

TelemFFB (if running)
    ↓ (supplemental/override effects)
    +─→ FFB Device (via OS/driver)
        └─→ VPforce Configurator settings applied
                ↓
                Physical motor output (combines with DCS effects)
```

Both DCS and TelemFFB send their force commands to the same device. The device receives all commands and applies VPforce Configurator settings (gains, damping, etc.) to determine the final motor behavior.

#### Testing Without TelemFFB

To experience and evaluate native DCS FFB effects without any TelemFFB customization:

1. Close TelemFFB entirely
2. Verify your VPforce Configurator device settings are configured appropriately
3. Start DCS and load the aircraft/module you want to test
4. Reproduce flight conditions (stall, high-G turns, gunfire, landing, etc.)
5. Observe and evaluate the native FFB behavior
6. Adjust VPforce Configurator gains and apply (not store) to see how device settings affect the feel

This baseline understanding of native DCS behavior will help you make informed decisions about which TelemFFB customizations are useful for your preferences.

#### When TelemFFB is Running

When TelemFFB is running and connected to a loaded aircraft:

- Native DCS FFB effects continue to be sent to the device
- TelemFFB simultaneously adds or (if configured) overrides specific effects
- VPforce Configurator settings shape how all incoming FFB commands are rendered on the device
- Changing a TelemFFB setting takes effect nearly immediately (slight delay while the application processes the adjustment)

TelemFFB can also dynamically push VPforce Configurator profiles or individual gain overrides to your device. These changes affect how subsequent FFB commands from both DCS and TelemFFB are rendered.

#### Monitoring DCS vs TelemFFB Effects Using the Configurator Debug Tab

VPforce Configurator includes a debug tab that displays all FFB effects being sent to your device in real-time. Each effect is labeled with an effect ID and includes a source badge that identifies where the effect originates.

**Effect Source Badges:**

The debug tab displays source badges for each effect:

- **configurator** - Effects generated by VPforce Configurator device firmware (reserved effects with ID ≤ 4)
- **game** - Effects generated by DCS (native FFB effects with ID > 4)
- **telemFFB** - Effects generated by the TelemFFB application

These badges make it easy to quickly identify which system is responsible for each effect without needing to manually reference effect IDs.

**Testing Procedure:**

To isolate and observe native DCS FFB effects without TelemFFB interference:

1. Close TelemFFB completely
2. Open VPforce Configurator and navigate to the debug tab
3. Start DCS and load the aircraft/module you want to test
4. In the debug tab, you will see effects appearing in real-time as you fly
5. Look for effects with the **game** badge—these are native DCS effects that demonstrate what the simulator provides by default
6. Reproduce specific flight conditions (stall, high-G maneuvers, gunfire, landing) to observe corresponding effects
7. Note which DCS effects are active and their behavior with your current VPforce Configurator settings

**With TelemFFB Running:**

When you restart TelemFFB after completing your DCS-only testing:

- The debug tab will show effects with all three source badges: **configurator**, **game**, and **telemFFB**
- Effects with the **telemFFB** badge are supplemental effects added by TelemFFB
- You can compare the effect list before and after TelemFFB is running to understand what supplemental effects TelemFFB adds
- This helps you make informed decisions about which TelemFFB customizations enhance your experience

!!! tip
    Save a screenshot or note of the effect IDs you see in the debug tab while running DCS alone. This baseline reference makes it easier to identify TelemFFB-specific effects when you enable TelemFFB later.
