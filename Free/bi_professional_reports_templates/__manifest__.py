# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Perpul Professional Report Templates',
    'version': '1.0',
    'summary': 'Easily Customizable Report Template for Quotation/SO/Sales, Invoice, Picking/Delivery Order,RFQ/PO/Purchases',
    'category': 'Tools',
    'description': """
		Customize report, customize pdf report, customize template report, Customize Sales Order report,Customize Purchase Order report, Customize invoice report, Customize delivery Order report, Accounting Reports, Easy reports, Flexible report,Fancy Report template.
		
    """,
    'author': 'BrowseInfo',
    'website': 'http://www.browseinfo.in',
    'depends': ['base', 'account', 'sale', 'purchase', 'stock', 'sale_stock', 'base_vat'],
    'data': [
		"res_company.xml",
		"invoice_report/fency_report_account.xml",
		"invoice_report/fency_report_invoice.xml",
		"invoice_report/report_invoice_classic.xml",
		"invoice_report/report_invoice_modern.xml",
"invoice_report/report_invoice_flectra_standard.xml",

"delivery_report/stock_report_classic.xml",
"delivery_report/fency_report_deliveryslip.xml",
"delivery_report/modern_report_deliveryslip.xml",
"delivery_report/flectra_standard_report_deliveryslip.xml",
"delivery_report/report_deliveryslip_classic.xml",

"purchase_report/classic_purchase_report.xml",
"purchase_report/classic_report_purchaseorder.xml",
"purchase_report/classic_report_purchasequotation.xml",
"purchase_report/fency_report_purchaseorder.xml",
"purchase_report/fency_report_purchasequotation.xml",
"purchase_report/modern_report_purchaseorder.xml",
"purchase_report/modern_report_purchasequotation.xml",
"purchase_report/flectra_standard_report_purchaseorder.xml",
"purchase_report/flectra_standard_report_purchasequotation.xml",

"sale_report/classic_sale_report.xml",
"sale_report/classic_report_saleorder.xml",
"sale_report/fency_report_saleorder.xml",
"sale_report/modern_report_saleorder.xml",
"sale_report/flectra_standard_report_saleorder.xml",
             ],
	'qweb': [
		],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
    "images":['static/description/Banner.png'],
}
