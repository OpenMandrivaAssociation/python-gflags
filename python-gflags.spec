%define module gflags

Name:           python-%{module}
Version:        2.0
Release:        2
Summary:        Commandline flags module for Python
Group:          Development/Python
License:        BSD
URL:            http://code.google.com/p/python-gflags/
Source0:        http://python-gflags.googlecode.com/files/python-gflags-%{version}.tar.gz
BuildRequires:  python-devel
BuildRequires:  python-distribute
Buildarch:	noarch

%description
This project is the python equivalent of google-gflags, a Google commandline
flag implementation for C++. It is intended to be used in situations where a
project wants to mimic the command-line flag handling of a C++ app that uses
google-gflags, or for a Python app that, via swig or some other means, is
linked with a C++ app that uses google-gflags.

The gflags package contains a library that implements commandline flags
processing. As such it's a replacement for getopt(). It has increased
flexibility, including built-in support for Python types, and the ability to
define flags in the source file in which they're used. (This last is its major
difference from OptParse.)

%prep
%setup -q
# Fix non-executable-script error (from SUSE spec file)
sed -i '/^#!\/usr\/bin\/env python$/,+1 d' %{module}.py

%build
CFLAGS="%{optflags}" python setup.py build

%install
%{__python} setup.py install --root $RPM_BUILD_ROOT --install-purelib=%{python_sitelib}

%files
%doc AUTHORS ChangeLog COPYING README PKG-INFO 
%{python_sitelib}/%{module}.py*
%{python_sitelib}/python_gflags-%{version}-*egg-info
%{python_sitelib}/gflags_validators.py
%{_bindir}/gflags2man.py



%changelog
* Thu Feb 16 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.0-1
+ Revision: 775472
- version update 2.0

* Wed Jun 08 2011 Antoine Ginies <aginies@mandriva.com> 1.4-1
+ Revision: 683248
- import python-gflags

