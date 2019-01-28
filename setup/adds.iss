; -- Example1.iss --
; Demonstrates copying 3 files and creating an icon.

; SEE THE DOCUMENTATION FOR DETAILS ON CREATING .ISS SCRIPT FILES!

#define MyAppName "Trevexs Adds"
#define MyAppExeName "main.exe"
#define MyAppIcoName "icon.ico"
#define SourcePath "E:\Projects\ESAI\PROGRAMMING\PYTHON\adds\dist\main"

[Setup]
AppName={#MyAppName}
AppVersion=1.0.1
DefaultDirName={pf}\{#MyAppName}
DefaultGroupName={#MyAppName}
UninstallDisplayIcon={app}\run.bat
Compression=lzma2
SolidCompression=yes
OutputDir=userdocs:Adds Project
ChangesAssociations = yes

[Registry]
Root: HKCR; Subkey: ".trad";                            ValueData: "{#MyAppName}";          Flags: uninsdeletevalue; ValueType: string;  ValueName: ""
Root: HKCR; Subkey: "{#MyAppName}";                     ValueData: "{#MyAppName}";          Flags: uninsdeletekey;   ValueType: string;  ValueName: ""
Root: HKCR; Subkey: "{#MyAppName}\DefaultIcon";         ValueData: """{app}\icon.ico""";                     ValueType: string;  ValueName: ""
Root: HKCR; Subkey: "{#MyAppName}\shell\open\command";  ValueData: """{app}\{#MyAppExeName}"" ""%1""";               ValueType: string;  ValueName: ""

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; \
    GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
;
;Program icon
Source: "icon.ico"; DestDir: "{app}"
;
;Files in assests folder
Source: "{#SourcePath}\assests\header_attribs.json"; DestDir: "{app}\assests"
Source: "{#SourcePath}\assests\layers.json"; DestDir: "{app}\assests"
;
;Files in ezdxf folder
Source: "{#SourcePath}\ezdxf\templates\AC1024.dxf"; DestDir: "{app}\ezdxf\templates"
;
;Files in input folder
Source: "{#SourcePath}\input\sample1.trad"; DestDir: "{userdesktop}\{#MyAppName}"
Source: "{#SourcePath}\input\sample1.trad"; DestDir: "{localappdata}\{#MyAppName}\data"

;
;Files in main Folder
Source: "{#SourcePath}\_bz2.pyd"; DestDir: "{app}"
Source: "{#SourcePath}\_ctypes.pyd"; DestDir: "{app}"
Source: "{#SourcePath}\_hashlib.pyd"; DestDir: "{app}"
Source: "{#SourcePath}\_lzma.pyd"; DestDir: "{app}"
Source: "{#SourcePath}\_socket.pyd"; DestDir: "{app}"
Source: "{#SourcePath}\_ssl.pyd"; DestDir: "{app}"
Source: "{#SourcePath}\base_library.zip"; DestDir: "{app}"
Source: "{#SourcePath}\libcrypto-1_1-x64.dll"; DestDir: "{app}"; CopyMode: alwaysskipifsameorolder; Flags: onlyifdoesntexist restartreplace sharedfile 64bit; Check: IsWin64
Source: "{#SourcePath}\libssl-1_1-x64.dll"; DestDir: "{app}"; CopyMode: alwaysskipifsameorolder; Flags: onlyifdoesntexist restartreplace sharedfile 64bit; Check: IsWin64
Source: "{#SourcePath}\python37.dll"; DestDir: "{app}"; CopyMode: alwaysskipifsameorolder; Flags: onlyifdoesntexist restartreplace sharedfile 64bit; Check: IsWin64
Source: "{#SourcePath}\pywintypes37.dll"; DestDir: "{app}"; CopyMode: alwaysskipifsameorolder; Flags: onlyifdoesntexist restartreplace sharedfile 64bit; Check: IsWin64
Source: "{#SourcePath}\VCRUNTIME140.dll"; DestDir: "{app}"; CopyMode: alwaysskipifsameorolder; Flags: onlyifdoesntexist restartreplace sharedfile 64bit; Check: IsWin64
Source: "{#SourcePath}\main.exe"; DestDir: "{app}"
Source: "{#SourcePath}\main.exe.manifest"; DestDir: "{app}"
Source: "{#SourcePath}\pyexpat.pyd"; DestDir: "{app}"
Source: "{#SourcePath}\run.bat"; DestDir: "{app}"
Source: "{#SourcePath}\select.pyd"; DestDir: "{app}"
Source: "{#SourcePath}\unicodedata.pyd"; DestDir: "{app}"
Source: "{#SourcePath}\win32wnet.pyd"; DestDir: "{app}"
Source: "{#SourcePath}\read_me.pdf"; DestDir: "{app}\docs"; Flags: isreadme

[Icons]
Name: "{group}\Trevexs Adds"; Filename: "{app}\run.bat"; IconFilename: "{app}\icon.ico"
Name: "{group}\Uninstall {#MyAppName}"; Filename: "{uninstallexe}"; IconFilename: "{app}\icon.ico"
Name: "{userdesktop}\{#MyAppName}"; Filename: "{app}\run.bat"; Tasks: desktopicon; IconFilename: "{app}\icon.ico"
