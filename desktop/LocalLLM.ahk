#Requires AutoHotkey v2.0
#SingleInstance Force
; Compact native Windows control. No browser, Python polling or GPU subprocesses.
Root := A_Args.Length ? A_Args[1] : 'E:\llm'
StateDir := Root '\widget'
DirCreate StateDir
ActionPid := 0
LastState := ''
Nvml := 0
Device := 0
Status := 'Checking'
ConfigText := FileRead(Root '\runtime-config.json','UTF-8')
if !RegExMatch(ConfigText,'"alias"\s*:\s*"([^"]+)"',&AliasMatch)
    throw Error('Configured model alias is missing.')
ExpectedAlias := AliasMatch[1]
Palette := Map('green','86E3A7','amber','FFD07D','red','FF9A9E','muted','AABACB')
Try {
    Nvml := DllCall('LoadLibrary', 'Str', A_WinDir '\System32\nvml.dll', 'Ptr')
    if !Nvml || DllCall(Nv('nvmlInit_v2'), 'Cdecl UInt')
        throw Error('NVML unavailable')
    if DllCall(Nv('nvmlDeviceGetHandleByIndex_v2'), 'UInt',0,'Ptr*',&Device,'Cdecl UInt')
        throw Error('GPU0 unavailable')
} catch {
    Nvml := 0
}

Panel := Gui('+AlwaysOnTop -Caption +ToolWindow','Local LLM · Resource Widget')
Panel.BackColor := '16202D'
Panel.SetFont('s9 cAABACB','Segoe UI')
Title := Panel.AddText('x16 y10 w380 h18','LOCAL LLM   /   Ctrl + Alt + L')
Title.OnEvent('Click', (*) => PostMessage(0xA1,2,,, 'ahk_id ' Panel.Hwnd))
HideButton := Panel.AddText('x498 y6 w28 h24 Center','—')
HideButton.OnEvent('Click', (*) => Panel.Hide())
Panel.SetFont('s13 Bold c86E3A7')
Power := Panel.AddText('x16 y34 w132 h28','● Checking')
Power.OnEvent('Click', (*) => Act('Toggle'))
Panel.SetFont('s9 Norm cAABACB')
Hint := Panel.AddText('x16 y64 w142 h20','Click to start / stop')
Hint.OnEvent('Click', (*) => Act('Toggle'))
Vram := Metric(172,'VRAM')
Gpu := Metric(298,'GPU')
Ram := Metric(400,'RAM')
Panel.OnEvent('Escape', (*) => Panel.Hide())
Panel.OnEvent('Close', (*) => Panel.Hide())
Panel.OnEvent('ContextMenu', (*) => A_TrayMenu.Show())
A_TrayMenu.Delete()
A_TrayMenu.Add('Show widget', (*) => ShowPanel())
A_TrayMenu.Add('Toggle model  ·  Ctrl+Alt+L', (*) => Act('Toggle'))
A_TrayMenu.Add('Stop model (free memory)', (*) => Act('Stop'))
A_TrayMenu.Add('Open control guide', (*) => Run('notepad.exe ' Q(A_ScriptDir '\README.md')))
A_TrayMenu.Add()
A_TrayMenu.Add('Hide widget', (*) => Panel.Hide())
A_TrayMenu.Add('Exit widget (leave model as-is)', (*) => ExitApp())
A_TrayMenu.Default := 'Show widget'
A_TrayMenu.ClickCount := 1
Hotkey '^!l', (*) => Act('Toggle')
OnMessage(0x404, TrayEvent)
OnExit Cleanup
ShowPanel()
Refresh()
SetTimer Refresh, 3000
SetTimer FinishAction, 500

Metric(x, label) {
    global Panel
    Panel.SetFont('s9 Norm cAABACB')
    title := Panel.AddText('x' x ' y32 w120 h17', label)
    Panel.SetFont('s12 Bold c86E3A7')
    value := Panel.AddText('x' x ' y52 w124 h26','—')
    title.OnEvent('Click', (*) => Act('Toggle'))
    value.OnEvent('Click', (*) => Act('Toggle'))
    return value
}

Q(value) {
    return '"' value '"'
}

Nv(name) {
    global Nvml
    proc := DllCall('GetProcAddress','Ptr',Nvml,'AStr',name,'Ptr')
    if !proc
        throw Error('NVML entry point missing: ' name)
    return proc
}

ShowPanel() {
    global Panel, StateDir
    MonitorGetWorkArea(, &left, &top, &right, &bottom)
    scale := A_ScreenDPI / 96
    x := Max(left, Min(right-540*scale, IniRead(StateDir '\widget.ini','position','x',left+16)))
    y := Max(top, Min(bottom-96*scale, IniRead(StateDir '\widget.ini','position','y',bottom-110*scale)))
    Panel.Show('NA x' Round(x) ' y' Round(y) ' w540 h92')
    WinGetPos(,, &w, &h, 'ahk_id ' Panel.Hwnd)
    WinSetRegion('0-0 w' w ' h' h ' R16-16', 'ahk_id ' Panel.Hwnd)
}

Color(percent) {
    global Palette
    return Palette[percent >= 90 ? 'red' : percent >= 70 ? 'amber' : 'green']
}

Refresh() {
    global Ram, Gpu, Vram, Device, Nvml, Palette, Status, Power, Hint, ActionPid, LastState, Root, StateDir, ExpectedAlias
    memory := Buffer(64,0)
    NumPut('UInt',64,memory)
    if DllCall('GlobalMemoryStatusEx','Ptr',memory) {
        total := NumGet(memory,8,'UInt64') / 1073741824
        used := total - NumGet(memory,16,'UInt64') / 1073741824
        Ram.Text := Format('{:.1f} / {:.0f}G',used,total)
        Ram.SetFont('c' Color(100*used/total))
    }
    if Nvml {
        try {
            gpuMemory := Buffer(24,0), util := Buffer(8,0)
            if DllCall(Nv('nvmlDeviceGetMemoryInfo'),'Ptr',Device,'Ptr',gpuMemory,'Cdecl UInt')
                throw Error('VRAM unavailable')
            gpuTotal := NumGet(gpuMemory,0,'UInt64') / 1073741824
            gpuUsed := NumGet(gpuMemory,16,'UInt64') / 1073741824
            Vram.Text := Format('{:.1f} / {:.0f}G',gpuUsed,gpuTotal)
            Vram.SetFont('c' Color(100*gpuUsed/gpuTotal))
            if DllCall(Nv('nvmlDeviceGetUtilizationRates'),'Ptr',Device,'Ptr',util,'Cdecl UInt')
                throw Error('GPU utilization unavailable')
            usage := NumGet(util,0,'UInt')
            Gpu.Text := usage '%'
            Gpu.SetFont('c' Color(usage))
        } catch {
            Vram.Text := 'Unavailable', Gpu.Text := 'Unavailable'
        }
    } else {
        Vram.Text := 'Unavailable', Gpu.Text := 'Unavailable'
    }
    state := 'Stopped'
    if ActionPid {
        state := 'Working'
    } else {
        try {
            http := ComObject('WinHttp.WinHttpRequest.5.1')
            http.SetTimeouts(500,500,500,500)
            http.Open('GET','http://127.0.0.1:8080/props',false)
            http.Send()
            if http.Status = 200 {
                if !RegExMatch(http.ResponseText,'"model_alias"\s*:\s*"([^"]+)"',&model) || model[1] != ExpectedAlias
                    state := 'Other model'
                else
                    state := RegExMatch(http.ResponseText,'"is_sleeping"\s*:\s*true') ? 'Sleeping' : 'Ready'
            } else {
                state := 'Loading'
            }
        } catch {
            ; A waking runtime can briefly time out. Do not flash a false Off state.
            try {
                saved := FileRead(Root '\server-settings.json','UTF-8')
                if RegExMatch(saved,'"pid"\s*:\s*(\d+)',&pidMatch) && ProcessExist(Integer(pidMatch[1]))
                    state := 'Loading'
            }
        }
    }
    ; A hotkey may interrupt a COM status request. Preserve the newer action state.
    if ActionPid
        state := 'Working'
    Status := state
    shade := state = 'Ready' ? 'green' : state = 'Stopped' ? 'red' : 'amber'
    Power.Text := '● ' state
    Power.SetFont('c' Palette[shade])
    Hint.Text := state = 'Sleeping' ? 'Next message wakes me' : state = 'Working' ? 'Please wait…' : 'Click to start / stop'
    A_IconTip := 'Local LLM: ' state '`nVRAM ' Vram.Text ' · GPU ' Gpu.Text ' · RAM ' Ram.Text '`nCtrl+Alt+L toggles the model'
    if state != LastState {
        icon := StateDir '\' shade '.ico'
        if FileExist(icon)
            TraySetIcon icon
        Log('state=' state)
        LastState := state
    }
    ; Passive data for reproducible UI/resource tests, not used to drive actions.
    IniWrite state, StateDir '\telemetry.ini','live','state'
    IniWrite Vram.Text, StateDir '\telemetry.ini','live','vram'
    IniWrite Gpu.Text, StateDir '\telemetry.ini','live','gpu'
    IniWrite Ram.Text, StateDir '\telemetry.ini','live','ram'
}

Act(action) {
    global ActionPid, StateDir, Root
    if ActionPid {
        TrayTip('A model action is already in progress.','Local LLM','Iconi Mute')
        return
    }
    result := StateDir '\action.ini'
    if FileExist(result)
        FileDelete result
    command := 'powershell.exe -NoProfile -NonInteractive -ExecutionPolicy Bypass -File ' Q(A_ScriptDir '\control.ps1') ' -Root ' Q(Root) ' -Action ' action ' -ResultFile ' Q(result)
    Run command,, 'Hide', &ActionPid
    Log('action=' action ' pid=' ActionPid)
    TrayTip('Switching model state. The widget will update when ready.','Local LLM','Iconi Mute')
    Refresh()
}

FinishAction() {
    global ActionPid, StateDir
    if !ActionPid || ProcessExist(ActionPid)
        return
    ActionPid := 0
    result := StateDir '\action.ini'
    status := IniRead(result,'result','status','error')
    message := IniRead(result,'result','message','Action ended without a result. Check the launcher logs.')
    TrayTip(message,'Local LLM',status = 'error' ? 'Iconx Mute' : 'Iconi Mute')
    Log('result=' status ' ' message)
    Refresh()
}

TrayEvent(wParam,lParam,msg,hwnd) {
    if hwnd = A_ScriptHwnd && (lParam & 0xFFFF) = 0x202 {
        ; Handle a tray left-click explicitly; Windows shell click routing can
        ; bypass the default menu item when the floating window is hidden.
        SetTimer ShowPanel, -1
        return 0
    }
    if hwnd = A_ScriptHwnd && (lParam = 1026 || lParam = 1027)
        Log('notification_event=' lParam)
}

Log(message) {
    global StateDir
    FileAppend FormatTime(,'yyyy-MM-dd HH:mm:ss') ' ' message '`n', StateDir '\widget.log','UTF-8'
}

Cleanup(*) {
    global Panel, StateDir, Nvml
    ; Gui.GetPos works while hidden; WinGetPos's default visible-only lookup
    ; throws during exit/reload of a hidden widget and blocks single-instance.
    try {
        Panel.GetPos(&x,&y)
        IniWrite x, StateDir '\widget.ini','position','x'
        IniWrite y, StateDir '\widget.ini','position','y'
    } catch {
        ; Position persistence must never prevent exit.
    }
    try {
        if Nvml
            DllCall(Nv('nvmlShutdown'),'Cdecl UInt')
    }
}
