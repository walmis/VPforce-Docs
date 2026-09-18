# MSFS In-Sim Toolbar Panel

TelemFFB includes an in-sim toolbar panel for Microsoft Flight Simulator. The panel shows the current aircraft's TelemFFB settings and lets you change them without leaving the cockpit. Toggles, choice pills, and sliders are sized for VR laser-pointer and controller use.

The panel talks to a small local HTTP server built into TelemFFB. This server runs only while MSFS is the active sim.

## Enable the panel server

1. Open **System → System Settings → Sim Setup**.
2. On the **MSFS** tab, enable **MSFS**.
3. Enable **Start in-sim settings panel server**. This setting is on by default.

## Install the panel

TelemFFB can install the panel for you.

1. Open **System → System Settings → Sim Setup → MSFS**.
2. Under **In-sim panel installs**, TelemFFB lists each MSFS 2020/2024 copy it finds (Microsoft Store or Steam), with its Community folder path and install status.
3. Click **Install** next to the copy you want. If a version is already installed, this button reads **Update** or **Reinstall** instead.
4. Confirm the prompt. TelemFFB copies the panel into that copy's Community folder.
5. Restart MSFS for the change to take effect.

!!! note "Panel version"
    TelemFFB shows the installed panel version next to each detected copy, alongside the version it can install. Click **Update** when a newer version is available.

## Install the panel manually

Auto-install fails if TelemFFB cannot find your Community folder. When this happens, the install list shows **Couldn't find Community folder (check UserCfg.opt)** and disables the **Install** button for that copy. In that case, copy the panel in yourself:

1. Find the `vpforce-telemffb-panel` folder inside your TelemFFB install directory, at `assets\msfs-panel\vpforce-telemffb-panel`.
2. Copy this whole folder into your MSFS Community folder.
3. Restart MSFS.

!!! tip "Finding your Community folder"
    The Community folder location depends on your MSFS version and edition (Microsoft Store or Steam). Check `UserCfg.opt` for your installed packages path, or see Microsoft's documentation for the exact location on your system.

## Using the panel in MSFS

Open the toolbar at the top of the screen and select the **VPforce Settings** icon. The panel loads the current aircraft's TelemFFB settings once TelemFFB detects that aircraft. Until then, it shows **Waiting for TelemFFB / MSFS aircraft...**

Changes you make in the panel save to the same profile the desktop Settings dialog uses. If the aircraft's active profile is **Built-In**, TelemFFB creates a new **Auto User** profile for it, the same as when you change a setting from the desktop app.
