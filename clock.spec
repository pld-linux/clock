Summary:	A utility for querying and setting system time
Summary(pl):	Narzêdzie do odczytu i ustawiania zegara systemowego
Name:		clock
Version:	1.1
Release:	7
License:	distributable
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	%{name}-%{version}.tar.gz
Patch0:		%{name}-fix.patch
Patch1:		%{name}-fix2.patch
ExclusiveArch:	sparc alpha
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The clock utility is used to query and set system time.

%description -l pl
Narzêdzie clock s³u¿y do odczytywania i ustawiania zegara systemowego.

%prep 
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__cc} %{rpmcflags} -Wall -o clock clock-$(uname -m).c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/sbin,%{_mandir}/man8}

install clock $RPM_BUILD_ROOT/sbin
install clock.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) /sbin/clock

%{_mandir}/man8/clock.8*
