import frappe

@frappe.whitelist(allow_guest=True)
def test_api():
    return frappe.msgprint("API works !!")
