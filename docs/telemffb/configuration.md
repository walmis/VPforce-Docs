# System Settings

In the System Menu, choose System Settings. The dialog opens from the **master instance** and configures everything, including the settings of every device instance. Child instances have no settings dialog of their own.

The dialog has four tabs:

- **Devices** - which device each instance connects to, how the instances launch, and each device's own settings.
- **Button Devices** - other detected game controllers which can be used for button bindings within TelemFFB.
- **System** - global application settings and startup behavior.
- **Simulator Setup** - per-simulator setup.

!!! note
    For where these settings are stored on disk, see [How Settings Work](settings-model.md).

## Import, Export, and Reset

The dialog's **File** menu backs up and restores the whole configuration:

- **Export Settings...**

    - Writes every stored setting to a JSON file, master and child instances alike, since the whole configuration lives in one store. The file is a complete system-settings backup, suitable for migrating to another machine. Window positions and similar UI state are not portable and are left out.

- **Import Settings...**

    - Loads an export file into the dialog without committing anything. The imported values land in the form exactly as if you had clicked them in, so saving runs every normal check: validation, the live device switch, restart notices, the DirectInput Tap reconcile. Review the tabs, then **Save** to apply or **Cancel** to discard. Devices in the file that are not currently connected survive the import; TelemFFB reconnects them when they appear.

- **Reset to Defaults**

    - Fills the form with the default values. Like an import, nothing is written until you Save.

## Devices Tab

![](images/devices-instances/devices-tab.png){ width="650px" }

### Devices

The **Devices** area holds one **card per device role**: joystick, pedals, collective, trim wheel. Each card carries the device selector, the device's USB IDs, a display name field, and its launch controls: the master-instance marker, the card's auto-launch switch, and a **Window Mode** selection (Normal, Minimized, or Headless). A global **Enable Auto-Launch** switch sits above the cards. The joystick card can hold up to three devices for per-aircraft switching.

[Devices & Instances](devices-instances.md) covers the cards, auto-assignment, multiple joysticks, and the launch options in detail. When a DirectInput device holds a role, its row also carries the axis and force-direction controls described in [DirectInput Devices](devices-instances.md#directinput-devices).

### Device Settings

Below the cards, the **Device Settings** area has one tab per configured device. Each device's page holds the settings that apply to that instance alone:

- **System Logging Level**

    - Logging verbosity for the instance (INFO or DEBUG).

- **Telemetry Timeout (ms)**

    - How long the instance waits for telemetry before treating the sim as stopped.

- **Restore window position** / **Restore last tab view**

    - Remember and restore the instance's window position, per-tab window sizes, and last viewed tab.

- **VPforce Configurator profiles**

    - **Load on Startup** - a Configurator profile to load when TelemFFB starts, with **Make Startup Profile Global Default** to use it as the fallback profile.
    - **Load on Exit** - a profile to load when TelemFFB exits.
    - **Restore Startup Gains on Exit** - re-push the gain values read from the device at startup when TelemFFB exits, leaving the device as it was found. Disabled by default.

    See [VPforce Configurator Integration](vpconf-profiles.md) for how these interact with per-aircraft profiles and gain overrides.

## Button Devices Tab

Any bindable button setting in TelemFFB can be bound to a button on any available game controller:

![System Settings, Button Devices: six controllers listed, two of them enabled and reading, with button 37 held on the VPC Throttle](images/configuration/button-devices-tab.png){ width="650px" }

- **Enabled** - Enable or disable button detection for this device.
- **Status**
    
    - **reading** - TelemFFB is monitoring the device for button events
    - **off** - Detection is disabled for the device 
    - **not readable** - When the device cannot be read. Xbox-style controller connected over USB using X-Input are not supported.

- **Pressed** - The button IDs being detected, live. Use it to confirm the row you expect reacts to the controller.

A hat switch appears as four buttons after the controller's last real button: up, right, down, left. A diagonal presses two of them. A controller whose firmware reports the hat as real buttons as well shows both; a bind takes the lowest number, which matches the Windows game controller test page.

A binding records the controller's IDs, so it follows the controller to another USB port. Two controllers of the same model without serial numbers are told apart by port order, so their bindings swap if you swap their ports.

Child instances show the list read-only; the master instance reads the controllers and relays the buttons.

## System Tab

![](images/configuration/system-settings.png){ width="650px" }

### Global System Settings

- **Theme**

    - **Light** - the light color palette.
    - **Dark** - the dark color palette.
    - **System** (default) - follow the Windows app theme.

- **Prune Logs (Global)**

    - Enable log pruning. Archived log zip files older than the configured threshold are deleted at TelemFFB startup.

- **Disable Update Prompt on Startup**

    - Suppress the new-update prompt at startup. The master instance performs the update check, so this is a global setting.

### Startup Behavior

- **Start with Windows**

    - Add a Windows registry entry that starts TelemFFB automatically when Windows starts.

    !!! note
        Only available with the EXE distribution of TelemFFB. This option is disabled when running from source.

- **Start in System Tray**

    - Start minimized to the system tray. Recall the main window by double-clicking the tray icon or from its right-click context menu.

- **Start Minimized**

    - Start with the main window minimized to the taskbar.

    !!! note
        Start in System Tray and Start Minimized are mutually exclusive; only one may be enabled.

- **Closing App Sends to Tray**

    - The window close button minimizes the application to the system tray instead of exiting. Exit TelemFFB from the System menu or from the tray icon's right-click context menu.

### Integrations

- **DirectLink for TelemFFB**

    - List DirectInput Force Feedback devices (shown with a `[DI]` prefix) alongside VPforce hardware in the device selectors, so they can be assigned to any role. Requires **DirectLink**, a separate product distributed on its own; a status line below the toggle reports the installed version. Most VPforce users can leave this off - it exists to drive non-VPforce hardware.

## Simulator Setup Tab

One page per simulator (DCS, MSFS, X-Plane, IL-2, and BMS), each with its enable switch, auto-setup options, and install paths. [Connecting Your Simulator](sim-setup.md) covers each simulator's page.

The DCS, IL-2, and BMS pages also hold the **DirectInput Tap** section for that simulator; see [The DirectInput Tap](dinput-tap.md).
