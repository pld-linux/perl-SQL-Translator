#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	SQL
%define	pnam	Translator
Summary:	SQL::Translator - manipulate structure data definitions (database schemas)
Summary(pl.UTF-8):   SQL::Translator - manipulowanie definicjami struktur danych (schematami baz danych)
Name:		perl-SQL-Translator
Version:	0.07
Release:	1
License:	GPL v2
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5e6d8be5f6256343125a130a57a3e463
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-Module-Build
%if %{with tests}
BuildRequires:	perl-Class-Base
BuildRequires:	perl-Class-Data-Inheritable >= 0.02
BuildRequires:	perl-Class-MakeMethods
BuildRequires:	perl-DBI
BuildRequires:	perl-GD
BuildRequires:	perl-GraphViz
BuildRequires:	perl-Log-Log4perl
BuildRequires:	perl-Parse-RecDescent >= 1.94
BuildRequires:	perl-Pod-Parser
BuildRequires:	perl-Spreadsheet-ParseExcel >= 0.2602
BuildRequires:	perl-Template-Toolkit >= 2.10
BuildRequires:	perl-Template-Toolkit-Plugin-Date
BuildRequires:	perl-Test-Differences
BuildRequires:	perl-Test-Exception
BuildRequires:	perl-Test-Simple >= 0.60
BuildRequires:	perl-Text-RecordParser >= 0.02
BuildRequires:	perl-XML-Writer >= 0.500
BuildRequires:	perl-XML-XPath >= 1.13
BuildRequires:	perl-YAML >= 0.39
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

%description -l pl.UTF-8
SQL::Translator to grupa modułów Perla obrabiających definicje danych
struktur (głównie schematów baz danych) na ciekawe sposoby, takie jak
konwersja między różnymi dialektami składni CREATE (np. MySQL do
Oracle), wizualizacja schematów (diagramy pseudo-ER, GraphViz i
GD), automatyczne generowanie kodu (przy użyciu Class::DBI), konwersja
plików nie będących relacyjnymi bazami danych do schematów SQL (pliki
tekstowe xSV, arkusze Excela), serializacja przetworzonych schematów
(poprzez Storable, YAML i XML), tworzenie dokumentacji (HTML i POD)
itd. Istnieje także możliwość bezpośredniej komunikacji z bazą danych
poprzez DBI w celu odpytania o struktury różnych baz.

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
