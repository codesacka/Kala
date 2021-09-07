# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Areas(models.Model):
    area_code = models.AutoField(primary_key=True)
    description = models.CharField(unique=True, max_length=60)
    inactive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'areas'


class Attachments(models.Model):
    description = models.CharField(max_length=60)
    type_no = models.IntegerField()
    trans_no = models.IntegerField()
    unique_name = models.CharField(max_length=60)
    tran_date = models.DateField()
    filename = models.CharField(max_length=60)
    filesize = models.IntegerField()
    filetype = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'attachments'


class AuditTrail(models.Model):
    type = models.PositiveSmallIntegerField()
    trans_no = models.PositiveIntegerField()
    user = models.PositiveSmallIntegerField()
    stamp = models.DateTimeField()
    description = models.CharField(max_length=60, blank=True, null=True)
    fiscal_year = models.IntegerField()
    gl_date = models.DateField()
    gl_seq = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'audit_trail'


class BankAccounts(models.Model):
    account_code = models.CharField(max_length=15)
    account_type = models.SmallIntegerField()
    bank_account_name = models.CharField(max_length=60)
    bank_account_number = models.CharField(max_length=100)
    bank_name = models.CharField(max_length=60)
    bank_address = models.TextField(blank=True, null=True)
    bank_curr_code = models.CharField(max_length=3)
    dflt_curr_act = models.IntegerField()
    id = models.SmallAutoField(primary_key=True)
    bank_charge_act = models.CharField(max_length=15)
    last_reconciled_date = models.DateTimeField()
    ending_reconcile_balance = models.FloatField()
    inactive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bank_accounts'


class BankTrans(models.Model):
    type = models.SmallIntegerField(blank=True, null=True)
    trans_no = models.IntegerField(blank=True, null=True)
    bank_act = models.CharField(max_length=15)
    ref = models.CharField(max_length=40, blank=True, null=True)
    trans_date = models.DateField()
    amount = models.FloatField(blank=True, null=True)
    dimension_id = models.IntegerField()
    dimension2_id = models.IntegerField()
    person_type_id = models.IntegerField()
    person_id = models.TextField(blank=True, null=True)
    reconciled = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bank_trans'


class Bom(models.Model):
    id = models.AutoField()
    parent = models.CharField(primary_key=True, max_length=20)
    component = models.CharField(max_length=20)
    workcentre_added = models.IntegerField()
    loc_code = models.CharField(max_length=5)
    quantity = models.FloatField()

    class Meta:
        managed = False
        db_table = 'bom'
        unique_together = (('parent', 'component', 'workcentre_added', 'loc_code'),)


class BudgetTrans(models.Model):
    tran_date = models.DateField()
    account = models.CharField(max_length=15)
    memo_field = models.TextField(db_column='memo_')  # Field renamed because it ended with '_'.
    amount = models.FloatField()
    dimension_id = models.IntegerField(blank=True, null=True)
    dimension2_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'budget_trans'


class ChartClass(models.Model):
    cid = models.CharField(primary_key=True, max_length=3)
    class_name = models.CharField(max_length=60)
    ctype = models.IntegerField()
    inactive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'chart_class'


class ChartMaster(models.Model):
    account_code = models.CharField(primary_key=True, max_length=15)
    account_code2 = models.CharField(max_length=15)
    account_name = models.CharField(max_length=60)
    account_type = models.CharField(max_length=10)
    inactive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'chart_master'


class ChartTypes(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=60)
    class_id = models.CharField(max_length=3)
    parent = models.CharField(max_length=10)
    inactive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'chart_types'


class Comments(models.Model):
    type = models.IntegerField()
    id = models.IntegerField()
    date_field = models.DateField(db_column='date_', blank=True, null=True)  # Field renamed because it ended with '_'.
    memo_field = models.TextField(db_column='memo_', blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'comments'


class CreditStatus(models.Model):
    reason_description = models.CharField(unique=True, max_length=100)
    dissallow_invoices = models.IntegerField()
    inactive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'credit_status'


class CrmCategories(models.Model):
    type = models.CharField(max_length=20)
    action = models.CharField(max_length=20)
    name = models.CharField(max_length=30)
    description = models.TextField()
    system = models.IntegerField()
    inactive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'crm_categories'
        unique_together = (('type', 'action'), ('type', 'name'),)


class CrmContacts(models.Model):
    person_id = models.IntegerField()
    type = models.CharField(max_length=20)
    action = models.CharField(max_length=20)
    entity_id = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_contacts'


class CrmPersons(models.Model):
    ref = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    name2 = models.CharField(max_length=60, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    phone2 = models.CharField(max_length=30, blank=True, null=True)
    fax = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    lang = models.CharField(max_length=5, blank=True, null=True)
    notes = models.TextField()
    inactive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'crm_persons'


class Currencies(models.Model):
    currency = models.CharField(max_length=60)
    curr_abrev = models.CharField(primary_key=True, max_length=3)
    curr_symbol = models.CharField(max_length=10)
    country = models.CharField(max_length=100)
    hundreds_name = models.CharField(max_length=15)
    auto_update = models.IntegerField()
    inactive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'currencies'


class CustAllocations(models.Model):
    person_id = models.IntegerField(blank=True, null=True)
    amt = models.FloatField(blank=True, null=True)
    date_alloc = models.DateField()
    trans_no_from = models.IntegerField(blank=True, null=True)
    trans_type_from = models.IntegerField(blank=True, null=True)
    trans_no_to = models.IntegerField(blank=True, null=True)
    trans_type_to = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cust_allocations'
        unique_together = (('person_id', 'trans_type_from', 'trans_no_from', 'trans_type_to', 'trans_no_to'),)


class CustBranch(models.Model):
    branch_code = models.AutoField(primary_key=True)
    debtor_no = models.IntegerField()
    br_name = models.CharField(max_length=60)
    branch_ref = models.CharField(max_length=30)
    br_address = models.TextField()
    area = models.IntegerField(blank=True, null=True)
    salesman = models.IntegerField()
    default_location = models.CharField(max_length=5)
    tax_group_id = models.IntegerField(blank=True, null=True)
    sales_account = models.CharField(max_length=15)
    sales_discount_account = models.CharField(max_length=15)
    receivables_account = models.CharField(max_length=15)
    payment_discount_account = models.CharField(max_length=15)
    default_ship_via = models.IntegerField()
    br_post_address = models.TextField()
    group_no = models.IntegerField()
    notes = models.TextField()
    bank_account = models.CharField(max_length=60, blank=True, null=True)
    inactive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cust_branch'
        unique_together = (('branch_code', 'debtor_no'),)


class DebtorTrans(models.Model):
    trans_no = models.PositiveIntegerField()
    type = models.PositiveSmallIntegerField(primary_key=True)
    version = models.PositiveIntegerField()
    debtor_no = models.PositiveIntegerField()
    branch_code = models.IntegerField()
    tran_date = models.DateField()
    due_date = models.DateField()
    reference = models.CharField(max_length=60)
    tpe = models.IntegerField()
    order_field = models.IntegerField(db_column='order_')  # Field renamed because it ended with '_'.
    ov_amount = models.FloatField()
    ov_gst = models.FloatField()
    ov_freight = models.FloatField()
    ov_freight_tax = models.FloatField()
    ov_discount = models.FloatField()
    alloc = models.FloatField()
    prep_amount = models.FloatField()
    rate = models.FloatField()
    ship_via = models.IntegerField(blank=True, null=True)
    dimension_id = models.IntegerField()
    dimension2_id = models.IntegerField()
    payment_terms = models.IntegerField(blank=True, null=True)
    tax_included = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'debtor_trans'
        unique_together = (('type', 'trans_no', 'debtor_no'),)


class DebtorTransDetails(models.Model):
    debtor_trans_no = models.IntegerField(blank=True, null=True)
    debtor_trans_type = models.IntegerField(blank=True, null=True)
    stock_id = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    unit_price = models.FloatField()
    unit_tax = models.FloatField()
    quantity = models.FloatField()
    discount_percent = models.FloatField()
    standard_cost = models.FloatField()
    qty_done = models.FloatField()
    src_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'debtor_trans_details'


class DebtorsMaster(models.Model):
    debtor_no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    debtor_ref = models.CharField(unique=True, max_length=30)
    address = models.TextField(blank=True, null=True)
    tax_id = models.CharField(max_length=55)
    curr_code = models.CharField(max_length=3)
    sales_type = models.IntegerField()
    dimension_id = models.IntegerField()
    dimension2_id = models.IntegerField()
    credit_status = models.IntegerField()
    payment_terms = models.IntegerField(blank=True, null=True)
    discount = models.FloatField()
    pymt_discount = models.FloatField()
    credit_limit = models.FloatField()
    notes = models.TextField()
    inactive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'debtors_master'


class Dimensions(models.Model):
    reference = models.CharField(unique=True, max_length=60)
    name = models.CharField(max_length=60)
    type_field = models.IntegerField(db_column='type_')  # Field renamed because it ended with '_'.
    closed = models.IntegerField()
    date_field = models.DateField(db_column='date_')  # Field renamed because it ended with '_'.
    due_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'dimensions'


class ExchangeRates(models.Model):
    curr_code = models.CharField(max_length=3)
    rate_buy = models.FloatField()
    rate_sell = models.FloatField()
    date_field = models.DateField(db_column='date_')  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'exchange_rates'
        unique_together = (('curr_code', 'date_field'),)


class FiscalYear(models.Model):
    begin = models.DateField(unique=True, blank=True, null=True)
    end = models.DateField(unique=True, blank=True, null=True)
    closed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fiscal_year'


class GlTrans(models.Model):
    counter = models.AutoField(primary_key=True)
    type = models.SmallIntegerField()
    type_no = models.IntegerField()
    tran_date = models.DateField()
    account = models.CharField(max_length=15)
    memo_field = models.TextField(db_column='memo_')  # Field renamed because it ended with '_'.
    amount = models.FloatField()
    dimension_id = models.IntegerField()
    dimension2_id = models.IntegerField()
    person_type_id = models.IntegerField(blank=True, null=True)
    person_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gl_trans'


class GrnBatch(models.Model):
    supplier_id = models.IntegerField()
    purch_order_no = models.IntegerField(blank=True, null=True)
    reference = models.CharField(max_length=60)
    delivery_date = models.DateField()
    loc_code = models.CharField(max_length=5, blank=True, null=True)
    rate = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grn_batch'


class GrnItems(models.Model):
    grn_batch_id = models.IntegerField(blank=True, null=True)
    po_detail_item = models.IntegerField()
    item_code = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    qty_recd = models.FloatField()
    quantity_inv = models.FloatField()

    class Meta:
        managed = False
        db_table = 'grn_items'


class Groups(models.Model):
    id = models.SmallAutoField(primary_key=True)
    description = models.CharField(unique=True, max_length=60)
    inactive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'groups'


class ItemCodes(models.Model):
    item_code = models.CharField(max_length=20)
    stock_id = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    category_id = models.PositiveSmallIntegerField()
    quantity = models.FloatField()
    is_foreign = models.IntegerField()
    inactive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'item_codes'
        unique_together = (('stock_id', 'item_code'),)


class ItemTaxTypeExemptions(models.Model):
    item_tax_type_id = models.IntegerField(primary_key=True)
    tax_type_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'item_tax_type_exemptions'
        unique_together = (('item_tax_type_id', 'tax_type_id'),)


class ItemTaxTypes(models.Model):
    name = models.CharField(unique=True, max_length=60)
    exempt = models.IntegerField()
    inactive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'item_tax_types'


class ItemUnits(models.Model):
    abbr = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(unique=True, max_length=40)
    decimals = models.IntegerField()
    inactive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'item_units'


class Journal(models.Model):
    type = models.SmallIntegerField(primary_key=True)
    trans_no = models.IntegerField()
    tran_date = models.DateField(blank=True, null=True)
    reference = models.CharField(max_length=60)
    source_ref = models.CharField(max_length=60)
    event_date = models.DateField(blank=True, null=True)
    doc_date = models.DateField()
    currency = models.CharField(max_length=3)
    amount = models.FloatField()
    rate = models.FloatField()

    class Meta:
        managed = False
        db_table = 'journal'
        unique_together = (('type', 'trans_no'),)


class LocStock(models.Model):
    loc_code = models.CharField(primary_key=True, max_length=5)
    stock_id = models.CharField(max_length=20)
    reorder_level = models.FloatField()

    class Meta:
        managed = False
        db_table = 'loc_stock'
        unique_together = (('loc_code', 'stock_id'),)


class Locations(models.Model):
    loc_code = models.CharField(primary_key=True, max_length=5)
    location_name = models.CharField(max_length=60)
    delivery_address = models.TextField()
    phone = models.CharField(max_length=30)
    phone2 = models.CharField(max_length=30)
    fax = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=30)
    fixed_asset = models.IntegerField()
    inactive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'locations'


class PaymentTerms(models.Model):
    terms_indicator = models.AutoField(primary_key=True)
    terms = models.CharField(unique=True, max_length=80)
    days_before_due = models.SmallIntegerField()
    day_in_following_month = models.SmallIntegerField()
    inactive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'payment_terms'


class Prices(models.Model):
    stock_id = models.CharField(max_length=20)
    sales_type_id = models.IntegerField()
    curr_abrev = models.CharField(max_length=3)
    price = models.FloatField()

    class Meta:
        managed = False
        db_table = 'prices'
        unique_together = (('stock_id', 'sales_type_id', 'curr_abrev'),)


class PrintProfiles(models.Model):
    id = models.SmallAutoField(primary_key=True)
    profile = models.CharField(max_length=30)
    report = models.CharField(max_length=5, blank=True, null=True)
    printer = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'print_profiles'
        unique_together = (('profile', 'report'),)


class Printers(models.Model):
    name = models.CharField(unique=True, max_length=20)
    description = models.CharField(max_length=60)
    queue = models.CharField(max_length=20)
    host = models.CharField(max_length=40)
    port = models.PositiveSmallIntegerField()
    timeout = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'printers'


class PurchData(models.Model):
    supplier_id = models.IntegerField(primary_key=True)
    stock_id = models.CharField(max_length=20)
    price = models.FloatField()
    suppliers_uom = models.CharField(max_length=50)
    conversion_factor = models.FloatField()
    supplier_description = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'purch_data'
        unique_together = (('supplier_id', 'stock_id'),)


class PurchOrderDetails(models.Model):
    po_detail_item = models.AutoField(primary_key=True)
    order_no = models.IntegerField()
    item_code = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    delivery_date = models.DateField()
    qty_invoiced = models.FloatField()
    unit_price = models.FloatField()
    act_price = models.FloatField()
    std_cost_unit = models.FloatField()
    quantity_ordered = models.FloatField()
    quantity_received = models.FloatField()

    class Meta:
        managed = False
        db_table = 'purch_order_details'


class PurchOrders(models.Model):
    order_no = models.AutoField(primary_key=True)
    supplier_id = models.IntegerField()
    comments = models.TextField(blank=True, null=True)
    ord_date = models.DateField()
    reference = models.TextField()
    requisition_no = models.TextField(blank=True, null=True)
    into_stock_location = models.CharField(max_length=5)
    delivery_address = models.TextField()
    total = models.FloatField()
    prep_amount = models.FloatField()
    alloc = models.FloatField()
    tax_included = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'purch_orders'


class QuickEntries(models.Model):
    id = models.SmallAutoField(primary_key=True)
    type = models.IntegerField()
    description = models.CharField(max_length=60)
    usage = models.CharField(max_length=120, blank=True, null=True)
    base_amount = models.FloatField()
    base_desc = models.CharField(max_length=60, blank=True, null=True)
    bal_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'quick_entries'


class QuickEntryLines(models.Model):
    id = models.SmallAutoField(primary_key=True)
    qid = models.PositiveSmallIntegerField()
    amount = models.FloatField(blank=True, null=True)
    memo = models.TextField()
    action = models.CharField(max_length=2)
    dest_id = models.CharField(max_length=15)
    dimension_id = models.PositiveSmallIntegerField(blank=True, null=True)
    dimension2_id = models.PositiveSmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quick_entry_lines'


class RecurrentInvoices(models.Model):
    id = models.SmallAutoField(primary_key=True)
    description = models.CharField(unique=True, max_length=60)
    order_no = models.PositiveIntegerField()
    debtor_no = models.PositiveIntegerField(blank=True, null=True)
    group_no = models.PositiveSmallIntegerField(blank=True, null=True)
    days = models.IntegerField()
    monthly = models.IntegerField()
    begin = models.DateField()
    end = models.DateField()
    last_sent = models.DateField()

    class Meta:
        managed = False
        db_table = 'recurrent_invoices'


class Reflines(models.Model):
    trans_type = models.IntegerField()
    prefix = models.CharField(max_length=5)
    pattern = models.CharField(max_length=35)
    description = models.CharField(max_length=60)
    default = models.IntegerField()
    inactive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'reflines'
        unique_together = (('trans_type', 'prefix'),)


class Refs(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.IntegerField()
    reference = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'refs'
        unique_together = (('id', 'type'),)


class SalesOrderDetails(models.Model):
    order_no = models.IntegerField()
    trans_type = models.SmallIntegerField()
    stk_code = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    qty_sent = models.FloatField()
    unit_price = models.FloatField()
    quantity = models.FloatField()
    invoiced = models.FloatField()
    discount_percent = models.FloatField()

    class Meta:
        managed = False
        db_table = 'sales_order_details'


class SalesOrders(models.Model):
    order_no = models.IntegerField()
    trans_type = models.SmallIntegerField(primary_key=True)
    version = models.PositiveIntegerField()
    type = models.IntegerField()
    debtor_no = models.IntegerField()
    branch_code = models.IntegerField()
    reference = models.CharField(max_length=100)
    customer_ref = models.TextField()
    comments = models.TextField(blank=True, null=True)
    ord_date = models.DateField()
    order_type = models.IntegerField()
    ship_via = models.IntegerField()
    delivery_address = models.TextField()
    contact_phone = models.CharField(max_length=30, blank=True, null=True)
    contact_email = models.CharField(max_length=100, blank=True, null=True)
    deliver_to = models.TextField()
    freight_cost = models.FloatField()
    from_stk_loc = models.CharField(max_length=5)
    delivery_date = models.DateField()
    payment_terms = models.IntegerField(blank=True, null=True)
    total = models.FloatField()
    prep_amount = models.FloatField()
    alloc = models.FloatField()

    class Meta:
        managed = False
        db_table = 'sales_orders'
        unique_together = (('trans_type', 'order_no'),)


class SalesPos(models.Model):
    id = models.SmallAutoField(primary_key=True)
    pos_name = models.CharField(unique=True, max_length=30)
    cash_sale = models.IntegerField()
    credit_sale = models.IntegerField()
    pos_location = models.CharField(max_length=5)
    pos_account = models.PositiveSmallIntegerField()
    inactive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sales_pos'


class SalesTypes(models.Model):
    sales_type = models.CharField(unique=True, max_length=50)
    tax_included = models.IntegerField()
    factor = models.FloatField()
    inactive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sales_types'


class Salesman(models.Model):
    salesman_code = models.AutoField(primary_key=True)
    salesman_name = models.CharField(unique=True, max_length=60)
    salesman_phone = models.CharField(max_length=30)
    salesman_fax = models.CharField(max_length=30)
    salesman_email = models.CharField(max_length=100)
    provision = models.FloatField()
    break_pt = models.FloatField()
    provision2 = models.FloatField()
    inactive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'salesman'


class SecurityRoles(models.Model):
    role = models.CharField(unique=True, max_length=30)
    description = models.CharField(max_length=50, blank=True, null=True)
    sections = models.TextField(blank=True, null=True)
    areas = models.TextField(blank=True, null=True)
    inactive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'security_roles'


class Shippers(models.Model):
    shipper_id = models.AutoField(primary_key=True)
    shipper_name = models.CharField(unique=True, max_length=60)
    phone = models.CharField(max_length=30)
    phone2 = models.CharField(max_length=30)
    contact = models.TextField()
    address = models.TextField()
    inactive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shippers'


class SqlTrail(models.Model):
    sql = models.TextField()
    result = models.IntegerField()
    msg = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'sql_trail'


class StockCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    description = models.CharField(unique=True, max_length=60)
    dflt_tax_type = models.IntegerField()
    dflt_units = models.CharField(max_length=20)
    dflt_mb_flag = models.CharField(max_length=1)
    dflt_sales_act = models.CharField(max_length=15)
    dflt_cogs_act = models.CharField(max_length=15)
    dflt_inventory_act = models.CharField(max_length=15)
    dflt_adjustment_act = models.CharField(max_length=15)
    dflt_wip_act = models.CharField(max_length=15)
    dflt_dim1 = models.IntegerField(blank=True, null=True)
    dflt_dim2 = models.IntegerField(blank=True, null=True)
    inactive = models.IntegerField()
    dflt_no_sale = models.IntegerField()
    dflt_no_purchase = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stock_category'


class StockFaClass(models.Model):
    fa_class_id = models.CharField(primary_key=True, max_length=20)
    parent_id = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    long_description = models.TextField()
    depreciation_rate = models.FloatField()
    inactive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stock_fa_class'


class StockMaster(models.Model):
    stock_id = models.CharField(primary_key=True, max_length=20)
    category_id = models.IntegerField()
    tax_type_id = models.IntegerField()
    description = models.CharField(max_length=200)
    long_description = models.TextField()
    units = models.CharField(max_length=20)
    mb_flag = models.CharField(max_length=1)
    sales_account = models.CharField(max_length=15)
    cogs_account = models.CharField(max_length=15)
    inventory_account = models.CharField(max_length=15)
    adjustment_account = models.CharField(max_length=15)
    wip_account = models.CharField(max_length=15)
    dimension_id = models.IntegerField(blank=True, null=True)
    dimension2_id = models.IntegerField(blank=True, null=True)
    purchase_cost = models.FloatField()
    material_cost = models.FloatField()
    labour_cost = models.FloatField()
    overhead_cost = models.FloatField()
    inactive = models.IntegerField()
    no_sale = models.IntegerField()
    no_purchase = models.IntegerField()
    editable = models.IntegerField()
    depreciation_method = models.CharField(max_length=1)
    depreciation_rate = models.FloatField()
    depreciation_factor = models.FloatField()
    depreciation_start = models.DateField()
    depreciation_date = models.DateField()
    fa_class_id = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'stock_master'


class StockMoves(models.Model):
    trans_id = models.AutoField(primary_key=True)
    trans_no = models.IntegerField()
    stock_id = models.CharField(max_length=20)
    type = models.SmallIntegerField()
    loc_code = models.CharField(max_length=5)
    tran_date = models.DateField()
    price = models.FloatField()
    reference = models.CharField(max_length=40)
    qty = models.FloatField()
    standard_cost = models.FloatField()

    class Meta:
        managed = False
        db_table = 'stock_moves'


class SuppAllocations(models.Model):
    person_id = models.IntegerField(blank=True, null=True)
    amt = models.FloatField(blank=True, null=True)
    date_alloc = models.DateField()
    trans_no_from = models.IntegerField(blank=True, null=True)
    trans_type_from = models.IntegerField(blank=True, null=True)
    trans_no_to = models.IntegerField(blank=True, null=True)
    trans_type_to = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supp_allocations'
        unique_together = (('person_id', 'trans_type_from', 'trans_no_from', 'trans_type_to', 'trans_no_to'),)


class SuppInvoiceItems(models.Model):
    supp_trans_no = models.IntegerField(blank=True, null=True)
    supp_trans_type = models.IntegerField(blank=True, null=True)
    gl_code = models.CharField(max_length=15)
    grn_item_id = models.IntegerField(blank=True, null=True)
    po_detail_item_id = models.IntegerField(blank=True, null=True)
    stock_id = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    quantity = models.FloatField()
    unit_price = models.FloatField()
    unit_tax = models.FloatField()
    memo_field = models.TextField(db_column='memo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    dimension_id = models.IntegerField()
    dimension2_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'supp_invoice_items'


class SuppTrans(models.Model):
    trans_no = models.PositiveIntegerField()
    type = models.PositiveSmallIntegerField(primary_key=True)
    supplier_id = models.PositiveIntegerField()
    reference = models.TextField()
    supp_reference = models.CharField(max_length=60)
    tran_date = models.DateField()
    due_date = models.DateField()
    ov_amount = models.FloatField()
    ov_discount = models.FloatField()
    ov_gst = models.FloatField()
    rate = models.FloatField()
    alloc = models.FloatField()
    tax_included = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'supp_trans'
        unique_together = (('type', 'trans_no', 'supplier_id'),)


class Suppliers(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    supp_name = models.CharField(max_length=60)
    supp_ref = models.CharField(max_length=30)
    address = models.TextField()
    supp_address = models.TextField()
    gst_no = models.CharField(max_length=25)
    contact = models.CharField(max_length=60)
    supp_account_no = models.CharField(max_length=40)
    website = models.CharField(max_length=100)
    bank_account = models.CharField(max_length=60)
    curr_code = models.CharField(max_length=3, blank=True, null=True)
    payment_terms = models.IntegerField(blank=True, null=True)
    tax_included = models.IntegerField()
    dimension_id = models.IntegerField(blank=True, null=True)
    dimension2_id = models.IntegerField(blank=True, null=True)
    tax_group_id = models.IntegerField(blank=True, null=True)
    credit_limit = models.FloatField()
    purchase_account = models.CharField(max_length=15)
    payable_account = models.CharField(max_length=15)
    payment_discount_account = models.CharField(max_length=15)
    notes = models.TextField()
    inactive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'suppliers'


class SysPrefs(models.Model):
    name = models.CharField(primary_key=True, max_length=35)
    category = models.CharField(max_length=30, blank=True, null=True)
    type = models.CharField(max_length=20)
    length = models.SmallIntegerField(blank=True, null=True)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'sys_prefs'


class TagAssociations(models.Model):
    record_id = models.CharField(primary_key=True, max_length=15)
    tag_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tag_associations'
        unique_together = (('record_id', 'tag_id'),)


class Tags(models.Model):
    type = models.SmallIntegerField()
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=60, blank=True, null=True)
    inactive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tags'
        unique_together = (('type', 'name'),)


class TaxGroupItems(models.Model):
    tax_group_id = models.IntegerField(primary_key=True)
    tax_type_id = models.IntegerField()
    tax_shipping = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tax_group_items'
        unique_together = (('tax_group_id', 'tax_type_id'),)


class TaxGroups(models.Model):
    name = models.CharField(unique=True, max_length=60)
    inactive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tax_groups'


class TaxTypes(models.Model):
    rate = models.FloatField()
    sales_gl_code = models.CharField(max_length=15)
    purchasing_gl_code = models.CharField(max_length=15)
    name = models.CharField(max_length=60)
    inactive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tax_types'


class TransTaxDetails(models.Model):
    trans_type = models.SmallIntegerField(blank=True, null=True)
    trans_no = models.IntegerField(blank=True, null=True)
    tran_date = models.DateField()
    tax_type_id = models.IntegerField()
    rate = models.FloatField()
    ex_rate = models.FloatField()
    included_in_price = models.IntegerField()
    net_amount = models.FloatField()
    amount = models.FloatField()
    memo = models.TextField(blank=True, null=True)
    reg_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trans_tax_details'


class Useronline(models.Model):
    timestamp = models.IntegerField()
    ip = models.CharField(max_length=40)
    file = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'useronline'


class Users(models.Model):
    id = models.SmallAutoField(primary_key=True)
    user_id = models.CharField(unique=True, max_length=60)
    password = models.CharField(max_length=100)
    real_name = models.CharField(max_length=100)
    role_id = models.IntegerField()
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=100, blank=True, null=True)
    language = models.CharField(max_length=20, blank=True, null=True)
    date_format = models.IntegerField()
    date_sep = models.IntegerField()
    tho_sep = models.IntegerField()
    dec_sep = models.IntegerField()
    theme = models.CharField(max_length=20)
    page_size = models.CharField(max_length=20)
    prices_dec = models.SmallIntegerField()
    qty_dec = models.SmallIntegerField()
    rates_dec = models.SmallIntegerField()
    percent_dec = models.SmallIntegerField()
    show_gl = models.IntegerField()
    show_codes = models.IntegerField()
    show_hints = models.IntegerField()
    last_visit_date = models.DateTimeField(blank=True, null=True)
    query_size = models.PositiveIntegerField()
    graphic_links = models.IntegerField(blank=True, null=True)
    pos = models.SmallIntegerField(blank=True, null=True)
    print_profile = models.CharField(max_length=30)
    rep_popup = models.IntegerField(blank=True, null=True)
    sticky_doc_date = models.IntegerField(blank=True, null=True)
    startup_tab = models.CharField(max_length=20)
    transaction_days = models.SmallIntegerField()
    save_report_selections = models.SmallIntegerField()
    use_date_picker = models.IntegerField()
    def_print_destination = models.IntegerField()
    def_print_orientation = models.IntegerField()
    inactive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users'


class Voided(models.Model):
    type = models.IntegerField()
    id = models.IntegerField()
    date_field = models.DateField(db_column='date_')  # Field renamed because it ended with '_'.
    memo_field = models.TextField(db_column='memo_')  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'voided'
        unique_together = (('type', 'id'),)


class WoCosting(models.Model):
    workorder_id = models.IntegerField()
    cost_type = models.IntegerField()
    trans_type = models.IntegerField()
    trans_no = models.IntegerField()
    factor = models.FloatField()

    class Meta:
        managed = False
        db_table = 'wo_costing'


class WoIssueItems(models.Model):
    stock_id = models.CharField(max_length=40, blank=True, null=True)
    issue_id = models.IntegerField(blank=True, null=True)
    qty_issued = models.FloatField(blank=True, null=True)
    unit_cost = models.FloatField()

    class Meta:
        managed = False
        db_table = 'wo_issue_items'


class WoIssues(models.Model):
    issue_no = models.AutoField(primary_key=True)
    workorder_id = models.IntegerField()
    reference = models.CharField(max_length=100, blank=True, null=True)
    issue_date = models.DateField(blank=True, null=True)
    loc_code = models.CharField(max_length=5, blank=True, null=True)
    workcentre_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wo_issues'


class WoManufacture(models.Model):
    reference = models.CharField(max_length=100, blank=True, null=True)
    workorder_id = models.IntegerField()
    quantity = models.FloatField()
    date_field = models.DateField(db_column='date_')  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'wo_manufacture'


class WoRequirements(models.Model):
    workorder_id = models.IntegerField()
    stock_id = models.CharField(max_length=20)
    workcentre = models.IntegerField()
    units_req = models.FloatField()
    unit_cost = models.FloatField()
    loc_code = models.CharField(max_length=5)
    units_issued = models.FloatField()

    class Meta:
        managed = False
        db_table = 'wo_requirements'


class Workcentres(models.Model):
    name = models.CharField(unique=True, max_length=40)
    description = models.CharField(max_length=50)
    inactive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'workcentres'


class Workorders(models.Model):
    wo_ref = models.CharField(unique=True, max_length=60)
    loc_code = models.CharField(max_length=5)
    units_reqd = models.FloatField()
    stock_id = models.CharField(max_length=20)
    date_field = models.DateField(db_column='date_')  # Field renamed because it ended with '_'.
    type = models.IntegerField()
    required_by = models.DateField()
    released_date = models.DateField()
    units_issued = models.FloatField()
    closed = models.IntegerField()
    released = models.IntegerField()
    additional_costs = models.FloatField()

    class Meta:
        managed = False
        db_table = 'workorders'
