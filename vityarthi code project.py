import datetime

def generate_super_readable_receipt():
    """Generates a highly readable receipt"""

    
    CURRENCY = "₹" 
    WIDTH = 75 

    print(" Enter Payment Receipt Information")
    
    # Organization Info
    name = input("Enter Business Name: ")
    address = input("Enter Business Address: ")
    
    # Payer Info
    payer_name = input("Enter Name of Customer: ")
    
    # Transaction Info
    receipt_number = input("Enter Unique Receipt Number: ")
    purpose = input("Enter Description: ")
    
    subtotal_str = input("Enter Base Amount/Subtotal: ")
    tax_rate_str = input("Enter Tax Rate as a percentage (e.g., 18): ")
    payment_method = input("Enter Payment Method: ")
    transaction_id = input("Enter Transaction ID (or N/A): ")

    try:
        
        subtotal = float(subtotal_str)
        tax_rate = float(tax_rate_str) / 100
        
        tax_amount = subtotal * tax_rate
        total_amount = subtotal + tax_amount
        
    
        subtotal_f = f"{CURRENCY} {subtotal:,.2f}"
        tax_amount_f = f"{CURRENCY} {tax_amount:,.2f}"
        total_amount_f = f"{CURRENCY} {total_amount:,.2f}"
        
    except ValueError:
        print("\n[ERROR] Financial inputs must be valid number")
        subtotal_f = f"N/A ({subtotal_str})"
        tax_amount_f = "N/A"
        total_amount_f = "N/A"

    now = datetime.datetime.now()
    receipt_date = now.strftime("%B %d, %Y")
    receipt_time = now.strftime("%I:%M:%S %p")

    
    separator_heavy = "=" * WIDTH
    separator_light = "-" * WIDTH

    # Function for center alignment
    def center_text(text):
        return text.center(WIDTH)

    # Function for left/right alignment (Key/Value pairs)
    def format_line(key, value, fill_char=' '):
        return f"{key}{value.rjust(WIDTH - len(key), fill_char)}"

    receipt_content = f"""
{separator_heavy}
{center_text(name.upper())}
{center_text(address)}
{center_text("OFFICIAL PAYMENT RECEIPT")}
{separator_heavy}

{format_line("Receipt Number:", receipt_number)}
{format_line("Date:", receipt_date)}
{format_line("Time:", receipt_time)}

{separator_light}

**PAYMENT RECEIVED FROM**
{format_line("Customer Name:", payer_name.title())}
{format_line("Service/Purpose:", purpose)}

{separator_light}

**AMOUNT BREAKDOWN**
{format_line("Base Amount (Subtotal):", subtotal_f)}
{format_line(f"Tax ({tax_rate_str}%):", tax_amount_f)}

{separator_light}

**TOTAL PAID**
{format_line("**TOTAL AMOUNT PAID:**", total_amount_f, fill_char='.')}

{separator_light}

**TRANSACTION DETAILS**
{format_line("Payment Method:", payment_method)}
{format_line("Reference ID:", transaction_id if transaction_id else 'N/A')}

{separator_heavy}
{center_text("Thank You for Your Business!")}
{center_text("Authorized Signature: _________________________")}
{separator_heavy}
"""


    print("\n" + separator_heavy)
    print(" Super Readable Receipt Generated!")
    print(separator_heavy)
    print(receipt_content)
    
if __name__ == "__main__":
    generate_super_readable_receipt()
