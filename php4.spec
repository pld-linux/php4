#
# Conditional build:
# _with_oracle  - with oracle support 
# _with_oci8    - with oci8 support
# _with_java    - with Java support
# _with_openssl - with OpenSSL support
# _with_wddx    - with WDDX support
# _with_xslt    - with XSLT support
# _without_imap   - without IMAP support
# _without_ldap   - without LDAP support
# _without_odbc   - without ODBC support
# _without_snmp   - without SNMP support
#
Summary:	The PHP HTML-embedded scripting language for use with Apache
Summary(fr):	Le langage de script embarque-HTML PHP pour Apache
Summary(pl):	Jêzyk skryptowy PHP -- u¿ywany wraz z serwerem Apache
Name:		php
Version:	4.0.6
Release:	13
Epoch:		1
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	âÉÂÌÉÏÔÅËÉ
Group(uk):	â¦ÂÌ¦ÏÔÅËÉ
License:	The PHP license (see "LICENSE" file included in distribution)
Source0:	http://www.php.net/distributions/%{name}-%{version}.tar.gz
Source1:	FAQ.php
Source2:	%{name}.ini
Source3:	zend.gif
Source4:	http://www.php.net/distributions/manual/php_manual_en.tar.bz2
Source5:	php-module-install
Patch0:		%{name}-imap.patch
Patch1:		%{name}-mysql-socket.patch
Patch2:		%{name}-mail.patch
Patch3:		%{name}-link-libs.patch
Patch4:		%{name}-session-path.patch
Patch5:		%{name}-am_ac_lt.patch
Patch6:		%{name}-fastcgi.patch
Patch7:		%{name}-shared.patch
Patch8:		%{name}-ac250.patch
Patch9:		%{name}-pearinstall.patch
Patch10:	%{name}-pldlogo.patch
Patch11:	%{name}-libxml2.patch
Patch12:	%{name}-mailsecurity2.patch
Patch13:	%{name}-ZVAL.patch
Patch14:	%{name}-oracle9.patch
Icon:		php4.gif
URL:		http://www.php.net/
BuildRequires:	apache(EAPI)-devel
BuildRequires:	autoconf >= 1.4
BuildRequires:	automake >= 1.4d
BuildRequires:	bison
BuildRequires:	bzip2-devel
BuildRequires:	curl-devel
BuildRequires:	db3-devel >= 3.1.17
BuildRequires:	flex
BuildRequires:	gmp-devel
BuildRequires:	freetype-devel >= 2.0
BuildRequires:	gd-devel >= 2.0.1
BuildRequires:	gdbm-devel
%{!?_without_imap:BuildRequires: imap-devel >= 1:2001-0.BETA.200107022325.2 }
# I think jdk is better for java
# BuildRequires:	jdk
%{?_with_java:BuildRequires:	kaffe-devel}
BuildRequires:	libjpeg-devel
BuildRequires:	libltdl-devel >= 1.4
BuildRequires:	libmcrypt-devel >= 2.4.4
BuildRequires:	libpng >= 1.0.8
BuildRequires:	libtiff-devel
BuildRequires:	libtool >= 1.4
BuildRequires:	libxml2-devel >= 2.2.7
BuildRequires:	mhash-devel
BuildRequires:	ming-devel >= 0.1.0
BuildRequires:	mm-devel >= 1.1.3
BuildRequires:	mysql-devel >= 3.23.32
%{!?_without_ldap:BuildRequires: openldap-devel >= 2.0}
BuildRequires:	pam-devel
BuildRequires:	pdflib-devel >= 4.0.0
BuildRequires:	perl
BuildRequires:	pkgconfig
BuildRequires:	postgresql-devel
BuildRequires:	recode-devel >= 3.5d-3
BuildRequires:	t1lib-devel
%{!?_without_snmp:BuildRequires: ucd-snmp-devel >= 4.2.3}
%{!?_without_odbc:BuildRequires: unixODBC-devel}
BuildRequires:	zip
BuildRequires:	zlib-devel >= 1.0.9
#BuildRequires:	fastcgi-devkit
%if %(expr %{?_with_openssl:1}%{!?_with_openssl:0} + %{!?_without_ldap:1}%{?_without_ldap:0})
BuildRequires:	openssl-devel >= 0.9.6a
%endif
%{?_with_xslt:BuildRequires:	sablotron-devel}
%{?_with_xslt:BuildRequires:	expat-devel}
%{?_with_xslt:BuildRequires:	w3c-libwww-devel}
Prereq:		apache(EAPI) >= 1.3.9
Prereq:		perl
Prereq:		%{_sbindir}/apxs
PreReq:		%{name}-common = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	phpfi

%define		_sysconfdir	/etc/php
%define 	extensionsdir %{_libdir}/php
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
integre dans des pages web. Ce package contient PHP version
%{version}. Si vous utilisez des applications qui utilisent
specifiquement PHP/FI, vous devrez installer le module PHP/FI inclus
dans le package mod_php. Si vous debutez avec PHP, vous devriez
installer ce package. Vous aurez egalement besoin d'installer le
serveur web Apache.

%description -l pl
PHP jest jêzykiem skryptowym, którego polecenia umieszcza siê w
plikach HTML. Pakiet ten zawiera modu³ przeznaczony dla serwera HTTP
(jak np. Apache), który interpretuje te polecenia. Umo¿liwia to
tworzenie dynamicznie stron WWW. Spora czê¶æ sk³adni PHP zapo¿yczona
zosta³a z jêzyków: C, Java i Perl.

%package cgi
Summary:	PHP as CGI program
Summary(pl):	PHP jako program CGI
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	âÉÂÌÉÏÔÅËÉ
Group(uk):	â¦ÂÌ¦ÏÔÅËÉ
PreReq:		%{name}-common = %{version}

%description cgi
PHP as CGI program.

%description cgi -l pl
PHP jako program CGI.

%package common
Summary:	Common files nneded by both apache module and CGI
Summary(pl):	Wspólne pliki dla modu³u apacha i programu CGI
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	âÉÂÌÉÏÔÅËÉ
Group(uk):	â¦ÂÌ¦ÏÔÅËÉ

%description common
Common files needed by both apache module and CGI.

%description common -l pl
Wspólne pliki dla modu³u apacha i programu CGI.

%package mysql
Summary:	MySQL database module for PHP
Summary(pl):	Modu³ bazy danych MySQL dla PHP
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	âÉÂÌÉÏÔÅËÉ
Group(uk):	â¦ÂÌ¦ÏÔÅËÉ
PreReq:		%{name}-common = %{version}

%description mysql
This is a dynamic shared object (DSO) for Apache that will add MySQL
database support to PHP. If you need back-end support for MySQL, you
should install this package in addition to the main %{name} package.

%description mysql -l pl
Modu³ PHP umo¿liwiaj±cy dostêp do bazy danych MySQL.

%package pdf
Summary:	libPDF module for PHP
Summary(pl):	Modu³ do tworzenia plików PDF dla PHP
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	âÉÂÌÉÏÔÅËÉ
Group(uk):	â¦ÂÌ¦ÏÔÅËÉ
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
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	âÉÂÌÉÏÔÅËÉ
Group(uk):	â¦ÂÌ¦ÏÔÅËÉ
PreReq:		%{name}-common = %{version}

%description pgsql
This is a dynamic shared object (DSO) for Apache that will add
PostgreSQL database support to PHP. If you need back-end support for
PostgreSQL, you should install this package in addition to the main
%{name} package.

%description pgsql -l pl
Modu³ PHP umo¿liwiaj±cy dostêp do bazy danych PostgreSQL.

%package oci8
Summary:	Oracle 8 database module for PHP
Summary(pl):	Modu³ bazy danych Oracle 8 dla PHP
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	âÉÂÌÉÏÔÅËÉ
Group(uk):	â¦ÂÌ¦ÏÔÅËÉ
PreReq:		%{name}-common = %{version}
Autoreq:	false

%description oci8
This is a dynamic shared object (DSO) for Apache that will add Oracle
8 database support to PHP. If you need back-end support for Oracle 8,
you should install this package in addition to the main %{name}
package.

%description oci8 -l pl
Modu³ PHP umo¿liwiaj±cy dostêp do bazy danych Oracle 8.

%package oracle
Summary:	Oracle 7 database module for PHP
Summary(pl):	Modu³ bazy danych Oracle 7 dla PHP
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	âÉÂÌÉÏÔÅËÉ
Group(uk):	â¦ÂÌ¦ÏÔÅËÉ
PreReq:		%{name}-common = %{version}
Autoreq:	false

%description oracle
This is a dynamic shared object (DSO) for Apache that will add Oracle
7 database support to PHP. If you need back-end support for Oracle 7,
you should install this package in addition to the main %{name}
package.

%description oracle -l pl
Modu³ PHP umo¿liwiaj±cy dostêp do bazy danych Oracle 7.

%package gd
Summary:	GD extension module for PHP
Summary:	Modu³ GD dla PHP
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	âÉÂÌÉÏÔÅËÉ
Group(uk):	â¦ÂÌ¦ÏÔÅËÉ
PreReq:		%{name}-common = %{version}

%description gd
This is a dynamic shared object (DSO) for Apache that will add GD
support to PHP. You should install this package in addition to the
main %{name} package if you want to create and manipulate images with
PHP.

%description gd -l pl
Modu³ PHP umo¿liwiaj±cy korzystanie z biblioteki GD - do obróbki
obrazków z poziomu PHP.

%package java
Summary:	Java extension module for PHP
Summary(pl):	Modu³ Javy dla PHP
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	âÉÂÌÉÏÔÅËÉ
Group(uk):	â¦ÂÌ¦ÏÔÅËÉ
PreReq:		%{name}-common = %{version}

%description java
This is a dynamic shared object (DSO) for Apache that will add JAVA
support to PHP. This extension provides a simple and effective means
for creating and invoking methods on Java objects from PHP.

%description java -l pl
Modu³ PHP dodaj±cy wsparcie dla Javy. Umo¿liwia odwo³ywanie siê do
obiektów Javy z poziomu PHP.

%package xml
Summary:	XML extension module for PHP
Summary(pl):	Modu³ XML dla PHP
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	âÉÂÌÉÏÔÅËÉ
Group(uk):	â¦ÂÌ¦ÏÔÅËÉ
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

%package dba
Summary:	DBA extension module for PHP
Summary(pl):	Modu³ DBA dla PHP
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	âÉÂÌÉÏÔÅËÉ
Group(uk):	â¦ÂÌ¦ÏÔÅËÉ
PreReq:		%{name}-common = %{version}

%description dba
This is a dynamic shared object (DSO) for Apache that will add
flat-file databases (DBA) support to PHP.

#%description dba -l pl

%package odbc
Summary:	ODBC extension module for PHP
Summary(pl):	Modu³ ODBC dla PHP
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	âÉÂÌÉÏÔÅËÉ
Group(uk):	â¦ÂÌ¦ÏÔÅËÉ
PreReq:		%{name}-common = %{version}

%description odbc
This is a dynamic shared object (DSO) for Apache that will add ODBC
support to PHP.

%description odbc -l pl
Modu³ PHP ze wsparciem dla ODBC.

%package calendar
Summary:	Calendar extension module for PHP
Summary(pl):	Modu³ funkcji kalendarza dla PHP
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	âÉÂÌÉÏÔÅËÉ
Group(uk):	â¦ÂÌ¦ÏÔÅËÉ
PreReq:		%{name}-common = %{version}

%description calendar
This is a dynamic shared object (DSO) for Apache that will add
calendar support to PHP.

#%description calendar -l pl

%package dbase
Summary:	DBase extension module for PHP
Summary(pl):	Modu³ DBase dla PHP
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	âÉÂÌÉÏÔÅËÉ
Group(uk):	â¦ÂÌ¦ÏÔÅËÉ
PreReq:		%{name}-common = %{version}

%description dbase
This is a dynamic shared object (DSO) for Apache that will add DBase
support to PHP.

%description dbase -l pl
Modu³ PHP ze wsparciem dla DBase.

%package filepro
Summary:	FilePro extension module for PHP
Summary(pl):	Modu³ FilePro dla PHP
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	âÉÂÌÉÏÔÅËÉ
Group(uk):	â¦ÂÌ¦ÏÔÅËÉ
PreReq:		%{name}-common = %{version}

%description filepro
This is a dynamic shared object (DSO) for Apache that will add FilePro
support to PHP.

#%description filepro -l pl

%package posix
Summary:	POSIX extension module for PHP
Summary(pl):	Modu³ POSIX dla PHP
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	âÉÂÌÉÏÔÅËÉ
Group(uk):	â¦ÂÌ¦ÏÔÅËÉ
PreReq:		%{name}-common = %{version}

%description posix
This is a dynamic shared object (DSO) for Apache that will add POSIX
functions support to PHP.

%description posix -l pl
Modu³ PHP umo¿liwiaj±cy korzystanie z funkcji POSIX.

%package pcre
Summary:	PCRE extension module for PHP
Summary(pl):	Modu³ PCRE dla PHP
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	âÉÂÌÉÏÔÅËÉ
Group(uk):	â¦ÂÌ¦ÏÔÅËÉ
PreReq:		%{name}-common = %{version}

%description pcre
This is a dynamic shared object (DSO) for Apache that will add Perl
Compatible Regular Expression support to PHP.

%description pcre -l pl
Modu³ PHP umo¿liwiaj±cy korzystanie z perlowych wyra¿eñ regularnych
(Perl Compatible Regular Expressions)

%package sysvsem
Summary:	SysV sem extension module for PHP
Summary(pl):	Modu³ SysV sem dla PHP
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	âÉÂÌÉÏÔÅËÉ
Group(uk):	â¦ÂÌ¦ÏÔÅËÉ
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
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	âÉÂÌÉÏÔÅËÉ
Group(uk):	â¦ÂÌ¦ÏÔÅËÉ
PreReq:		%{name}-common = %{version}

%description sysvshm
This is a dynamic shared object (DSO) for Apache that will add SysV
Shared Memory support to PHP.

%description sysvshm -l pl
Modu³ PHP umo¿liwiaj±cy korzystanie z pamiêci dzielonej SysV.

%package yp
Summary:	NIS (yp) extension module for PHP
Summary(pl):	Modu³ NIS (yp) dla PHP
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	âÉÂÌÉÏÔÅËÉ
Group(uk):	â¦ÂÌ¦ÏÔÅËÉ
PreReq:		%{name}-common = %{version}

%description yp
This is a dynamic shared object (DSO) for Apache that will add NIS
(Yellow Pages) support to PHP.

#%description yp -l pl

%package bcmath
Summary:	bcmath extension module for PHP
Summary(pl):	Modu³ bcmath dla PHP
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	âÉÂÌÉÏÔÅËÉ
Group(uk):	â¦ÂÌ¦ÏÔÅËÉ
PreReq:		%{name}-common = %{version}

%description bcmath
This is a dynamic shared object (DSO) for Apache that will add bc
style precision math functions support to PHP.

%description bcmath -l pl
Modu³ PHP umo¿liwiaj±cy korzystanie z dok³adnych funkcji
matematycznych takich jak w programie bc.

%package ftp
Summary:	FTP extension module for PHP
Summary(pl):	Modu³ FTP dla PHP
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	âÉÂÌÉÏÔÅËÉ
Group(uk):	â¦ÂÌ¦ÏÔÅËÉ
PreReq:		%{name}-common = %{version}

%description ftp
This is a dynamic shared object (DSO) for Apache that will add FTP
support to PHP.

%description ftp -l pl
Modu³ PHP dodaj±cy obs³ugê protoko³u FTP.

%package zlib
Summary:	Zlib extension module for PHP
Summary(pl):	Modu³ zlib dla PHP
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	âÉÂÌÉÏÔÅËÉ
Group(uk):	â¦ÂÌ¦ÏÔÅËÉ
PreReq:		%{name}-common = %{version}

%description zlib
This is a dynamic shared object (DSO) for Apache that will add
compression (zlib) support to PHP.

%description zlib -l pl
Modu³ PHP umo¿liwiaj±cy u¿ywanie kompresji (poprzez bibliotekê zlib).

%package exif
Summary:	exif extension module for PHP
Summary(pl):	Modu³ exif dla PHP
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	âÉÂÌÉÏÔÅËÉ
Group(uk):	â¦ÂÌ¦ÏÔÅËÉ
PreReq:		%{name}-common = %{version}

%description exif
This is a dynamic shared object (DSO) for Apache that will add exif
support to PHP.

%description exif -l pl
Modu³ PHP dodaj±cy obs³ugê plików EXIF.

%package recode
Summary:	recode extension module for PHP
Summary(pl):	Modu³ recode dla PHP
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	âÉÂÌÉÏÔÅËÉ
Group(uk):	â¦ÂÌ¦ÏÔÅËÉ
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
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	âÉÂÌÉÏÔÅËÉ
Group(uk):	â¦ÂÌ¦ÏÔÅËÉ
PreReq:		%{name}-common = %{version}

%description session
This is a dynamic shared object (DSO) for Apache that will add session
support to PHP.

%description session -l pl
Modu³ PHP dodaj±cy obs³ugê sesji.

%package gettext
Summary:	gettext extension module for PHP
Summary(pl):	Modu³ gettext dla PHP
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	âÉÂÌÉÏÔÅËÉ
Group(uk):	â¦ÂÌ¦ÏÔÅËÉ
PreReq:		%{name}-common = %{version}

%description gettext
This is a dynamic shared object (DSO) for Apache that will add gettext
support to PHP.

%description gettext -l pl
Modu³ PHP dodaj±cy obs³ugê lokalizacji przez gettext.

%package snmp
Summary:	SNMP extension module for PHP
Summary(pl):	Modu³ SNMP dla PHP
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	âÉÂÌÉÏÔÅËÉ
Group(uk):	â¦ÂÌ¦ÏÔÅËÉ
PreReq:		%{name}-common = %{version}

%description snmp
This is a dynamic shared object (DSO) for Apache that will add SNMP
support to PHP.

%description snmp -l pl
Modu³ PHP dodaj±cy obs³ugê SNMP.

%package imap
Summary:	IMAP extension module for PHP
Summary(pl):	Modu³ IMAP dla PHP
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	âÉÂÌÉÏÔÅËÉ
Group(uk):	â¦ÂÌ¦ÏÔÅËÉ
PreReq:		%{name}-common = %{version}

%description imap
This is a dynamic shared object (DSO) for Apache that will add IMAP
support to PHP.

%description imap -l pl
Modu³ PHP dodaj±cy obs³ugê skrzynek IMAP.

%package ldap
Summary:	LDAP extension module for PHP
Summary(pl):	Modu³ LDAP dla PHP
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	âÉÂÌÉÏÔÅËÉ
Group(uk):	â¦ÂÌ¦ÏÔÅËÉ
PreReq:		%{name}-common = %{version}

%description ldap
This is a dynamic shared object (DSO) for Apache that will add LDAP
support to PHP.

%description ldap -l pl
Modu³ PHP dodaj±cy obs³ugê LDAP.

%package sockets
Summary:	sockets extension module for PHP
Summary(pl):	Modu³ socket dla PHP
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	âÉÂÌÉÏÔÅËÉ
Group(uk):	â¦ÂÌ¦ÏÔÅËÉ
PreReq:		%{name}-common = %{version}

%description sockets
This is a dynamic shared object (DSO) for Apache that will add sockets
support to PHP.

%description sockets -l pl
Modu³ PHP dodaj±cy obs³ugê gniazdek.

%package mcrypt
Summary:	mcrypt extension module for PHP
Summary(pl):	Modu³ mcrypt dla PHP
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	âÉÂÌÉÏÔÅËÉ
Group(uk):	â¦ÂÌ¦ÏÔÅËÉ
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
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	âÉÂÌÉÏÔÅËÉ
Group(uk):	â¦ÂÌ¦ÏÔÅËÉ
PreReq:		%{name}-common = %{version}

%description mhash
This is a dynamic shared object (DSO) for Apache that will add mhash
support to PHP.

%description mhash -l pl
Modu³ PHP udostêpniaj±cy funkcje mieszaj±ce z biblioteki mhash.

%package doc
Summary:	Online manual for PHP
Summary(pl):	Dokumentacja dla PHP
Group:		Networking/Daemons
Group(de):	Netzwerkwesen/Server
Group(pl):	Sieciowe/Serwery
Obsoletes:	php-manual

%description doc
Comprehensive documentation for PHP, viewable through your web server,
too!

%description doc -l pl
Dokumentacja dla pakietu PHP. Mo¿na j± równie¿ ogl±daæ poprzez serwer
WWW.

%package pear
Summary:	PEAR - PHP Extension and Application Repository
Summary(pl):	PEAR - Rozszerzenie PHP i Repozytorium Aplikacji
Group:		Development/Languages/PHP
Group(de):	Entwicklung/Sprachen/PHP
Group(pl):	Programowanie/Jêzyki/PHP

%description pear
PEAR - PHP Extension and Application Repository.

%description pear -l pl
PEAR (PHP Extension and Application Repository) - Rozszerzenie PHP i
Repozytorium Aplikacji.

%package domxml
Summary:        DOM XML module
Summary(pl):	Modu³ DOM XML
Group:          Development/Languages/PHP
Group(de):	Entwicklung/Sprachen/PHP
Group(pl):	Programowanie/Jêzyki/PHP

%description domxml
DOM XML module.

%description domxml -l pl
Modu³ DOM XML.

%package devel
Summary:	Files for PHP modules development
Summary(pl):	Pliki do kompilacji modu³ów PHP
Group:		Development/Languages/PHP
Group(de):	Entwicklung/Sprachen/PHP
Group(pl):	Programowanie/Jêzyki/PHP
Requires:	%{name}-common = %{version}

%description devel
Files for PHP modules development.

%description devel -l pl
Pliki potrzebne do kompilacji modu³ów PHP.

%package curl
Summary:	curl extension module for PHP
Summary(pl):	Modu³ curl dla PHP
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	âÉÂÌÉÏÔÅËÉ
Group(uk):	â¦ÂÌ¦ÏÔÅËÉ
PreReq:		%{name}-common = %{version}

%description curl
This is a dynamic shared object (DSO) for Apache that will add curl
support to PHP.

%description curl -l pl
Modu³ PHP umo¿liwiaj±cy korzystanie z biblioteki curl.

%package xslt
Summary:	xslt extension module for PHP
Summary(pl):	Modu³ xslt dla PHP
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	âÉÂÌÉÏÔÅËÉ
Group(uk):	â¦ÂÌ¦ÏÔÅËÉ
PreReq:		%{name}-common = %{version}

%description xslt
This is a dynamic shared object (DSO) for Apache that will add xslt
support to PHP.

%description xslt -l pl
Modu³ PHP umo¿liwiaj±cy korzystanie z technologii xslt.

%package wddx
Summary:	wddx extension module for PHP
Summary(pl):	Modu³ wddx dla PHP
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	âÉÂÌÉÏÔÅËÉ
Group(uk):	â¦ÂÌ¦ÏÔÅËÉ
PreReq:		%{name}-common = %{version}

%description wddx
This is a dynamic shared object (DSO) for Apache that will add wddx
support to PHP.

%description wddx -l pl
Modu³ PHP umo¿liwiaj±cy korzystanie z wddx.

%package ming
Summary:	ming extension module for PHP
Summary(pl):	Modu³ ming dla PHP
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	âÉÂÌÉÏÔÅËÉ
Group(uk):	â¦ÂÌ¦ÏÔÅËÉ
PreReq:		%{name}-common = %{version}

%description ming
This is a dynamic shared object (DSO) for Apache that will add ming
(Flash - .swf files) support to PHP.

%description ming -l pl
Modu³ PHP dodaj±cy obs³ugê plików Flash (.swf) poprzez bibliotekê
ming.

%prep
%setup  -q
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

install -d manual
bzip2 -dc %{SOURCE4} | tar -xf - -C manual

%build
CFLAGS="%{rpmcflags} -DEAPI -I/usr/X11R6/include"; export CFLAGS
EXTENSION_DIR="%{extensionsdir}"; export EXTENSION_DIR
./buildconf
libtoolize --copy --force
aclocal
autoconf
#for i in cgi fastcgi apxs ; do
for i in cgi apxs ; do
%configure \
	`[ $i = cgi ] && echo --enable-discard-path` \
	`[ $i = fastcgi ] && echo --enable-discard-path --with-fastcgi=/usr` \
	`[ $i = apxs ] && echo --with-apxs=%{_sbindir}/apxs` \
	--with-config-file-path=%{_sysconfdir} \
	--with-exec-dir=%{_bindir} \
	--disable-debug \
	--enable-magic-quotes \
	--enable-shared \
	--enable-track-vars \
	--enable-safe-mode \
	--enable-trans-sid \
	--enable-sysvsem=shared \
	--enable-sysvshm=shared \
	--enable-shmop=shared \
	--enable-session \
	--enable-exif=shared \
	--with-regex=php \
	--with-gettext=shared \
	%{!?_without_ldap:--with-ldap=shared} \
	--with-mysql=shared,/usr \
	--with-mysql-sock=/var/lib/mysql/mysql.sock \
	--with-gd=shared \
	--with-jpeg-dir=shared \
	--with-zlib-dir=shared \
	--with-png-dir=shared \
	--enable-gd-native-ttf \
	--with-freetype-dir=shared \
	--with-t1lib=shared \
	--with-dbase=shared \
	--with-filepro=shared \
	--enable-ftp=shared \
	--with-hyperwave \
	--with-pdflib=shared \
	--with-cpdflib=shared \
	%{?_with_java:--with-java} \
	--with-pgsql=shared,/usr \
	%{!?_without_imap:--with-imap=shared --with-imap-ssl} \
	--enable-bcmath=shared \
	--enable-calendar=shared \
	--with-mm \
	--with-pcre-regex=shared \
	--enable-posix=shared \
	--with-recode=shared \
	--enable-ucd-snmp-hack \
	--enable-dba=shared \
	%{!?_without_snmp:--with-snmp=shared} \
	--with-gdbm \
	--with-db3 \
	--enable-yp=shared \
	--with-xml=shared \
	--enable-xml=shared \
	--with-zlib=shared \
	--with-mcrypt=shared \
	--enable-sockets=shared \
	--with-bz2=shared \
	--with-ctype=shared \
	--with-mhash=shared \
	--with-curl=shared \
	--with-gmp=shared \
	--with-ming=shared \
	%{?_with_openssl:--with-openssl} \
	%{!?_without_odbc:--with-unixODBC=shared} \
	%{?_with_oracle:--with-oracle=shared} \
	%{?_with_oci8:--with-oci8=shared} \
	--without-db2 \
	--with-dom=shared \
    %{?_with_xslt:--enable-xslt=shared} \
    %{?_with_xslt:--with-xslt-sablot=shared} \
    %{?_with_wddx:--enable-wddx=shared} \
	--with-pear=%{peardir}
done

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
		$RPM_BUILD_ROOT{%{_sbindir},%{_bindir}}

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT \
	INSTALL_IT="install libs/libphp4.so $RPM_BUILD_ROOT%{_libdir}/apache/ ; install libs/libphp_common*.so.*.*.* $RPM_BUILD_ROOT%{_libdir}"

install .libs/php $RPM_BUILD_ROOT%{_bindir}/php

#exit 1
#install .libs/*.so	$RPM_BUILD_ROOT%{_pkglibdir}
#install modules/*.so	$RPM_BUILD_ROOT%{_pkglibdir}/php

install %{SOURCE2}		$RPM_BUILD_ROOT%{_sysconfdir}/php.ini
install %{SOURCE3} php4.gif	$RPM_BUILD_ROOT/home/httpd/icons
install %{SOURCE5} $RPM_BUILD_ROOT/%{_sbindir}


install %{SOURCE1} .
gzip -9nf CODING_STANDARDS CREDITS \
      EXTENSIONS NEWS TODO* LICENSE Zend/LICENSE \
      Zend/ZEND_CHANGES README.SELF-CONTAINED-EXTENSIONS README.EXT_SKEL

%post
%{_sbindir}/apxs -e -a -n php4 %{_pkglibdir}/libphp4.so 1>&2
perl -pi -e 's|^#AddType application/x-httpd-php \.php|AddType application/x-httpd-php .php|' \
	/etc/httpd/httpd.conf
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
fi

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

%post common -p /sbin/ldconfig
%postun common -p /sbin/ldconfig

%post bcmath
%{_sbindir}/php-module-install install bcmath %{_sysconfdir}/php.ini

%preun bcmath
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove bcmath %{_sysconfdir}/php.ini
fi

%post calendar
%{_sbindir}/php-module-install install calendar %{_sysconfdir}/php.ini

%preun calendar
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove calendar %{_sysconfdir}/php.ini
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

%if %{?_without_imap:0}%{!?_without_imap:1}
%post imap
%{_sbindir}/php-module-install install imap %{_sysconfdir}/php.ini

%preun imap
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove imap %{_sysconfdir}/php.ini
fi
%endif

%if %{?bond_on_java:1}%{!?bond_on_java:0}
%post java
%{_sbindir}/php-module-install install libphp_java %{_sysconfdir}/php.ini

%preun java
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove libphp_java %{_sysconfdir}/php.ini
fi
%endif

%if %{?_without_ldap:0}%{!?_without_ldap:1}
%post ldap
%{_sbindir}/php-module-install install ldap %{_sysconfdir}/php.ini

%preun ldap
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove ldap %{_sysconfdir}/php.ini
fi
%endif

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

%post mysql
%{_sbindir}/php-module-install install mysql %{_sysconfdir}/php.ini

%preun mysql
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove mysql %{_sysconfdir}/php.ini
fi

%post pdf
%{_sbindir}/php-module-install install libpdf_php %{_sysconfdir}/php.ini

%preun pdf
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove libpdf_php %{_sysconfdir}/php.ini
fi

%preun domxml
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove domxml %{_sysconfdir}/php.ini
fi

%post domxml
%{_sbindir}/php-module-install install domxml %{_sysconfdir}/php.ini

%if %{?_with_oci8:1}%{!?_with_oci8:0}
%post oci8
%{_sbindir}/php-module-install install oci8 %{_sysconfdir}/php.ini

%preun oci8
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove oci8 %{_sysconfdir}/php.ini
fi
%endif

%if %{?_without_odbc:0}%{!?_without_odbc:1}
%post odbc
%{_sbindir}/php-module-install install odbc %{_sysconfdir}/php.ini

%preun odbc
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove odbc %{_sysconfdir}/php.ini
fi
%endif

%if %{?_with_oracle:1}%{!?_with_oracle:0}
%post oracle
%{_sbindir}/php-module-install install oracle %{_sysconfdir}/php.ini

%preun oracle
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove oracle %{_sysconfdir}/php.ini
fi
%endif

%post pcre
%{_sbindir}/php-module-install install pcre %{_sysconfdir}/php.ini

%preun pcre
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove pcre %{_sysconfdir}/php.ini
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

%if %{?_without_snmp:0}%{!?_without_snmp:1}
%post snmp
%{_sbindir}/php-module-install install snmp %{_sysconfdir}/php.ini

%preun snmp
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove snmp %{_sysconfdir}/php.ini
fi
%endif

%post sockets
%{_sbindir}/php-module-install install sockets %{_sysconfdir}/php.ini

%preun sockets
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove sockets %{_sysconfdir}/php.ini
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

%post xml
%{_sbindir}/php-module-install install xml %{_sysconfdir}/php.ini

%preun xml
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove xml %{_sysconfdir}/php.ini
fi

%post yp
%{_sbindir}/php-module-install install yp %{_sysconfdir}/php.ini

%preun yp
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove yp %{_sysconfdir}/php.ini
fi

%post zlib
%{_sbindir}/php-module-install install zlib %{_sysconfdir}/php.ini

%preun zlib
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove zlib %{_sysconfdir}/php.ini
fi

%post curl
%{_sbindir}/php-module-install install curl %{_sysconfdir}/php.ini

%preun curl
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove curl %{_sysconfdir}/php.ini
fi

#%post xslt
#%{_sbindir}/php-module-install install xslt %{_sysconfdir}/php.ini
#
#%preun xslt
#if [ "$1" = "0" ]; then
#        %{_sbindir}/php-module-install remove xslt %{_sysconfdir}/php.ini
#fi
#
#%post wddx
#%{_sbindir}/php-module-install install wddx %{_sysconfdir}/php.ini
#
#%preun wddx
#if [ "$1" = "0" ]; then
#        %{_sbindir}/php-module-install remove wddx %{_sysconfdir}/php.ini
#fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/apache/libphp4.so

%files cgi
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/php

%files common
%defattr(644,root,root,755)
%doc {CODING_STANDARDS,CREDITS,Zend/ZEND_CHANGES}.gz
%doc {LICENSE,Zend/LICENSE,EXTENSIONS,NEWS,TODO*}.gz  
%doc {README.EXT_SKEL,README.SELF-CONTAINED-EXTENSIONS}.gz

%dir %{_sysconfdir}
%attr(644,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/php.ini

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

%files domxml
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/domxml.so

%files pear
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pear
%{peardir}

%files mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/mysql.so

%files pdf
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/libpdf_php.so

%files pgsql
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/pgsql.so

%if %{?_with_oracle:1}%{!?_with_oracle:0}
%files oracle
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/oracle.so
%endif

%if %{?_with_oci8:1}%{!?_with_oci8:0}
%files oci8
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/oci8.so
%endif

%files gd
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/gd.so

# To check
#%files xml
#%defattr(644,root,root,755)
#%attr(755,root,root) %{extensionsdir}/xml.so

%files dba
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/dba.so

%files dbase
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/dbase.so

%files filepro
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/filepro.so

%files pcre
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/pcre.so

%files posix
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/posix.so

%files sysvsem
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/sysvsem.so

%files sysvshm
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/sysvshm.so

%files yp
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/yp.so

%files calendar
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/calendar.so

%files bcmath
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/bcmath.so

%files ftp
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/ftp.so

%files zlib
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/zlib.so

%files exif
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/exif.so

%files recode
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/recode.so

#%files session
#%defattr(644,root,root,755)
#%attr(755,root,root) %{extensionsdir}/session.so

%files gettext
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/gettext.so

%if %{?_without_imap:0}%{!?_without_imap:1}
%files imap
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/imap.so
%endif

%if %{?_without_snmp:0}%{!?_without_snmp:1}
%files snmp
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/snmp.so
%endif

%if %{?_with_java:1}%{!?_with_java:0}
%files java
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/libphp_java.so
%endif

%if %{?_without_ldap:0}%{!?_without_ldap:1}
%files ldap
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/ldap.*
%endif

%files sockets
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/sockets.so

%files mcrypt
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/mcrypt.so

%files mhash
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/mhash.so

%if %{?_without_odbc:0}%{!?_without_odbc:1}
%files odbc
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/odbc.so
%endif

%files doc
%defattr(644,root,root,755)
%doc manual/*

%files curl
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/curl.so

%files ming
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/ming.so

%if %{?_with_xslt:1}%{!?_with_xslt:0}
%files xslt
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/xslt.so
%endif

%if %{?_with_wddx:1}%{!?_with_wddx:0}
%files wddx
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/wddx.so
%endif
