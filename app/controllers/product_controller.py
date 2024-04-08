from flask import request, jsonify
from app.models import Product  
from app import mongo  
from bson import ObjectId

class ProductController:
    def get_all_products(self):
        products = list(mongo.db.products.find())
        product_list = []
        for product in products:
            product_dict = {
                'title': product['title'],
                'description': product['description'],
                'price': product['price']
            }
            product_list.append(product_dict)
        return jsonify(product_list), 200

    def get_product(self, id):
        
        try:
            product_id = ObjectId(id)
        except:
            return jsonify({'error': 'Invalid product ID format'}), 400
        
        
        product = mongo.db.products.find_one({'_id': product_id})

        
        if product:
            
            product['_id'] = str(product['_id'])
            return jsonify(product), 200
        else:
            return jsonify({'error': 'Product not found'}), 404

    def create_product(self):
        data = request.json
        product = Product(data)  
        mongo.db.products.insert_one(product.__dict__)
        return jsonify({'message': 'Product created successfully'}), 201

    def update_product(self, id):
        data = request.json
        try:
            product_id = ObjectId(id)
        except:
            return jsonify({'error': 'Invalid product ID format'}), 400

        result = mongo.db.products.update_one({'_id': product_id}, {'$set': data})
        if result.modified_count:
            return jsonify({'message': 'Product updated successfully'}), 200
        else:
            return jsonify({'error': 'Product not found'}), 404

    def delete_product(self, id):
        try:
            product_id = ObjectId(id)
        except:
            return jsonify({'error': 'Invalid product ID format'}), 400

        result = mongo.db.products.delete_one({'_id': product_id})
        if result.deleted_count:
            return jsonify({'message': 'Product deleted successfully'}), 200
        else:
            return jsonify({'error': 'Product not found'}), 404
