from setuptools import setup, find_packages

setup(
    name = 'django_extend_model',
    packages = find_packages(),
    version = '1.0.0',
    description = 'Decorator for extending Django models in a sane way.',
    author = 'Adam Mckaig',
    author_email = 'adam.mckaig@gmail.com',
    url = 'http://github.com/mikexstudios/django-extend-model',
    classifiers=[
        'Programming Language :: Python', 
        'Framework :: Django', 
        #'License :: OSI Approved :: BSD License',
    ]
)

