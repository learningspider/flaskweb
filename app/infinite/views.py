# -*- coding:utf-8 -*-

from flask import render_template,session,redirect,url_for,flash,abort
from . import infinite

@infinite.route('/',methods=['GET','POST'])
def index():
#     form = NameForm()
#     if form.validate_on_submit():
#         #...
#         return redirect(url_for('.index'))
#     return render_template('index.html',
#                             form=form,name=session.get('name'),
#                             known=session.get('known',False),
#                             current_time=datetime.utcnow())
    #return render_template('index.html')
    return "asfsadfdsa"