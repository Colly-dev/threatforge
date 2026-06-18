rule RansomwareNote {
    meta:
        description = "Detects common ransomware notes"
    strings:
        $s1 = "Your files have been encrypted"
    condition:
        $s1
}
