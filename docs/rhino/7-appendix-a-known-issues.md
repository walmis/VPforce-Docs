# Appendix A: Known issues

The following is a collection of issues that are known
to cause issues with the VPforce Rhino or FFB in general:

If you have other issues you feel would be useful to
document here, please post in the discord.

**DCS**

1.  Axis curves are generally incompatible with FFB. This also applies to axis saturation settings in DCS. When curves or axis saturation are used, the FFB absolute position is no longer in sync with the logical position as a result of the curve. This will result in incorrect trimming, autopilot issues and particularly bad force-trimming in helicopters.

2.  The SimHaptic application by rkApps has an "auto start" feature that will launch the application when DCS starts. It is unknown whether the issue is on the SimHaptic side or the DCS side, however this auto-start feature will interfere with and stop FFB from working in DCS. Disabling the auto-start feature in this app will resolve the issue (Issue still exists as of April 2025).

3.  vJoy can also cause issues with FFB device detection in DCS. Ultimately, DCS only supports 1 FFB device. If you are experiencing issues with FFB properly working in DCS, check the DCS logs for vJoy starting and see if it indicates support for FFB in the log message. Either uninstall vJoy or disable the FFB capabilities of vJoy to resolve.

**IL2**

1.  IL-2 only supports 8 USB devices. It is common for users to have more than 8 peripheral devices. While possible to unplug un-needed devices during gameplay so that IL2 will see your Rhino devices, a better solution is to use [*devreorder*](https://forum.il2sturmovik.com/topic/72473-so-you-went-and-bought-too-many-peripherals/) to alter which devices IL2 will see and in what order they will

