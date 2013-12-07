%define shortname	simplejson

# Disable useless provides ('_speedups.so' and similar)
%define __noautoprov '_.*\.so'

Summary:	Simple, fast, extensible JSON encoder/decoder for Python
Name:		python-%{shortname}
Version:	3.3.0
Release:	6
Group:		Development/Python
License:	MIT
Url:		http://undefined.org/python/#simplejson
Source0:	http://pypi.python.org/packages/source/s/simplejson/%{shortname}-%{version}.tar.gz
BuildRequires:	python-distribute
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

%prep
%setup -qn %{shortname}-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot} --install-purelib=%{py_platsitedir}

%files
%{py_platsitedir}/*

