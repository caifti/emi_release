Name: emi-release
Version: 3.0.0
Release: 2%{?dist}
Summary: EMI 3 Release
License: Apache Software License
Source: %{name}-%{version}.src.tgz
Vendor: EMI
Group: System Environment/Libraries
BuildArch: noarch
Requires: yum-protectbase
Requires: yum-priorities
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
#BuildRoot: %{_tmppath}/%{name}-%{version}-build


%description
EMI middleware release files

%prep
%setup -q

%build
#Nothing to build

%install
rm -rf %{buildroot}
make install prefix=%{buildroot}

%clean
rm -rf ${buildroot}

%post
if [ -f /etc/yum/pluginconf.d/priorities.conf ]; then grep -q -e "check_obsoletes" /etc/yum/pluginconf.d/priorities.conf || sed -i -e "/^\[main\]/{G;s/$/\# added by the emi-release package\\ncheck_obsoletes = 1/;}" /etc/yum/pluginconf.d/priorities.conf; fi

%postun
if [ "$1" = "0" ]; then grep -q -e "emi-release" /etc/yum/pluginconf.d/priorities.conf && sed -i '/emi-release/d;/check_obsoletes/d' /etc/yum/pluginconf.d/priorities.conf; fi

%files
%defattr(-,root,root,-)

/etc/emi-release
/etc/pki/rpm-gpg/RPM-GPG-KEY-emi
/etc/yum.repos.d/emi3-base.repo
/etc/yum.repos.d/emi3-contribs.repo
/etc/yum.repos.d/emi3-third-party.repo
/etc/yum.repos.d/emi3-updates.repo

%changelog
* Thu Mar 07 2013 Cristina Aiftimiei <aiftim@pd.infn.it>
- raise priority for Deb
* Fri Oct 19 2012 Cristina Aiftimiei <aiftim@pd.infn.it>
- first version from source
