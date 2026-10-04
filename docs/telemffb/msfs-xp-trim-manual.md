# Manual Trim Tuning (Legacy)

Before [Automatic Trim Calibration](msfs-xp-trim-calibration.md) existed, users tuned the trim-following gains manually using the procedure below. The calibration tool is the recommended method — it measures the aircraft's actual trim response and computes the values for you. This page remains for reference, for aileron and rudder gains (which the calibration tool does not cover), and for those who prefer manual tuning.

## Suggested Starting Points

Physical & virtual gains should be configured per aircraft. Reasonable starting values are:

| Setting | Physical | Virtual |
|---|---|---|
| Aileron (X) | 50% | 20% |
| Elevator (Y) | 100% | 20% |
| Rudder | 50% | 20% |

Aileron (X) and rudder gains can usually be left at their defaults; many aircraft have no cockpit trim on those axes, and where they do it is a set-and-forget adjustment. The **elevator (Y)** trim is used constantly, so *Y Trim Gain Virtual* is the value most worth tuning per aircraft.

## Tuning the Elevator Trim by Hand

1. Fly the aircraft and trim for level flight at cruise speed.
2. In the VPforce Configurator (or a knob assigned to spring/master gain), temporarily set **spring to 0%** and **friction** high enough that the stick stays put when you let go. *Apply* the setting (do not store it).
3. Without moving the stick, use your trim to nose the aircraft down.
4. Watch the nose:
    - If the nose **goes up**, raise **Y Trim Gain Virtual** by ~10%.
    - If the nose **goes down**, lower it by ~10%. It may need to go negative.
5. Re-trim and observe again. The goal is for trim adjustments to have **no effect on pitch while the stick is held still**. Fine-tune in 5% then 1% steps as you get close.

Remember to restore your normal spring and friction settings when you are done.
