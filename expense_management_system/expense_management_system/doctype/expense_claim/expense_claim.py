# Copyright (c) 2024, VRINDA and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class ExpenseClaim(Document):  
    def validate(self):  
        total_amount = 0  

        if not self.items:  
            frappe.throw("Please provide the expense details")  

        for expense in self.items:   
            total_amount += expense.get('amount', 0)   

        self.total_amount = total_amount


