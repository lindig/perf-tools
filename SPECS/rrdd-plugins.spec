Name:           rrdd-plugins
Version:        1.0.0
Release:        1%{?dist}
Summary:        RRDD metrics plugins
License:        LGPL+linking exception
Group:          System/Hypervisor
URL:            https://github.com/xenserver/rrdd-plugins/
Source0:        https://github.com/xenserver/rrdd-plugins/archive/%{version}/rrdd-plugins-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml
BuildRequires:  oasis
BuildRequires:  blktap-devel
BuildRequires:  forkexecd-devel
BuildRequires:  ocaml-rrdd-plugin-devel
BuildRequires:  ocaml-xcp-idl-devel
BuildRequires:  ocaml-xen-api-libs-transitional-devel
BuildRequires:  xen-ocaml-devel
BuildRequires:  ocaml-xenops-devel
BuildRequires:  ocaml-xenstore-devel
BuildRequires:  ocaml-xcp-rrd-devel
BuildRequires:  xen-dom0-libs-devel
BuildRequires:  xen-libs-devel
Requires:       xsifstat
Requires:       xsiostat

%description
This package contains plugins registering to the RRD daemon and exposing
various metrics.

%prep
%setup -q

%build
mkdir -p %{buildroot}
DESTDIR=%{buildroot} %{__make}

%install
rm -rf %{buildroot}
DESTDIR=%{buildroot} %{__make} install

%clean
rm -rf %{buildroot}

%post
[ -x /sbin/chkconfig ] && chkconfig --add xcp-rrdd-plugins
exit 0

%preun
# Run chkconfig --del if this is an uninstall (rather than an upgrade)
[ $1 -eq 0 ] && [ -x /sbin/chkconfig ] && chkconfig --del xcp-rrdd-plugins
exit 0

%files
%defattr(-,root,root,-)
/etc/logrotate.d/xcp-rrdd-plugins
/etc/rc.d/init.d/xcp-rrdd-plugins
/etc/sysconfig/xcp-rrdd-plugins
/opt/xensource/libexec/xcp-rrdd-plugins/xcp-rrdd-iostat
/opt/xensource/libexec/xcp-rrdd-plugins/xcp-rrdd-squeezed
/opt/xensource/libexec/xcp-rrdd-plugins/xcp-rrdd-xenpm
/etc/xensource/bugtool/xcp-rrdd-plugins.xml
/etc/xensource/bugtool/xcp-rrdd-plugins/stuff.xml

%changelog
* Tue Apr 26 2016 Si Beaumont <simon.beaumont@citrix.com> - 1.0.0-1
- Update to 1.0.0

* Fri Jul 11 2014 John Else <john.else@citrix.com> - 0.1.0-1
- Initial package for planex
