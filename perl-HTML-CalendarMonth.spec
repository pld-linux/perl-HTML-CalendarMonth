#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	HTML
%define	pnam	CalendarMonth
Summary:	HTML::CalendarMonth - generating and manipulating HTML calendar months
Summary(pl):	HTML::CalendarMonth - generowanie i obrabianie miesiêcznych kalendarzy w HTML
Name:		perl-HTML-CalendarMonth
Version:	1.09
Release:	1
# same as perl
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ef6c4b2167265e47e08dac467832b2e7
%if %{with tests}
BuildRequires:	perl-Date-Calc
BuildRequires:	perl-Date-Manip
BuildRequires:	perl-HTML-Element-Extended
%endif
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML::CalendarMonth is a module that simplifies the rendering of a
calendar month in HTML. It is NOT a scheduling system.

Calendars are represented as HTML::Element based structures, derived
from the HTML::ElementTable class.

The module includes support for 'week of the year' numbering,
arbitrary 1st day of the week definitions, and aliasing so that you
can express any element in any language HTML can handle.

If you wish to use 'week of the year' numbering, or want to explore
dates beyond the capability of the internal Perl time functions,
then you will need Date::Calc or Date::Manip.

%description -l pl
HTML::CalendarMonth to modu³ upraszczaj±cy renderowanie miesiêcznych
kalendarzy w HTML-u. To NIE jest jest system planowania.

Kalendarze s± reprezentowane jako struktury HTML::Element,
wyprowadzone z klasy HTML::ElementTable.

Modu³ obs³uguje numerowanie tygodni w roku, dowolne definicje
pierwszego dnia tygodnia oraz aliasy, co pozwala na wyra¿anie
dowolnego elementu w dowolnym jêzyku, jaki mo¿e obs³u¿yæ HTML.

Do numerowania tygodni w roku albo obs³ugi dat spoza zakresu
obs³ugiwanego wewnêtrznie przez funkcje Perla potrzebny jest modu³
Date::Calc lub Date::Manip.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/HTML/CalendarMonth.pm
%{_mandir}/man3/*
