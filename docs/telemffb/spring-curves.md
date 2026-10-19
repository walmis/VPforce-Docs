# Advanced Spring & G-Force Curves

## Advanced Dynamic Spring Curve Dialog

The advanced spring setting is supported across all simulators in some form. It defines the spring gain mapping as a visual curve across a custom airspeed envelope.

To enable the Advance Spring mode, change the **Joystick Spring Mode** for the desired aircraft to the "**Advanced Dynamic**" mode. Then click the **Configure Settings** button (**Edit Settings** once a curve has been saved) to open the configuration dialog.

On DCS, IL-2 and Falcon BMS the curve reshapes the game's own spring, so the game's trim and center movements keep working underneath it. A VPforce device does this in firmware. A [DirectLink](devices-instances.md) device, or any device the [DirectInput Tap](dinput-tap.md) is capturing, needs the tap: TelemFFB then renders the game's captured spring itself with the curve applied. Without a tap capturing that device, the mode reports that no game spring is available to render.

![](images/spring-curves/adv-spring-entry.png){ width="401px" height="105px" }
![](images/spring-curves/adv-spring-dialog.png){ width="413px" height="462px" }

The form is separated into the X and Y axis configurations. Each axis may be configured separately, although the airspeed scale will be the same for each axis.
Within each axis configuration the following controls are available:

- **Max Force:**

    - The maximum applied spring gain where the configured curve meets %100 on the Y scale.

- **Enable Smooth Curve:**

    - Switch between linear segmented and smooth-curved configurations.

    !!! note
        At least 4 points are required to enable smooth curve mode.

- **Reset**

    - Resets the curve back to a simple 2 point linear curve

Between the two curve configurations, use the ⬆️and ⬇️buttons to copy the X or Y axis curve up or down to the other axis.

Along the bottom there are several additional controls

- **Airspeed Range**

    - **⏪- **Decrease 100 "units"
    - **◀️- **Decrease 10 "units"
    - **Manual **- Enter the airspeed range manually
    - **▶️- **Increase 10 "units"
    - **⏩- **Increase 100 "units
    - **Import VNE (MSFS/XPlane Only)**

        - Import the published (or calculated) VNE from the aircraft telemetry.
        - The sim must be active and telemetry must be flowing to enable the button.

- **Airspeed Unit**

    - Set the airspeed units used by the curves. Regardless of the configured unit, the settings will be scaled to work properly with the live airspeed of the aircraft (usually in m/s as received from the sim)

- **Import**

    - Import a curve setting that was previously exported from TelemFFB

- **Export**

    - Export a curve setting that can be shared or imported into another aircraft

- **Live View**

    - When Live View is enabled, an additional crosshair will appear on the graph when the sim is loaded and telemetry is flowing from the aircraft. The crosshairs will indicate the calculated spring gain at the current airspeed based on the saved curve.

!!! note
    Note that curve modifications are not instant. If the curve has been modified, it must be applied or saved for the modifications to take effect

![](images/spring-curves/adv-spring-curve.gif){ width="564px" height="322px" }

### Working with the Curves

The actual curve editor is a custom widget written entirely in python. The curve uses the Akami algorithm as opposed to other traditional spline methods for its tighter control on overshoot interpolation wildly affecting portions of the curve outside of the segment being edited.

Its use is fairly straight forward with some conditions:

- A minimum of 4 points are required to enable curve smoothing

- The curve must not exceed 0% or %100 spring gain. The widget will prohibit further movement of a point if it will cause **any** point of the curve to exceed the limits

- The widget prohibit smooth curve if the resulting curve would exceed limits

- The widget will not let you add a point that will result in the curve exceeding the limits

The curve controls are as follows:

- **Add Point**

    - To add a point, **right-click** on the graph where you would like the point to be added

- **Move/Drag Point**

    - To move a point, left-click on the point and drag the point where you would like

- **Delete Point**

    - To delete a point, right-click on the desired point and select delete from the popup menu.

![](images/spring-curves/adv-spring-smooth.gif){ width="523px" height="243px" }

### Driving the Curves From a Telemetry Item

Some aircraft change their control feel with something other than airspeed. One example is a jet whose pitch feel unit varies with stabilizer trim position. On such an aircraft, set the [trimmed stick position](msfs-xp-trim-calibration.md#trimmed-stick-position) to **Stays Centered** and draw the elevator curve against trim units.

On MSFS and X-Plane, each curve has its own **Curve Input** selector under its slider, so the X and Y curves can follow different things:

- **Airspeed**: the curve follows airspeed, with the airspeed range and unit controls described above.
- **Telemetry item**: the curve follows the value of a source you choose.

![The Advanced Spring dialog with the X curve on Airspeed and the Y curve on a Telemetry item: a reversed axis from 6.0 to 1.0 in trim units with a rising elevator curve, and the Source, Min, Max and Read Value controls under the Y curve's header](images/spring-curves/curve-input-item.png){ width="475px" height="418px" }

With **Telemetry item** selected, a row under the curve's header shows these controls:

- **Source**: the value the curves follow. The list holds the telemetry items in the Monitor tab, and you can type another name.
- **Min** and **Max**: the left and right ends of the x axis, in the units of the source. Enter Min above Max to reverse the axis, for a source whose value falls as the force should rise.
- **Read Value**: select **Set as Min** or **Set as Max** to fill that field with the live value of the source. The value itself shows beside the button while telemetry is flowing.

The source can be any telemetry item, including one you create with the [overrides editor](telem-overrides.md). It can also be a sim variable that TelemFFB subscribes for the curve: a SimVar, an `L:` var or a `B:` input event on MSFS, or a dataref path on X-Plane. The Monitor tab shows a subscribed variable as `SpringCurveInput_<device>_<curve>`, for example `SpringCurveInput_joystick_y`.

Outside the range, the curve holds its end values: the first point below Min and the last point above Max. A flat section at either end of the curve gives a constant gain there. If the value stops arriving, the last gain stays applied. Live View plots each curve's current x value when an aircraft is loaded.

!!! note
    The curve points keep their x positions when you change the Curve Input. Redraw the curves after you change it. A change back to **Airspeed** restores the airspeed unit and range.

## Advanced Custom Curve G-Force Effect Dialog

The G-Force effect can also be configured through a custom curve. Many aircraft do not have a linear, or even similar, g-loading response, and the standard exponential-curve g-force effect can produce lackluster or erratic behavior on them.

To enable, select "Custom Curve" as the G-Force Effect and click the **Configure Settings** button (**Edit Settings** once a curve has been saved)

![](images/spring-curves/gforce-curve-dialog.png){ width="456px" height="76px" }

Using the same new curve widget as the Advanced Spring Curve feature, a new custom curve G-Effect was created.

![](images/spring-curves/gforce-curve-example.png){ width="382px" height="512px" }

The form is separated into Positive and Negative G scale
configurations.

- **Maximum Force Slider:**

    - Adjust the overall intensity of the effect. Depending on the selected "Force Mode" configuration, it will either adjust the maximum constant force effect application or how much spring center offset is applied to produce the effect.

- **Enable Smooth Curve:**

    - Switch between linear segmented and smooth-curved configurations.

    !!! note
        At least 4 points are required to enable smooth curve mode.

- **Reset**

    - Resets the curve back to a simple 2 point linear curve

In between the positive and negative configurations:

- **Effect Force Mode:**

    - **Constant Force**

        - In this mode, a dynamically changing constant force effect is applied based on the curve point at a given G-loading.

    - **Spring Offset**

        - In this mode, when the G-Effect is playing, a temporary spring center point offset is applied, shifting the center point in the direction required to induce a strengthening of the spring.

### Working with the Curves

See the ***Advanced Custom Spring*** section for guidance on using the curve editor
