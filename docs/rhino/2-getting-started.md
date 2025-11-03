# Getting Started

Force feedback is a fascinating but occasionally tricky subject. The complexity doesn't come from the Rhino itself so much as from the sheer number of ways this technology can be used. Every simulator, every software layer, and every user's setup brings its own flavor to the mix. The good news is that once you understand the basics, it all starts to make sense - and you can eat Rhinos the same way you eat elephants: *one bite at a time*.

This section of the manual is designed to guide you through that first meal. We'll start with the essentials - getting your Rhino physically installed, connected, and recognized by the system - and move on to configuring the software so that you can experience your first proper force feedback flight or drive. By the end of this section, you'll have a fully functional controller, ready to use with any simulator that supports FFB. The finer details, like tuning response curves, effect strengths, and simulator integrations, will come later once you're ready for more.

Before diving in, it's helpful to know what you're actually working with. The Rhino isn't just a joystick base with motors; it's a high-precision control loading system capable of recreating complex physical sensations - from aerodynamic forces to mechanical friction - in real time. Each motor in the Rhino responds to both software commands and your own inputs, constantly adjusting torque to simulate how a real control stick behaves under load. That means correct setup and calibration are key to unlocking its full potential.

In this section, we'll cover:

-   **Mounting and physical setup:** How to secure the Rhino safely and give it the stability it deserves (and demands).
-   **Connecting and powering up:** What to check before plugging it in and how to avoid common pitfalls.
-   **Basic software configuration:** Installing and launching the FFB Configurator, testing motor response, and ensuring everything communicates correctly.
-   **Initial calibration and safety:** How to center, verify movement, and use the safety stop effectively before your first live test.

Once these steps are complete, you'll have a working Rhino that's ready to stretch its legs - or, more accurately, its torque. You'll be able to jump straight into a simulator like *DCS World* or *IL-2 Great Battles* and feel genuine aerodynamic resistance, not just spring tension.

The deeper sections of this manual will then show you how to fine-tune those sensations - how to make it feel heavier, smoother, lighter, or more "alive" depending on what you're flying or driving. But for now, take it slow, enjoy the process, and remember: taming a Rhino isn't difficult. You just have to start with one careful bite.


## Technical Specifications

- Weight: 5.2 kg
- Size: 205mm x 180mm base
- height to the top of the grip connector 290mm
- Motors:
    -   Two type 57BLF03 NEMA servo motors
    -   Max 30A drive current per motor
    -   Resolution: 14 bit / Rev, 13 bit effective stick resolution\
        12 bit / Rev, 11bit effective stick resolution (before 2023 Q2)
    -   Typical power: 150W
- Maximum torque: 9 N‧m per-axis
- Gimbal: 3D Printed PETG / Aluminum / Bearings
- Transmission: 1:6.2 ratio belt drive
- Maximum throw: 22 degrees each direction
- Built-in functions: 1 bindable rotary axis (defaults to spring force strength)
- One emergency button that cuts off all power to the motors
- Cooling: Two fans kick in when the motors reach 50°C
- Power source: 180W, 20V

Grip Compatibility:

- Thrustmaster directly
- Virpil directly (T-50CM2, WarBRD, Constellation Alpha, V.F.X)
- VKB with an adapter and a black box
- WinWing with an adapter

## Physical Setup

![](media/Pictures/10000201000008000000068638AB768B99FDE16D.png){ width="336px" height="274px" }

The VPforce Rhino can be attached to any suitably durable and rigid mounting with four 6mm bolts (see schematic).

Due to the weight and strength of the hardware, the mounting structure needs to be designed accordingly. Also note that the gear and belt drives are on the outside of the base structure and it is important to make sure that they do not make any contact with other parts of the mounting system or the person in the pilot's seat.

Attach the power cable and the included USB cable to the Rhino base and then connect them to the power socket and computer respectively.

The big red button is an important safety feature, make sure that you have unrestricted access to it at all times. To facilitate this you can rotate the Rhino and reverse the axis in software (see 2.4 for details).

To cut off all power to the motors, simply push down on the big red button until it locks.

To reset, rotate clockwise and let the button pop up.

The rotating knob can be used to control different features of the Rhino (see software sections for details), by default it controls the spring force.

The Rhino supports Thrustmaster (Cougar, Warthog, F/A-18C) and Virpil grips directly.

Note that rotating Thrustmaster grips requires the use of an extension. For VKB and Winwing see below.

###  The VKB Adapter

![](media/Pictures/1000020100000727000008001DBCB6BB2E3883E3.png){ width="156px" height="174px" }

The VKB Adapter allows for the mounting of any socket rev. B and C style VKB grips. In addition to the Adapter, you will need a VKB main controller (black box) to operate VKB grips with the Rhino. 

!!! note
    The adapter has an external cable that attaches to the black box (see picture).

To connect the adapter to your VKB grip, push the connector into the grip until it makes contact and secure with the little screw thing - basically exactly as with a normal VKB base.

**Important:** if the connector is tight and doesn't want to go in easily, DO NOT apply force to the rotating lower part. This can pinch and mangle the wire coming out of the adapter. Sitting on the adapter is also highly not recommended.

There is no electrical connection between the adapter and the Rhino, so you can simply place the adapter on the Rhino connector, rotate the grip freely into a suitably ergonomic position and screw the adapter's lower part in until the connection is secure enough to hold the grip without rotating under stress. Re-tighten if necessary.

!!! note
    The black box will blink a red light, because it doesn't see any axis (only the grip connects to the black box). This is normal and will not hamper the operation of the device.

To use a VKB grip's buttons for force trim or other functions in the Rhino software, you need to use the included RhinoLoopback app. See details in the relevant section.

![](media/Pictures/10000000000004E200000539F6FC95994BDEBD44.png){ width="170px" height="182px" }

###  The WinWing Adapter

The WinWing adapter adapts the WinWing grips to the Rhino interface both mechanically and electrically. Tested and correctly working correctly with the WinWing F-16EX and F-18 grips.

It converts the proprietary WinWing protocol to a TM standard 5-pin interface and also passes analog axis data such as brake lever and thumbsticks. It should be compatible with TM/Virpil bases, but without the analog axis functionality and possibly limited to 24 buttons.

In some rare cases a WinWing grip will not report analog axis data, in that case a calibration of the grip analog functions needs to be performed via WinWing software on a WinWing base.

To use the full grip functionality on the Rhino base the "WinWing adapter" grip type needs to be selected in the drop down menu.

![](media/Pictures/100002010000029C0000001C8EB99BF61ACD2EA1.png){ width="624px" height="27px" }

![](media/Pictures/100002010000003600000068B5D6998D65E731A8.png){ width="40px" height="77px" }

On newer revisions of the WinWing adapter firmware, button number 32 will illuminate if the Grip connection with the WinWing grip is not functioning/disconnected.

###  The RHINO Throw Limiter Adapters

The RHINO has a significant amount of throw - 22 degrees - and a long shaft compared to most comparable controllers. The long throw does help with accuracy, but especially with extensions the wide movement range can become excessive. It is possible to set limiters in software, but depending on how much force you are using in general, the software limiter may not feel strong enough. The physical throw limiter adapters offer a simple to install alternative solution that sets hard physical limits to the stick's movement.

The adapters come in two pieces - front and back. They can be ordered in different configurations and may have different movement ranges in different directions. To install the adapter plates,

1.  Unscrew the four Torx T5 screws that connect the dust cover at the base of the stick shaft to the RHINO base and lift the cover slightly - you don't need to remove it completely. With the cover out of the way, you should now be able to see the opening the stick shaft goes through and the top of the gimbal assembly inside the base.

2.  Insert the two limiter plates in the stick shaft opening. **Text side is up** and **FWD is forwards**. When installed correctly, the plates should fit snugly in the opening and stay firmly in place.

3.  Place the dust cover plate on top of the limiter plates so that the screw holes align and reattach the screws so that they hold the whole shebang in place. There is no need to go full gorilla on the screws, but do note that they are now holding in place not just the dust cover, but also the limiters that make physical and sometimes somewhat forcible contact with the stick shaft.

4.  Recalibrate the controller for the new throw ranges.

## Initial Connection and Updating the Firmware

When you connect the **Rhino** to your computer for the first time, a popup should appear with a link to the **VPforce WebUSB Tool**. If you miss the popup, you can visit the site directly:[](https://vpforcecontrols.com/usb/rhino/)[*https://vpforcecontrols.com/usb/rhino/*](https://vpforcecontrols.com/usb/rhino/).

On the website, click **"Connect"** to access firmware updates and basic configuration utilities. Select the correct Rhino from the list (for most users, it will be the only one shown) and click **"Connect"** again to establish the connection.

![](media/Pictures/10000201000002B7000001ED6823A57A905CB1E9.png){ width="403px" height="286px" }

If the system detects that a newer firmware version is available, it will give you the option to update it - unsurprisingly labeled **"Update Firmware"**.

The same website also provides access to download the **Rhino Desktop Software** package for more advanced configuration and control.

!!! note
    WebUSB requires a Chromium-based browser to function. Supported browsers include **Google Chrome, Brave, Microsoft Edge, Opera**, and similar. **Firefox and other non-Chromium browsers do not support WebUSB**, so the connection will not work in them.

## Installing the Software and Basic Operation

###  Installing and Using the VPforce FFB Configurator

1.  **Download and Install the Software** Go to [](https://vpforcecontrols.com/usb/rhino/)[*https://vpforcecontrols.com/usb/rhino/*](https://vpforcecontrols.com/usb/rhino/) and download the latest **Rhino Desktop Software package**. While older versions are available, it's recommended to use the latest release. The software comes as a simple ZIP file - unpack it to a folder of your choice.\ To start the configurator, double-click **"VPforce_FFB_Configurator.exe"** inside the folder.

2.  **Verify Connection** Once open, you should see values like **raw_x** and **raw_y** react as you move the stick, along with **curr_x**, **curr_y**, and other parameters. If nothing appears:

    - Check that the **Power supply** and **USB cable** are connected.
    - Make sure the **big red button** is not pressed in (rotate clockwise to reset if needed).

3.  Additional troubleshooting tips can be found in the relevant sections of this manual.

4.  **Calibrate the Sensors**

    -   **This step is not required for production units, since they are calibrated before shipping**
    -   Go to the **Settings tab** and click **"Auto Calibrate"**.
    -   Move the stick to all extremes to allow the software to detect the full range of motion.
    -   Turn off **Auto Calibrate**, then click **"Send Config"** to make the calibration active.

5.  **Saving the Configuration:**

    - **Apply Config:** Activates the current configuration temporarily; it will be lost on device restart.
    - **Store Config:** Saves the configuration permanently to the Rhino's flash memory.
    - **Read Config:** Loads the stored device configuration back into the software.

!!! tip
    If the stick's movement feels excessive, see the **"Endstops"** section in the main software chapter. Or a **physical limiter** can be placed.

7.  **Basic Settings Overview**

    -   **Master Gain (Settings tab):** This is the main power slider for the Rhino. Start at 100% to explore the full range, or lower it to suit your setup.

    -   **Periodic Effects (below Master Gain):** Used for in-game events like stall shakes, gunfire, or engine vibrations.

8.  **Testing the Controller**

    -   Go to the **Effects tab** and select **"Spring"**, setting its gain to 100%.
    -   Ensure the **Spring slider** in the Settings tab is not at zero.
    -   The stick will otherwise feel limp until it receives input from a game or software. The **Spring effect** in the configurator provides basic centering so you can feel the Rhino and experiment with other settings.

9.  **Important:** Do not select **"Sticky"** at this point. Keeping it active will override other software and prevent your simulator from controlling the force feedback properly.

10. **Next Steps**
    Once calibration and basic settings are complete, you're ready to start testing the Rhino in your simulator. For detailed configuration options, advanced effects, and game-specific setups, see the main sections of this manual.

    With this setup, you're now ready to begin your journey into the
subtle art, and raw power, of Rhino force feedback.
