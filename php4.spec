
%define	_apache2	%(rpm -q apache-devel 2> /dev/null | grep -Eq '\\-2\\.[0-9]+\\.' && echo 1 || echo 0)

%if %{_apache2}
%define _without_recode 1
%define _without_mm 1
%endif

%ifnarch %{ix86}
%define _without_msession 1
%endif

# Conditional build:
# _with_cpdf		- with cpdf extension module
# _with_interbase	- with InterBase extension module
# _with_java		- with Java extension module
# _with_oci8		- with Oracle oci8 extension module
# _with_oracle		- with oracle extension module
# _with_sybase_ct	- with Sybase-CT extension module
# _without_domxslt	- without DOM XSLT/EXSLT support in DOM XML extension module
# _without_imap		- without IMAP extension module
# _without_ldap		- without LDAP extension module
# _without_mm		- without mm support for session storage
# _without_msession	- without msession extension module
# _without_odbc		- without ODBC extension module
# _without_openssl	- with OpenSSL support
# _without_snmp		- without SNMP extension module
# _without_recode	- without recode extension module
# _without_wddx		- without WDDX extension module
# _without_xslt		- without XSLT extension module
Summary:	The PHP HTML-embedded scripting language for use with Apache
Summary(fr):	Le langage de script embarque-HTML PHP pour Apache
Summary(pl):	Jêzyk skryptowy PHP -- u¿ywany wraz z serwerem Apache
Summary(pt_BR):	A linguagem de script PHP
Name:		php
Version:	4.2.1
Release:	4
Epoch:		3
Group:		Libraries
License:	The PHP license (see "LICENSE" file included in distribution)
Source0:	http://www.php.net/distributions/%{name}-%{version}.tar.bz2
Source1:	FAQ.%{name}
Source2:	%{name}.ini
Source3:	zend.gif
Source4:	http://www.php.net/distributions/manual/%{name}_manual_en.tar.bz2
Source5:	%{name}-module-install
Source6:	%{name}-mod_php.conf
Source7:	%{name}-cgi.ini
Source8:	%{name}-apache.ini
Patch0:		%{name}-shared.patch
Patch1:		%{name}-pldlogo.patch
Patch2:		%{name}-mysql-socket.patch
Patch3:		%{name}-mail.patch
Patch4:		%{name}-link-libs.patch
Patch5:		%{name}-fastcgi.patch
Patch6:		%{name}-no_%{name}_pcre_in_SAPI_c.patch
Patch7:		%{name}-libpq_fs_h_path.patch
Patch8:		%{name}-wddx-fix.patch
Patch9:		%{name}-cpdf-fix.patch
Patch10:	%{name}-session-fix-shared.patch
Patch11:	%{name}-hyperwave-fix.patch
Patch12:	%{name}-openssl-for-ext-only.patch
Patch13:	%{name}-java-fix.patch
Patch14:	%{name}-mcal-shared-lib.patch
Patch15:	%{name}-msession-shared-lib.patch
Patch16:	%{name}-xmlrpc-includes.patch
Patch17:	%{name}-build_modules.patch
Patch18:	%{name}-sapi-ini-file.patch
Patch19:	%{name}-apache2_broken_macro.patch
Icon:		php4.gif
URL:		http://www.php.net/
BuildRequires:	apache-devel
BuildRequires:	autoconf >= 1.4
BuildRequires:	automake >= 1.4d
BuildRequires:	bison
BuildRequires:	bzip2-devel
BuildRequires:	cracklib-devel >= 2.7-15
BuildRequires:	curl-devel
BuildRequires:	cyrus-sasl-devel
BuildRequires:	db3-devel >= 3.1.17
BuildRequires:	expat-devel
BuildRequires:	flex
%{?_with_sybase_ct:BuildRequires:	freetds-devel}
BuildRequires:	freetype-devel >= 2.0
BuildRequires:	gd-devel >= 2.0.1
BuildRequires:	gdbm-devel
BuildRequires:	gmp-devel
%{!?_without_imap:BuildRequires: imap-devel >= 1:2001-0.BETA.200107022325.2 }
%{?_with_java:BuildRequires:	jdk >= 1.1}
%{?_with_cpdf:BuildRequires:	libcpdf-devel >= 2.02r1-2}
BuildRequires:	libjpeg-devel
BuildRequires:	libltdl-devel >= 1.4
BuildRequires:	libmcal-devel
BuildRequires:	libmcrypt-devel >= 2.4.4
BuildRequires:	libpng >= 1.0.8
BuildRequires:	libtiff-devel
BuildRequires:	libtool >= 0:1.4.2-9
BuildRequires:	libxml2-devel >= 2.2.7
%{!?_without_domxslt:BuildRequires:	libxslt >= 1.0.3}
BuildRequires:	mhash-devel
BuildRequires:	ming-devel >= 0.1.0
%{!?_without_mm:BuildRequires:	mm-devel >= 1.1.3}
BuildRequires:	mnogosearch-devel < 3.2.5
BuildRequires:	mysql-devel >= 3.23.32
%{!?_without_ldap:BuildRequires: openldap-devel >= 2.0}
%if %(expr %{?_without_openssl:0}%{!?_without_openssl:1} + %{?_without_ldap:0}%{!?_without_ldap:1})
BuildRequires:	openssl-devel >= 0.9.6a
%endif
BuildRequires:	pam-devel
BuildRequires:	pdflib-devel >= 4.0.0
BuildRequires:	perl
%{!?_without_msession:BuildRequires:	phoenix-devel}
BuildRequires:	pkgconfig
BuildRequires:	postgresql-devel
BuildRequires:  postgresql-backend-devel >= 7.2
BuildRequires:	pspell-devel
%{!?_without_recode:BuildRequires:	recode-devel >= 3.5d-3}
%{!?_without_xslt:BuildRequires:	sablotron-devel}
BuildRequires:	t1lib-devel
%{!?_without_snmp:BuildRequires: ucd-snmp-devel >= 4.2.3}
%{!?_without_odbc:BuildRequires: unixODBC-devel}
BuildRequires:	xmlrpc-epi-devel
BuildRequires:	yaz-devel
BuildRequires:	zip
BuildRequires:	zlib-devel >= 1.0.9
BuildRequires:	zziplib-devel
#BuildRequires:	fastcgi-devkit
# apache 1.3 vs apache 2.0
%if %{_apache2}
PreReq:		apache >= 2.0.39
%else
PreReq:		apache(EAPI) < 2.0.0
PreReq:		apache(EAPI) >= 1.3.9
%endif
PreReq:		perl
PreReq:		%{_sbindir}/apxs
PreReq:		%{name}-common = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	phpfi
Obsoletes:	apache-mod_php

%define		_sysconfdir	/etc/php
%define		extensionsdir	%{_libdir}/php
%define		peardir		%{_datadir}/pear

%description
PHP is an HTML-embedded scripting language. PHP attempts to make it
easy for developers to write dynamically generated web pages. PHP also
offers built-in database integration for several commercial and
non-commercial database management systems, so writing a
database-enabled web page with PHP is fairly simple. The most common
use of PHP coding is probably as a replacement for CGI scripts. The
mod_php module enables the Apache web server to understand and process
the embedded PHP language in web pages. This package contains PHP
version %{version}. If you use applications which specifically rely on
PHP/FI (PHP v2 and earlier), you should instead install the PHP/FI
module contained in the phpfi package. If you're just starting with
PHP, you should install this package. You'll also need to install the
Apache web server.

%description -l fr
PHP est un langage de script embarque dans le HTM. PHP essaye de
rendre simple aux developpeurs d'ecrire des pages web generees
dynamiquement. PHP incorpore egalement une integration avec plusieurs
systemes de gestion de bases de donnees commerciaux et
non-connerciaux, qui rent facile la creation de pages web liees avec
des bases de donnees. L'utilisation la plus commune de PHP est
probablement en remplacement de scripts CGI. Le module mod_php permet
au serveur web apache de comprendre et de traiter le langage PHP
integre dans des pages web. Ce package contient PHP version %{version}.
Si vous utilisez des applications qui utilisent specifiquement PHP/FI,
vous devrez installer le module PHP/FI inclus dans le package mod_php.
Si vous debutez avec PHP, vous devriez installer ce package. Vous
aurez egalement besoin dinstaller le serveur web Apache.

%description -l pl
PHP jest jêzykiem skryptowym, którego polecenia umieszcza siê w
plikach HTML. Pakiet ten zawiera modu³ przeznaczony dla serwera HTTP
(jak np. Apache), który interpretuje te polecenia. Umo¿liwia to
tworzenie dynamicznie stron WWW. Spora czê¶æ sk³adni PHP zapo¿yczona
zosta³a z jêzyków: C, Java i Perl.

%description -l pt_BR
PHP: Preprocessador de Hipertexto versão 4 é uma linguagem script
embutida em HTML. Muito de sua sintaxe é emprestada de C, Java e Perl,
com algumas características únicas, específicas ao PHP. O objetivo da
linguagem é permitir que desenvolvedores web escrevam páginas
dinamicamente geradas de forma rápida.

%package cgi
Summary:	PHP as CGI program
Summary(pl):	PHP jako program CGI
Group:		Libraries
PreReq:		%{name}-common = %{version}

%description cgi
PHP as CGI program.

%description cgi -l pl
PHP jako program CGI.

%package common
Summary:	Common files nneded by both apache module and CGI
Summary(pl):	Wspólne pliki dla modu³u apacha i programu CGI
Group:		Libraries
Provides:	%{name}-session = %{version}
Obsoletes:	%{name}-session <= %{epoch}:%{version}-%{release}

%description common
Common files needed by both apache module and CGI.

%description common -l pl
Wspólne pliki dla modu³u apacha i programu CGI.

%package devel
Summary:	Files for PHP modules development
Summary(pl):	Pliki do kompilacji modu³ów PHP
Summary(pt_BR):	Arquivos de desenvolvimento para PHP
Group:		Development/Languages/PHP
Requires:	%{name}-common = %{version}

%description devel
Files for PHP modules development.

%description devel -l pl
Pliki potrzebne do kompilacji modu³ów PHP.

%description devel -l pt_BR
Este pacote contém arquivos usados no desenvolvimento de programas ou
módulos PHP.

%package doc
Summary:	Online manual for PHP
Summary(pl):	Dokumentacja dla PHP
Summary(pt_BR):	Manual da linguagem PHP, em formato HTML
Group:		Networking/Daemons
Obsoletes:	php-manual

%description doc
Comprehensive documentation for PHP, viewable through your web server,
too!

%description doc -l pl
Dokumentacja dla pakietu PHP. Mo¿na j± równie¿ ogl±daæ poprzez serwer
WWW.

%description doc -l pt_BR
Manual da linguagem PHP, em formato HTML.

%package pear
Summary:	PEAR - PHP Extension and Application Repository
Summary(pl):	PEAR - Rozszerzenie PHP i Repozytorium Aplikacji
Group:		Development/Languages/PHP
Requires:	%{name}-cgi = %{version}
Requires:	%{name}-pcre = %{version}
Requires:	%{name}-xml = %{version}

%description pear
PEAR - PHP Extension and Application Repository.

%description pear -l pl
PEAR (PHP Extension and Application Repository) - Rozszerzenie PHP i
Repozytorium Aplikacji.

%package bcmath
Summary:	bcmath extension module for PHP
Summary(pl):	Modu³ bcmath dla PHP
Group:		Libraries
PreReq:		%{name}-common = %{version}

%description bcmath
This is a dynamic shared object (DSO) for Apache that will add bc
style precision math functions support to PHP.

%description bcmath -l pl
Modu³ PHP umo¿liwiaj±cy korzystanie z dok³adnych funkcji
matematycznych takich jak w programie bc.

%package bzip2
Summary:	Bzip2 extension module for PHP
Summary(pl):	Modu³ bzip2 dla PHP
Group:		Libraries
PreReq:		%{name}-common = %{version}

%description bzip2
This is a dynamic shared object (DSO) for Apache that will add
compression (bzip2) support to PHP.

%description bzip2 -l pl
Modu³ PHP umo¿liwiaj±cy u¿ywanie kompresji (poprzez bibliotekê bzip2).

%package calendar
Summary:	Calendar extension module for PHP
Summary(pl):	Modu³ funkcji kalendarza dla PHP
Group:		Libraries
PreReq:		%{name}-common = %{version}

%description calendar
This is a dynamic shared object (DSO) for Apache that will add
calendar support to PHP.

%description calendar -l pl
Dynamiczny obiekt wspó³dzielony (DSO) dla Apache'a, dodaj±cy do PHP
wsparcie dla kalendarza.

%package cpdf
Summary:	cpdf extension module for PHP
Summary(pl):	Modu³ cpdf dla PHP
Group:		Libraries
PreReq:		%{name}-common = %{version}

%description cpdf
This is a dynamic shared object (DSO) for Apache that will add libcpdf
support to PHP.

%description cpdf -l pl
Modu³ PHP dodaj±cy obs³ugê biblioteki libcpdf.

%package crack
Summary:	crack extension module for PHP
Summary(pl):	Modu³ crack dla PHP
Group:		Libraries
PreReq:		%{name}-common = %{version}

%description crack
This is a dynamic shared object (DSO) for Apache that will add
cracklib support to PHP.

Warning: this is an experimental module.

%description crack -l pl
Modu³ PHP umo¿liwiaj±cy korzystanie z biblioteki cracklib.

Uwaga: to jest modu³ eksperymentalny.

%package ctype
Summary:	ctype extension module for PHP
Summary(pl):	Modu³ ctype dla PHP
Group:		Libraries
PreReq:		%{name}-common = %{version}

%description ctype
This is a dynamic shared object (DSO) for Apache that will add
ctype support to PHP.

%description crack -l pl
Modu³ PHP umo¿liwiaj±cy korzystanie z funkcji ctype.

%package curl
Summary:	curl extension module for PHP
Summary(pl):	Modu³ curl dla PHP
Group:		Libraries
PreReq:		%{name}-common = %{version}

%description curl
This is a dynamic shared object (DSO) for Apache that will add curl
support to PHP.

%description curl -l pl
Modu³ PHP umo¿liwiaj±cy korzystanie z biblioteki curl.

%package dba
Summary:	DBA extension module for PHP
Summary(pl):	Modu³ DBA dla PHP
Group:		Libraries
PreReq:		%{name}-common = %{version}

%description dba
This is a dynamic shared object (DSO) for Apache that will add
flat-file databases (DBA) support to PHP.

%description dba -l pl
Dynamiczny obiekt wspó³dzielony (DSO) dla Apache'a, dodaj±cy do PHP
wsparcie dla baz danych opartych na plikach (DBA).

%package dbase
Summary:	DBase extension module for PHP
Summary(pl):	Modu³ DBase dla PHP
Group:		Libraries
PreReq:		%{name}-common = %{version}

%description dbase
This is a dynamic shared object (DSO) for Apache that will add DBase
support to PHP.

%description dbase -l pl
Modu³ PHP ze wsparciem dla DBase.

%package dbx
Summary:	DBX extension module for PHP
Summary(pl):	Modu³ DBX dla PHP
Group:		Libraries
PreReq:		%{name}-common = %{version}

%description dbx
This is a dynamic shared object (DSO) for Apache that will add
DB abstraction layer to PHP. DBX supports odbc, mysql, pgsql, mssql,
fbsql and more.

%description dbx -l pl
Dynamiczny obiekt wspó³dzielony (DSO) dla Apache'a, dodaj±cy do PHP
warstwê abstrakcji do obs³ugi baz danych. DBX obs³uguje bazy odbc,
mysql, pgsql, mssql, fbsql i inne.

%package dio
Summary:	Direct I/O extension module for PHP
Summary(pl):	Modu³ Direct I/O dla PHP
Group:		Libraries
PreReq:		%{name}-common = %{version}

%description dio
This is a dynamic shared object (DSO) for Apache that will add
direct file I/O support to PHP.

Warning: this is an experimental module.

%description dio -l pl
Dynamiczny obiekt wspó³dzielony (DSO) dla Apache'a, dodaj±cy do PHP
obs³ugê bezpo¶rednich operacji I/O na plikach.

Uwaga: to jest modu³ eksperymentalny.

%package domxml
Summary:	DOM XML extension module for PHP
Summary(pl):	Modu³ DOM XML dla PHP
Group:		Libraries

%description domxml
This is a dynamic shared object (DSO) for Apache that will add DOM XML
support to PHP.

Warning: this is an experimental module.

%description domxml -l pl
Modu³ PHP dodaj±cy obs³ugê DOM XML.

Uwaga: to jest modu³ eksperymentalny.

%package exif
Summary:	exif extension module for PHP
Summary(pl):	Modu³ exif dla PHP
Group:		Libraries
PreReq:		%{name}-common = %{version}

%description exif
This is a dynamic shared object (DSO) for Apache that will add exif
support to PHP.

%description exif -l pl
Modu³ PHP dodaj±cy obs³ugê plików EXIF.

%package filepro
Summary:	filePro extension module for PHP
Summary(pl):	Modu³ filePro dla PHP
Group:		Libraries
PreReq:		%{name}-common = %{version}

%description filepro
This is a dynamic shared object (DSO) for Apache that will add PHP
support for read-only access to filePro databases.

%description filepro -l pl
Dynamiczny obiekt wspó³dzielony (DSO) dla Apache'a, dodaj±cy do PHP
mo¿liwo¶æ dostêpu (tylko do odczytu) do baz danych filePro.

%package ftp
Summary:	FTP extension module for PHP
Summary(pl):	Modu³ FTP dla PHP
Group:		Libraries
PreReq:		%{name}-common = %{version}

%description ftp
This is a dynamic shared object (DSO) for Apache that will add FTP
support to PHP.

%description ftp -l pl
Modu³ PHP dodaj±cy obs³ugê protoko³u FTP.

%package gd
Summary:	GD extension module for PHP
Summary:	Modu³ GD dla PHP
Group:		Libraries
PreReq:		%{name}-common = %{version}

%description gd
This is a dynamic shared object (DSO) for Apache that will add GD
support to PHP. You should install this package in addition to the
main %{name} package if you want to create and manipulate images with
PHP.

%description gd -l pl
Modu³ PHP umo¿liwiaj±cy korzystanie z biblioteki GD - do obróbki
obrazków z poziomu PHP.

%package gettext
Summary:	gettext extension module for PHP
Summary(pl):	Modu³ gettext dla PHP
Group:		Libraries
PreReq:		%{name}-common = %{version}

%description gettext
This is a dynamic shared object (DSO) for Apache that will add gettext
support to PHP.

%description gettext -l pl
Modu³ PHP dodaj±cy obs³ugê lokalizacji przez gettext.

%package gmp
Summary:	gmp extension module for PHP
Summary(pl):	Modu³ gmp dla PHP
Group:		Libraries
PreReq:		%{name}-common = %{version}

%description gmp
This is a dynamic shared object (DSO) for Apache that will add
arbitrary length number support with GNU MP library to PHP.

%description gmp -l pl
Modu³ PHP umorzliwiaj±cy korzystanie z biblioteki gmp.

%package hyperwave
Summary:	Hyperwave extension module for PHP
Summary(pl):	Modu³ Hyperwave dla PHP
Group:		Libraries
PreReq:		%{name}-common = %{version}

%description hyperwave
This is a dynamic shared object (DSO) for Apache that will add
Hyperwave support to PHP.

%description hyperwave -l pl
Modu³ PHP dodaj±cy obs³ugê Hyperwave.

%package iconv
Summary:	iconv extension module for PHP
Summary(pl):	Modu³ iconv dla PHP
Group:		Libraries
PreReq:		%{name}-common = %{version}

%description iconv
This is a dynamic shared object (DSO) for Apache that will add iconv
support to PHP.

%description iconv -l pl
Modu³ PHP dodaj±cy obs³ugê iconv.

%package imap
Summary:	IMAP extension module for PHP
Summary(pl):	Modu³ IMAP dla PHP
Summary(pt_BR):	Um módulo para aplicações PHP que usam IMAP
Group:		Libraries
PreReq:		%{name}-common = %{version}

%description imap
This is a dynamic shared object (DSO) for Apache that will add IMAP
support to PHP.

%description imap -l pl
Modu³ PHP dodaj±cy obs³ugê skrzynek IMAP.

%description imap -l pt_BR
Um módulo para aplicações PHP que usam IMAP.

%package interbase
Summary:	Interbase database module for PHP
Summary(pl):	Modu³ bazy danych Interbase dla PHP
Group:		Libraries
PreReq:		%{name}-common = %{version}
Autoreq:	false

%description interbase
This is a dynamic shared object (DSO) for Apache that will add
InterBase database support to PHP. If you need back-end support for
InterBase, you should install this package in addition to the main
%{name} package.

%description interbase -l pl
Modu³ PHP umo¿liwiaj±cy dostêp do bazy danych InterBase.

%package java
Summary:	Java extension module for PHP
Summary(pl):	Modu³ Javy dla PHP
Group:		Libraries
PreReq:		%{name}-common = %{version}

%description java
This is a dynamic shared object (DSO) for Apache that will add JAVA
support to PHP. This extension provides a simple and effective means
for creating and invoking methods on Java objects from PHP.

%description java -l pl
Modu³ PHP dodaj±cy wsparcie dla Javy. Umo¿liwia odwo³ywanie siê do
obiektów Javy z poziomu PHP.

%package ldap
Summary:	LDAP extension module for PHP
Summary(pl):	Modu³ LDAP dla PHP
Summary(pt_BR):	Um módulo para aplicações PHP que usam LDAP
Group:		Libraries
PreReq:		%{name}-common = %{version}

%description ldap
This is a dynamic shared object (DSO) for Apache that will add LDAP
support to PHP.

%description ldap -l pl
Modu³ PHP dodaj±cy obs³ugê LDAP.

%description ldap -l pt_BR
Um módulo para aplicações PHP que usam LDAP.
%package mbstring
Summary:	mbstring extension module for PHP
Summary(pl):	Modu³ mbstring dla PHP
Group:		Libraries
PreReq:		%{name}-common = %{version}

%description mbstring
This is a dynamic shared object (DSO) for Apache that will add
multibyte string support to PHP.

%description mbstring -l pl
Modu³ PHP dodaj±cy obs³ugê ci±gów znaków wielobajtowych.

%package mcal
Summary:	mcal extension module for PHP
Summary(pl):	Modu³ mcal dla PHP
Group:		Libraries
PreReq:		%{name}-common = %{version}

%description mcal
This is a dynamic shared object (DSO) for Apache that will add mcal
(Modular Calendar Access Library) support to PHP.

%description mcal -l pl
Modu³ PHP umo¿liwiaj±cy korzystanie z biblioteki mcal (daj±cej dostêp
do kalendarzy).

%package mcrypt
Summary:	mcrypt extension module for PHP
Summary(pl):	Modu³ mcrypt dla PHP
Group:		Libraries
PreReq:		%{name}-common = %{version}

%description mcrypt
This is a dynamic shared object (DSO) for Apache that will add mcrypt
support to PHP.

%description mcrypt -l pl
Modu³ PHP dodaj±cy mo¿liwo¶æ szyfrowania poprzez bibliotekê mcrypt.

%package mhash
Summary:	mhash extension module for PHP
Summary(pl):	Modu³ mhash dla PHP
Group:		Libraries
PreReq:		%{name}-common = %{version}

%description mhash
This is a dynamic shared object (DSO) for Apache that will add mhash
support to PHP.

%description mhash -l pl
Modu³ PHP udostêpniaj±cy funkcje mieszaj±ce z biblioteki mhash.

%package ming
Summary:	ming extension module for PHP
Summary(pl):	Modu³ ming dla PHP
Group:		Libraries
PreReq:		%{name}-common = %{version}

%description ming
This is a dynamic shared object (DSO) for Apache that will add ming
(Flash - .swf files) support to PHP.

%description ming -l pl
Modu³ PHP dodaj±cy obs³ugê plików Flash (.swf) poprzez bibliotekê
ming.

%package mnogosearch
Summary:	mnoGoSearch extension module for PHP
Summary(pl):	Modu³ mnoGoSearch dla PHP
Group:		Libraries
PreReq:		%{name}-common = %{version}

%description mnogosearch
This is a dynamic shared object (DSO) for Apache that will allow
you to access mnoGoSearch free search engine in PHP.

%description mnogosearch -l pl
Modu³ PHP dodaj±cy pozwalaj±cy na dostêp do wolnodostêpnego silnika
wyszukiwarki mnoGoSearch.

%package msession
Summary:	msession extension module for PHP
Summary(pl):	Modu³ msession dla PHP
Group:		Libraries
PreReq:		%{name}-common = %{version}

%description msession
This is a dynamic shared object (DSO) for Apache that will allow
you to use msession in PHP. msession is a high speed session daemon
which can run either locally or remotely. It is designed to provide
consistent session management for a PHP web farm.

%description msession -l pl
Modu³ PHP dodaj±cy umo¿liwiaj±cy korzystanie z demona msession. Jest
to demon szybkiej obs³ugi sesji, który mo¿e dzia³aæ lokalnie lub na
innej maszynie. S³u¿y do zapewniania spójnej obs³ugi sesji dla farmy
serwerów.

%package mysql
Summary:	MySQL database module for PHP
Summary(pl):	Modu³ bazy danych MySQL dla PHP
Summary(pt_BR):	Um módulo para aplicações PHP que usam bancos de dados MySQL
Group:		Libraries
PreReq:		%{name}-common = %{version}

%description mysql
This is a dynamic shared object (DSO) for Apache that will add MySQL
database support to PHP. If you need back-end support for MySQL, you
should install this package in addition to the main %{name} package.

%description mysql -l pl
Modu³ PHP umo¿liwiaj±cy dostêp do bazy danych MySQL.

%description mysql -l pt_BR
Um módulo para aplicações PHP que usam bancos de dados MySQL.

%package oci8
Summary:	Oracle 8 database module for PHP
Summary(pl):	Modu³ bazy danych Oracle 8 dla PHP
Group:		Libraries
PreReq:		%{name}-common = %{version}
Autoreq:	false

%description oci8
This is a dynamic shared object (DSO) for Apache that will add Oracle
7 and Oracle 8 database support to PHP through Oracle8 Call-Interface
(OCI8).

%description oci8 -l pl
Modu³ PHP umo¿liwiaj±cy dostêp do bazy danych Oracle 7 i Oracle 8
poprzez interfejs Oracle8 Call-Interface (OCI8).

%package odbc
Summary:	ODBC extension module for PHP
Summary(pl):	Modu³ ODBC dla PHP
Summary(pt_BR):	Um módulo para aplicações PHP que usam bases de dados ODBC
Group:		Libraries
PreReq:		%{name}-common = %{version}
Requires:	unixODBC >= 2.1.1-3

%description odbc
This is a dynamic shared object (DSO) for Apache that will add ODBC
support to PHP.

%description odbc -l pl
Modu³ PHP ze wsparciem dla ODBC.

%description odbc -l pt_BR
Um módulo para aplicações PHP que usam ODBC.

%package openssl
Summary:	OpenSSL extension module for PHP
Summary(pl):	Modu³ OpenSSL dla PHP
Group:		Libraries
PreReq:		%{name}-common = %{version}

%description openssl
This is a dynamic shared object (DSO) for Apache that will add OpenSSL
support to PHP.

Warning: this is an experimental module.

%description openssl -l pl
Modu³ PHP umo¿liwiaj±cy korzystanie z biblioteki OpenSSL.

Uwaga: to jest modu³ eksperymentalny.

%package oracle
Summary:	Oracle 7 database module for PHP
Summary(pl):	Modu³ bazy danych Oracle 7 dla PHP
Group:		Libraries
PreReq:		%{name}-common = %{version}
Autoreq:	false

%description oracle
This is a dynamic shared object (DSO) for Apache that will add Oracle
7 database support to PHP.

%description oracle -l pl
Modu³ PHP umo¿liwiaj±cy dostêp do bazy danych Oracle 7.

%package overload
Summary:	Overload extension module for PHP
Summary(pl):	Modu³ Overload dla PHP
Group:		Libraries
PreReq:		%{name}-common = %{version}

%description overload
This is a dynamic shared object (DSO) for Apache that will add
user-space object overloading support to PHP.

Warning: this is an experimental module.

%description overload -l pl
Modu³ PHP umo¿liwiaj±cy przeci±¿anie obiektów.

Uwaga: to jest modu³ eksperymentalny.

%package pcntl
Summary:	Process Control extension module for PHP
Summary(pl):	Modu³ Process Control dla PHP
Group:		Libraries
PreReq:		%{name}-common = %{version}

%description pcntl
This is a dynamic shared object (DSO) for Apache that will add process
spawning and control support to PHP. It supports functions like
fork(), waitpid(), signal() etc.

Warning: this is an experimental module. Also, don't use it in
webserver environment!

%description pcntl -l pl
Modu³ PHP umo¿liwiaj±cy tworzenie nowych procesów i kontrolê nad nimi.
Obs³uguje funkcje takie jak fork(), waitpid(), signal() i podobne.

Uwaga: to jest modu³ eksperymentalny. Ponadto nie jest przeznaczony do
u¿ywania z serwerem WWW - nie próbuj tego!

%package pcre
Summary:	PCRE extension module for PHP
Summary(pl):	Modu³ PCRE dla PHP
Group:		Libraries
PreReq:		%{name}-common = %{version}

%description pcre
This is a dynamic shared object (DSO) for Apache that will add Perl
Compatible Regular Expression support to PHP.

%description pcre -l pl
Modu³ PHP umo¿liwiaj±cy korzystanie z perlowych wyra¿eñ regularnych
(Perl Compatible Regular Expressions)

%package pdf
Summary:	libPDF module for PHP
Summary(pl):	Modu³ do tworzenia plików PDF dla PHP
Group:		Libraries
PreReq:		%{name}-common = %{version}
PreReq:		pdflib

%description pdf
This is a dynamic shared object (DSO) for Apache that will add PDF
support to PHP.

%description pdf -l pl
Modu³ PHP umo¿liwiaj±cy tworzenie plików PDF. Wykorzystuje bibliotekê
pdflib.

%package pgsql
Summary:	PostgreSQL database module for PHP
Summary(pl):	Modu³ bazy danych PostgreSQL dla PHP
Group:		Libraries
PreReq:		%{name}-common = %{version}

%description pgsql
This is a dynamic shared object (DSO) for Apache that will add
PostgreSQL database support to PHP. If you need back-end support for
PostgreSQL, you should install this package in addition to the main
%{name} package.

%description pgsql -l pl
Modu³ PHP umo¿liwiaj±cy dostêp do bazy danych PostgreSQL.

%description pgsql -l pt_BR
Um módulo para aplicações PHP que usam bancos de dados postgresql.

%package posix
Summary:	POSIX extension module for PHP
Summary(pl):	Modu³ POSIX dla PHP
Group:		Libraries
PreReq:		%{name}-common = %{version}

%description posix
This is a dynamic shared object (DSO) for Apache that will add POSIX
functions support to PHP.

%description posix -l pl
Modu³ PHP umo¿liwiaj±cy korzystanie z funkcji POSIX.

%package pspell
Summary:	pspell extension module for PHP
Summary(pl):	Modu³ pspell dla PHP
Group:		Libraries
PreReq:		%{name}-common = %{version}

%description pspell
This is a dynamic shared object (DSO) for Apache that will add pspell
support to PHP. It allows to check the spelling of a word and offer
suggestions.

%description pspell -l pl
Modu³ PHP umo¿liwiaj±cy korzystanie z pspella. Pozwala on na
sprawdzanie pisowni s³owa i sugerowanie poprawek.

%package recode
Summary:	recode extension module for PHP
Summary(pl):	Modu³ recode dla PHP
Group:		Libraries
PreReq:		%{name}-common = %{version}
Requires:	recode >= 3.5d-3

%description recode
This is a dynamic shared object (DSO) for Apache that will add recode
support to PHP.

%description recode -l pl
Modu³ PHP dodaj±cy mo¿liwo¶æ konwersji kodowania plików (poprzez
bibliotekê recode).

%package session
Summary:	session extension module for PHP
Summary(pl):	Modu³ session dla PHP
Group:		Libraries
PreReq:		%{name}-common = %{version}

%description session
This is a dynamic shared object (DSO) for Apache that will add session
support to PHP.

%description session -l pl
Modu³ PHP dodaj±cy obs³ugê sesji.

%package shmop
Summary:	Shared Memory Operations extension module for PHP
Summary(pl):	Modu³ shmop dla PHP
Group:		Libraries
PreReq:		%{name}-common = %{version}

%description shmop
This is a dynamic shared object (DSO) for Apache that will add
Shared Memory Operations support to PHP.

Warning: this is an experimental module.

%description shmop -l pl
Modu³ PHP umo¿liwiaj±cy korzystanie z pamiêci dzielonej.

Uwaga: to jest modu³ eksperymentalny.

%package snmp
Summary:	SNMP extension module for PHP
Summary(pl):	Modu³ SNMP dla PHP
Group:		Libraries
PreReq:		%{name}-common = %{version}

%description snmp
This is a dynamic shared object (DSO) for Apache that will add SNMP
support to PHP.

%description snmp -l pl
Modu³ PHP dodaj±cy obs³ugê SNMP.

%package sockets
Summary:	sockets extension module for PHP
Summary(pl):	Modu³ socket dla PHP
Group:		Libraries
PreReq:		%{name}-common = %{version}

%description sockets
This is a dynamic shared object (DSO) for Apache that will add sockets
support to PHP.

Warning: this is an experimental module.

%description sockets -l pl
Modu³ PHP dodaj±cy obs³ugê gniazdek.

Uwaga: to jest modu³ eksperymentalny.

%package sybase-ct
Summary:	Sybase-CT extension module for PHP
Summary(pl):	Modu³ Sybase-CT dla PHP
Group:		Libraries
PreReq:		%{name}-common = %{version}

%description sybase-ct
This is a dynamic shared object (DSO) for Apache that will add
Sybase and MS SQL databases support through CT-lib to PHP.

%description sybase-ct -l pl
Modu³ PHP dodaj±cy obs³ugê baz danych Sybase oraz MS SQL poprzez
CT-lib.

%package sysvsem
Summary:	SysV sem extension module for PHP
Summary(pl):	Modu³ SysV sem dla PHP
Group:		Libraries
PreReq:		%{name}-common = %{version}

%description sysvsem
This is a dynamic shared object (DSO) for Apache that will add SysV
semafores support to PHP.

%description sysvsem -l pl
Modu³ PHP umo¿liwiaj±cy korzystanie z semaforów SysV.

%package sysvshm
Summary:	SysV shm extension module for PHP
Summary(pl):	Modu³ SysV shm dla PHP
Group:		Libraries
PreReq:		%{name}-common = %{version}

%description sysvshm
This is a dynamic shared object (DSO) for Apache that will add SysV
Shared Memory support to PHP.

%description sysvshm -l pl
Modu³ PHP umo¿liwiaj±cy korzystanie z pamiêci dzielonej SysV.

%package wddx
Summary:	wddx extension module for PHP
Summary(pl):	Modu³ wddx dla PHP
Group:		Libraries
PreReq:		%{name}-common = %{version}
PreReq:		%{name}-session = %{version}

%description wddx
This is a dynamic shared object (DSO) for Apache that will add wddx
support to PHP.

%description wddx -l pl
Modu³ PHP umo¿liwiaj±cy korzystanie z wddx.

%package xml
Summary:	XML extension module for PHP
Summary(pl):	Modu³ XML dla PHP
Group:		Libraries
PreReq:		%{name}-common = %{version}

%description xml
This is a dynamic shared object (DSO) for Apache that will add XML
support to PHP. This extension lets you create XML parsers and then
define handlers for different XML events. If you want to be able to
parse XML documents you should install this package in addition to the
main %{name} package.

%description xml -l pl
Modu³ PHP umo¿liwiaj±cy parsowanie plików XML i obs³ugê zdarzeñ
zwi±zanych z tymi plikami.

%package xmlrpc
Summary:	xmlrpc extension module for PHP
Summary(pl):	Modu³ xmlrpc dla PHP
Group:		Libraries
PreReq:		%{name}-common = %{version}

%description xmlrpc
This is a dynamic shared object (DSO) for Apache that will add XMLRPC
support to PHP.

Warning: this is an experimental module.

%description xmlrpc -l pl
Modu³ PHP dodaj±cy obs³ugê XMLRPC.

Uwaga: to jest modu³ eksperymentalny.

%package xslt
Summary:	xslt extension module for PHP
Summary(pl):	Modu³ xslt dla PHP
Group:		Libraries
PreReq:		%{name}-common = %{version}

%description xslt
This is a dynamic shared object (DSO) for Apache that will add xslt
support to PHP.

%description xslt -l pl
Modu³ PHP umo¿liwiaj±cy korzystanie z technologii xslt.

%package yaz
Summary:	yaz extension module for PHP
Summary(pl):	Modu³ yaz dla PHP
Group:		Libraries
PreReq:		%{name}-common = %{version}

%description yaz
This is a dynamic shared object (DSO) for Apache that will add yaz
support to PHP. yaz toolkit implements the Z39.50 protocol for
information retrieval.

%description yaz -l pl
Modu³ PHP umo¿liwiaj±cy korzystanie z yaz - implementacji protoko³u
Z39.50 s³u¿±cego do pozyskiwania informacji.

%package yp
Summary:	NIS (yp) extension module for PHP
Summary(pl):	Modu³ NIS (yp) dla PHP
Group:		Libraries
PreReq:		%{name}-common = %{version}

%description yp
This is a dynamic shared object (DSO) for Apache that will add NIS
(Yellow Pages) support to PHP.

%description yp -l pl
Dynamiczny obiekt wspó³dzielony (DSO) dla Apache'a, dodaj±cy do PHP
wsparcie dla NIS (Yellow Pages).

%package zip
Summary:	zip extension module for PHP
Summary(pl):	Modu³ zip dla PHP
Group:		Libraries
PreReq:		%{name}-common = %{version}

%description zip
This is a dynamic shared object (DSO) for Apache that will add
ZZipLib (read-only access to ZIP archives) support to PHP.

%description zip -l pl
Modu³ PHP umo¿liwiaj±cy korzystanie z bibliotekli ZZipLib
(pozwalaj±cej na odczyt archiwów ZIP).

%package zlib
Summary:	Zlib extension module for PHP
Summary(pl):	Modu³ zlib dla PHP
Group:		Libraries
PreReq:		%{name}-common = %{version}

%description zlib
This is a dynamic shared object (DSO) for Apache that will add
compression (zlib) support to PHP.

%description zlib -l pl
Modu³ PHP umo¿liwiaj±cy u¿ywanie kompresji (poprzez bibliotekê zlib).

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1

install -d manual
bzip2 -dc %{SOURCE4} | tar -xf - -C manual

%build
CFLAGS="%{rpmcflags} -DEAPI=1 -I%{_prefix}/X11R6/include"
EXTENSION_DIR="%{extensionsdir}"; export EXTENSION_DIR
./buildconf
%{__libtoolize}
aclocal
autoconf
#for i in cgi fastcgi apxs ; do
for i in cgi apxs ; do
%configure \
	`[ $i = cgi ] && echo --enable-discard-path` \
	`[ $i = fastcgi ] && echo --enable-discard-path --with-fastcgi=%{_prefix}` \
%if %{_apache2}	
	`[ $i = apxs ] && echo --with-apxs2=%{_sbindir}/apxs` \
%else
	`[ $i = apxs ] && echo --with-apxs=%{_sbindir}/apxs` \
%endif	
	--with-config-file-path=%{_sysconfdir} \
	--with-exec-dir=%{_bindir} \
	--%{!?debug:dis}%{?debug:en}able-debug \
	--enable-bcmath=shared \
	--enable-calendar=shared \
	--disable-cli \
	--enable-ctype=shared \
	--enable-dba=shared \
	--enable-dbx=shared \
	--enable-dio=shared \
	--enable-exif=shared \
	--enable-ftp=shared \
	--enable-gd-native-ttf \
	--enable-magic-quotes \
	--enable-mbstring=shared --disable-mbstr-enc-trans --enable-mbregex \
	--enable-overload=shared \
	--disable-pcntl \
	--enable-posix=shared \
	--enable-session \
	--enable-shared \
	--enable-shmop=shared \
	--enable-sysvsem=shared \
	--enable-sysvshm=shared \
	--enable-track-vars \
	--enable-trans-sid \
	--enable-safe-mode \
	--enable-sockets=shared \
	--enable-ucd-snmp-hack \
	%{!?_without_wddx:--enable-wddx=shared} \
	--enable-xml=shared \
	%{!?_without_xslt:--enable-xslt=shared} \
	--enable-yp=shared \
	--with-bz2=shared \
	%{?_with_cpdf:--with-cpdflib=shared} \
	--with-crack=shared \
	--with-curl=shared \
	--without-db2 \
	--with-db3 \
	--with-dbase=shared \
	--with-dom=shared \
	%{!?_without_libxslt:--with-dom-xslt=shared --with-dom-exslt=shared} \
	--with-expat-dir=shared,/usr \
	--with-iconv=shared \
	--with-filepro=shared \
	--with-freetype-dir=shared \
	--with-gettext=shared \
	--with-gd=shared \
	--with-gdbm \
	--with-gmp=shared \
	--with-hyperwave=shared \
	%{!?_without_imap:--with-imap=shared --with-imap-ssl} \
	%{?_with_interbase:--with-interbase=shared} \
	%{?_with_java:--with-java} \
	--with-jpeg-dir=shared,/usr \
	%{!?_without_ldap:--with-ldap=shared} \
	--with-mcal=shared,/usr \
	--with-mcrypt=shared \
	--with-mhash=shared \
	--with-ming=shared \
	%{!?_without_mm:--with-mm} \
	--with-mnogosearch=shared,/usr \
	%{!?_without_msession:--with-msession=shared} \
	--with-mysql=shared,/usr \
	--with-mysql-sock=/var/lib/mysql/mysql.sock \
	%{?_with_oci8:--with-oci8=shared} \
	%{!?_without_openssl:--with-openssl=shared} \
	%{?_with_oracle:--with-oracle=shared} \
	--with-pcre-regex=shared \
	--with-pdflib=shared \
	--with-pear=%{peardir} \
	--with-pgsql=shared,/usr \
	--with-png-dir=shared,/usr \
	--with-pspell=shared \
	%{!?_without_recode:--with-recode=shared} \
	--with-regex=php \
	--with-sablot-js=shared,no \
	%{!?_without_snmp:--with-snmp=shared} \
	%{?_with_sybase_ct:--with-sybase-ct=shared,/usr} \
	--with-t1lib=shared \
	--with-tiff-dir=shared,/usr \
	%{!?_without_odbc:--with-unixODBC=shared} \
	--with-xmlrpc=shared,/usr \
	%{!?_without_xslt:--with-xslt-sablot=shared} \
	--with-yaz=shared \
	--with-zip=shared \
	--with-zlib=shared \
	--with-zlib-dir=shared
done

# for now session_mm doesn't work with shared session module...
# --enable-session=shared
# %{?_without_mm:--with-mm=shared,no}%{!?_without_mm:--with-mm=shared}

# TODO --with-pspell=/usr,shared (pspell missing)
#	--with-qtdom=shared

%{__make}
%{__make} CFLAGS="%{rpmcflags} -DDISCARD_PATH=1" -C sapi/cgi

# Kill -rpath from php binary and libphp4.so
perl -pi -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
perl -pi -e 's|^runpath_var=.*|runpath_var=|g' libtool
%{__make} CFLAGS="%{rpmcflags} -DDISCARD_PATH=1" php

perl -pi -e 's|^hardcode_into_libs=.*|hardcode_into_libs=no|g' libtool
rm libphp4.la ; %{__make} libphp4.la

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/{php,apache},%{_sysconfdir}/{apache,cgi}} \
	$RPM_BUILD_ROOT/home/httpd/icons \
	$RPM_BUILD_ROOT{%{_sbindir},%{_bindir}} \
	$RPM_BUILD_ROOT/var/run/php \
	$RPM_BUILD_ROOT/etc/httpd/httpd.conf

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT \
	INSTALL_IT="install libs/libphp4.so $RPM_BUILD_ROOT%{_libdir}/apache/ ; install libs/libphp_common*.so.*.*.* $RPM_BUILD_ROOT%{_libdir}"

%{?_with_java:install ext/java/php_java.jar $RPM_BUILD_ROOT%{_libdir}}

install .libs/php $RPM_BUILD_ROOT%{_bindir}/php

install %{SOURCE2}		$RPM_BUILD_ROOT%{_sysconfdir}/php.ini
install %{SOURCE7} %{SOURCE8} $RPM_BUILD_ROOT%{_sysconfdir}
install %{SOURCE3} php.gif $RPM_BUILD_ROOT/home/httpd/icons
install %{SOURCE5} $RPM_BUILD_ROOT%{_sbindir}
install %{SOURCE6} $RPM_BUILD_ROOT/etc/httpd/httpd.conf/70_mod_php.conf

install %{SOURCE1} .

mv -f Zend/LICENSE{,.Zend}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%if ! %{_apache2}
perl -pi -e 's|^#AddType application/x-httpd-php \.php|AddType application/x-httpd-php .php|' \
	/etc/httpd/httpd.conf
%{_sbindir}/apxs -e -a -n php4 %{_pkglibdir}/libphp4.so 1>&2
%endif
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
fi

%if %{_apache2}
%postun
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi
%else
%preun
if [ "$1" = "0" ]; then
	%{_sbindir}/apxs -e -A -n php4 %{_pkglibdir}/libphp4.so 1>&2
	perl -pi -e \
		's|^AddType application/x-httpd-php \.php|#AddType application/x-httpd-php .php|' \
		/etc/httpd/httpd.conf
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi
%endif

%post	common -p /sbin/ldconfig
%postun	common -p /sbin/ldconfig

%post bcmath
%{_sbindir}/php-module-install install bcmath %{_sysconfdir}/php.ini

%preun bcmath
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove bcmath %{_sysconfdir}/php.ini
fi

%post bzip2
%{_sbindir}/php-module-install install bz2 %{_sysconfdir}/php.ini

%preun bzip2
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove bz2 %{_sysconfdir}/php.ini
fi

%post calendar
%{_sbindir}/php-module-install install calendar %{_sysconfdir}/php.ini

%preun calendar
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove calendar %{_sysconfdir}/php.ini
fi

%post cpdf
%{_sbindir}/php-module-install install cpdf %{_sysconfdir}/php.ini

%preun cpdf
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove cpdf %{_sysconfdir}/php.ini
fi

%post crack
%{_sbindir}/php-module-install install crack %{_sysconfdir}/php.ini

%preun crack
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove crack %{_sysconfdir}/php.ini
fi

%post ctype
%{_sbindir}/php-module-install install ctype %{_sysconfdir}/php.ini

%preun ctype
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove ctype %{_sysconfdir}/php.ini
fi

%post curl
%{_sbindir}/php-module-install install curl %{_sysconfdir}/php.ini

%preun curl
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove curl %{_sysconfdir}/php.ini
fi

%post dba
%{_sbindir}/php-module-install install dba %{_sysconfdir}/php.ini

%preun dba
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove dba %{_sysconfdir}/php.ini
fi

%post dbase
%{_sbindir}/php-module-install install dbase %{_sysconfdir}/php.ini

%preun dbase
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove dbase %{_sysconfdir}/php.ini
fi

%post dbx
%{_sbindir}/php-module-install install dbx %{_sysconfdir}/php.ini

%preun dbx
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove dbx %{_sysconfdir}/php.ini
fi

%post dio
%{_sbindir}/php-module-install install dbx %{_sysconfdir}/php.ini

%preun dio
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove dbx %{_sysconfdir}/php.ini
fi

%post domxml
%{_sbindir}/php-module-install install domxml %{_sysconfdir}/php.ini

%preun domxml
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove domxml %{_sysconfdir}/php.ini
fi

%post exif
%{_sbindir}/php-module-install install exif %{_sysconfdir}/php.ini

%preun exif
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove exif %{_sysconfdir}/php.ini
fi

%post filepro
%{_sbindir}/php-module-install install filepro %{_sysconfdir}/php.ini

%preun filepro
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove filepro %{_sysconfdir}/php.ini
fi

%post ftp
%{_sbindir}/php-module-install install ftp %{_sysconfdir}/php.ini

%preun ftp
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove ftp %{_sysconfdir}/php.ini
fi

%post gd
%{_sbindir}/php-module-install install gd %{_sysconfdir}/php.ini

%preun gd
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove gd %{_sysconfdir}/php.ini
fi

%post gettext
%{_sbindir}/php-module-install install gettext %{_sysconfdir}/php.ini

%preun gettext
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove gettext %{_sysconfdir}/php.ini
fi

%post gmp
%{_sbindir}/php-module-install install gmp %{_sysconfdir}/php.ini

%preun gmp
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove gmp %{_sysconfdir}/php.ini
fi

%post hyperwave
%{_sbindir}/php-module-install install hyperwave %{_sysconfdir}/php.ini

%preun hyperwave
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove hyperwave %{_sysconfdir}/php.ini
fi

%post iconv
%{_sbindir}/php-module-install install iconv %{_sysconfdir}/php.ini

%preun iconv
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove iconv %{_sysconfdir}/php.ini
fi

%post imap
%{_sbindir}/php-module-install install imap %{_sysconfdir}/php.ini

%preun imap
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove imap %{_sysconfdir}/php.ini
fi

%post interbase
%{_sbindir}/php-module-install install interbase %{_sysconfdir}/php.ini

%preun interbase
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove interbase %{_sysconfdir}/php.ini
fi
	
%post java
%{_sbindir}/php-module-install install java %{_sysconfdir}/php.ini

%preun java
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove java %{_sysconfdir}/php.ini
fi

%post ldap
%{_sbindir}/php-module-install install ldap %{_sysconfdir}/php.ini

%preun ldap
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove ldap %{_sysconfdir}/php.ini
fi

%post mbstring
%{_sbindir}/php-module-install install mbstring %{_sysconfdir}/php.ini

%preun mbstring
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove mbstring %{_sysconfdir}/php.ini
fi

%post mcal
%{_sbindir}/php-module-install install mcal %{_sysconfdir}/php.ini

%preun mcal
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove mcal %{_sysconfdir}/php.ini
fi

%post mcrypt
%{_sbindir}/php-module-install install mcrypt %{_sysconfdir}/php.ini

%preun mcrypt
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove mcrypt %{_sysconfdir}/php.ini
fi

%post mhash
%{_sbindir}/php-module-install install mhash %{_sysconfdir}/php.ini

%preun mhash
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove mhash %{_sysconfdir}/php.ini
fi

%post ming
%{_sbindir}/php-module-install install ming %{_sysconfdir}/php.ini

%preun ming
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove ming %{_sysconfdir}/php.ini
fi

%post mnogosearch
%{_sbindir}/php-module-install install mnogosearch %{_sysconfdir}/php.ini

%preun mnogosearch
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove mnogosearch %{_sysconfdir}/php.ini
fi

%post msession
%{_sbindir}/php-module-install install msession %{_sysconfdir}/php.ini

%preun msession
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove msession %{_sysconfdir}/php.ini
fi

%post mysql
%{_sbindir}/php-module-install install mysql %{_sysconfdir}/php.ini

%preun mysql
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove mysql %{_sysconfdir}/php.ini
fi

%post oci8
%{_sbindir}/php-module-install install oci8 %{_sysconfdir}/php.ini

%preun oci8
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove oci8 %{_sysconfdir}/php.ini
fi

%post odbc
%{_sbindir}/php-module-install install odbc %{_sysconfdir}/php.ini

%preun odbc
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove odbc %{_sysconfdir}/php.ini
fi

%post openssl
%{_sbindir}/php-module-install install openssl %{_sysconfdir}/php.ini

%preun openssl
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove openssl %{_sysconfdir}/php.ini
fi

%post oracle
%{_sbindir}/php-module-install install oracle %{_sysconfdir}/php.ini

%preun oracle
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove oracle %{_sysconfdir}/php.ini
fi

%post overload
%{_sbindir}/php-module-install install overload %{_sysconfdir}/php.ini

%preun overload
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove overload %{_sysconfdir}/php.ini
fi

%post pcntl
%{_sbindir}/php-module-install install pcntl %{_sysconfdir}/php.ini

%preun pcntl
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove pcntl %{_sysconfdir}/php.ini
fi

%post pcre
%{_sbindir}/php-module-install install pcre %{_sysconfdir}/php.ini

%preun pcre
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove pcre %{_sysconfdir}/php.ini
fi

%post pdf
%{_sbindir}/php-module-install install pdf %{_sysconfdir}/php.ini

%preun pdf
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove pdf %{_sysconfdir}/php.ini
fi

%post pgsql
%{_sbindir}/php-module-install install pgsql %{_sysconfdir}/php.ini

%preun pgsql
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove pgsql %{_sysconfdir}/php.ini
fi

%post posix
%{_sbindir}/php-module-install install posix %{_sysconfdir}/php.ini

%preun posix
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove posix %{_sysconfdir}/php.ini
fi

%post pspell
%{_sbindir}/php-module-install install pspell %{_sysconfdir}/php.ini

%preun pspell
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove pspell %{_sysconfdir}/php.ini
fi

%post recode
%{_sbindir}/php-module-install install recode %{_sysconfdir}/php.ini

%preun recode
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove recode %{_sysconfdir}/php.ini
fi

%post session
%{_sbindir}/php-module-install install session %{_sysconfdir}/php.ini

%preun session
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove session %{_sysconfdir}/php.ini
fi

%post shmop
%{_sbindir}/php-module-install install shmop %{_sysconfdir}/php.ini

%preun shmop
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove shmop %{_sysconfdir}/php.ini
fi

%post snmp
%{_sbindir}/php-module-install install snmp %{_sysconfdir}/php.ini

%preun snmp
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove snmp %{_sysconfdir}/php.ini
fi

%post sockets
%{_sbindir}/php-module-install install sockets %{_sysconfdir}/php.ini

%preun sockets
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove sockets %{_sysconfdir}/php.ini
fi

%post sybase-ct
%{_sbindir}/php-module-install install sybase_ct %{_sysconfdir}/php.ini

%preun sybase-ct
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove sybase_ct %{_sysconfdir}/php.ini
fi

%post sysvsem
%{_sbindir}/php-module-install install sysvsem %{_sysconfdir}/php.ini

%preun sysvsem
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove sysvsem %{_sysconfdir}/php.ini
fi

%post sysvshm
%{_sbindir}/php-module-install install sysvshm %{_sysconfdir}/php.ini

%preun sysvshm
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove sysvshm %{_sysconfdir}/php.ini
fi

%post wddx
%{_sbindir}/php-module-install install wddx %{_sysconfdir}/php.ini

%preun wddx
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove wddx %{_sysconfdir}/php.ini
fi

%post xml
%{_sbindir}/php-module-install install xml %{_sysconfdir}/php.ini

%preun xml
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove xml %{_sysconfdir}/php.ini
fi

%post xmlrpc
%{_sbindir}/php-module-install install xmlrpc %{_sysconfdir}/php.ini

%preun xmlrpc
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove xmlrpc %{_sysconfdir}/php.ini
fi

%post xslt
%{_sbindir}/php-module-install install xslt %{_sysconfdir}/php.ini

%preun xslt
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove xslt %{_sysconfdir}/php.ini
fi

%post yaz
%{_sbindir}/php-module-install install yaz %{_sysconfdir}/php.ini

%preun yaz
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove yaz %{_sysconfdir}/php.ini
fi

%post yp
%{_sbindir}/php-module-install install yp %{_sysconfdir}/php.ini

%preun yp
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove yp %{_sysconfdir}/php.ini
fi

%post zip
%{_sbindir}/php-module-install install zip %{_sysconfdir}/php.ini

%preun zip
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove zip %{_sysconfdir}/php.ini
fi

%post zlib
%{_sbindir}/php-module-install install zlib %{_sysconfdir}/php.ini

%preun zlib
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove zlib %{_sysconfdir}/php.ini
fi

%files
%defattr(644,root,root,755)
%if %{_apache2}
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/httpd/httpd.conf/*_mod_php.conf
%endif
%attr(755,root,root) %{_libdir}/apache/libphp4.so
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/php-apache.ini

%files cgi
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/php
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/php-cgi.ini

%files common
%defattr(644,root,root,755)
%doc CODING_STANDARDS CREDITS Zend/ZEND_CHANGES
%doc LICENSE Zend/LICENSE.Zend EXTENSIONS NEWS TODO*
%doc README.EXT_SKEL README.SELF-CONTAINED-EXTENSIONS

%dir %{_sysconfdir}
%attr(644,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/php.ini
%attr(730,root,http) %dir %verify(not group mode) /var/run/php

/home/httpd/icons/*
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_libdir}/libphp_common*.so.*.*.*
%dir %{extensionsdir}

%files devel
%defattr(644,root,root,755)
%{_includedir}/php
%{_libdir}/php/build
%attr(755,root,root) %{_bindir}/phpextdist
%attr(755,root,root) %{_bindir}/phpize
%attr(755,root,root) %{_bindir}/php-config

%files doc
%defattr(644,root,root,755)
%doc manual/*

%files bcmath
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/bcmath.so

%files bzip2
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/bz2.so

%files calendar
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/calendar.so

%if %{?_with_cpdf:1}%{!?_with_cpdf:0}
%files cpdf
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/cpdf.so
%endif

%files crack
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/crack.so

%files ctype
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/ctype.so

%files curl
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/curl.so

%files dba
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/dba.so

%files dbase
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/dbase.so

%files dbx
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/dbx.so

%files dio
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/dio.so

%files domxml
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/domxml.so

%files exif
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/exif.so

%files filepro
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/filepro.so

%files ftp
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/ftp.so

%files gd
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/gd.so

%files gettext
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/gettext.so

%files gmp
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/gmp.so

%files hyperwave
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/hyperwave.so

%files iconv
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/iconv.so

%if %{?_without_imap:0}%{!?_without_imap:1}
%files imap
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/imap.so
%endif

%if %{?_with_interbase:1}%{!?_with_interbase:0}
%files interbase
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/interbase.so
%endif

%if %{?_with_java:1}%{!?_with_java:0}
%files java
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/java.so
%{_libdir}/php_java.jar
%endif

%if %{?_without_ldap:0}%{!?_without_ldap:1}
%files ldap
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/ldap.so
%endif

%files mbstring
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/mbstring.so

%files mcal
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/mcal.so

%files mcrypt
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/mcrypt.so

%files mhash
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/mhash.so

%files ming
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/ming.so

%files mnogosearch
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/mnogosearch.so

%if %{?_without_msession:0}%{!?_without_msession:1}
%files msession
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/msession.so
%endif

%files mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/mysql.so

%if %{?_with_oci8:1}%{!?_with_oci8:0}
%files oci8
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/oci8.so
%endif

%if %{?_without_odbc:0}%{!?_without_odbc:1}
%files odbc
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/odbc.so
%endif

%if %{?_without_openssl:0}%{!?_without_odbc:1}
%files openssl
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/openssl.so
%endif

%if %{?_with_oracle:1}%{!?_with_oracle:0}
%files oracle
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/oracle.so
%endif

%files overload
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/overload.so

# disabled in 4.2.0 - it segfaults
#%files pcntl
#%defattr(644,root,root,755)
#%attr(755,root,root) %{extensionsdir}/pcntl.so

%files pcre
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/pcre.so

%files pear
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pear
%attr(755,root,root) %{_bindir}/pearize
%attr(755,root,root) %{_bindir}/phptar
%{peardir}

%files pdf
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/pdf.so

%files pgsql
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/pgsql.so

%files posix
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/posix.so

%files pspell
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/pspell.so

%if %{?_without_recode:0}%{!?_without_recode:1}
%files recode
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/recode.so
%endif

# session_mm doesn't work with shared session
#%files session
#%defattr(644,root,root,755)
#%attr(755,root,root) %{extensionsdir}/session.so

%files shmop
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/shmop.so

%if %{?_without_snmp:0}%{!?_without_snmp:1}
%files snmp
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/snmp.so
%endif

%files sockets
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/sockets.so

%if %{?_with_sybase_ct:1}%{!?_with_sybase_ct:0}
%files sybase-ct
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/sybase_ct.so
%endif

%files sysvsem
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/sysvsem.so

%files sysvshm
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/sysvshm.so

%if %{?_without_wddx:0}%{!?_without_wddx:1}
%files wddx
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/wddx.so
%endif

%files xml
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/xml.so

%files xmlrpc
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/xmlrpc.so

%if %{?_without_xslt:0}%{!?_without_xslt:1}
%files xslt
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/xslt.so
%endif

%files yaz
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/yaz.so

%files yp
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/yp.so

%files zip
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/zip.so

%files zlib
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/zlib.so
