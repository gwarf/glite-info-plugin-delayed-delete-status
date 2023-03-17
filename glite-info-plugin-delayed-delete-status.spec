Name: glite-info-plugin-delayed-delete-status
Version: 2.0.1
Release: 1%{?dist}
Summary: Updates GLUE state attributes of delayed delete entries in the Top BDII
Group: Development/Libraries
License: ASL 2.0
URL: https://github.com/EGI-Federation/glite-info-plugin-delayed-delete-status
Source: %{name}-%{version}.tar.gz
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-build

BuildRequires: rsync
BuildRequires: make
BuildRequires: python3-rpm-macros
Requires: openldap-servers
Requires: python3

%description
Updates GLUE state attributes of delayed delete entries in the Top BDII

%prep
%setup -q

%build
# Nothing to build

%install
rm -rf %{buildroot}
make install prefix=%{buildroot}

%post
touch /var/log/glite/glite-info-plugin-delayed-delete-status.log
chmod 0644 /var/log/glite/glite-info-plugin-delayed-delete-status.log
chown ldap:ldap /var/log/glite/glite-info-plugin-delayed-delete-status.log

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%dir /var/log/glite
%{_libexecdir}/glite-info-plugin-delayed-delete-status
%doc %{_docdir}/%{name}-%{version}/README.md
%doc %{_docdir}/%{name}-%{version}/AUTHORS.md
%license /usr/share/licenses/%{name}-%{version}/COPYRIGHT
%license /usr/share/licenses/%{name}-%{version}/LICENSE.txt

%changelog
* Fri Mar 17 2023 Baptiste Grenier <baptiste.grenier@egi.eu> - 2.0.1-1
- Build using AlmaLinux 8 and 9 (#7) (Baptiste Grenier)

* Fri Dec 16 2022 Baptiste Grenier <baptiste.grenier@egi.eu> - 2.0.0-1
- Import community files, setup GitHub Actions, move to python3 (#4) (Baptiste Grenier)

* Tue Nov 16 2021 Andrea Manzi <andrea.manzi@egi.eu> - 1.0.1-2
- Add missing dependency to openldap-servers

* Mon Sep 02 2013 Maria Alandes <maria.alandes.pradillo@cern.ch> - 1.0.1-1
- Fixed wrong attribute name GlueCEStatus to GlueCEStateStatus

* Fri Aug 02 2013 Maria Alandes <maria.alandes.pradillo@cern.ch> - 1.0.0-1
- Initial release
