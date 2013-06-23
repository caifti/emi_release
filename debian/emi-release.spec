%define topdir %(pwd)/rpmbuild
%define _topdir %{topdir}
Summary:      EMI middleware release files
Name:         NNAME
Version:      VV
Release:      RR
BuildArch:    noarch
Vendor:       EMI
Packager:     EMI Project
Group:        System Environment/Base
License:      Apache Software License
Source:       %{name}.src.tgz
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
%description
EMI middleware release files

%prep

%setup

%build
make install prefix=%{buildroot}%{prefix}

#%install
#rm -rf $RPM_BUILD_ROOT
#make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{prefix}/etc/emi-release
%{prefix}/etc/apt/sources.list.d/emi3.list
%{prefix}/etc/apt/preferences.d/emi3

%changelog
* Fri Oct 19 2012 <cristina.aiftimiei@pd.infn.it>
- Added first version
