from flask import Blueprint
from .controllers.product_controller import ProductController

api_bp = Blueprint('api', __name__)

product_controller = ProductController()

@api_bp.route('/products', methods=['GET'])
def get_products():
    return product_controller.get_all_products()

@api_bp.route('/products/<id>', methods=['GET'])
def get_product(id):
    return product_controller.get_product(id)

@api_bp.route('/products', methods=['POST'])
def create_product():
    return product_controller.create_product()

@api_bp.route('/products/<id>', methods=['PUT'])
def update_product(id):
    return product_controller.update_product(id)

@api_bp.route('/products/<id>', methods=['DELETE'])
def delete_product(id):
    return product_controller.delete_product(id)
