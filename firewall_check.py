
# Basic Firewall Rule Validation

def check_firewall_rule(port, action):
    if port < 1 or port > 65535:
        return "INVALID: Port number is not valid."

    if action.lower() not in ["allow", "deny"]:
        return "INVALID: Firewall action is not valid."

    if port == 3389 and action.lower() == "allow":
        return "WARNING: RDP access should be restricted."

    return "VALID: Firewall rule passed basic checks."


print(check_firewall_rule(80, "allow"))
print(check_firewall_rule(3389, "allow"))
print(check_firewall_rule(70000, "deny"))
