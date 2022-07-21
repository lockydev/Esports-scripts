robocopy bin C:\LockysRestrictions
icacls C:\LockysRestrictions /t /c /deny Student:R
icacls C:\LockysRestrictions /t /c /deny Student:W