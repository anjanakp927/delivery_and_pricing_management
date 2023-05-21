{
    'name': "Delivery and Pricing Management ",
    'version': '0.1',
    'summary': "Module to add delivery charges in sale orders and invoices and minimum cost and brand name fields in product master",
    'description': """
        This module adds a field in the sale order to enter the delivery charges.
        And adds minimum cost and brand name, in the product master.
        It also includes the brand field in the sale order line, which autofills based on the selected product. 
        The delivery charge is automatically calculated as 10% of the total amount.
        When creating an invoice from the sale order, the delivery charge is passed to the invoice.
    """,
    'category': 'Sales',
    'depends': ['base', 'sale', 'account','product'],
    'data': [
        'views/sale_order.xml',
        'views/account_move.xml',
        'views/product_template.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
