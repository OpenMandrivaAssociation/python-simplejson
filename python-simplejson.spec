%define shortname	simplejson

Name:           python-%{shortname}
Version:        2.1.1
Release:        %mkrel 1
Summary:        Simple, fast, extensible JSON encoder/decoder for Python
Group:          Development/Python
License:        MIT
URL:            http://undefined.org/python/#simplejson
Source0:        http://pypi.python.org/packages/source/s/simplejson/%{shortname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	python-setuptools
%py_requires -d

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
%setup -q -n %{shortname}-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot} --install-purelib=%py_platsitedir

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{py_platsitedir}/*
