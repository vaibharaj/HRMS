# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt


import frappe
from frappe import _


def execute(filters=None):
    if not filters:
        filters = {}

    columns = get_columns()
    data = get_employees(filters)

    return columns, data


def get_columns():
    return [
        _("Employee") + ":Link/Employee:180",
        _("Name") + ":Data:200",
        _("Date of Joining") + ":Date:200",
        _("Department") + ":Link/Department:220",
        _("Designation") + ":Link/Designation:150",
        _("Gender") + "::100",
    ]


def get_employees(filters):
    conditions = get_conditions(filters)
    return frappe.db.sql(
        """select name, employee_name, date_of_joining,
	 department, designation,
	gender from tabEmployee where status = 'Active' %s"""
        % conditions,
        as_list=1,
    )


def get_conditions(filters):
    conditions = ""
    if filters.get("month"):
        month = [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
        ].index(filters["month"]) + 1
        conditions += " and month(date_of_joining) = '%s'" % month

    if filters.get("company"):
        conditions += " and company = '%s'" % filters["company"].replace(
            "'", "\\'")

    return conditions
