# SteamVR System Report Error Analyzer
A simple python program to analyze steamvr system reports easier to output only error codes and remove the rest. 

To create a system report see: https://youtu.be/51RxkL8KzVk?si=1xQhGYHRctngj3eo&t=69 

Please note the current release only works with system reports that are outputted in English text.

## SteamVR Error Code Definitions and Solutions: 

• HMD Error Code Dictionaries: https://github.com/ValveSoftware/openvr/wiki/HmdError

• Valve\'s direct troubleshooting site based on what error code your log shows: https://help.steampowered.com/en/wizard/HelpWithGameIssue/?appid=250820&issueid=374  

• Valve\'s dev site on error codes: https://developer.valvesoftware.com/wiki/SteamVR/Error_Codes  

• Toms Guide that goes into different details on error codes: https://forums.tomsguide.com/faq/what-each-steamvr-error-code-means-and-how-to-fix-them.111358/ 

•	Steam Error 208 (HMD Display not found): https://help.steampowered.com/en/wizard/HelpWithGameIssue/?appid=250820&issueid=374&nodeid=39&return_nodeid=71 |  

•	Steam Error 109: https://discord.com/channels/816371255539138620/1192675050818637856/1192675050818637856  

•	Steam Error 301 (Connect Failed): https://developer.valvesoftware.com/wiki/SteamVR/Error_Codes | As well try SteamVR Beta Branch | https://help.steampowered.com/en/wizard/HelpWithGameIssue/?appid=250820&issueid=374&nodeid=40&return_nodeid=71  

•	Steam Error -203/-204: Try turning OFF GPU Scheduling (HAGS) via windows settings, Windows settings (Settings -> System -> Display -> Graphics -> Change default graphics settings -> Disable Hardware-accelerated GPU scheduling) 

•	Steam Error 200 (Driver Failed): https://developer.valvesoftware.com/wiki/SteamVR/Error_Codes 

•	Back-facing hits/non-clustered hits: These errors causes are more than likely reflections in your play space. Finding reflections is often hard but here is a nice video on how to find major ones (using your phone flashlight can work fine as well): https://www.youtube.com/watch?v=UGJFACuQVG8 (Alternatives to a strobe light would be a narrow flashlight or even your phones flashlight. 
•	One note, this method may not show all reflective surfaces since base stations do emit IR lasers however this method can at least help find major sources)
![image](https://github.com/user-attachments/assets/45488021-341a-4949-afc6-32477e5bf37c)


•	Assertion failed/Unexpected centroid ordering error: These errors can often be reflection related and/or USB power settings problem. In windows power management plan advanced settings, it is recommended to have USB selective suspend setting disabled, see photo. 
•	Also sometimes using other USB ports may work but if needed, getting a separate PCIE usb controller would yield better results. Get any FL1100EX cards from this list: https://developer.valvesoftware.com/wiki/Valve_Index/USB_3.0_Controller  
•	As well can turn off "Pause VR when headset is idle" (Steamvr settings -> Video Settings) and disable Power Management, found in steamvr developer settings. 
![image](https://github.com/user-attachments/assets/d2bc91a8-83de-4bc9-9cca-79839dff8e20) 

•	No optical samples: These errors are can be called 'flash-bang reflections'.

•	Samples didn't yield successful bootstrap pose/Not enough contiguous samples for a bootstrap pose: These errors are steamVR trying to initialize tracking and is struggling.

•	Calibration failed: These errors are where tracking is completely lost and steam thinks the object is somewhere it is not.

•	IMU went off scale: These errors can be related to controllers and sometimes FBT trackers.

•	Malformed wireless packet: This would be caused by any wifi devices around your playspace that are putting out high interference, turning those devices off and then test to see any improvements.

•	Rotors on basestation out of 180-degree phase lock: Lighthouse/Basestation is about to die, need to replace.

•	Base may have been bumped or power cycled: Lighthouse/Basestation is not mounted properly (wobbly) or the Lighthouse/Basestation got nudged. Could also be a early warning of Lighthouse/Basestation dying. 

•	HMD detected over USB, but Monitor not found: HMD cannot be picked up correctly over displayport, this could be a bad DP cable or link-box or other possible steamvr settings, see 208 error. 

•	IMU misalignment unreasonably large: This represents bad tracking, from either bad EMI (electro-magnetic interference) or a hardware issues with the HMD, tracker or controller the error is attached to. Use ferrite cores on the main HMD cable or linkbox cables to attempt to fix. 

•	Faults: If you see any faults other than 0, could be a possible Lighthouse/Basestation issue. 

•	Received advertisement report: this line shows any other bluetooth devices broadcasting signals

•	Steam Error 475: Usually related to virtual desktop error, try to either uninstall steamvr and reinstall, if this does not work, run steamvr as system admin.

•	Steam Error 436: Often this error is simple as unplugging and replugging your HMD cable, as well sometimes if your HMD cable is USB-C, flip the cable 180 and replug. 

•	However, this error can also be related to DSC for high resolution HMDs that use DSC, in which if you have a DSC monitor, for example a 1440p 360hz monitor, that needs to be turned off before running steamvr, then it will work, this is a DSC bandwidth limitation. To see if your monitor uses DSC, use: https://trychen.com/feature/video-bandwidth and if the 1.4 icon is a yellow !, that monitor needs to be powered off. 

•	Refreshing audio devices: Often this error popping up a lot means HMD connection issues, i.e: 'headset starts to disconnect a bit', see cable connections.

## General PC/VR Solutions: 

•	If none of the above specific solutions are working, general troubleshooting would be: check for windows updates, steamvr updates, cpu chipset updates, bios updates and gpu driver updates. (Note for GPU driver updates, I recommend to check the Nvidia or AMD subreddits to see if the latest drivers have any issues, newest GPU drivers are not always the best.) 

•	If you still have issues, one recommendation is to completely wipe steamvr, here is a nice guide on how to: https://steamcommunity.com/app/250820/discussions/2/1640917625015598552/ 

•	Program to see where your basestations are seeing (useful to make sure they are pointing in the center of your playspace): https://nono-00.itch.io/base-station-fov-viewer

•	Great guide on dongle placement and dongle replacements (akro dongles being very good as individual dongle replacements): https://www.notion.so/yeove/SteamVR-Hardware-troubleshooting-Megathread-Setup-Guide-16fc956d336a8037b738d1b0b1ded2f0?pvs=4 

•	Another great guide that focuses on more steamvr and windows settings changes for VR in general and VRChat: https://docs.google.com/document/u/0/d/1BdyWxQhFoRkJVfsLvcPNHgvL-esUEE76WbDfguOVbMg/mobilebasic



