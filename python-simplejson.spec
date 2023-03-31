# Work around incomplete debug packages
%global _empty_manifest_terminate_build 0

# Disable useless provides ('_speedups.so' and similar)
%define __noautoprov '_.*\.so'

%define shortname simplejson

Name:           python-%{shortname}
Version:	3.17.2
Release:	2
Summary:	Simple, fast, extensible JSON encoder/decoder for Python
Group:		Development/Python
License:	MIT
URL:		https://undefined.org/python/#simplejson
Source0:	https://files.pythonhosted.org/packages/98/87/a7b98aa9256c8843f92878966dc3d8d914c14aad97e2c5ce4798d5743e07/simplejson-%{version}.tar.gz
BuildRequires:	python-sphinx
BuildRequires:	pkgconfig(python)
BuildRequires:	python3dist(setuptools)
Obsoletes:	python2-simplejson

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

%prep
%autosetup -n %{shortname}-%{version} -p1

%build
python setup.py build

%install
python setup.py install -O1 --skip-build --root %{buildroot} --install-purelib=%{py_platsitedir}

%files
%doc LICENSE.txt
%{py_platsitedir}/*
