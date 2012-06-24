#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	SQL
%define	pnam	Translator
Summary:	SQL::Translator - manipulate structure data definitions (database schemas)
Summary(pl):	SQL::Translator - manipulowanie definicjami struktur danych (schematami baz danych)
Name:		perl-SQL-Translator
Version:	0.06
Release:	1
License:	GPL v2
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e7aae659a682ddbb46bbd6b2c15a4b6e
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-Base
BuildRequires:	perl-Parse-RecDescent >= 1.94
BuildRequires:	perl-Pod-Parser
BuildRequires:	perl-Template-Toolkit >= 2.1
BuildRequires:	perl-Text-RecordParser
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SQL::Translator is a group of Perl modules that manipulate structure
data definitions (mostly database schemas) in interesting ways, such
as converting among different dialects of CREATE syntax (e.g.,
MySQL-to-Oracle), visualizations of schemas (pseudo-ER diagrams
GraphViz or GD), automatic code generation (using Class::DBI),
converting non-RDBMS files to SQL schemas (xSV text files, Excel
spreadsheets), serializing parsed schemas (via Storable, YAML and
XML), creating documentation (HTML and POD), and more. We also have
the ability to talk directly to a database through DBI to query for
the structures of several databases.

%description -l pl
SQL::Translator to grupa modu��w Perla obrabiaj�cych definicje danych
struktur (g��wnie schemat�w baz danych) na ciekawe sposoby, takie jak
konwersja mi�dzy r�nymi dialektami sk�adni CREATE (np. MySQL do
Oracle), wizualizacja schemat�w (diagramy pseudo-ER, GraphViz i
GD), automatyczne generowanie kodu (przy u�yciu Class::DBI), konwersja
plik�w nie b�d�cych relacyjnymi bazami danych do schemat�w SQL (pliki
tekstowe xSV, arkusze Excela), serializacja przetworzonych schemat�w
(poprzez Storable, YAML i XML), tworzenie dokumentacji (HTML i POD)
itd. Istnieje tak�e mo�liwo�� bezpo�redniej komunikacji z baz� danych
poprzez DBI w celu odpytania o struktury r�nych baz.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	installdirs=vendor \
	destdir=$RPM_BUILD_ROOT
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS Changes README TODO *.rdf
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/SQL/*.pm
%{perl_vendorlib}/SQL/Translator
%{perl_vendorlib}/Test/SQL/*.pm
%{_mandir}/man?/*
