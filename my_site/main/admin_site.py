from django.contrib.admin import AdminSite

class CustomAdminSite(AdminSite):
    site_header = "پنل مدیریت سایت"
    site_title = "سایت من"
    index_title = "به پنل مدیریت خوش آمدید"

custom_admin_site = CustomAdminSite(name='custom_admin')