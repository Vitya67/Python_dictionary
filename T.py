def parse_sales(file_path):
    sales = {}
    with open(file_path, 'r') as file:
        for line in file:
            customer, item, quantity = line.split()
            if customer not in sales:
                sales[customer] = {}
            if item not in sales[customer]:
                sales[customer][item] = 0
            sales[customer][item] += int(quantity)
    return sales

def print_sales(sales):
    sorted_customers = sorted(sales.keys())
    for customer in sorted_customers:
        print(customer + ":")
        customer_sales = sales[customer]
        sorted_items = sorted(customer_sales.keys())
        for item in sorted_items:
            print(item, customer_sales[item])

sales_data = parse_sales("sales.txt")
print_sales(sales_data)
