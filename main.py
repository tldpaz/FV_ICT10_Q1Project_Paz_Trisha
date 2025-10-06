from pyscript import display, document

# General info
store_name = "Lorr De Lorran"
owner_name = "Owner: Trisha Lorainne Paz"
year_founded = "Est. 2025"
business_hours = "Open: 11:00 AM - 10:00 PM"

# Menu with images + prices
menu_prices = {
    "Carbonara": {"price": 79.99, "img": "https://i.imgur.com/VnViS6Q.jpg"},
    "Garlic Bread": {"price": 50.00, "img": "https://i.imgur.com/PSnx3eD.jpg"},
    "Caesar Salad": {"price": 150.00, "img": "https://i.imgur.com/RSbcpjM.jpg"},
    "Iced Tea": {"price": 30.00, "img": "https://i.imgur.com/yUJp4GH.jpg"},
    "Sparkling Water": {"price": 20.00, "img": "https://i.imgur.com/4A0NqBA.jpg"}
}

# ===== Homepage content =====
if document.getElementById("storeName"):
    display(store_name, target="storeName")
if document.getElementById("ownerName"):
    display(owner_name, target="ownerName")
if document.getElementById("yearFounded"):
    display(year_founded, target="yearFounded")
if document.getElementById("output4"):
    display(business_hours, target="output4")

# Generate pricelist (for homepage)
if document.getElementById("menu_list"):
    menu_html = ""
    for item, data in menu_prices.items():
        menu_html += f"<li>{item}: ₱{data['price']:.2f}</li>"
    document.getElementById("menu_list").innerHTML = menu_html


# ===== Order page content =====
if document.getElementById("menu_options"):
    menu_html = ""
    for item, data in menu_prices.items():
        menu_html += f"""
        <div class='menu-item mb-2'>
            <input type='checkbox' value='{item}' class='form-check-input me-2'>
            <img src='{data["img"]}' alt='{item}' width='50' height='50' class='me-2 rounded'>
            <label>{item} - ₱{data["price"]:.2f}</label>
        </div>
        """
    document.getElementById("menu_options").innerHTML = menu_html

    # Create order function
    def create_order(event):
        name = document.querySelector("#custName").value
        addr = document.querySelector("#custAddr").value
        phone = document.querySelector("#custPhone").value
        checkboxes = document.querySelectorAll("#menu_options input[type=checkbox]")

        selected_items = []
        total = 0
        for cb in checkboxes:
            if cb.checked:
                selected_items.append(cb.value)
                total += menu_prices[cb.value]["price"]

        if not selected_items:
            summary_html = "<p class='text-danger'>Please select at least one item.</p>"
        else:
            summary_html = f"""
            <p><strong>Order for:</strong> {name}</p>
            <p><strong>Address:</strong> {addr}</p>
            <p><strong>Contact number:</strong> {phone}</p>
            <p><strong>Items:</strong> {', '.join(selected_items)}</p>
            <h5 class='mt-3 text-primary'><strong>Total:</strong> ₱{total:.2f}</h5>
            """
        document.getElementById("order_summary").innerHTML = summary_html

        # MAM I GOT IT TO WORK NYAHAHAHAHAHAHHAHAHAHAHAHHAHAH YAYYYYYY (ALTHOUGH IM A BIT LATE SO YES CRIES BUT STILL YAYAYAYAYAYYA)
