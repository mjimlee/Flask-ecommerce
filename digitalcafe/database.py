import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

products_db = myclient["products"]
branches_db = myclient["branches"]
order_management_db = myclient["order_management"]

# branches = {
#     1: {"name":"Katipunan","phonenumber":"09179990000"},
#     2: {"name":"Tomas Morato","phonenumber":"09179990001"},
#     3: {"name":"Eastwood","phonenumber":"09179990002"},
#     4: {"name":"Tiendesitas","phonenumber":"09179990003"},
#     5: {"name":"Arcovia","phonenumber":"09179990004"},
# }

def get_product(code):
    products_coll = products_db["products"]

    product = products_coll.find_one({"code":code},{"_id":0})

    return product

def get_products():
    product_list = []

    products_coll = products_db["products"]

    for p in products_coll.find({},{"_id":0}):
        product_list.append(p)

    return product_list

def get_branch(code):
    branches_coll = branches_db["branches"]

    branches = branches_coll.find_one({"code":code})

    return branches

def get_branches():
    branch_list = []

    branch_coll = branches_db["branches"]

    for m in branch_coll.find({}):
        branch_list.append(m)

    return branch_list

def get_user(username):
    customers_coll = order_management_db['customers']
    user=customers_coll.find_one({"username":username})
    return user

def create_order(order):
    orders_coll = order_management_db['orders']
    orders_coll.insert(order)
