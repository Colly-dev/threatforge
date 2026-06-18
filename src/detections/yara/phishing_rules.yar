rule PhishingRule {
    meta:
        description = "Detects phishing emails"
    strings:
        $s1 = "Verify your account"
    condition:
        $s1
}
