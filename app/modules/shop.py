# encoding: utf-8
from app.modules import base

class shop(base):
    def render(self, template_name, **kwargs):
        super(shop, self).render("shop/" + template_name, **kwargs)

class ShopHandler(shop):
	def get(self):
		if self.get_secure_cookie('u', None) is not None:
			users = self.db.client().data
			self.render('index.html', users=users)
		else:
			self.redirect('/')
		return

class NotFoundHandler(shop):
    def get(self):
        self.write("Sorry, Page not Found.. Go <a href=\"/\">back</a>")

url_prefix = '/shop'

urls = [
    ('?', ShopHandler)
]