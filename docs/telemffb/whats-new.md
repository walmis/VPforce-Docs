# What's New in TelemFFB 2.0

### TelemFFB 2.0 - New Features and functionality

Version 2.0 of TelemFFB, released in October 2025, is a major upgrade from the previous versions. Updated/New features include, but are not limited to:

-   New UI framework supporting dark/light mode themes

-   Completely new offline/class/sim default editor interface

-   Multiple aircraft profile support for the same sim/aircraft combination

-   Aircraft profile import/export

-   Advanced spring-curve mapping for custom dynamic spring force configuration

-   New effects

-   Beta support for Falcon BMS

    -   Basic effects are functional. Little testing has been performed given this developer's lack of experience with BMS.

    -   There are likely many effect settings which are not properly plumbed or the effect does not work as expected due to limited/non-existent telemetry data

    -   The more people use it and report feedback, the better it will become

### Upgrading from previous TelemFFB Versions

When you load TelemFFB 2.0 for the first time, your existing TelemFFB settings file (userconfig.xml) will be upgraded to the new v2 format. The following conversions will take place:

-   All existing user aircraft settings will be converted into user profiles. The auto-created user profiles are called "Auto User". You may rename the profiles after the conversion process via the Profiles→Profile Manager interface.

-   Any user defined aircraft that do not have a default profile will become "User Default" aircraft. While you can create further custom profiles based on these User Default entries, you can not rename User Default.

-   Configurations that previously had multiple toggle flags to configure different versions of the same thing have been converted into pulldown options to enable a specific setting and show the appropriate sub settings. An example of this is the spring mode for MSFS. Previously you could enable "FBW" or "Spring Centered (non FBW)" but these were two separate toggles that needed to be manually enabled/disabled. The new pull-down options allow you to select the appropriate top level setting which will then only show the corresponding sub settings.

Upgrading to version 2.0 requires no further action.
