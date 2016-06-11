Name:           op-tec-release
Version:        0.0.1
Release:        1%{?dist}
Summary:        RPM Package containing my repository file and GPG Key

License:        The Unlicence
URL:            http://yum.op-ezy.co.uk/
Source0:        op-tec-release-0.0.1.tar.gz

%description
Installs the OP-TEC repo configuration file and GPG key


%prep
%setup -q


%build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/
cp -p op-tec.repo $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/
cp -p OP-TEC $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
/etc/yum.repos.d/op-tec.repo
/etc/pki/rpm-gpg/OP-TEC

%changelog
* Sat Jun 11 2016 Robert Ian Hawdon <mail@robertianhawdon.me.uk> 0.0.1
- This is the RPM for the OP-TEC repo files and GPG key required to install
