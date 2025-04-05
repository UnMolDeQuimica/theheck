@set PYTHONIOENCODING=utf-8
@powershell -noprofile -c "cmd /c \"$(theheck %* $(doskey /history)[-2])\"; [Console]::ResetColor();"
