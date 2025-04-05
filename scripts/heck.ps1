if ((Get-Command "heck").CommandType -eq "Function") {
	heck @args;
	[Console]::ResetColor()
	exit
}

"First time use of theheck detected. "

if ((Get-Content $PROFILE -Raw -ErrorAction Ignore) -like "*theheck*") {
} else {
	"  - Adding theheck intialization to user `$PROFILE"
	$script = "`n`$env:PYTHONIOENCODING='utf-8' `niex `"`$(theheck --alias)`"";
	Write-Output $script | Add-Content $PROFILE
}

"  - Adding heck() function to current session..."
$env:PYTHONIOENCODING='utf-8'
iex "$($(theheck --alias).Replace("function heck", "function global:heck"))"

"  - Invoking heck()`n"
heck @args;
[Console]::ResetColor()
