from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # ================================
    #     📦 روابط التطبيقات
    # ================================
    path('', include('store.urls')),        # الصفحة الرئيسية من المتجر
    path('cart/', include('cart.urls')),    # السلة والطلبات
    path('accounts/', include('accounts.urls')),  # تسجيل الدخول والمستخدمين
]
