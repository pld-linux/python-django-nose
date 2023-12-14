#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Make Django tests simple and snappy
Summary(pl.UTF-8):	Testy Django jako proste i żwawe
Name:		python-django-nose
Version:	1.4.7
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/django-nose/
Source0:	https://files.pythonhosted.org/packages/source/d/django-nose/django-nose-%{version}.tar.gz
# Source0-md5:	fe386c6e218b0f7b353494329c380a79
URL:		https://pypi.org/project/django-nose/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-django
BuildRequires:	python-nose >= 1.2.1
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-django
BuildRequires:	python3-nose >= 1.2.1
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	sphinx-pdg-3
%endif
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
django-nose provides all the goodness of "nose" in your Django tests,
like:
- Testing just your apps by default, not all the standard ones that
  happen to be in INSTALLED_APPS
- Running the tests in one or more specific modules (or apps, or
  classes, or folders, or just running a specific test)
- Obviating the need to import all your tests into tests/__init__.py.
  This not only saves busy-work but also eliminates the possibility of
  accidentally shadowing test classes.
- Taking advantage of all the useful nose plugins.

%description -l pl.UTF-8
django-nose udostępnia całe dobro "nose" dla testów Django, w tym:
- testowanie domyślnie tylko własnych aplikacji, a nie tylko
  standardowych, które akurat są w INSTALLED_APPS
- uruchamianie testów w jednym lub większej liczbie określonych
  modułów (lub aplikacji, klas, katalogów, albo uruchamianie tylko
  konkretnego testu)
- uniknięcie potrzeby importowania wszystkich testów w
  tests/__init__.py; to nie tylko oszczędza pracy, ale eliminuje też
  możliwość przypadkowego przykrycia klas testowych
- korzystanie z zalet wszystkich przydatnych wtyczek nose.

%package -n python3-django-nose
Summary:	Make Django tests simple and snappy
Summary(pl.UTF-8):	Testy Django jako proste i żwawe
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-django-nose
django-nose provides all the goodness of "nose" in your Django tests,
like:
- Testing just your apps by default, not all the standard ones that
  happen to be in INSTALLED_APPS
- Running the tests in one or more specific modules (or apps, or
  classes, or folders, or just running a specific test)
- Obviating the need to import all your tests into tests/__init__.py.
  This not only saves busy-work but also eliminates the possibility of
  accidentally shadowing test classes.
- Taking advantage of all the useful nose plugins.

%description -n python3-django-nose -l pl.UTF-8
django-nose udostępnia całe dobro "nose" dla testów Django, w tym:
- testowanie domyślnie tylko własnych aplikacji, a nie tylko
  standardowych, które akurat są w INSTALLED_APPS
- uruchamianie testów w jednym lub większej liczbie określonych
  modułów (lub aplikacji, klas, katalogów, albo uruchamianie tylko
  konkretnego testu)
- uniknięcie potrzeby importowania wszystkich testów w
  tests/__init__.py; to nie tylko oszczędza pracy, ale eliminuje też
  możliwość przypadkowego przykrycia klas testowych
- korzystanie z zalet wszystkich przydatnych wtyczek nose.

%package apidocs
Summary:	API documentation for Python django-nose module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona django-nose
Group:		Documentation

%description apidocs
API documentation for Python django-nose module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona django-nose.

%prep
%setup -q -n django-nose-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
nosetests-%{py_ver} unittests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
nosetests-%{py3_ver} unittests
%endif
%endif

%if %{with doc}
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/testapp
%endif

%if %{with python3}
%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/testapp
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS.rst LICENSE README.rst changelog.rst
%{py_sitescriptdir}/django_nose
%{py_sitescriptdir}/django_nose-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-django-nose
%defattr(644,root,root,755)
%doc AUTHORS.rst LICENSE README.rst changelog.rst
%{py3_sitescriptdir}/django_nose
%{py3_sitescriptdir}/django_nose-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_static,*.html,*.js}
%endif
