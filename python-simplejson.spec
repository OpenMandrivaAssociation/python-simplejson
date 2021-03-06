%global debug_package %{nil}

# Disable useless provides ('_speedups.so' and similar)
%define __noautoprov '_.*\.so'

%define shortname simplejson

Name:           python-%{shortname}
Version:	3.17.2
Release:	1
Summary:        Simple, fast, extensible JSON encoder/decoder for Python
Group:          Development/Python
License:        MIT
URL:            https://undefined.org/python/#simplejson
Source0:	https://files.pythonhosted.org/packages/98/87/a7b98aa9256c8843f92878966dc3d8d914c14aad97e2c5ce4798d5743e07/simplejson-%{version}.tar.gz
BuildRequires:	python2dist(setuptools)
BuildRequires:	python-sphinx
BuildRequires:	pkgconfig(python2)
BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)

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
%{__python3} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot} --install-purelib=%{py_platsitedir}

pushd %{py2dir}
%{__python2} setup.py install --skip-build --root=%{buildroot}
popd

%files
%doc LICENSE.txt
%{py_platsitedir}/*

%files -n python2-simplejson
%doc LICENSE.txt
%{python2_sitearch}/*
