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

%description
This nagios plugin provides the nessecary scripts and config files to test
 b2safe/iRODS.

%prep
%setup -q

%define _unpackaged_files_terminate_build 0 

%install

install -d %{buildroot}/%{_libexecdir}/argo-monitoring/probes/eudat-b2safe
install -d %{buildroot}/%{_sysconfdir}/nagios/plugins/eudat-b2safe
install -m 755 check_irods.sh %{buildroot}/%{_libexecdir}/argo-monitoring/probes/eudat-b2safe/check_irods.sh

%files
%dir /%{_libexecdir}/argo-monitoring
%dir /%{_libexecdir}/argo-monitoring/probes/
%dir /%{_libexecdir}/argo-monitoring/probes/eudat-b2safe

%attr(0755,root,root) /%{_libexecdir}/argo-monitoring/probes/eudat-b2safe/check_irods.sh


%post
%changelog
* Tue Jul 26 2016  Robert Verkerk <robert.verkerk@surfsara.nl> 1.0
- Initial version of b2safe nagios plugin
