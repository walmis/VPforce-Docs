# Grip Adapters

The VPforce mainboard uses a Thrustmaster-compatible 5-pin grip interface. The adapter you need depends on which grip manufacturer you use.

---

## Native Support (No Adapter Required)

- **Thrustmaster grips** (Cougar, Warthog, F/A-18C) — connect directly to the 5-pin interface. Up to 24 buttons.
- **Virpil grips** (MongoosT-50, WarBRD, Constellation Alpha, Alpha Prime, VFX, AH-64, UH-60, FLNKR) — connect directly. Analog axis data and LED control are supported natively.
- **FC Technologies grips** — connect directly to the 5-pin interface.

---

## WinWing Adapter

![WinWing Adapter](../rhino/media/Pictures/10000000000004E200000539F6FC95994BDEBD44.png){ width="200px" }

The WinWing adapter converts WinWing's proprietary protocol to the Thrustmaster 5-pin standard mechanically and electrically. Unlike native Thrustmaster or Virpil connections, this adapter passes **analog axis data** (brake levers and thumbsticks) to the mainboard.

**Tested and working with:** WinWing F-16EX and F/A-18.

**Setup:**

1.  Mount the WinWing grip onto the adapter.
2.  In the VPforce Configurator, select **"WinWing adapter"** as the grip type from the dropdown menu.

!!! note "Button 32 indicator"

    On newer WinWing adapter firmware revisions, button 32 activates if the grip connection is not detected or is disconnected. This is normal behavior, not an error.

!!! note "Analog axis calibration"

    If a WinWing grip does not report analog axis data, calibrate it in WinWing software on a WinWing base first, then reconnect the grip to the Rhino.

---

## VKB Adapter

![VKB Adapter (revB)](../rhino/media/Pictures/1000020100000727000008001DBCB6BB2E3883E3.png){ width="200px" }

This page covers separate VKB adapter variants for socket rev. B and rev. C grips. Choose the adapter revision that matches your grip socket.

**Requirements:**

- The VKB adapter (mechanical mount).
- A VKB main controller ("Black Box") — required to operate the grip buttons.

**How it works:**

There is no electrical connection between the adapter and the VPforce mainboard. The Black Box connects to the grip via the external adapter cable and handles all button inputs independently. The Black Box may blink red because it does not detect axis inputs. This is normal and does not affect operation.

**Installing the adapter:**

1.  Push the connector into the grip until it makes contact.
2.  Secure the grip with the locking collar.

If the connector is tight, do not apply force to the rotating lower part only. Rotate the entire lower half instead.

**Using VKB buttons in VPforce software:**

To use VKB grip buttons in the Rhino software, run the **RhinoLoopback** companion app and set **Grip Type** to **Loopback** so the Black Box buttons are forwarded to the Rhino. See the [Configurator Settings](../rhino/using-the-rhino.md#grip-type-selection-and-calibration) section in the Rhino manual for setup details.

---

## Custom Grips (Shift-Register)

The VPforce mainboard supports custom-built grips using generic shift-register button inputs via the 5-pin interface. To use a custom grip, select **"Generic (shift-register)"** as the grip type in the VPforce Configurator.

This allows DIY builders to wire their own button matrices using shift registers (e.g., 74HC165) connected to the mainboard's SPI interface.

---

## Troubleshooting

### Connectivity

**Symptom:** WinWing grip buttons or axes do not respond.  
**Cause:** Incorrect grip type selected in the VPforce Configurator or loose adapter connection.  
**Resolution:** Verify that **"WinWing adapter"** is selected in the **Settings** tab and ensure the locking collar is fully tightened.

**Symptom:** VKB grip buttons do not trigger Rhino functions.  
**Cause:** RhinoLoopback is not running, so the VKB Black Box buttons are not being forwarded to the Rhino.  
**Resolution:** Start the **RhinoLoopback** app and set the Grip Type to **"Loopback"** in the VPforce Configurator.

**Symptom:** Button 32 is permanently active on a WinWing grip.  
**Cause:** The grip is disconnected or the adapter firmware is a newer revision.  
**Resolution:** Check the physical connection. If the grip works otherwise, ignore the indicator as it is a normal presence detection behavior on newer firmware.

### Axis Issues

**Symptom:** WinWing brake lever or thumbstick reports no movement.  
**Cause:** The grip requires periodic re-calibration or is not initialized.  
**Resolution:** Connect the grip to an original WinWing base and perform an axis calibration using WinWing software, then return it to the Rhino.

**Symptom:** VKB "Black Box" light blinks red.  
**Cause:** The controller does not see any axis inputs (expected behavior as Rhino handles axes).  
**Resolution:** This is normal operation. No action is required. If the cable from the Black Box to the grip is loose or disconnected, reconnect it.

---

## Further Reading

- [Physical Setup (Rhino Manual)](../rhino/getting-started.md) — full adapter installation instructions with photos
