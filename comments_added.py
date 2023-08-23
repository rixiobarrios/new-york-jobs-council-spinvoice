from datetime import datetime


class Invoice:
    """Represents an invoice for a collection of services rendered to a recipient"""

    def __init__(self,
                 sender_name,
                 recipient_name,
                 sender_address,
                 recipient_address,
                 sender_email,
                 recipient_email):
        # externally determined variables
        self.sender_name = sender_name
        self.recipient_name = recipient_name
        self.sender_address = sender_address
        self.recipient_address = recipient_address
        self.sender_email = sender_email
        self.recipient_email = recipient_email

        # internally determined variables
        self.date = datetime.now()
        self.items = []
        self.comments = []  # Store comments as a list

    def add_item(self, name, price, tax):
        # python makes working with trivial data-objects quite easy
        item = {
            "name": name,
            "price": price,
            "tax": tax
        }

        # hold on to the unmodified item for later, we'll do tax/discount calculations on an as-needed basis
        self.items.append(item)

    def calculate_total(self, discount):
        # determine how much the invoice total should be by summing all individual item totals
        total = 0
        for item in self.items:
            price = item["price"]
            tax = item["tax"]

            # Apply the discount to the item price before tax calculation
            discounted_price = price * (1 - discount)

            # Calculate the tax amount for this item based on the discounted price
            item_tax = discounted_price * tax

            # Add the discounted price and tax amount to the total
            total += discounted_price + item_tax
        return total

    def add_comment(self, comment):
        # Add a comment to the invoice
        self.comments.append(comment)

    def get_comments(self):
        # Return a string representation of all comments in the invoice
        return "\n".join(self.comments)


if __name__ == '__main__':
    invoice = Invoice(
        "Larry Jinkles",
        "Tod Hooper",
        "34 Windsor Ln.",
        "14 Manslow road",
        "lejank@billing.com",
        "discreetclorinator@hotmail.com"
    )

    invoice.add_item("34 floor building", 3400, .1)
    invoice.add_item("Equipment Rental", 1000, .1)
    invoice.add_item("Fear Tax", 340, 0.0)

    # Add comments to the invoice
    invoice.add_comment("Great service!")
    invoice.add_comment(
        "Please send the invoice to the provided email addresses.")

    invoice_total = invoice.calculate_total(.2)
    comments = invoice.get_comments()

    print(f"Invoice Total: {invoice_total}")
    print("Comments:")
    print(comments)
