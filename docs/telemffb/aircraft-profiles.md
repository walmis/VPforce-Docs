# Aircraft Profiles

## How TelemFFB Matches an Aircraft

Every aircraft profile has a **match string**. When an aircraft loads, TelemFFB compares each match string with the aircraft name the simulator reports. That name is shown as **Current Aircraft** in the status area. The match string that wins is shown as **Matched Model**.

A match string is a regular expression, and matching starts at the beginning of the name. `Cessna 172` therefore matches `Cessna 172`, `Cessna 172 Skyhawk` and any livery whose name starts that way. `Cessna 172` and `Cessna 172.*` behave the same. Only `^Cessna 172$` matches that one name and nothing longer.

### Which Match String Wins

Several match strings can fit the same aircraft. The most specific one wins:

1. An exact match string, written as `^Name$`, beats every other form.
2. Otherwise, the match string with the longer run of fixed text wins. `737-600.*` beats `737.*`.
3. If two match strings fix the same text, the one that requires it at the start of the name wins. `C-17.*` beats `.*C-17.*`.
4. If they are still equal, the built-in profile wins over yours. Within one file, the earlier entry wins.

!!! note "Only the winning profile applies"

    Settings and [telemetry overrides](telem-overrides.md) come from the one profile that matched. A broader profile that also fits the name adds nothing. The Settings tab shows what is in effect.

    Anything the winning profile leaves unset comes from your class and sim overrides, then from the shipped defaults. See [How Settings Work](settings-model.md).

!!! tip "Checking a match"

    The log line `Pattern Match:` names the winning match string each time an aircraft loads.

## Adding New Aircraft Support

While TelemFFB has default profiles for many aircraft already, there are many hundreds of possible aircraft between all of the simulators that are supported. So, inevitably you will run into an aircraft that does not already have a built-in profile.

There are two ways to add support for new or unknown aircraft to TelemFFB:

- Dynamically when a new aircraft is loaded in a simulator
- Via the Profile Manager, independent of any running sim

### Accessing the New Aircraft Dialog

#### Dynamically from Main Window (Recommended)

When you load an aircraft that matches no profile, the main window shows a red **No Profile Found for** prompt that names the aircraft. Click it to open the New Aircraft Wizard. Use this method where you can, because TelemFFB already knows the exact name the simulator sends.

Until the profile exists, the controls on the Settings tab are disabled. An unknown aircraft has no profile to store a change in. The aircraft still gets the sim defaults and, where the simulator reports the aircraft type, the defaults for that class.

![](images/aircraft-profiles/new-aircraft-main.png){ width="650px" }

#### Adding New Aircraft via Profile Manager

Open the Profile Manager and select the "New Aircraft Wizard" button. This method is not recommended, because it is difficult to know the exact name TelemFFB will receive from a given simulator.

![](images/aircraft-profiles/wizard-1.png){ width="335px" height="126px" }

![](images/aircraft-profiles/wizard-2.png){ width="415px" height="353px" }

### The Add New Aircraft Wizard

After accessing the wizard via one of the two methods above, simply follow the steps in the wizard to add the new aircraft.

**Page 1:**

1. **If manually adding a new aircraft**, select the simulator on the first page.

**Page 2:**

1. Select the appropriate aircraft class for the aircraft you are adding.

    - Note that for MSFS, the aircraft type will be auto-detected based on telemetry data. However, you should validate that the selection is correct.
    - This matters most for aircraft with special treatment, such as those from **HPG**, **FlyInside** and **CowanSim**. The simulator reports them as plain helicopters. They need their own TelemFFB class to work fully. See [Aircraft with Special Treatment](msfs-xp-special-aircraft.md) for the full roster.

**Page 3:**

1. **If manually adding a new aircraft**, enter the full aircraft name that will be sent via telemetry from the simulator.

    - If auto-detected, this will already be filled out for you.
2. Choose a match string for the aircraft. See [How TelemFFB Matches an Aircraft](#how-telemffb-matches-an-aircraft) for the rules.

    - The wizard suggests match strings built from the aircraft name, most specific first. The list starts with the exact form, `^Full Name$`. It continues with the whole name followed by `.*`, then drops one word at a time from the end.
    - The wizard preselects the suggestion that drops the last word. The last word of a name is usually the livery, the variant or the registration, and a match string that includes it fits only that one aircraft. If dropping a word would leave only the manufacturer, the wizard keeps the whole name.
    - Pick a shorter suggestion to cover a family of liveries or variants with one profile. Pick the exact form to cover one aircraft only.
    - You can also type your own match string. The field turns red when the string does not match the aircraft name.

    ![The match string page of the New Aircraft Wizard, with the suggestions listed most specific first](images/aircraft-profiles/wizard-match-string.png){ width="600px" }

3. Optional: clone from an existing aircraft.

    - The new aircraft starts with a copy of the chosen profile's settings and telemetry overrides.

    !!! note "Classes that must be cloned"

        For **HPG** and **FlyInside** aircraft, cloning from one of the built-in profiles is mandatory. Some of the telemetry sources those classes read differ per aircraft, so they live in the aircraft's profile.

        The other special classes carry their telemetry sources on the class itself. For those, selecting the correct class on Page 2 is enough.

## Overlapping Profiles

A TelemFFB update can ship a built-in profile for an aircraft you already made a profile for. When both match the loaded aircraft, the main window shows a **Multiple matching profiles detected** prompt, and a tray notification if the window is hidden. Click the prompt to decide what to do.

![The Multiple matching profiles prompt on the main window](images/aircraft-profiles/multi-match-prompt.png){ width="650px" }

The more specific match string names the aircraft, and the built-in wins a tie. The dialog says which side applies today, and lists the settings and telemetry overrides of both next to the result of a merge. **Bold** rows would change if you merge. Amber rows are values the two sides set differently; yours wins. Hover a button to see exactly what it does.

![The Multiple matching profiles dialog, showing the built-in, your profile and the merged result side by side](images/aircraft-profiles/multi-match-dialog.png){ width="760px" }

- **Merge into the built-in** - your profiles and telemetry overrides move to the built-in as user profiles, and your active profile stays active. **User Default** becomes **Auto User**. Nothing you set is lost. If your match string was broader than the built-in's, it stays for the other aircraft it names, and your profiles are copied instead of moved.
- **Keep mine** / **Don't ask again** - leave everything as it is. Offered only while your settings still apply: when your match string is the more specific one, or identical to the built-in's.
- **Not now** - decide later. The prompt stays until you answer.

A **Keep mine** or **Don't ask again** answer lapses when a later release changes the built-in profile, and TelemFFB asks again. To be asked again now, use **Profiles → Reset Dismissed Profile Prompts**. A merge is permanent.

## Forking a Profile

A broad profile can cover many liveries or variants of an aircraft. Sometimes one of them needs settings of its own. The **fork button** beside **Matched Model** in the status area does this without any hand-editing: it forks the loaded aircraft off its current match onto a new, more specific one.

![The status area, with the fork button beside the Matched Model row](images/aircraft-profiles/split-button.png){ width="450px" }

The button is available once a profile names the loaded aircraft. It is disabled on child instances and in the offline editor. When nothing matches, the **No Profile Found for** prompt takes its place.

Click the button to open the New Aircraft Wizard, already filled in for the loaded aircraft:

![The New Aircraft Wizard opened from the fork button](images/aircraft-profiles/split-wizard.png){ width="600px" }

1. Check the aircraft class. It is preselected from the profile in effect now. Click **Next**.

2. Choose the match string.

    - The wizard offers only match strings that are more specific than the current one. A broader or equal match string would lose to the current profile, and the new profile would never apply.
    - If you type your own match string and it is not specific enough, the field turns red and its tooltip says why.

3. Choose what the new profile starts from.

    - **Inherit settings from the current match / profile** copies the settings and telemetry overrides of the profile in effect now. Use this when the aircraft is close to its neighbors and needs a few changes. The **Clone From** list shows the profile it copies.
    - **Create a new model with no inherited settings** starts with the aircraft class and nothing else. Use this when the aircraft matched the wrong profile. This choice is not available for classes that must be cloned.

![The match string page when opened from the fork button, with the choice between inheriting and starting new](images/aircraft-profiles/split-wizard-choice.png){ width="600px" }

After you finish, the new profile names the aircraft at once. The other aircraft that the broader profile covers are not affected.

!!! note

    A profile made this way does not trigger the **Multiple matching profiles** prompt. Both profiles are yours, and the wizard already asked what to copy.

## Profile Manager

TelemFFB supports multiple settings profiles for any given aircraft, all centrally managed through the Profile Manager.

In the main window of the profile manager is a tree list of all of the built-in default, user created default and individual profiles. Built-in profiles are fixed and can not be deleted, exported or modified. They can be cloned into new profiles, but the original built-in settings will be retained in the built-in profile.

Only aircraft for simulators that are enabled in the ***system settings*** will be shown in the list.

![](images/aircraft-profiles/profile-manager.png){ width="568px" height="565px" }

There is a series of radio buttons that will change the scope of the displayed profiles.

![](images/aircraft-profiles/profile-manager-context.png){ width="390px" height="120px" }

- **Active\\Inactive checkboxes**

    - Filter the list of profiles to show Active, Inactive or both. The active profile is the profile that will be used when the aircraft is loaded in a simulator

- **Show All**
    - Displays all built-in and user default profiles
- **Show Built-in**
    - Displays only the built-in profiles
- **Show User**
    - Displays only user created aircraft and user profiles
- **Show Currently Loaded Aircraft**
    - If an aircraft is currently loaded in TelemFFB, this shows only profiles related to that specific aircraft

The profile types are as follows:

- **Built-in**

    - Built-in profiles are those included by default with TelemFFB. When an aircraft is loaded, the default profile will be used if there is no user defined profile

- **User Aircraft**

    - User Aircraft are the base profile for user created aircraft entries. When you use the new aircraft wizard, either dynamically when a new aircraft is loaded or via the button on the profile manager page, a new "User Aircraft" entry will be created.
    - These behave just like profiles and can be modified, deleted, exported and cloned

- **Settings Profile**

    - Settings Profiles are unique sets of settings for a given aircraft. You can create multiple settings profiles and easily switch between them either by setting them active from the profile manager, or by selecting them from the profile drop down on the main page in the application status area

### Managing Profiles
There are various buttons along the right side of the window that are used for managing the profiles. It is possible to multi-select profiles either by click-dragging or by ctrl+click on individual profiles. The action buttons on the right will enable or disable depending on what is available based on the combination of profiles that are selected.

When multiple profiles are selected:

- If any built-in profiles are part of the selection, only the export action is available. However, any selected built-in profiles will be excluded from the resulting export wizard.
- If there are no built-in profiles selected, only the Delete and Export actions are available.
- All other actions are only available when a single profile is selected.

#### Deleting Profile(s)

To delete one or more profiles, select the profile(s) that you would like to delete and then press the delete action button. If any of the profiles being deleted are the active profile, you will be prompted to select a new active profile for that aircraft.

#### Cloning a Profile

To clone a profile, select the single source profile and press the clone action button. Enter a new name for the profile. Optionally, set the "make active" flag in the window to make the newly created profile active for that aircraft.

#### Activating a Profile

To make a profile active, select the desired profile and press the Activate action button.

#### Renaming a Profile

To rename a profile, select the desired settings profile and press the Rename action button. Note that Built-in and User Aircraft profile types cannot be renamed.

#### Editing a Profile

To edit a profile, select the desired profile entry and press the Edit action button. This will put TelemFFB into offline editing mode and load that aircraft profile in the editor window.

### Exporting Profile(s)

To export one or more profiles, first select the profiles that you would like to export and then choose the Export action button. This will load the export wizard dialog:

![](images/aircraft-profiles/export-dialog.png){ width="334px" height="474px" }

The resulting window will display the profiles to be exported along with the export options:

- **Override Options**

    - **Include Sim Overrides**  
      Enable this option to include any sim level default overrides that would apply to the selected aircraft profiles. This will ensure that the profile, once imported, will match exactly with how the settings work in your configured setup.

    - **Include Class Overrides**  
      Enable this option to include any class level default overrides that would apply to the selected aircraft profiles. This will ensure that the profile, once imported, will match exactly with how the settings work in your configured setup.

- **Export Mode**

    - **Single File**  
      All settings will be exported into a single XML file containing all of the aircraft and settings. You will be given the opportunity to name the exported file.

    - **Multiple Files**  
      Each aircraft will export into a single file. In this mode, you will select the export location. The files will be auto-named, including the sim and aircraft IDs for each aircraft.

- **Included Devices**  
  These options will include or exclude settings for specific devices. If you have multiple devices but only want to export your Joystick settings, disable the checkboxes for the other devices.


### Importing Profile(s)

The import wizard provides a comprehensive set of options and information for the incoming settings in the selected export file.

![](images/aircraft-profiles/import-1.png){ width="680px" height="568px" }

Any line highlighted in **red** indicates a conflict that must be resolved before importing.

There are three main sections:

- **Detected Models**  
    This section lists all aircraft models and profiles found in the imported file.

    ![](images/aircraft-profiles/import-2.png){ width="629px" height="192px" }

    - The **Action** column pulldown lets you change the import behavior. You can **import** as is, **rename**, **skip**, or, if there is a profile name conflict, **overwrite** your existing profile of the same name.
    - To resolve a conflict, either set the action to **rename** and enter a new name in the "**imported name**" field, or choose to skip or overwrite.

- **Detected Overrides**  
    This section displays any simulator or class-level overrides included in the incoming settings file.

    ![](images/aircraft-profiles/import-3.png){ width="618px" height="189px" }

    - Conflicting settings are highlighted in **red**. These are settings where a matching override already exists in your configuration. The current user value and the incoming value are shown in their respective columns. You can choose to **overwrite** or **exclude** the setting using the **actions** dropdown.
    - Settings marked as "**match**" in the conflict column are identical to your existing override and will be ignored.
    - For all other incoming settings, you can choose to **include** or **exclude** each entry via the **action** setting.

- **Device Options**  
    This section allows you to filter out settings for specific device types. If a device type is not present in the incoming file, its toggle will be disabled.

    If a device type is disabled, any override settings or profiles that only contain settings for that device will be excluded from the import.

    ![](images/aircraft-profiles/import-4.png){ width="367px" height="165px" }
