# Disable useless provides ('_speedups.so' and similar)
%define __noautoprov '_.*\.so'

%define shortname simplejson

Name:           python-%{shortname}
Version:        3.6.5
Release:        1
Summary:        Simple, fast, extensible JSON encoder/decoder for Python
Group:          Development/Python
License:        MIT
URL:            http://undefined.org/python/#simplejson
Source0:        http://pypi.python.org/packages/source/s/simplejson/simplejson-%{version}.tar.gz
BuildRequires:	python-distribute
BuildRequires:	python-sphinx
BuildRequires:	pkgconfig(python)

%description
simplejson is a simple, fast, complete, correct and extensible JSON
(http://json.org) encoder and decoder for Python 2.3+. It is pure Python code
with no dependencies, but includes an optional C extension for a serious speed
boost.

simplejson was formerly known as simple_json, but changed its name to comply
with PEP 8 module naming guidelines.

The encoder may be subclassed to provide serialization in any kind of
situation, without any special support by the objects to be serialized
(somewhat like pickle).

The decoder can handle incoming JSON strings of any specified encoding (UTF-8
by default).

%package -n python2-simplejson
Summary:        Simple, fast, extensible JSON encoder/decoder for Python3
Group:          Development/Python

%description -n python2-simplejson
simplejson is a simple, fast, complete, correct and extensible JSON
<http://json.org> encoder and decoder for Python3.3+ It is pure
Python code with no dependencies, but includes an optional C extension for a
serious speed boost.

%prep
%setup -q -n %{shortname}-%{version}
cp -a . %{py2dir}

%build
pushd %{py2dir}
%{__python2} setup.py build
popd
python setup.py build
./scripts/make_docs.py

%install
python setup.py install -O1 --skip-build --root %{buildroot} --install-purelib=%{py_platsitedir}
rm docs/.buildinfo
rm docs/.nojekyll

pushd %{py2dir}
%{__python2} setup.py install --skip-build --root=%{buildroot}
popd

%files
%doc docs LICENSE.txt
%{py_platsitedir}/*

%files -n python2-simplejson
%doc LICENSE.txt
%{python2_sitearch}/*
