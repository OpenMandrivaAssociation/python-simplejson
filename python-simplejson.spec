# Work around incomplete debug packages
%global _empty_manifest_terminate_build 0

# Disable useless provides ('_speedups.so' and similar)
%define __noautoprov '_.*\.so'

%define module simplejson

Name:		python-simplejson
Version:	3.20.2
Release:	1
Summary:	Simple, fast, extensible JSON encoder/decoder for Python
Group:		Development/Python
License:	MIT
URL:		https://github.com/simplejson/simplejson
Source0:	https://files.pythonhosted.org/packages/source/s/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(sphinx)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
Obsoletes:	python2-simplejson = %{EVRD}

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
%autosetup -n %{module}-%{version} -p1
# Remove bundled egg-info
rm -rf %{module}.egg-info

%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{ldflags} -lpython%{py_ver}"
%py_build

%files
%doc README.rst
%license LICENSE.txt
%{py_platsitedir}/*
