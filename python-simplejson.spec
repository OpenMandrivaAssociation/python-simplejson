%define shortname	simplejson

Name:           python-%{shortname}
Version:        3.3.0
Release:        1
Summary:        Simple, fast, extensible JSON encoder/decoder for Python
Group:          Development/Python
License:        MIT
URL:            http://undefined.org/python/#simplejson
Source0:        http://pypi.python.org/packages/source/s/simplejson/%{shortname}-%{version}.tar.gz
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
%{__python} setup.py install -O1 --skip-build --root %{buildroot} --install-purelib=%py_platsitedir

%files
%{py_platsitedir}/*


%changelog
* Sat Jun 25 2011 Sandro Cazzaniga <kharec@mandriva.org> 2.1.6-1mdv2011.0
+ Revision: 687183
- new version 2.1.6

* Mon May 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.1.5-1
+ Revision: 662540
- update to new version 2.1.5

* Sat Feb 05 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.1.3-1
+ Revision: 636247
- update to new version 2.1.3

* Mon Nov 29 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.1.2-1mdv2011.0
+ Revision: 603074
- update to new version 2.1.2

* Fri Oct 29 2010 Michael Scherer <misc@mandriva.org> 2.1.1-2mdv2011.0
+ Revision: 589993
- rebuild for python 2.7

* Sun Apr 04 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.1.1-1mdv2010.1
+ Revision: 531329
- update to new version 2.1.1

* Sun Mar 28 2010 Sandro Cazzaniga <kharec@mandriva.org> 2.1.0-1mdv2010.1
+ Revision: 528584
- update tp 2.1.0

* Tue Jun 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.0.9-1mdv2010.0
+ Revision: 384257
- update to new version 2.0.9

* Sun Jan 11 2009 Funda Wang <fwang@mandriva.org> 2.0.7-1mdv2009.1
+ Revision: 328232
- New version 2.0.7

* Sat Dec 27 2008 Adam Williamson <awilliamson@mandriva.org> 2.0.6-1mdv2009.1
+ Revision: 319720
- fix requires / buildrequires
- rebuild with python 2.6
- new release 2.0.6

* Sat Nov 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.0.3-1mdv2009.1
+ Revision: 305881
- update to new version 2.0.3

* Thu Sep 04 2008 Jérôme Soyer <saispo@mandriva.org> 1.9.2-1mdv2009.0
+ Revision: 280563
- New version

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 1.7.3-4mdv2009.0
+ Revision: 259780
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 1.7.3-3mdv2009.0
+ Revision: 247636
- rebuild
- fix description-line-too-long
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun Oct 21 2007 Colin Guthrie <cguthrie@mandriva.org> 1.7.3-1mdv2008.1
+ Revision: 100737
- import python-simplejson


