from datetime import date
Today = date.today()
from sys import argv
from string import punctuation
from collections import *
from tkinter import Tk, Label
from tkinter import filedialog
from tkinter import ttk
from pathlib import Path

# Getting users download folder path to store as variable
downloads_path = str(Path.home() / "Downloads")
downloads_path = downloads_path.replace("\\", "/")
downloads_path = downloads_path + "/"

# Tkinter Window:
def open_win_diag():
    global file
    file = filedialog.askopenfilename(initialdir="C:/Downloads")

def close_window():
    win.destroy()

win = Tk()
win.geometry("700x200")
win.title("SteamVR System Report Analyzer")

# Create an instance of style class
style = ttk.Style(win)

# Configure style for the window
win.configure(bg='#f0f0f0')  # Light gray background

# Configure style for the label
style.configure('Header.TLabel', font=('Arial', 14, 'bold'), background='#f0f0f0')

# Create a label widget
label = ttk.Label(win, text="Select your SteamVR System Report and then close the window:", style='Header.TLabel')
label.pack(pady=20)

# Configure style for the buttons
style.configure('TButton', font=('Arial', 12))

# Create a button to open the dialog box
button = ttk.Button(win, text="Open File (Must be in english)", command=open_win_diag)
button.pack(pady=10)

# Create a button to close the window
button_2 = ttk.Button(win, text="Close Window", command=close_window)
button_2.pack(pady=5)

win.mainloop()

##################################################################################################################

# Creating the results text file that will show in detail the specific error line being output from the SteamVR log file based on key word/error critera below
error_list = open(f'{file}', 'r')
error_list_2 = open(f'{file}', 'r')

error_words = ['Malformed', 'NVAPI', 'back-facing', 'Error', '(208)', '(113)', '(200)', '(206)', '(301)', 'SteamVR Version', 'Display Mode', 'Could not find monitor of expected size', 'Direct Mode Vendor', 'Direct Mode Version', 'RGB', 'Fan', '(-203)', '(436)', 'non-clustered', 
               'centroid errors', 'world pop', 'no optical samples', 'Not enough contiguous samples for a bootstrap pose', 'Assertion failed', 'Unexpected centroid ordering error', 'rejected updates', 'IMU went off scale', '(109)', '(108)', 'Failed to Download Config Backup',
               'Can\'t parse HMD config', 'Error parsing config', 'VRApplicationError_IPCFailed', '(125)', '(126)', '(211)', '(100)', '(207)', '(302)', '(1101)', '(109)', '(1102)', '(1103)', '(1104)', '(1105)', '(1106)', '(1107)', '(1108)', '(1108)', '(1109)', '(1110)', '(1111)',
               '(1112)', '(110)', '(-204)', '(200)', 'Samples didn\'t yield successful bootstrap pose', 'Calibration failed', 'Rotors on basestation out of 180-degree phase lock', 'Base may have been bumped or power cycled', 'HMD detected over USB, but Monitor not found',
               'faults', 'IMU misalignment unreasonably large', 'Received advertisement report', '(103)', 'HmdError_Init_FileNotFound', 'HmdError_Init_InstallationNotFound', 'HmdError_Init_InstallationCorrupt', 'HmdError_Init_VRClientDLLNotFound', 'HmdError_Init_FactoryNotFound',
               'HmdError_Init_InterfaceNotFound', 'HmdError_Init_UserConfigDirectoryInvalid', 'HmdError_Init_PathRegistryNotFound', 'HmdError_Init_NoConfigPath', 'HmdError_Init_NoLogPath', 'HmdError_Init_PathRegistryNotWritable', 'HmdError_IPC_ConnectFailed', 'HmdError_IPC_SharedStateInitFailed',
               'HmdError_IPC_CompositorInitFailed', 'HmdError_IPC_MutexInitFailed', 'HmdError_VendorSpecific_UnableToConnectToOculusRuntime', '(475)']

with open(f'{downloads_path}/SteamVR Log Results - {Today}.txt', 'w', encoding='utf-8') as f:
    for line in error_list:
        if any(word in line for word in error_words):
                f.write(line)
                f.write('\n')

##################################################################################################################

# Appending to the top lines of the results file to give hyperlinks/information on how to read the log file/fixes 
with open(f"{downloads_path}/SteamVR Log Results - {Today}.txt", encoding='utf-8') as f: 
    lines = f.readlines() # read 
     
    # Appended lines: 
    lines[0] = "HMD Error Code Dictionaries: https://github.com/ValveSoftware/openvr/wiki/HmdError\n"
    lines[1] = "Valve\'s direct troubleshooting site based on what error code your log shows: https://help.steampowered.com/en/wizard/HelpWithGameIssue/?appid=250820&issueid=374 \n" 
    lines[2] = "Valve\'s dev site on error codes: https://developer.valvesoftware.com/wiki/SteamVR/Error_Codes \n" 
    lines[3] = "Toms Guide that goes into different details on error codes: https://forums.tomsguide.com/faq/what-each-steamvr-error-code-means-and-how-to-fix-them.111358/ \n"
    lines[4] = "\n"
    lines[5] = "\n"
    lines[6] = "\n"
    lines[7] = "SteamVR Error Code Definitions and Solutions: \n"
    lines[8] = "Steam Error 208 (HMD Display not found): https://help.steampowered.com/en/wizard/HelpWithGameIssue/?appid=250820&issueid=374&nodeid=39&return_nodeid=71 | \n" 
    lines[9] = "Steam Error 109: https://discord.com/channels/816371255539138620/1192675050818637856/1192675050818637856 \n" 
    lines[10] = "Steam Error 301 (Connect Failed): https://developer.valvesoftware.com/wiki/SteamVR/Error_Codes | As well try SteamVR Beta Branch | https://help.steampowered.com/en/wizard/HelpWithGameIssue/?appid=250820&issueid=374&nodeid=40&return_nodeid=71 \n" 
    lines[11] = "Steam Error -203/-204: Try turning OFF GPU Scheduling (HAGS) via windows settings, Windows settings (Settings -> System -> Display -> Graphics -> Change default graphics settings -> Disable Hardware-accelerated GPU scheduling) \n"
    lines[12] = "Steam Error 200 (Driver Failed): https://developer.valvesoftware.com/wiki/SteamVR/Error_Codes \n"
    lines[13] = "Back-facing hits/non-clustered hits: These errors causes are more than likely reflections in your play space, see:  \n"
    lines[14] = "Assertion failed/Unexpected centroid ordering error: These errors can often be reflection related and/or USB power settings prolblem. In windows power management plan advanced settings, it is recommended to have USB selective suspend setting disabled. As well sometimes using other USB ports may work but if needed, getting a separate PCIE usb controller would yield better results. Get any FL1100EX cards from this list: https://developer.valvesoftware.com/wiki/Valve_Index/USB_3.0_Controller \n"
    lines[15] = "No optical samples: These errors are can be called 'flash-bang reflections', see:  \n"
    lines[16] = "Samples didn't yield successful bootstrap pose/Not enough contiguous samples for a bootstrap pose: These errors are steamVR trying to initialize tracking and is struggling, see:  \n"
    lines[17] = "Calibration failed: These errors are where tracking is completely lost and steam thinks the object is somewhere it is not, see:  \n"
    lines[18] = "IMU went off scale: These errors can be related to controllers and sometimes FBT trackers, see:  \n"
    lines[19] = "Malformed wireless packet: This would be caused by any wifi devices around your playspace that are putting out high interference, turning those devices off and then test to see any improvements.\n"
    lines[20] = "Rotors on basestation out of 180-degree phase lock: Lighthouse/Basestation is about to die, need to replace.\n"
    lines[21] = "Base may have been bumped or power cycled: Lighthouse/Basestation is not mounted properly (wobbly) or the Lighthouse/Basestation got nudged. Could also be a early warning of Lighthouse/Basestation dying. \n"
    lines[22] = "HMD detected over USB, but Monitor not found: HMD cannot be picked up correctly over displayport, this could be a bad DP cable or link-box or other possible steamvr settings, see 208 error. \n"
    lines[23] = "IMU misalignment unreasonably large: This represents bad tracking, from either bad EMI (electro-magnetic interference) or a hardware issues with the HMD, tracker or controller the error is attached to. Use ferrite cores on the main HMD cable or linkbox cables to attempt to fix. \n"
    lines[24] = "Faults: If you see any faults other than 0, could be a possible Lighthouse/Basestation issue. \n"
    lines[25] = "Received advertisement report: this line shows any other bluetooth devices broadcasting signals\n"
    lines[26] = "Steam Error 475: Usually related to virtual desktop error, try to either uninstall steamvr and reinstall, if this does not work, run steamvr as system admin."
    lines[27] = "Steam Error 436: Often this error is simple as unplugging and replugging your HMD cable, as well sometimes if your HMD cable is USB-C, flip the cable 180 and replug. \n"
    lines[28] = "However this error can also be related to DSC for high resolution HMDs that use DSC, in which if you have a DSC monitor, for exanpple a 1440p 360hz monitor, that needs to be turned off before running steamvr, then it will work, this is a DSC bandwidth limitation. To see if your monitor uses DSC, use: https://trychen.com/feature/video-bandwidth and if the 1.4 icon is an yellow !, that monitor needs to be powered off. \n"
    lines[29] = "\n"
    lines[30] = "\n"
    lines[31] = "\n"
    lines[32] = "General PC/VR Solutions: \n"
    lines[33] = "If none of the above specific solutions are working, general troubleshooting would be: check for windows updates, steamvr updates, cpu chipset updates, bios updates and gpu driver updates. (Note for GPU driver updates, I recommend to check the Nvidia or AMD subreddits to see if the latest drivers have any issues, newest GPU drivers are not always the best.) \n"
    lines[34] = "If you still have issues, one recommendation is to completely wipe steamvr, here is a nice guide on how to: https://steamcommunity.com/app/250820/discussions/2/1640917625015598552/ \n"
    lines[35] = "Program to see where your basestations are seeing (useful to make sure they are pointing in the center of your playspace): https://nono-00.itch.io/base-station-fov-viewer\n"
    lines[36] = "Great guide on dongle placement and dongle replacements (akro dongles being very good as individual dongle replacements): https://www.notion.so/yeove/SteamVR-Hardware-troubleshooting-Megathread-Setup-Guide-16fc956d336a8037b738d1b0b1ded2f0?pvs=4 \n"
    lines[37] = "\n"
    lines[38] = "\n"
    lines[39] = "\n"
    lines[40] = "SteamVR Errors Below: \n"
     
with open(f"{downloads_path}/SteamVR Log Results - {Today}.txt", "w", encoding='utf-8') as f: 
        f.writelines(lines) # write back 


f.close()
error_list.close()
error_list_2.close()