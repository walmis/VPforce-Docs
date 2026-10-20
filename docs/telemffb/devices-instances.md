# Devices & Instances

TelemFFB runs **one instance per FFB device**. If you fly with a single VPforce joystick base, one instance is all there is and you can mostly ignore this page. If you also have VPforce-powered pedals or a collective, a separate instance drives each device, and TelemFFB manages them for you.

## Master and Child Instances

The instance you launch is the **master**. It owns everything global:

- The System Settings dialog opens from the master and configures everything, including each child instance's own settings. Child instances have no settings dialog of their own.
- Auto-launching, monitoring, and revealing the **child** instances that drive your additional devices.

Child instances each connect to their own device and render effects for it, driven by the same simulator telemetry. They can run with a normal window, minimized, or headless (no window at all).

## Device Detection

In most cases, you do not need to configure anything: on startup, the master instance enumerates the connected VPforce devices and **auto-assigns** any unassigned device role.

- Assignment is by the device's name as configured in VPforce Configurator: a name containing *Joystick*, *Pedals*, *Collective*, or *Trim* assigns the device to that role.
- Each device takes at most one role, and auto-assignment never overrides an assignment you have already made.
- A device whose name identifies no role is not guessed at; assign it yourself on the Devices tab. On a first launch, TelemFFB reports the auto-assignment result and opens System Settings either way, so you can review and save the assignments ([Quick Start](quick-start.md#first-launch-system-settings)).

To assign devices manually, or fix an auto-assignment, each device role has a **selector pulldown** on its card on the **Devices** tab, listing the connected VPforce devices. With [DirectLink](configuration.md#integrations) enabled, the list also holds the DirectInput force feedback devices on the PC, marked `[DI]`. Pick the device for each role directly. If you pick a device that is already assigned to another role, TelemFFB asks whether to override the other assignment or cancel.

## The Devices Tab

These settings are found on the **Devices** tab of **System → System Settings**. They control which device each instance connects to and which instances start automatically.

![](images/devices-instances/devices-tab.png){ width="650px" }

The tab holds one **card per device role**: joystick, pedals, collective, trim wheel. Each card carries:

- **Device selector**

    - Select the connected device for the role. Auto-assigned devices appear pre-selected. The card shows the selected device's USB ids (`VID:PID`); the selector is the source of truth, so there is nothing to type.

- **Display name**

    - The text shown under the device's icon in the main window, up to 14 characters. Leave it blank to show the device's own name. Each device of the joystick card has its own.

- **Display name**

    - The text shown under the device's icon in the Active Devices panel, up to 14 characters. Leave it blank to show the device's own name, as set in VPforce Configurator.

- **Master instance marker**

    - The radio marker defines the device TelemFFB connects to when launched, the master instance. The master's card hides the launch controls below, because the master launches itself.

- **Auto Launch**

    - The global **Enable Auto-Launch** switch above the cards turns the feature on; each card's own switch controls whether that device's instance starts when the master loads. A card whose auto-launch is off collapses to its header.

- **Window Mode**

    - How the instance's window starts: **Normal** (a regular window), **Minimized** (started minimized to the taskbar), or **Headless** (no window at all; the instance runs invisibly, and everything is configured from the master).

Below the cards, the **Device Settings** area holds each device's per-instance settings: logging level, telemetry timeout, window restore options, and Configurator profiles. See [System Settings](configuration.md#device-settings).

### DirectInput Devices

A row that holds a `[DI]` device shows a few more controls, because a DirectInput base has no VPforce Configurator to set them in.

- **FFB Axis** and **Invert** (pedals, collective and trim wheel) - which of the device's force feedback axes the role drives. **Auto** uses the role's own axis when the device has it, otherwise the first axis that can render force. **Invert** reverses the axis, forces and position both, as reversing the axis in VPforce Configurator does. The joystick drives X and Y and has no choice to make.

- **Forces: Mirror X**, **Mirror Y** and **Rotation** - how the base renders the forces TelemFFB sends. Some bases play a force the opposite way, or turned by 90 degrees, while their position reads correctly. A mirror reverses the forces on one axis without touching the position; the rotation turns the direction of pushes and vibrations by 0, 90, 180 or 270 degrees. With nothing set, the forces go to the base as they are.

- **Detect...** - measures the base and fills in the three controls. Run it from the master instance, on the device the master is connected to. If a simulator is connected, TelemFFB pauses its telemetry for the run. The run has four stages, with a prompt for each: an input check (push the stick forward, then right, and let go), a light spring on each axis, two light pushes against a centering spring, and a verification of the result. Keep your hands off the stick except when a prompt asks for a push. At the end, the controls show the correction, and **Save** applies it.

    The run stops, and says why, when the base does something a mirror or a rotation cannot describe: an axis that reports movement the other way or on the other axis when you push (reverse it with **Invert**, or in the device's software, and run again), a spring that drives the stick to its stop, a push that does not move the stick, or a verification that fails.

- A base TelemFFB knows starts with the correction it needs, shown in the controls without a run. The Brunner CLS-E (USB ids `25BB:00CA`) is the one known base so far. A saved setting always takes precedence over the built-in one.

Which forces reach the base, and how strong, is set the same way as on a VPforce device: through the aircraft settings and the [effect levels](effect-levels.md).

## Multiple Joysticks (MSFS & X-Plane)

If you fly with more than one stick (a center stick, a yoke, and a side stick, for example), the joystick slot can hold up to three configured devices, and each aircraft can choose which one it uses.

### Configuring Alternate Devices

On the **Devices** tab, the joystick card has a **+ add device** button. Each added row gets its own device selector and icon.

![](images/devices-instances/joystick-alternates.png){ width="650px" }

- The radio marker on a row marks the **primary** device. The primary is the default: every aircraft and class uses it unless its own [Device selection](#choosing-a-device-per-aircraft) says otherwise, and it is the device the joystick instance connects to on startup.
- Selecting the marker on another row makes that device the primary when you save. The switch applies immediately; no restart is required.
- The **x** button removes an alternate row. The primary row cannot be removed, only replaced.

### Choosing a Device per Aircraft

With more than one joystick configured, aircraft settings gain a **Device** section with a **Joystick Device** selector.

![](images/devices-instances/aircraft-device.png){ width="550px" }

- **Primary (default)** uses whichever device is marked primary in System Settings. The `*` in the list shows which named device that currently is.
- Picking a named device switches to it while that aircraft is loaded, and back to the primary afterward. Nothing changes in System Settings.

!!! note
    The Device section only appears when more than one joystick device is configured. With a single stick there is nothing to choose, and the section stays hidden.

If you later replace a configured device in System Settings, TelemFFB offers to update the aircraft settings that reference the old one.

## Device Recovery

A device can drop off while TelemFFB runs: a cable gets pulled, a hub resets, or the device is power cycled. TelemFFB recovers without a restart.

- **A device that drops off** shows a yellow icon. TelemFFB looks for it by its USB identity, not by the port it was on, so plugging it into a different port or hub works. The retries slow down the longer the device stays away.
- **A device that is missing at startup** shows a red icon. TelemFFB keeps checking and opens the device when it appears.
- **After a power cycle** the firmware has lost what it held in memory. TelemFFB sends the active [VPforce Configurator profile](vpconf-profiles.md), the gain overrides and the configured deadzone again. The effects that were running resume.
- **If a different VPforce device is connected** while the configured one is missing, TelemFFB asks once whether to use it instead. Answer Yes and the selection is saved, the same as choosing it on the device card.

Changing a device on the Devices tab also takes effect at once. See [System Settings](configuration.md).

## Working with Child Instances

After starting TelemFFB with auto-launch enabled, all of the device icons appear in the master instance's **Active Devices** area. From there you can monitor each device's status and switch between devices to configure their settings; each device has its own settings for every aircraft, so your pedals and joystick are tuned independently. See [Active Devices Area](ui-overview.md#active-devices-area) for details. You can also show the device icons in a compact strip, in one of several locations; see [Where the Devices Are Shown](ui-overview.md#device-panel).

When you switch the master to a child device, the master's **Monitor** tab shows that device's telemetry and active effects. The child instance sends its telemetry to the master while you look at it. See [Child device data](ui-overview.md#child-device-data).

To bring up the window of a minimized or headless child instance:

- use the master instance's **Window** menu, or
- right-click the system tray icon and use the **Instances** menu.
