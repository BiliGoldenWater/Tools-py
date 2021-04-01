WinActivate, ahk_exe YuanShen.exe

getOffset(){
    offset := 0
    Random, offset, -30, 30
    return offset
}

Send F
Sleep, 1000
Click, 1780, 980 + getOffset()
Sleep, 1000
Click, 1780, 980 + getOffset()
Sleep, 1000
Click, 1780, 980 + getOffset()
Sleep, 1000
Click, 1780, 980 + getOffset()
Sleep, 1000
Click, 1780, 980 + getOffset()
Sleep, 1500
Click, 1780, 980 + getOffset()
Sleep, 500