# Example Krptn Integration with Django

**Note:** for multiple reasons, this example is not production ready. Please do not use this in such an environment but rather take ideas from here on how to integrate Flask and Krptn.

**Note:** in this example, the Django Admin page is not configured to work with Krptn.

Please see our [documentation for details](https://docs.krptn.dev/).

Don't forget to install Krptn & Django.

```shell
pip install -r requirements.txt
python manage.py runserver
```

Or (for Docker):

```shell
docker build -t django_example . && docker run --rm -p 8000:8000 -it django_example
```

This is an adapted version of [this tutorial](https://learndjango.com/tutorials/django-login-and-logout-tutorial).
