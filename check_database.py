"""
Script to check MongoDB database contents and diagnose issues
"""
from pymongo import MongoClient
from bson import ObjectId

# MongoDB connection
MONGO_URI = "mongodb+srv://v647414:223344vinay@cluster0.lus5rot.mongodb.net/"
client = MongoClient(MONGO_URI)
db = client['ecommerce']

print("=" * 60)
print("DATABASE DIAGNOSTIC REPORT")
print("=" * 60)

# Check comments
print("\n1. COMMENTS COLLECTION")
print("-" * 60)
comments_collection = db['comments']
total_comments = comments_collection.count_documents({})
print(f"Total comments: {total_comments}")

if total_comments > 0:
    print("\nSample comments:")
    for i, comment in enumerate(comments_collection.find({}).limit(3), 1):
        print(f"\n  Comment {i}:")
        print(f"    _id: {comment.get('_id')}")
        print(f"    productId: {comment.get('productId')} (type: {type(comment.get('productId'))})")
        print(f"    email: {comment.get('email')}")
        print(f"    comment: {comment.get('comment', '')[:50]}...")
        print(f"    createdAt: {comment.get('createdAt')}")
else:
    print("  ⚠️  No comments found!")

# Check products
print("\n2. PRODUCTS COLLECTION")
print("-" * 60)
products_collection = db['products']
total_products = products_collection.count_documents({})
print(f"Total products: {total_products}")

if total_products > 0:
    print("\nSample products:")
    for i, product in enumerate(products_collection.find({}).limit(3), 1):
        print(f"\n  Product {i}:")
        print(f"    _id: {product.get('_id')} (type: {type(product.get('_id'))})")
        print(f"    name: {product.get('name')}")
        print(f"    price: {product.get('price')}")
        print(f"    category: {product.get('category')}")
else:
    print("  ⚠️  No products found!")

# Check if productIds in comments match product _ids
print("\n3. ID MATCHING CHECK")
print("-" * 60)

if total_comments > 0 and total_products > 0:
    sample_comment = comments_collection.find_one({})
    product_id_from_comment = sample_comment.get('productId')
    
    print(f"Sample productId from comment: {product_id_from_comment}")
    print(f"Type: {type(product_id_from_comment)}")
    
    # Try to find matching product
    product = products_collection.find_one({'_id': product_id_from_comment})
    
    if product:
        print(f"✓ Found matching product: {product.get('name')}")
    else:
        print("✗ No direct match found")
        
        # Try converting to ObjectId if it's a string
        if isinstance(product_id_from_comment, str):
            try:
                product = products_collection.find_one({'_id': ObjectId(product_id_from_comment)})
                if product:
                    print(f"✓ Found product using ObjectId conversion: {product.get('name')}")
                else:
                    print("✗ Still no match with ObjectId conversion")
            except Exception as e:
                print(f"✗ Cannot convert to ObjectId: {e}")
        
        # Show what product IDs actually look like
        print("\nActual product _id samples:")
        for product in products_collection.find({}).limit(3):
            print(f"  {product.get('_id')} (type: {type(product.get('_id'))})")

# Check for comments with actual text
print("\n4. COMMENT TEXT ANALYSIS")
print("-" * 60)

comments_with_text = list(comments_collection.find({'comment': {'$exists': True, '$ne': ''}}))
print(f"Comments with text: {len(comments_with_text)}")

if comments_with_text:
    print("\nSample comment texts:")
    for i, comment in enumerate(comments_with_text[:3], 1):
        text = comment.get('comment', '')
        print(f"  {i}. {text[:100]}{'...' if len(text) > 100 else ''}")

# Summary
print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

issues = []

if total_comments == 0:
    issues.append("❌ No comments in database")
elif len(comments_with_text) == 0:
    issues.append("❌ Comments exist but have no text")

if total_products == 0:
    issues.append("❌ No products in database")

if total_comments > 0 and total_products > 0:
    # Check ID type mismatch
    sample_comment = comments_collection.find_one({})
    sample_product = products_collection.find_one({})
    
    comment_id_type = type(sample_comment.get('productId'))
    product_id_type = type(sample_product.get('_id'))
    
    if comment_id_type != product_id_type:
        issues.append(f"⚠️  ID type mismatch: comments use {comment_id_type.__name__}, products use {product_id_type.__name__}")

if not issues:
    print("✓ All checks passed! Database looks good.")
else:
    print("Issues found:")
    for issue in issues:
        print(f"  {issue}")

print("\n" + "=" * 60)
