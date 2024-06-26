import os
from flask import render_template, url_for, redirect, flash, request, current_app
from werkzeug.utils import secure_filename
from .forms import ProductForm
from .models import Product
from . import db

def register_routes(app):
    @app.route('/')
    @app.route('/index')
    def index():
        return render_template('index.html')

    @app.route('/catalog')
    def catalog():
        products = Product.query.all()
        return render_template('catalog.html', products=products)

    @app.route('/new_product', methods=['GET', 'POST'])
    def new_product():
        form = ProductForm()
        if form.validate_on_submit():
            image_file = form.image.data
            if image_file:
                filename = secure_filename(image_file.filename)
                image_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
                image_file.save(image_path)
            else:
                filename = 'default.jpg'

            product = Product(
                name=form.name.data,
                description=form.description.data,
                price=form.price.data,
                image_file=filename
            )
            db.session.add(product)
            db.session.commit()
            flash('Product added successfully!', 'success')
            return redirect(url_for('catalog'))
        return render_template('new_product.html', form=form)

    @app.route('/edit_product/<int:product_id>', methods=['GET', 'POST'])
    def edit_product(product_id):
        product = Product.query.get_or_404(product_id)
        form = ProductForm(obj=product)
        if form.validate_on_submit():
            product.name = form.name.data
            product.description = form.description.data
            product.price = form.price.data

            image_file = form.image.data
            if image_file:
                filename = secure_filename(image_file.filename)
                image_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
                image_file.save(image_path)
                product.image_file = filename

            db.session.commit()
            flash('Product updated successfully!', 'success')
            return redirect(url_for('catalog'))
        return render_template('edit_product.html', form=form)

    @app.route('/delete_product/<int:product_id>', methods=['POST'])
    def delete_product(product_id):
        product = Product.query.get_or_404(product_id)
        db.session.delete(product)
        db.session.commit()
        flash('Product deleted successfully!', 'success')
        return redirect(url_for('catalog'))