; -- add.iss --

; Set up trevexs add project installer

#define MyAppName "Trevexs Adds"
#define MyAppSetUpName "adds_setup-"
#define MyAppExeName "main.exe"
#define MyAppIcoName "icon.ico"
#define MyAppVersion "1.0.3"
#define SourcePath "E:\Projects\ESAI\PROGRAMMING\PYTHON\adds\dist\main"
;
[Setup]
AppPublisher=Trevexs, Inc.    
AppPublisherURL=http://www.trevexs.com/
;SignTool=mycustom sign /debug /f $qE:\Projects\ESAI\PROGRAMMING\PYTHON\adds\setup\trevexs.pfx$q /p sseka123 /n $qTrevexs Inc$q /t http://timestamp.verisign.com/scripts/timstamp.dll /d $qAdds Design Application$q $f
;SignedUninstaller=yes
AppName={#MyAppName}
AppVersion={#MyAppVersion}
DefaultDirName={pf}\{#MyAppName}
DefaultGroupName={#MyAppName}
UninstallDisplayIcon={app}\{#MyAppExeName}
Compression=lzma2
SolidCompression=yes
OutputDir=setups
ChangesAssociations = yes
OutputBaseFilename={#MyAppSetUpName}{#MyAppVersion}

[Registry]
Root: HKCR; Subkey: ".trad";                            ValueData: "{#MyAppName}";          Flags: uninsdeletevalue; ValueType: string;  ValueName: ""
Root: HKCR; Subkey: "{#MyAppName}";                     ValueData: "{#MyAppName}";          Flags: uninsdeletekey;   ValueType: string;  ValueName: ""
Root: HKCR; Subkey: "{#MyAppName}\DefaultIcon";         ValueData: """{app}\icon.ico""";                             ValueType: string;  ValueName: ""
Root: HKCR; Subkey: "{#MyAppName}\shell\open\command";  ValueData: """{app}\{#MyAppExeName}"" ""%1""";               ValueType: string;  ValueName: ""

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; \
    GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
;
;Program icon
Source: "icon.ico"; DestDir: "{app}"
Source: "{#SourcePath}\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs
;
;Files in assests folder
; Source: "{#SourcePath}\assests\header_attribs.json"; DestDir: "{app}\assests"
; Source: "{#SourcePath}\assests\layers.json"; DestDir: "{app}\assests"
; Source: "{#SourcePath}\assests\text_styles.json"; DestDir: "{app}\assests"
;
;Files in ezdxf folder
; Source: "{#SourcePath}\ezdxf\templates\AC1024.dxf"; DestDir: "{app}\ezdxf\templates"
;
;Files in input folder for general use
Source: "{#SourcePath}\input\sample1.trad"; DestDir: "{userdesktop}\{#MyAppName}"
Source: "{#SourcePath}\input\philip.trad"; DestDir: "{userdesktop}\{#MyAppName}"
Source: "{#SourcePath}\input\sample1.trad"; DestDir: "{localappdata}\{#MyAppName}\data"

;
;Files in main Folder
; Source: "{#SourcePath}\_bz2.pyd"; DestDir: "{app}"
; Source: "{#SourcePath}\_ctypes.pyd"; DestDir: "{app}"
; Source: "{#SourcePath}\_hashlib.pyd"; DestDir: "{app}"
; Source: "{#SourcePath}\_lzma.pyd"; DestDir: "{app}"
; Source: "{#SourcePath}\_socket.pyd"; DestDir: "{app}"
; Source: "{#SourcePath}\_ssl.pyd"; DestDir: "{app}"
; Source: "{#SourcePath}\base_library.zip"; DestDir: "{app}"
Source: "{#SourcePath}\libcrypto-1_1-x64.dll"; DestDir: "{app}"; Flags: onlyifdoesntexist restartreplace sharedfile 64bit; Check: IsWin64
Source: "{#SourcePath}\libssl-1_1-x64.dll"; DestDir: "{app}"; Flags: onlyifdoesntexist restartreplace sharedfile 64bit; Check: IsWin64
Source: "{#SourcePath}\python37.dll"; DestDir: "{app}"; Flags: onlyifdoesntexist restartreplace sharedfile 64bit; Check: IsWin64
Source: "{#SourcePath}\pywintypes37.dll"; DestDir: "{app}"; Flags: onlyifdoesntexist restartreplace sharedfile 64bit; Check: IsWin64
Source: "{#SourcePath}\VCRUNTIME140.dll"; DestDir: "{app}"; Flags: onlyifdoesntexist restartreplace sharedfile 64bit; Check: IsWin64
; Source: "{#SourcePath}\main.exe"; DestDir: "{app}"
; Source: "{#SourcePath}\main.exe.manifest"; DestDir: "{app}"
; Source: "{#SourcePath}\pyexpat.pyd"; DestDir: "{app}"
; Source: "{#SourcePath}\{#MyAppExeName}"; DestDir: "{app}"
; Source: "{#SourcePath}\select.pyd"; DestDir: "{app}"
; Source: "{#SourcePath}\unicodedata.pyd"; DestDir: "{app}"
; Source: "{#SourcePath}\win32wnet.pyd"; DestDir: "{app}"
Source: "{#SourcePath}\release_update.pdf"; DestDir: "{app}\docs"; Flags: isreadme
Source: "{#SourcePath}\read_me.pdf"; DestDir: "{app}\docs"; Flags: isreadme


[Icons]
Name: "{group}\Trevexs Adds"; Filename: "{app}\{#MyAppExeName}"; IconFilename: "{app}\icon.ico"
Name: "{group}\Uninstall {#MyAppName}"; Filename: "{uninstallexe}"; IconFilename: "{app}\icon.ico"
Name: "{userdesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon; IconFilename: "{app}\icon.ico"
