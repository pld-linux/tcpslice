Summary:	tcpslice - extract pieces of and/or merge together pcap files
Summary(pl.UTF-8):	tcpslice - wydobywanie fragmentów i/lub łączenie plików pcap
Name:		tcpslice
Version:	1.5
Release:	1
License:	BSD
Group:		Networking/Utilities
Source0:	https://www.tcpdump.org/release/%{name}-%{version}.tar.gz
# Source0-md5:	8907e60376e629f6e6ce2255988aaf47
URL:		https://www.tcpdump.org/
BuildRequires:	autoconf >= 2.64
BuildRequires:	libnids-devel
BuildRequires:	libosip2-devel
BuildRequires:	libpcap-devel
BuildRequires:	ooh323c-devel >= 0.9.3-3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tcpslice is a program for extracting portions of packet-trace files
generated using tcpdump's -w flag. It can also be used to merge
together several such files.

%description -l pl.UTF-8
Tcpslice to program do wydobywania ragmentów plików śladów pakietów,
wygenerowanych przy użyciu flagi -w programu tcpdump. Potrafi także
łączyć kilka takich plików.

%prep
%setup -q

%build
%{__autoconf}
CPPFLAGS="%{rpmcppflags} -I/usr/include/ooh323c"
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES CREDITS README.md
%attr(755,root,root) %{_bindir}/tcpslice
%{_mandir}/man1/tcpslice.1*
