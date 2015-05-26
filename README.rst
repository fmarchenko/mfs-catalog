=====
Catalog
=====



Quick start
-----------

1. Add "catalog" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'catalog',
    )

2. Include the catalog URLconf in your project urls.py like this::

    url(r'^catalog/', include('catalog.urls')),

3. Run `python manage.py migrate` to create the catalog models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a catalog (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/catalog/ to participate in the catalog.