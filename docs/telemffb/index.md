# VPforce TelemFFB Application

TelemFFB is an open source community-driven Python/Qt application. It receives telemetry from a simulator and uses that data to produce force feedback effects.

Download the latest version from the [GitHub releases page](https://github.com/walmis/VPforce-TelemFFB/releases).

Supported simulators:

- DCS World
- Microsoft Flight Simulator
- IL-2 Sturmovik
- X-Plane 11/12
- Beta support for Falcon BMS (4.38+)

For **DCS** and **IL-2**, which support native FFB, TelemFFB adds supplemental effects: gunfire, engine rumble, helicopter ETL shaking, deceleration force, and g-loading.

For **MSFS** and **X-Plane**, which do not have native FFB support, TelemFFB provides the complete force feedback implementation: dynamic axis spring forces plus all supplemental effects listed above.

**Falcon BMS** falls between these categories. The game supports limited native FFB, but its primary F-16 aircraft is fly-by-wire and has no traditional force feedback on the side-stick. TelemFFB adds haptic effects such as gunfire and buffeting.

## How It Works

TelemFFB began as a simple haptic effect generator for DCS. It added supplemental effects such as engine rumble and gunfire on top of the simulator's native force feedback.

The application now supports full dynamic FFB modeling for simulators without any native FFB support, plus all supplemental haptic effects.

TelemFFB receives telemetry from your simulator and creates effects from real-time analysis of that data. The exact behavior depends on whether the simulator has native FFB support.

**Sims with native FFB**

- This includes **DCS**, **IL-2** and, to some extent, **BMS**. TelemFFB adds supplemental effects on top of the simulator's native spring effect. You can configure overrides to let TelemFFB manage the dynamic spring effect instead.
- By default, the game manages the spring effect, including trim and autopilot following.

**Sims without native FFB**

- This includes **Microsoft Flight Simulator** and **X-Plane**. Both provide rich telemetry data that supports spring forces based on calculated dynamic pressure across the aircraft speed envelope.
- TelemFFB handles the entire FFB implementation for these simulators.

For a detailed look at how native simulator FFB, TelemFFB, and VPforce Configurator device settings interact, see [Understanding Native DCS FFB, TelemFFB, and VPforce Configurator](sim-dcs.md#understanding-native-dcs-ffb-telemffb-and-vpforce-configurator) in the DCS guide.
