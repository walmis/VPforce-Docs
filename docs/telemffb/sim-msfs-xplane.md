# MSFS & X-Plane

Neither Microsoft Flight Simulator nor X-Plane has native force feedback support. For these simulators, TelemFFB provides the complete FFB implementation: the spring forces on your axes, trim and autopilot behavior, helicopter force trim, and the full effects suite, all driven by telemetry.

!!! important "Key points"
    - **MSFS**: when Axis Control is enabled, you must **unbind your joystick and pedal axes in MSFS**. See [Axis Control & Spring Modes](msfs-xp-axis-spring.md).
    - **X-Plane**: no unbinding is needed, but the **TelemFFB X-Plane plugin** must be installed. Enable *Auto X-Plane Setup* in [Connecting Your Simulator](sim-setup.md#x-plane-1112).
    - Per-aircraft tuning matters most for the **elevator trim response**; the [Automatic Trim Calibration](msfs-xp-trim-calibration.md) tool measures it for you.

This guide is split into chapters. For a first-time setup, read them in order:

1. **[Axis Control & Spring Modes](msfs-xp-axis-spring.md)** - how TelemFFB takes over your axes, and how the spring force is modeled (Basic Dynamic, Spring Centering, FBW, Advanced Dynamic).
2. **[Trim & Autopilot Following](msfs-xp-trim-following.md)** - the stick follows the aircraft's trim and autopilot, relieving control pressure like a real aircraft.
3. **[Automatic Trim Calibration](msfs-xp-trim-calibration.md)** - TelemFFB flies the aircraft briefly and measures the correct trim-following gains.
4. **[Helicopters](msfs-xp-helicopters.md)** - force trim emulation, plus the HPG and FlyInside integrations.
5. **[Aircraft with Special Treatment](msfs-xp-special-aircraft.md)** - the roster of addon aircraft with dedicated classes or curated profiles, and which of them need a cloned profile.

Sim-specific effect settings (buffeting, turbulence, engine rumble, and the rest) are covered in the [Effects Reference](effects-overview.md); see the full per-sim directories for [MSFS](effects-sim-msfs.md) and [X-Plane](effects-sim-xplane.md).

For advanced per-aircraft integration (re-sourcing a telemetry item from an addon's custom variables, or subscribing to additional ones), see [Telemetry Overrides](telem-overrides.md).

**MSFS only**: TelemFFB also offers an [In-Sim Toolbar Panel](msfs-toolbar-panel.md) that shows and edits the current aircraft's settings from inside the cockpit, without switching to the desktop app.

