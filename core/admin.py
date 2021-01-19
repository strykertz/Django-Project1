from django.contrib import admin

from .models import Produto, Cliente

admin.site.register(Produto)
admin.site.register(Cliente)

#necessária a importação de models produto para que seja visível na administração.
