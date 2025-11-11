# Appendix A: Known issues

The following is a collection of issues that are known
to cause issues with the VPforce Rhino or FFB in general:

If you have other issues you feel would be useful to
document here, please post in the discord.

**DCS**

1.  **Axis curves are incompatible with Force Feedback (FFB)**

    Using axis curves or saturation with an FFB device creates a mismatch between the physical position of your joystick and the logical position the game sees.

    *   **Physical Position:** Where your stick actually is. This is where FFB forces are applied.
    *   **Logical Position:** What the game sees after the curve is applied.

    The game sends FFB commands based on the logical position, but your joystick's motors act on the physical position. This disconnect causes several problems:

    *   **Incorrect Trimming:** When you trim, the stick will not stay in the position you released it. It will jump to a different physical spot.
    *   **Autopilot Errors:** The autopilot will make physical movements that are either too large or too small.
    *   **Unstable FFB:** The game and the FFB system are effectively fighting each other, leading to unpredictable behavior.

    !!! important "Solution"
        Always use linear (straight line) axis curves for your FFB device. If you need to adjust sensitivity, do so using in-game settings that do not affect the FFB data.

2.  The SimHaptic application by rkApps has an "auto start" feature that will launch the application when DCS starts. It is unknown whether the issue is on the SimHaptic side or the DCS side, however this auto-start feature will interfere with and stop FFB from working in DCS. Disabling the auto-start feature in this app will resolve the issue (Issue still exists as of April 2025).

3.  vJoy can also cause issues with FFB device detection in DCS. Ultimately, DCS only supports 1 FFB device. If you are experiencing issues with FFB properly working in DCS, check the DCS logs for vJoy starting and see if it indicates support for FFB in the log message. Either uninstall vJoy or disable the FFB capabilities of vJoy to resolve.

**IL2**

1.  IL-2 only supports 8 USB devices. It is common for users to have more than 8 peripheral devices. While possible to unplug un-needed devices during gameplay so that IL2 will see your Rhino devices, a better solution is to use [*devreorder*](https://forum.il2sturmovik.com/topic/72473-so-you-went-and-bought-too-many-peripherals/) to alter which devices IL2 will see and in what order they will

