Name:		nagios-plugins-eudat-b2safe
Version:	1.0
Release:	1%{?dist}
Summary:	nagios probe for b2safe

Group:		Application
License:	open BSD License
URL:		http://www.eudat.eu/b2safe
BuildArch:	noarch
Source:		%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

#BuildRequires:	
Requires:	irods-icommands

%define _whoami %(whoami)
%define _b2safehomepackaging %(pwd)
%define _b2safeNagiosPackage /usr/libexec/argo-monitoring/probes/eudat-b2safe
%define _b2safeNagiosTmp     /var/lib/argo-monitoring/eudat-b2safe
%define _b2safeNagiosConfig  /etc/nagios/plugins/eudat-b2safe

%description
This nagios plugin provides the nessecary scripts and config files to test
 b2safe/iRODS.

%prep
%setup -q

%define _unpackaged_files_terminate_build 0 

%install

install -d %{buildroot}/%{_b2safeNagiosPackage}
install -d %{buildroot}/%{_b2safeNagiosConfig}
install -m 755 check_irods.sh %{buildroot}/%{_b2safeNagiosPackage}/check_irods.sh
cp $RPM_SOURCE_DIR/*.json       %{buildroot}{_b2safeNagiosConfig}
cp $RPM_SOURCE_DIR/irods_passwd %{buildroot}{_b2safeNagiosConfig}

%files
%dir /%{_libexecdir}/argo-monitoring
%dir /%{_libexecdir}/argo-monitoring/probes/
%dir /%{_libexecdir}/argo-monitoring/probes/eudat-b2safe

# attributes on files and directory's
%attr(-,nagios,nagios)   %{_b2safeNagiosPackage}
%attr(-,nagios,nagios)   %{_b2safeNagiosTmp}
%attr(-,nagios,nagios)   %{_b2safeNagiosConfig}
%attr(750,nagios,nagios) %{_b2safeNagiosPackage}/*.sh
%attr(600,nagios,nagios) %{_b2safeNagiosConfig}/*.json
%attr(600,nagios,nagios) %{_b2safeNagiosConfig}/irods_passwd
%doc


%post
%changelog
* Tue Jul 26 2016  Robert Verkerk <robert.verkerk@surfsara.nl> 1.0
- Initial version of b2safe nagios plugin
