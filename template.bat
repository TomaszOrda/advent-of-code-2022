@echo off

set DayNumber=%1

type NUL > data\day_%DayNumber%.txt
type NUL > data\day_%DayNumber%_test.txt

set FileNameStem=solutions\day_%DayNumber%_part_

echo.>> %FileNameStem%1.py
echo.>> %FileNameStem%1.py
echo def solution(raw_input: str):>> %FileNameStem%1.py
echo.>> %FileNameStem%1.py
(echo     return None) >> %FileNameStem%1.py

copy %FileNameStem%1.py %FileNameStem%2.py
