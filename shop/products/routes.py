from flask import redirect,render_template,url_for,flash,request
from shop import app,db
from .models import Brand,Category
from .forms import Addproducts


@app.route('/addbrand', methods=['GET', 'POST'])
def addbrand():
    if request.method =="POST":
        getbrand = request.form.get('brand')
        brand = Brand(name=getbrand)
        db.session.add(brand)
        flash(f'The brand {getbrand} was added to your database','success')
        db.session.commit()
        return redirect(url_for('addbrand'))
    return render_template('products/addbrand.html',brands='brands', title='Add Brand')


@app.route('/addcat', methods=['GET', 'POST'])
def addcat():
    if request.method =="POST":
        getbrand = request.form.get('category')
        cat = Category(name=getbrand)
        db.session.add(cat)
        flash(f'The category {getbrand} was added to your database','success')
        db.session.commit()
        return redirect(url_for('addcat'))
    return render_template('products/addbrand.html', title='Add Category')

@app.route('/addproduct', methods=['GET', 'POST'])
def addproduct():
    brands = Brand.query.all()
    categories = Category.query.all()
    form = Addproducts(request.form)
    return render_template('products/addproduct.html', title='Add Product',form=form, brands=brands,categories=categories)