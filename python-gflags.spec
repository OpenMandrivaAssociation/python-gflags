%define module gflags

Name:           python-%{module}
Version:        1.4
Release:        %mkrel 1
Summary:        Commandline flags module for Python
Group:          Development/Python
License:        BSD
URL:            http://code.google.com/p/python-gflags/
Source0:        http://python-gflags.googlecode.com/files/python-gflags-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
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
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --root $RPM_BUILD_ROOT --install-purelib=%{python_sitelib}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README PKG-INFO 
%{python_sitelib}/%{module}.py*
%{python_sitelib}/python_gflags-%{version}-*egg-info
%{_bindir}/gflags2man.py

