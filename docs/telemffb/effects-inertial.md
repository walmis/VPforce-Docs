# Inertial Effects

Effects driven by acceleration telemetry, in the order they appear under the **Inertial** section of the Settings tab. The badge lines and sub-setting tables are generated from the application's settings catalog, so they always match the app.

## G-Force Effect

<!-- telemffb-effect name=gforce_effect_mode part=badges -->

Simulates the increasing pull force required on the stick as g-loading builds in a dive pull-out or hard turn. The force is a percentage of the constant-force value in VPforce Configurator. The mode dropdown selects between two implementations, each with its own sub-settings:

- **Exponential Curve (legacy)** - force ramps between *Minimum Gs* and *Maximum Gs*, shaped by the *G Force Curvature*: 1.0 is linear across the g range; higher values flatten the onset and steepen the force toward the top (default 2.2).

    ![Example curvature values and the resulting force curves](images/effects-inertial/gforce-curvature-plot.png){ width="411px" height="320px" }
- **Custom Curve** - a force is calculated from the current g-loading between the min and max G settings, and the **physical stick deflection** determines how much of it applies. Example: g-loading halfway between min and max gives a 50% calculated force; with the stick pulled back 50%, the output is 0.5 × 0.5 = 25%. As you pull harder, both factors rise. The *Y-Axis Max Point* sets the deflection at which 100% of the calculated force applies; negative-g support has mirrored settings. The *Advanced* option maps the response through a visual curve editor; see [Advanced Spring & G-Force Curves](spring-curves.md).

<!-- telemffb-effect name=gforce_effect_mode part=table -->

## Deceleration Effect

<!-- telemffb-effect name=deceleration_effect_enable part=badges -->

Monitors deceleration g-forces and, while the aircraft is on the ground, pushes the stick forward (away from the pilot) proportionally to the deceleration; braking you can feel. Capped at *Deceleration Max Force*, scalable, invertible, and restrictable to ground operations.

<!-- telemffb-effect name=deceleration_effect_enable part=table -->

## Simulated Lateral Force

<!-- telemffb-effect name=uncoordinated_turn_effect_enabled part=badges -->

Simulates the lateral acceleration felt in uncoordinated flight: slip or skid pushes the stick sideways, the way your body would lean in the real aircraft.

<!-- telemffb-effect name=uncoordinated_turn_effect_enabled part=table -->
