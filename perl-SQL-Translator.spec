#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	SQL
%define	pnam	Translator
Summary:	SQL::Translator - manipulate structure data definitions (database schemas)
Summary(pl.UTF-8):	SQL::Translator - manipulowanie definicjami struktur danych (schematami baz danych)
Name:		perl-SQL-Translator
Version:	0.11018
Release:	2
License:	GPL v2
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/SQL/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	03db60b963836ba2d264f33d585dffb3
URL:		http://search.cpan.org/dist/SQL-Translator/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-File-ShareDir >= 1.03
BuildRequires:	perl-Class-Base
BuildRequires:	perl-Class-Data-Inheritable >= 0.02
BuildRequires:	perl-Class-MakeMethods
BuildRequires:	perl-DBI
BuildRequires:	perl-GD
BuildRequires:	perl-GraphViz
BuildRequires:	perl-JSON
BuildRequires:	perl-Log-Log4perl
BuildRequires:	perl-Moo
BuildRequires:	perl-Package-Variant >= 1.001001
BuildRequires:	perl-Parse-RecDescent >= 1.967009
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
Requires:	perl-File-ShareDir >= 1.03
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# stupid rpm... should invoke perl.req for all files at once
%define		_noautoreq	'perl(SQL::Translator.*)'

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
Oracle), wizualizacja schematów (diagramy pseudo-ER, GraphViz i GD),
automatyczne generowanie kodu (przy użyciu Class::DBI), konwersja
plików nie będących relacyjnymi bazami danych do schematów SQL (pliki
tekstowe xSV, arkusze Excela), serializacja przetworzonych schematów
(poprzez Storable, YAML i XML), tworzenie dokumentacji (HTML i POD)
itd. Istnieje także możliwość bezpośredniej komunikacji z bazą danych
poprzez DBI w celu odpytania o struktury różnych baz.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	installdirs=vendor \
	destdir=$RPM_BUILD_ROOT
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/SQL/*.pm
%{perl_vendorlib}/SQL/Translator
%{perl_vendorlib}/Test/SQL
%{perl_vendorlib}/auto/share/dist/SQL-Translator
%{_mandir}/man?/*
