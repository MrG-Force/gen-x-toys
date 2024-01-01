from django import forms

from order.models import Address

INPUT_STYLES = "w-full p-2 border border-gray-300 rounded-md shadow-inner focus:outline-none focus:ring"


class BillingForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=50, required=True, widget=forms.TextInput(attrs={
        'id': 'billingFirstName',
        'class': INPUT_STYLES}))
    last_name = forms.CharField(label='Last Name', max_length=50, required=True, widget=forms.TextInput(attrs={
        'id': 'billingLastName',
        'class': INPUT_STYLES}))
    street_address = forms.CharField(label='Street Address', max_length=100, required=True, widget=forms.TextInput(attrs={
        'id': 'billingStreetAddress',
        'class': INPUT_STYLES}))
    unit_apt = forms.CharField(label='Unit/Apt', max_length=20, required=False, widget=forms.TextInput(attrs={
        'id': 'billingUnitApt',
        'class': INPUT_STYLES}))
    suburb = forms.CharField(label='Suburb', max_length=50, required=True, widget=forms.TextInput(attrs={
        'id': 'billingSuburb',
        'class': INPUT_STYLES}))
    state = forms.ChoiceField(label='State', choices=[('', 'Select State...')] + list(Address.STATES_CHOICES), required=True, widget=forms.Select(attrs={
        'id': 'billingState',
        'class': INPUT_STYLES,
        'placeholder': 'Select State...'}))
    postcode = forms.CharField(label='Postcode', max_length=4, required=True, widget=forms.TextInput(attrs={
        'id': 'billingPostcode',
        'class': INPUT_STYLES}))
    email = forms.EmailField(label='Email', max_length=254, required=True, widget=forms.EmailInput(attrs={
        'id': 'billingEmail',
        'class': INPUT_STYLES}))
    phone = forms.CharField(label='Phone', max_length=15, required=True, widget=forms.TextInput(attrs={
        'id': 'billingPhone',
        'class': INPUT_STYLES}))
    
class ShippingForm(forms.Form):

    first_name = forms.CharField(label='First Name', max_length=50, required=True, widget=forms.TextInput(attrs={
        'id': 'shippingFirstName',
        'class': INPUT_STYLES}))
    last_name = forms.CharField(label='Last Name', max_length=50, required=True, widget=forms.TextInput(attrs={
        'id': 'shippingLastName',
        'class': INPUT_STYLES}))
    street_address = forms.CharField(label='Street Address', max_length=100, required=True, widget=forms.TextInput(attrs={
        'id': 'shippingStreetAddress',
        'class': INPUT_STYLES}))
    unit_apt = forms.CharField(label='Unit/Apt', max_length=20, required=False, widget=forms.TextInput(attrs={
        'id': 'shippingUnitApt',
        'class': INPUT_STYLES}))
    suburb = forms.CharField(label='Suburb', max_length=50, required=True, widget=forms.TextInput(attrs={
        'id': 'shippingSuburb',
        'class': INPUT_STYLES}))
    state = forms.ChoiceField(label='State', choices=[('', 'Select State...')] + list(Address.STATES_CHOICES), required=True, widget=forms.Select(attrs={
        'id': 'shippingState',
        'class': INPUT_STYLES,
        'placeholder': 'Select State...'}))
    postcode = forms.CharField(label='Postcode', max_length=4, required=True, widget=forms.TextInput(attrs={
        'id': 'shippingPostcode',
        'class': INPUT_STYLES}))
    
class PaymentForm(forms.Form):
    MONTH_CHOICES = [
        ('', 'Select Month...'),
        ('01', '01 - January'),
        ('02', '02 - February'),
        ('03', '03 - March'),
        ('04', '04 - April'),
        ('05', '05 - May'),
        ('06', '06 - June'),
        ('07', '07 - July'),
        ('08', '08 - August'),
        ('09', '09 - September'),
        ('10', '10 - October'),
        ('11', '11 - November'),
        ('12', '12 - December'),
    ]
    YEAR_CHOICES = [
        ('', 'Select Year...'),
        ('2024', '2024'),
        ('2025', '2025'),
        ('2026', '2026'),
        ('2027', '2027'),
        ('2028', '2028'),
        ('2029', '2029'),
        ('2030', '2030')
    ]

    name_on_card = forms.CharField(label='Name on Card', max_length=50, required=True, widget=forms.TextInput(attrs={
        'id': 'nameOnCard',
        'class': INPUT_STYLES}))
    card_number = forms.CharField(label='Card Number', max_length=16, required=True, widget=forms.TextInput(attrs={
        'id': 'cardNumber',
        'class': INPUT_STYLES}))
    expiry_month = forms.ChoiceField(label='Expiry Month', choices=MONTH_CHOICES, required=True, widget=forms.Select(attrs={
        'id': 'expiryMonth',
        'class': INPUT_STYLES,
        'placeholder': 'Select Month...'}))
    expiry_year = forms.ChoiceField(label='Expiry Year', choices=YEAR_CHOICES, required=True, widget=forms.Select(attrs={
        'id': 'expiryYear',
        'class': INPUT_STYLES,
        'placeholder': 'Select Year...'}))
    cvv = forms.CharField(label='CVV', max_length=3, required=True, widget=forms.TextInput(attrs={
        'id': 'cvv',
        'class': INPUT_STYLES}))