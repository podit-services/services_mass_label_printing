
{
    "name": "Label Reporting",
    "version": "16.0.1.0.1",
    "category": "Tools",
    "license": "AGPL-3",
    "summary": "Generate customised labels of any document",
    "author": "Pod IT Services",
    "website": "https://poditservices.com/",
    "maintainer": "Pod IT Services",
    "depends": ["base"],
    "data": [
        "data/report_paperformat.xml",
        "security/label.brand.csv",
        "security/label.config.csv",
        "security/ir.model.access.csv",
        "data/label_size_data.xml",
        "views/label_config_view.xml",
        "views/label_print_view.xml",
        "wizard/label_print_wizard_view.xml",
        "views/label_report.xml",
        "report/dynamic_label.xml",
    ],
    "uninstall_hook": "uninstall_hook",
    "installable": True,
    "auto_install": False,
}
