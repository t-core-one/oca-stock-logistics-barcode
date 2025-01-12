import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-oca-stock-logistics-barcode",
    description="Meta package for oca-stock-logistics-barcode Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-barcodes_generator_abstract>=15.0dev,<15.1dev',
        'odoo-addon-barcodes_generator_product>=15.0dev,<15.1dev',
        'odoo-addon-base_gs1_barcode>=15.0dev,<15.1dev',
        'odoo-addon-product_multi_barcode>=15.0dev,<15.1dev',
        'odoo-addon-product_supplierinfo_barcode>=15.0dev,<15.1dev',
        'odoo-addon-stock_barcodes>=15.0dev,<15.1dev',
        'odoo-addon-stock_barcodes_elaboration>=15.0dev,<15.1dev',
        'odoo-addon-stock_barcodes_gs1>=15.0dev,<15.1dev',
        'odoo-addon-stock_barcodes_gs1_expiry>=15.0dev,<15.1dev',
        'odoo-addon-stock_barcodes_gs1_secondary_unit>=15.0dev,<15.1dev',
        'odoo-addon-stock_barcodes_picking_batch>=15.0dev,<15.1dev',
        'odoo-addon-stock_barcodes_picking_batch_revision>=15.0dev,<15.1dev',
        'odoo-addon-stock_picking_product_barcode_report>=15.0dev,<15.1dev',
        'odoo-addon-stock_picking_product_barcode_report_secondary_unit>=15.0dev,<15.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 15.0',
    ]
)
