from django.urls import path
from . import views

urlpatterns=[
	path('', views.index),
	path('admin', views.admin),
	path('auto', views.auto),
	path('leather', views.leather),
	path('emboss', views.emboss),
	path('interiors', views.interiors),
	path('plain', views.plain),
	path('tile', views.tile),
	path('metalglass', views.metalglass),
	path('mailing', views.mailing),
	path('shop', views.shop),
	path('showrooms', views.showrooms),
	path('contact', views.contact),
	path('products', views.product),
	path('press', views.press),
	path('metalglass/<str:thing>', views.metalglasses),
	path('plain/<str:thing>', views.plains),
	path('tile/<str:thing>', views.tiles),
	path('embossed/<str:thing>', views.embossed),
	path('autos/<str:car>', views.autos),
	path('press/<str:thing>', views.pressed),
	path('CMF', views.color),
	path('CMF/stories', views.stories),
	path('media', views.media)
]