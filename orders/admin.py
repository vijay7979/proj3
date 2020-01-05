from django.contrib import admin

from .models import Pizza, Sub, Topping, Addition, Order, Pasta, Salad, DinnerPlatter

# create a relationship from addition to order
class OrderInline(admin.StackedInline):
	model = Order.additions.through
	extra = 1

# adding an addition to order from addition as opposed to vice versa
class AdditionAdmin(admin.ModelAdmin):
 	inlines = [OrderInline]

# using arrows to add additions or toppings to given order as opposed to ctrl-click
class OrderAdmin(admin.ModelAdmin):
	filter_horizontal = ("additions", "toppings",)

# Register your models here.
admin.site.register(Pizza)
admin.site.register(Sub)
admin.site.register(Topping)
admin.site.register(Addition, AdditionAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(DinnerPlatter)
