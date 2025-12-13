from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# ==================================================
#   URL Patterns
# ==================================================
urlpatterns = [

    # لوحة التحكم
    path('admin/', admin.site.urls),

    # ==============================
    #   روابط التطبيقات
    # ==============================

    # الصفحة الرئيسية (المتجر)
    path('', include('store.urls')),

    # السلة والطلبات
    path('cart/', include('cart.urls')),

    # الحسابات (تسجيل / دخول / خروج)
    path('accounts/', include('accounts.urls')),
]


# ==================================================
#   دعم Media و Static أثناء التطوير
# ==================================================
if settings.DEBUG:
    # ملفات الوسائط (صور المنتجات)
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

    # ملفات static (اختياري أثناء التطوير)
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )
