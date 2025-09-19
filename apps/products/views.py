from django.views.generic import ListView
from .models import ProductModel, ProductCategory, ProductBrand, ProductColor, ProductSize


class ProductListView(ListView):
    model = ProductModel
    template_name = "products/products.html"
    context_object_name = "products"

    def get_queryset(self):
        products = super().get_queryset()

        cat_id = self.request.GET.get("cat")
        brand_id = self.request.GET.get("brand_id")
        color_id = self.request.GET.get("color_id")
        size_id = self.request.GET.get("size_id")
        q = self.request.GET.get("q")

        if cat_id:
            products = products.filter(categories=cat_id)

        if brand_id:
            products = products.filter(brand=brand_id)

        if color_id:
            products = products.filter(products_quantity__color=color_id)

        if size_id:
            products = products.filter(products_quantity__size=size_id)

        if q:
            products = products.filter(title__icontains=q)

        return products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = ProductCategory.objects.all()
        context["brands"] = ProductBrand.objects.all()
        context["colors"] = ProductColor.objects.all()
        context["sizes"] = ProductSize.objects.all()
        return context
