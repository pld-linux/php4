#
# Do NOT build openssl as shared module or
# fsockopen('tls://host',...) will not work!
#
# TODO:
# - make additional headers added by mail patch configurable
# - too many unneccessary libs:
#  - libkrb5.so.3 is needed by (installed) php4-common-4.4.8-15.i686
#  - php4-common-4.4.8-15.i686 marks net-snmp-libs-5.4.1.2-1.i686 (cap libnetsnmp.so.15)
#    php5-common doesn't have such deps
#  - php4-cli pulls: libltdl
# - above is caused by openssl linked in statically as openssl links with kerberos
#
# Conditional build:
%bcond_with	db3		# use db3 packages instead of db (4.x) for Berkeley DB support
%bcond_with	fdf		# with FDF (PDF forms) module		(BR: proprietary lib)
%bcond_with	hardening	# build with hardening patch applied (http://www.hardened-php.net/)
%bcond_with	interbase_inst	# use InterBase install., not Firebird	(BR: proprietary libs)
%bcond_with	java		# with Java extension module		(BR: jdk)
%bcond_with	oci8		# with Oracle oci8 extension module	(BR: proprietary libs)
%bcond_with	oracle		# with oracle extension module		(BR: proprietary libs)
%bcond_without	cpdf		# without cpdf extension module
%bcond_without	curl		# without CURL extension module
%bcond_without	domxslt		# without DOM XSLT/EXSLT support in DOM XML extension module
%bcond_with	fribidi		# without FriBiDi extension module (use pecl-fribidi)
%bcond_without	imap		# without IMAP extension module
%bcond_without	interbase	# without InterBase extension module
%bcond_without	ldap		# without LDAP extension module
%bcond_without	mhash		# without mhash extension module
%bcond_with	ming		# with ming extension module
%bcond_without	mm		# without mm support for session storage
%bcond_without	mnogosearch	# without mnogosearch extension module
%bcond_without	msession	# without msession extension module
%bcond_without	mssql		# without MS SQL extension module
%bcond_without	odbc		# without ODBC extension module
%bcond_without	openssl		# without OpenSSL support and OpenSSL extension (module)
%bcond_without	pcre		# without PCRE extension module
%bcond_without	pdf		# without PDF extension module
%bcond_without	pgsql		# without PostgreSQL extension module
%bcond_without	pspell		# without pspell extension module
%bcond_without	qtdom		# without Qt DOM extension module
%bcond_without	recode		# without recode extension module
%bcond_without	snmp		# without SNMP extension module
%bcond_without	sybase		# without Sybase and Sybase-CT extension modules
%bcond_without	wddx		# without WDDX extension module
%bcond_without	xml		# without XML and DOMXML extension modules
%bcond_without	xmlrpc		# without XML-RPC extension module
%bcond_with     system_xmlrpc_epi       # use system xmlrpc-epi library (broken on 64bit arches, see http://bugs.php.net/41611)
%bcond_without	xslt		# without XSLT extension module
%bcond_with	yaz		# without YAZ extension module
%bcond_with	yp
%bcond_without	apache1		# disable building apache 1.3.x module
%bcond_without	apache2		# disable building apache 2.x module
%bcond_without	fcgi		# disable building FCGI SAPI
%bcond_with	zts		# disable experimental-zts
%bcond_with	versioning	# build with experimental versioning (to load php4/php5 into same apache)

%define apxs1		/usr/sbin/apxs1
%define	apxs2		/usr/sbin/apxs

# mm is not thread safe
# ext/session/mod_mm.c:37:3: #error mm is not thread-safe
%if %{with zts}
%undefine	with_mm
%endif

%ifnarch %{ix86} %{x8664} sparc sparcv9 alpha
%undefine	with_interbase
%endif

# x86-only lib
%ifnarch %{ix86}
%undefine	with_msession
%endif

%define		rel 60
Summary:	PHP: Hypertext Preprocessor
Summary(fr.UTF-8):	Le langage de script embarque-HTML PHP
Summary(pl.UTF-8):	Język skryptowy PHP
Summary(pt_BR.UTF-8):	A linguagem de script PHP
Summary(ru.UTF-8):	PHP Версии 4 - язык препроцессирования HTML-файлов, выполняемый на сервере
Summary(uk.UTF-8):	PHP Версії 4 - мова препроцесування HTML-файлів, виконувана на сервері
Name:		php4
Version:	4.4.9
Release:	%{rel}%{?with_hardening:hardened}
Epoch:		3
License:	PHP
Group:		Libraries
Source0:	http://www.php.net/distributions/php-%{version}.tar.bz2
# Source0-md5:	2e3b2a0e27f10cb84fd00e5ecd7a1880
#Source0:	http://cvs.php.net/viewvc.cgi/phpweb/distributions/php-%{version}.tar.bz2?revision=1.1
Source3:	%{name}-mod_php.conf
Source4:	%{name}-cgi-fcgi.ini
Source5:	%{name}-cgi.ini
Source6:	%{name}-apache.ini
Source7:	%{name}-cli.ini
Source8:	http://www.hardened-php.net/hardening-patch-4.4.0-0.4.3.patch.gz
# Source8-md5:	6eac3c5c5a7473c68a043c7657298f48
Patch0:		%{name}-shared.patch
Patch1:		%{name}-pldlogo.patch
Patch2:		%{name}-xml-expat-fix.patch
Patch3:		%{name}-mail.patch
Patch4:		%{name}-link-libs.patch
Patch5:		%{name}-libpq_fs_h_path.patch
Patch6:		%{name}-wddx-fix.patch
Patch7:		%{name}-lib.patch
Patch8:		%{name}-hyperwave-fix.patch
Patch9:		%{name}-xslt-gcc33.patch
Patch10:	%{name}-java-norpath.patch
Patch11:	%{name}-mcal-shared-lib.patch
Patch12:	%{name}-msession-shared-lib.patch
Patch13:	%{name}-build_modules.patch
Patch14:	%{name}-sapi-ini-file.patch
Patch15:	%{name}-no-metaccld.patch
Patch16:	%{name}-session-unregister.patch
Patch17:	%{name}-ini.patch
Patch18:	%{name}-acam.patch
Patch19:	%{name}-xmlrpc-fix.patch
Patch20:	%{name}-libtool.patch
Patch21:	%{name}-allow-db31.patch
Patch22:	%{name}-threads-acfix.patch

Patch24:	%{name}-qt.patch
Patch25:	%{name}-no_pear_install.patch
Patch26:	%{name}-zlib.patch
Patch27:	%{name}-db-shared.patch
Patch28:	%{name}-sybase-fix.patch
Patch29:	%{name}-openssl.patch
Patch30:	%{name}-mnogosearch-fix.patch
Patch31:	%{name}-stupidapache_version.patch
Patch33:	%{name}-uint32_t.patch
Patch34:	%{name}-install_gd_headers.patch
Patch35:	%{name}-both-apxs.patch
Patch36:	php-dextension.patch
Patch37:	%{name}-zlib-for-getimagesize.patch
Patch38:	%{name}-ini-search-path.patch
Patch39:	%{name}-versioning.patch
Patch40:	%{name}-linkflags-clean.patch
Patch41:	%{name}-krb5.patch
Patch42:	%{name}-apr-apu.patch
Patch43:	%{name}-gd.patch
Patch45:	%{name}-config-dir.patch
Patch46:	%{name}-phpinfo_no_configure.patch
Patch47:	%{name}-ming.patch
Patch48:	%{name}-fcgi-graceful.patch
Patch49:	%{name}-ac.patch
Patch50:	%{name}-mime_magic.patch
Patch51:	%{name}-tds.patch
Patch52:	%{name}-lib64.patch
Patch53:	%{name}-silent-session-cleanup.patch
Patch54:	%{name}-m4-divert.patch
Patch55:	%{name}-libpng.patch
Patch56:	%{name}-gmp.patch
Patch57:	%{name}-pcre.patch
Patch58:	%{name}-apache24.patch
Patch59:	php-bug-68486.patch
Patch60:	%{name}-libx32.patch
URL:		http://www.php.net/
%{?with_interbase:%{!?with_interbase_inst:BuildRequires:	Firebird-devel >= 1.0.2.908-2}}
%{?with_pspell:BuildRequires:	aspell-devel >= 2:0.50.0}
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1.4d
BuildRequires:	bison
BuildRequires:	bzip2-devel
BuildRequires:	cracklib-devel >= 2.7-15
%{?with_curl:BuildRequires:	curl-devel >= 7.12.0}
BuildRequires:	cyrus-sasl-devel
%{!?with_db3:BuildRequires:	db-devel >= 4.0}
%{?with_db3:BuildRequires:	db3-devel >= 3.1}
BuildRequires:	elfutils-devel
%if %{with wddx} || %{with xml} || %{with xmlrpc}
BuildRequires:	expat-devel
%endif
%{?with_fcgi:BuildRequires:	fcgi-devel}
%{?with_fdf:BuildRequires:	fdftk-devel}
BuildRequires:	flex
%if %{with mssql} || %{with sybase}
BuildRequires:	freetds-devel >= 0.82
%endif
BuildRequires:	freetype-devel >= 2.0
%{?with_fribidi:BuildRequires:	fribidi-devel >= 0.10.4}
BuildRequires:	gdbm-devel
BuildRequires:	gmp-devel
%{?with_imap:BuildRequires:	heimdal-devel >= 0.7}
%{?with_imap:BuildRequires:	imap-devel >= 1:2001-0.BETA.200107022325.2}
%{?with_java:BuildRequires:	jdk >= 1.1}
%{?with_cpdf:BuildRequires:	libcpdf-devel >= 2.02r1-2}
BuildRequires:	libjpeg-devel
BuildRequires:	libltdl-devel >= 1.4
BuildRequires:	libmcal-devel
BuildRequires:	libmcrypt-devel >= 2.4.4
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libtiff-devel
%if "%{pld_release}" != "ac"
BuildRequires:	libtool >= 2:2.2
%else
BuildRequires:	libtool >= 1.4.3
%endif
%{?with_xml:BuildRequires:	libxml2-devel >= 2.2.7}
%{?with_domxslt:BuildRequires:	libxslt-devel >= 1.0.3}
%{?with_mhash:BuildRequires:	mhash-devel}
%{?with_ming:BuildRequires:	ming-devel >= 0.3.0}
%{?with_mm:BuildRequires:	mm-devel >= 1.3.0}
%{?with_mnogosearch:BuildRequires:	mnogosearch-devel >= 3.2.29}
BuildRequires:	mysql-devel >= 3.23.32
BuildRequires:	ncurses-ext-devel
%{?with_ldap:BuildRequires:	openldap-devel >= 2.3.0}
%if %{with openssl} || %{with ldap}
BuildRequires:	openssl-devel >= 0.9.7d
%endif
%{?with_snmp:BuildRequires:	net-snmp-devel >= 5.0.7}
BuildRequires:	pam-devel
BuildRequires:	pcre-devel
%{?with_pdf:BuildRequires:	pdflib-devel >= 4.0.0}
%{?with_msession:BuildRequires:	phoenix-devel}
BuildRequires:	pkgconfig
%{?with_pgsql:BuildRequires:	postgresql-backend-devel >= 7.2}
%{?with_pgsql:BuildRequires:	postgresql-devel}
%{?with_qtdom:BuildRequires:	qt-devel >= 2.2.0}
BuildRequires:	readline-devel
%{?with_recode:BuildRequires:	recode-devel >= 3.5d-3}
BuildRequires:	rpm >= 4.4.9-56
BuildRequires:	rpm-build >= 4.4.0
BuildRequires:	rpmbuild(macros) >= 1.236
%{?with_xslt:BuildRequires:	sablotron-devel >= 0.96}
BuildRequires:	sed >= 4.0
BuildRequires:	t1lib-devel
%{?with_odbc:BuildRequires:	unixODBC-devel}
%{?with_system_xmlrpc_epi:BuildRequires:	xmlrpc-epi-devel}
%{?with_yaz:BuildRequires:	yaz-devel >= 1.9}
BuildRequires:	zip
BuildRequires:	zlib-devel >= 1.0.9
BuildRequires:	zziplib-devel
%if %{with apache1}
BuildRequires:	apache1-devel >= 1.3.33-2
%endif
%if %{with apache2}
BuildRequires:	apache-devel >= 2.0.52-2
BuildRequires:	apr-devel >= 1:1.0.0
BuildRequires:	apr-util-devel >= 1:1.0.0
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/php4
%define		extensionsdir	%{_libdir}/php4

# must be in sync with source. extra check ensuring that it is so is done in %%build
%define		php_api_version		20020918
%define		zend_module_api		20020429
%define		zend_extension_api	20050606
%define		zend_zts			%{!?with_zts:0}%{?with_zts:1}
%define		php_debug			%{!?debug:0}%{?debug:1}

%description
PHP is an HTML-embedded scripting language. PHP attempts to make it
easy for developers to write dynamically generated web pages. PHP also
offers built-in database integration for several commercial and
non-commercial database management systems, so writing a
database-enabled web page with PHP is fairly simple. The most common
use of PHP coding is probably as a replacement for CGI scripts. The
mod_php module enables the Apache web server to understand and process
the embedded PHP language in web pages. This package contains php
version %{version}.

%description -l fr.UTF-8
PHP est un langage de script embarque dans le HTM. PHP essaye de
rendre simple aux developpeurs d'ecrire des pages web generees
dynamiquement. PHP incorpore egalement une integration avec plusieurs
systemes de gestion de bases de donnees commerciaux et
non-connerciaux, qui rent facile la creation de pages web liees avec
des bases de donnees. L'utilisation la plus commune de PHP est
probablement en remplacement de scripts CGI. Le module mod_php permet
au serveur web apache de comprendre et de traiter le langage PHP
integre dans des pages web. Ce package contient php version
%{version}.

%description -l pl.UTF-8
PHP jest językiem skryptowym, którego polecenia umieszcza się w
plikach HTML. Pakiet ten zawiera moduł przeznaczony dla serwera HTTP
(jak np. Apache), który interpretuje te polecenia. Umożliwia to
tworzenie dynamicznie stron WWW. Spora część składni PHP zapożyczona
została z języków: C, Java i Perl.

%description -l pt_BR.UTF-8
PHP: Preprocessador de Hipertexto versão 4 é uma linguagem script
embutida em HTML. Muito de sua sintaxe é emprestada de C, Java e Perl,
com algumas características únicas, específicas ao PHP. O objetivo da
linguagem é permitir que desenvolvedores web escrevam páginas
dinamicamente geradas de forma rápida.

%description -l ru.UTF-8
PHP4 - это язык написания скриптов, встраиваемых в HTML-код. PHP
предлагает интерграцию с множеством СУБД, поэтому написание скриптов
для работы с базами данных относительно просто. Наиболее популярное
использование PHP - замена для CGI скриптов.

Этот пакет содержит самодостаточную (CGI) версию интерпретатора языка.
Вы должны также установить пакет %{name}-common. Если вам нужен
интерпретатор PHP в качестве модуля apache, установите пакет
apache-php.

%description -l uk.UTF-8
PHP4 - це мова написання скриптів, що вбудовуються в HTML-код. PHP
пропонує інтеграцію з багатьма СУБД, тому написання скриптів для
роботи з базами даних є доволі простим. Найбільш популярне
використання PHP - заміна для CGI скриптів.

Цей пакет містить самодостатню (CGI) версію інтерпретатора мови. Ви
маєте також встановити пакет %{name}-common. Якщо вам потрібен
інтерпретатор PHP в якості модуля apache, встановіть пакет apache-php.

%package -n apache1-mod_php4
Summary:	php4 DSO module for apache 1.3.x
Summary(pl.UTF-8):	Moduł DSO (Dynamic Shared Object) php4 dla apache 1.3.x
Group:		Development/Languages/PHP
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	apache1(EAPI) >= 1.3.33-2
Requires:	apache1-mod_mime
Provides:	webserver(php) = %{version}
Obsoletes:	apache-mod_php < 1:4.1.1
Obsoletes:	phpfi
# Obsolete last version when apache module was in main package
Obsoletes:	php4 < 3:4.3.11-4.16

%description -n apache1-mod_php4
php4 as DSO module for apache 1.3.x.

%description -n apache1-mod_php4 -l pl.UTF-8
php4 jako moduł DSO (Dynamic Shared Object) dla apache 1.3.x.

%package -n apache-mod_php4
Summary:	php4 support for apache 2.x
Summary(pl.UTF-8):	Wsparcie php4 dla apache 2.x
Group:		Development/Languages/PHP
Requires:       apache-mod_php4-core = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	webserver(php) = %{version}
Obsoletes:	apache-mod_php < 1:4.1.1
Obsoletes:	phpfi
# Obsolete last version when apache module was in main package
Obsoletes:	php4 < 3:4.3.11-4.16

%description -n apache-mod_php4
php4 support for apache 2.x.

%description -n apache-mod_php4 -l pl.UTF-8
Wsparcie php4 dla apache 2.x.

%package -n apache-mod_php4-core
Summary:	php4 DSO module for apache 2.x
Summary(pl.UTF-8):	Moduł DSO (Dynamic Shared Object) php4 dla apache 2.x
Group:		Development/Languages/PHP
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	apache(modules-api) = %{apache_modules_api}
Requires:	apache-mod_mime

%description -n apache-mod_php4-core
php4 as DSO module for apache 2.x.

%description -n apache-mod_php4-core -l pl.UTF-8
php4 jako moduł DSO (Dynamic Shared Object) dla apache 2.x.

%package fcgi
Summary:	php4 as FastCGI program
Summary(pl.UTF-8):	php4 jako program FastCGI
Group:		Development/Languages/PHP
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-fcgi = %{epoch}:%{version}-%{release}
Provides:	webserver(php) = %{version}

%description fcgi
php4 as FastCGI program.

%description fcgi -l pl.UTF-8
php4 jako program FastCGI.

%package cgi
Summary:	php4 as CGI program
Summary(pl.UTF-8):	php4 jako program CGI
Group:		Development/Languages/PHP
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-cgi = %{epoch}:%{version}-%{release}
Provides:	php(cgi)

%description cgi
php4 as CGI program.

%description cgi -l pl.UTF-8
php4 jako program CGI.

%package cli
Summary:	php4 as CLI interpreter
Summary(pl.UTF-8):	php4 jako interpreter działający z linii poleceń
Group:		Development/Languages/PHP
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description cli
php4 as CLI interpreter.

%description cli -l pl.UTF-8
php4 jako interpreter działający z linii poleceń.

%package program
Summary:	/usr/bin/php symlink
Summary(pl.UTF-8):	Dowiązanie symboliczne /usr/bin/php
Group:		Development/Languages/PHP
Requires:	%{name}-cli = %{epoch}:%{version}-%{release}
Obsoletes:	/usr/bin/php

%description program
Package providing /usr/bin/php symlink to PHP CLI.

%description program -l pl.UTF-8
Pakiet dostarczający dowiązanie symboliczne /usr/bin/php do PHP CLI.

%package common
Summary:	Common files needed by all PHP SAPIs
Summary(pl.UTF-8):	Wspólne pliki dla modułu apache'a i programu CGI
Summary(ru.UTF-8):	Разделяемые библиотеки для php
Summary(uk.UTF-8):	Бібліотеки спільного використання для php
Group:		Libraries
# because of dlclose() bugs in glibc <= 2.3.4 causing SEGVs on exit
Requires(triggerun):	sed >= 4.0
Requires:	glibc >= 6:2.3.5
Requires:	php-dirs
Provides:	php(modules_api) = %{php_api_version}
Provides:	php(openssl)
Provides:	php(session)
Provides:	php(standard)
Provides:	php(zend_extension_api) = %{zend_extension_api}
Provides:	php(zend_module_api) = %{zend_module_api}
Provides:	php4(debug) = %{php_debug}
Provides:	php4(thread-safety) = %{zend_zts}
Obsoletes:	php-session < 3:4.2.1-2
Obsoletes:	php4-openssl < 3:4.4.0-4
# for the posttrans scriptlet, conflicts because in vserver environment rpm package is not installed.
Conflicts:	rpm < 4.4.2-0.2

%description common
Common files needed by all PHP SAPIs.

%description common -l pl.UTF-8
Wspólne pliki dla modułu apacha i programu CGI.

%description common -l ru.UTF-8
Этот пакет содержит общие файлы для разных вариантов реализации PHP
(самодостаточной и в качестве модуля apache).

%description common -l uk.UTF-8
Цей пакет містить спільні файли для різних варіантів реалізації PHP
(самодостатньої та в якості модуля apache).

%package devel
Summary:	Files for PHP modules development
Summary(pl.UTF-8):	Pliki do kompilacji modułów PHP
Summary(pt_BR.UTF-8):	Arquivos de desenvolvimento para PHP
Summary(ru.UTF-8):	Пакет разработки для построения расширений PHP
Summary(uk.UTF-8):	Пакет розробки для побудови розширень PHP
Group:		Development/Languages/PHP
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	autoconf
Requires:	automake
%if "%{pld_release}" != "ac"
Requires:	libtool >= 2:2.2
%else
Requires:	libtool
%endif
Obsoletes:	php-devel

%description devel
The php-devel package lets you compile dynamic extensions to PHP.
Included here is the source for the PHP extensions. Instead of
recompiling the whole php4 binary to add support for, say, oracle,
install this package and use the new self-contained extensions
support. For more information, read the file
SELF-CONTAINED-EXTENSIONS.

%description devel -l pl.UTF-8
Pliki potrzebne do kompilacji modułów PHP.

%description devel -l pt_BR.UTF-8
Este pacote contém arquivos usados no desenvolvimento de programas ou
módulos PHP.

%description devel -l uk.UTF-8
Пакет php-devel дає можливість компілювати динамічні розширення PHP.
До пакету включено вихідний код для розширень. Замість повторної
компіляції бінарного файлу php4 для додання, наприклад, підтримки
oracle, встановіть цей пакет для компіляції окремих розширень.
Детальніша інформація - в файлі SELF-CONTAINED-EXTENSIONS.

%description devel -l ru.UTF-8
Пакет php-devel дает возможность компилировать динамические расширения
PHP. Пакет включает исходный код этих расширений. Вместо повторной
компиляции бинарного файла php4 для добавления, например, поддержки
oracle, установите этот пакет для компилирования отдельных расширений.
Подробности - в файле SELF-CONTAINED-EXTENSIONS.

%package bcmath
Summary:	bcmath extension module for PHP
Summary(pl.UTF-8):	Moduł bcmath dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(bcmath)

%description bcmath
This is a dynamic shared object (DSO) for PHP that will add bc style
precision math functions support.

%description bcmath -l pl.UTF-8
Moduł PHP umożliwiający korzystanie z dokładnych funkcji
matematycznych takich jak w programie bc.

%package bzip2
Summary:	Bzip2 extension module for PHP
Summary(pl.UTF-8):	Moduł bzip2 dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(bzip2)

%description bzip2
This is a dynamic shared object (DSO) for PHP that will add bzip2
compression support to PHP.

%description bzip2 -l pl.UTF-8
Moduł PHP umożliwiający używanie kompresji bzip2.

%package calendar
Summary:	Calendar extension module for PHP
Summary(pl.UTF-8):	Moduł funkcji kalendarza dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(calendar)

%description calendar
This is a dynamic shared object (DSO) for PHP that will add calendar
support.

%description calendar -l pl.UTF-8
Moduł PHP dodający wsparcie dla kalendarza.

%package cpdf
Summary:	cpdf extension module for PHP
Summary(pl.UTF-8):	Moduł cpdf dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(cpdf)

%description cpdf
This is a dynamic shared object (DSO) for PHP that will add PDF
support through libcpdf library.

%description cpdf -l pl.UTF-8
Moduł PHP dodający obsługę plików PDF poprzez bibliotekę libcpdf.

%package crack
Summary:	crack extension module for PHP
Summary(pl.UTF-8):	Moduł crack dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(crack)

%description crack
This is a dynamic shared object (DSO) for PHP that will add cracklib
support to PHP.

Warning: this is an experimental module.

%description crack -l pl.UTF-8
Moduł PHP umożliwiający korzystanie z biblioteki cracklib.

Uwaga: to jest moduł eksperymentalny.

%package ctype
Summary:	ctype extension module for PHP
Summary(pl.UTF-8):	Moduł ctype dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(ctype)

%description ctype
This is a dynamic shared object (DSO) for PHP that will add ctype
support.

%description ctype -l pl.UTF-8
Moduł PHP umożliwiający korzystanie z funkcji ctype.

%package curl
Summary:	curl extension module for PHP
Summary(pl.UTF-8):	Moduł curl dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(curl)

%description curl
This is a dynamic shared object (DSO) for PHP that will add curl
support.

%description curl -l pl.UTF-8
Moduł PHP umożliwiający korzystanie z biblioteki curl.

%package db
Summary:	Old xDBM extension module for PHP
Summary(pl.UTF-8):	Moduł xDBM dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(db)

%description db
This is an old dynamic shared object (DSO) for PHP that will add DBM
databases support.

Warning: this module is deprecated and does not support database
locking correctly. Please use DBA extension which is a fully
operational superset.

%description db -l pl.UTF-8
Stary moduł PHP dodający obsługę baz danych DBM.

Uwaga: ten moduł jest przestarzały i nie obsługuje poprawnie
blokowania bazy danych. Zamiast niego lepiej używać rozszerzenia DBA,
które obsługuje nadzbiór funkcjonalności tego modułu.

%package dba
Summary:	DBA extension module for PHP
Summary(pl.UTF-8):	Moduł DBA dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(dba)

%description dba
This is a dynamic shared object (DSO) for PHP that will add flat-file
databases (DBA) support.

%description dba -l pl.UTF-8
Moduł dla PHP dodający obsługę dla baz danych opartych na plikach
(DBA).

%package dbase
Summary:	DBase extension module for PHP
Summary(pl.UTF-8):	Moduł DBase dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(dbase)

%description dbase
This is a dynamic shared object (DSO) for PHP that will add DBase
support.

%description dbase -l pl.UTF-8
Moduł PHP ze wsparciem dla DBase.

%package dbx
Summary:	DBX extension module for PHP
Summary(pl.UTF-8):	Moduł DBX dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(dbx)

%description dbx
This is a dynamic shared object (DSO) for PHP that will add DB
abstraction layer. DBX supports odbc, mysql, pgsql, mssql, fbsql and
more.

%description dbx -l pl.UTF-8
Moduł PHP dodający warstwę abstrakcji do obsługi baz danych. DBX
obsługuje bazy odbc, mysql, pgsql, mssql, fbsql i inne.

%package dio
Summary:	Direct I/O extension module for PHP
Summary(pl.UTF-8):	Moduł Direct I/O dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(dio)

%description dio
This is a dynamic shared object (DSO) for PHP that will add direct
file I/O support.

%description dio -l pl.UTF-8
Moduł PHP dodający obsługę bezpośrednich operacji I/O na plikach.

%package domxml
Summary:	DOM XML extension module for PHP
Summary(pl.UTF-8):	Moduł DOM XML dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(domxml)

%description domxml
This is a dynamic shared object (DSO) for PHP that will add DOM XML
support.

Warning: this is an experimental module.

%description domxml -l pl.UTF-8
Moduł PHP dodający obsługę DOM XML.

Uwaga: to jest moduł eksperymentalny.

%package exif
Summary:	exif extension module for PHP
Summary(pl.UTF-8):	Moduł exif dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(exif)

%description exif
This is a dynamic shared object (DSO) for PHP that will add EXIF tags
support in image files.

%description exif -l pl.UTF-8
Moduł PHP dodający obsługę znaczników EXIF w plikach obrazków.

%package fdf
Summary:	FDF extension module for PHP
Summary(pl.UTF-8):	Moduł FDF dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(fdf)

%description fdf
This PHP module adds support for PDF Forms through Adobe FDFTK
library.

%description fdf -l pl.UTF-8
Moduł PHP dodający obsługę formularzy PDF poprzez bibliotekę Adobe
FDFTK.

%package filepro
Summary:	filePro extension module for PHP
Summary(pl.UTF-8):	Moduł filePro dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(filepro)

%description filepro
This is a dynamic shared object (DSO) for PHP that will add support
for read-only access to filePro databases.

%description filepro -l pl.UTF-8
Moduł PHP dodający możliwość dostępu (tylko do odczytu) do baz danych
filePro.

%package fribidi
Summary:	FriBiDi extension module for PHP
Summary(pl.UTF-8):	Modułe FriBiDi dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(fribidi)

%description fribidi
This extension is basically a wrapper for the FriBidi implementation
of the Unicode Bidi algorithm. The need for such an algorithm rises
from the bidirectional language usage done by applications.
Arabic/Hebrew embedded within English is such a case.

%description fribidi -l pl.UTF-8
To rozszerzenie to głównie interfejs do implementacji FriBiDi
algorytmu Unicode Bidi. Taki algorytm jest potrzebny w przypadku
używania dwukierunkowego pisma w aplikacjach - na przykład przy
tekście arabskim lub hebrajskim osadzonym wewnątrz angielskiego.

%package ftp
Summary:	FTP extension module for PHP
Summary(pl.UTF-8):	Moduł FTP dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(ftp)

%description ftp
This is a dynamic shared object (DSO) for PHP that will add FTP
support.

%description ftp -l pl.UTF-8
Moduł PHP dodający obsługę protokołu FTP.

%package gd
Summary:	GD extension module for PHP
Summary(pl.UTF-8):	Moduł GD dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	gd >= 2.0.28-2
Requires:	gd(gif)
Provides:	php(gd)

%description gd
This is a dynamic shared object (DSO) for PHP that will add GD
support, allowing you to create and manipulate images with PHP.

%description gd -l pl.UTF-8
Moduł PHP umożliwiający korzystanie z biblioteki GD, pozwalającej na
tworzenie i obróbkę obrazków.

%package gettext
Summary:	gettext extension module for PHP
Summary(pl.UTF-8):	Moduł gettext dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(gettext)

%description gettext
This is a dynamic shared object (DSO) for PHP that will add gettext
support.

%description gettext -l pl.UTF-8
Moduł PHP dodający obsługę lokalizacji przez gettext.

%package gmp
Summary:	gmp extension module for PHP
Summary(pl.UTF-8):	Moduł gmp dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(gmp)

%description gmp
This is a dynamic shared object (DSO) for PHP that will add arbitrary
length number support with GNU MP library.

%description gmp -l pl.UTF-8
Moduł PHP umożliwiający korzystanie z biblioteki gmp do obliczeń na
liczbach o dowolnej długości.

%package hyperwave
Summary:	Hyperwave extension module for PHP
Summary(pl.UTF-8):	Moduł Hyperwave dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(hyperwave)

%description hyperwave
This is a dynamic shared object (DSO) for PHP that will add Hyperwave
support.

%description hyperwave -l pl.UTF-8
Moduł PHP dodający obsługę Hyperwave.

%package iconv
Summary:	iconv extension module for PHP
Summary(pl.UTF-8):	Moduł iconv dla PHP
Group:		Libraries
Requires:	%{_libdir}/gconv
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	iconv
Provides:	php(iconv)

%description iconv
This is a dynamic shared object (DSO) for PHP that will add iconv
support.

%description iconv -l pl.UTF-8
Moduł PHP dodający obsługę iconv.

%package imap
Summary:	IMAP extension module for PHP
Summary(pl.UTF-8):	Moduł IMAP dla PHP
Summary(pt_BR.UTF-8):	Um módulo para aplicações PHP que usam IMAP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(imap)

%description imap
This is a dynamic shared object (DSO) for PHP that will add IMAP
support.

%description imap -l pl.UTF-8
Moduł PHP dodający obsługę skrzynek IMAP.

%description imap -l pt_BR.UTF-8
Um módulo para aplicações PHP que usam IMAP.

%package interbase
Summary:	InterBase/Firebird database module for PHP
Summary(pl.UTF-8):	Moduł bazy danych InterBase/Firebird dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(interbase)
%{?with_interbase_inst:Autoreq:	false}

%description interbase
This is a dynamic shared object (DSO) for PHP that will add InterBase
and Firebird database support.

%description interbase -l pl.UTF-8
Moduł PHP umożliwiający dostęp do baz danych InterBase i Firebird.

%package java
Summary:	Java extension module for PHP
Summary(pl.UTF-8):	Moduł Javy dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(java)

%description java
This is a dynamic shared object (DSO) for PHP that will add Java
support to PHP. This extension provides a simple and effective means
for creating and invoking methods on Java objects from PHP.

Note: it requires setting LD_LIBRARY_PATH to JRE directories
containing JVM libraries (e.g. libjava.so, libverify.so and libjvm.so
for Sun's JRE) before starting Apache or PHP interpreter.

%description java -l pl.UTF-8
Moduł PHP dodający wsparcie dla Javy. Umożliwia odwoływanie się do
obiektów Javy z poziomu PHP.

Uwaga: moduł wymaga ustawienia LD_LIBRARY_PATH na katalogi JRE
zawierające biblioteki JVM (np. libjava.so, libverify.so i libjvm.so
dla JRE Suna) przed uruchomieniem Apache'a lub interpretera PHP.

%package ldap
Summary:	LDAP extension module for PHP
Summary(pl.UTF-8):	Moduł LDAP dla PHP
Summary(pt_BR.UTF-8):	Um módulo para aplicações PHP que usam LDAP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(ldap)

%description ldap
This is a dynamic shared object (DSO) for PHP that will add LDAP
support.

%description ldap -l pl.UTF-8
Moduł PHP dodający obsługę LDAP.

%description ldap -l pt_BR.UTF-8
Um módulo para aplicações PHP que usam LDAP.

%package mbstring
Summary:	mbstring extension module for PHP
Summary(pl.UTF-8):	Moduł mbstring dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(mbstring)

%description mbstring
This is a dynamic shared object (DSO) for PHP that will add multibyte
string support.

%description mbstring -l pl.UTF-8
Moduł PHP dodający obsługę ciągów znaków wielobajtowych.

%package mcal
Summary:	mcal extension module for PHP
Summary(pl.UTF-8):	Moduł mcal dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(mcal)

%description mcal
This is a dynamic shared object (DSO) for PHP that will add mcal
(Modular Calendar Access Library) support.

%description mcal -l pl.UTF-8
Moduł PHP umożliwiający korzystanie z biblioteki mcal (dającej dostęp
do kalendarzy).

%package mcrypt
Summary:	mcrypt extension module for PHP
Summary(pl.UTF-8):	Moduł mcrypt dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(mcrypt)

%description mcrypt
This is a dynamic shared object (DSO) for PHP that will add mcrypt
support.

%description mcrypt -l pl.UTF-8
Moduł PHP dodający możliwość szyfrowania poprzez bibliotekę mcrypt.

%package mhash
Summary:	mhash extension module for PHP
Summary(pl.UTF-8):	Moduł mhash dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(mhash)

%description mhash
This is a dynamic shared object (DSO) for PHP that will add mhash
support.

%description mhash -l pl.UTF-8
Moduł PHP udostępniający funkcje mieszające z biblioteki mhash.

%package mime_magic
Summary:	mime_magic extension module for PHP
Summary(pl.UTF-8):	Moduł mime_magic dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	/usr/share/misc/magic.mime
Provides:	php(mime_magic)

%description mime_magic
This PHP module adds support for MIME type lookup via file magic
numbers using magic.mime database.

%description mime_magic -l pl.UTF-8
Moduł PHP dodający obsługę wyszukiwania typów MIME według magicznych
znaczników plików z użyciem bazy danych magic.mime.

%package ming
Summary:	ming extension module for PHP
Summary(pl.UTF-8):	Moduł ming dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(ming)

%description ming
This is a dynamic shared object (DSO) for PHP that will add ming
(Flash - .swf files) support.

%description ming -l pl.UTF-8
Moduł PHP dodający obsługę plików Flash (.swf) poprzez bibliotekę
ming.

%package mnogosearch
Summary:	mnoGoSearch extension module for PHP
Summary(pl.UTF-8):	Moduł mnoGoSearch dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(mnogosearch)

%description mnogosearch
This is a dynamic shared object (DSO) for PHP that will allow you to
access mnoGoSearch free search engine.

%description mnogosearch -l pl.UTF-8
Moduł PHP dodający pozwalający na dostęp do wolnodostępnego silnika
wyszukiwarki mnoGoSearch.

%package msession
Summary:	msession extension module for PHP
Summary(pl.UTF-8):	Moduł msession dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(msession)

%description msession
This is a dynamic shared object (DSO) for PHP that will allow you to
use msession. msession is a high speed session daemon which can run
either locally or remotely. It is designed to provide consistent
session management for a PHP web farm.

%description msession -l pl.UTF-8
Moduł PHP dodający umożliwiający korzystanie z demona msession. Jest
to demon szybkiej obsługi sesji, który może działać lokalnie lub na
innej maszynie. Służy do zapewniania spójnej obsługi sesji dla farmy
serwerów.

%package mssql
Summary:	MS SQL extension module for PHP
Summary(pl.UTF-8):	Moduł MS SQL dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(mssql)
Conflicts:	%{name}-sybase
Conflicts:	%{name}-sybase-ct

%description mssql
This is a dynamic shared object (DSO) for PHP that will add MS SQL
databases support through FreeTDS library.

%description mssql -l pl.UTF-8
Moduł PHP dodający obsługę baz danych MS SQL poprzez bibliotekę
FreeTDS.

%package mysql
Summary:	MySQL database module for PHP
Summary(pl.UTF-8):	Moduł bazy danych MySQL dla PHP
Summary(pt_BR.UTF-8):	Um módulo para aplicações PHP que usam bancos de dados MySQL
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(mysql)

%description mysql
This is a dynamic shared object (DSO) for PHP that will add MySQL
database support.

%description mysql -l pl.UTF-8
Moduł PHP umożliwiający dostęp do bazy danych MySQL.

%description mysql -l pt_BR.UTF-8
Um módulo para aplicações PHP que usam bancos de dados MySQL.

%package ncurses
Summary:	ncurses module for PHP
Summary(pl.UTF-8):	Moduł ncurses dla PHP
Group:		Libraries
Requires:	%{name}-cli = %{epoch}:%{version}-%{release}
Provides:	php(ncurses)

%description ncurses
This PHP module adds support for ncurses functions (only for cli and
cgi SAPIs).

%description ncurses -l pl.UTF-8
Moduł PHP dodający obsługę funkcji ncurses (tylko do SAPI cli i cgi).

%package oci8
Summary:	Oracle 8 database module for PHP
Summary(pl.UTF-8):	Moduł bazy danych Oracle 8 dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(oci8)
Autoreq:	false

%description oci8
This is a dynamic shared object (DSO) for PHP that will add Oracle 7
and Oracle 8 database support through Oracle8 Call-Interface (OCI8).

%description oci8 -l pl.UTF-8
Moduł PHP umożliwiający dostęp do bazy danych Oracle 7 i Oracle 8
poprzez interfejs Oracle8 Call-Interface (OCI8).

%package odbc
Summary:	ODBC extension module for PHP
Summary(pl.UTF-8):	Moduł ODBC dla PHP
Summary(pt_BR.UTF-8):	Um módulo para aplicações PHP que usam bases de dados ODBC
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	unixODBC >= 2.1.1-3
Provides:	php(odbc)

%description odbc
This is a dynamic shared object (DSO) for PHP that will add ODBC
support.

%description odbc -l pl.UTF-8
Moduł PHP ze wsparciem dla ODBC.

%description odbc -l pt_BR.UTF-8
Um módulo para aplicações PHP que usam ODBC.

%package oracle
Summary:	Oracle 7 database module for PHP
Summary(pl.UTF-8):	Moduł bazy danych Oracle 7 dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(oracle)
Autoreq:	false

%description oracle
This is a dynamic shared object (DSO) for PHP that will add Oracle 7
database support.

%description oracle -l pl.UTF-8
Moduł PHP umożliwiający dostęp do bazy danych Oracle 7.

%package overload
Summary:	Overload extension module for PHP
Summary(pl.UTF-8):	Moduł Overload dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(overload)

%description overload
This is a dynamic shared object (DSO) for PHP that will add user-space
object overloading support.

Warning: this is an experimental module.

%description overload -l pl.UTF-8
Moduł PHP umożliwiający przeciążanie obiektów.

Uwaga: to jest moduł eksperymentalny.

%package pcntl
Summary:	Process Control extension module for PHP
Summary(pl.UTF-8):	Moduł Process Control dla PHP
Group:		Libraries
Requires:	%{name}-cli = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(pcntl)

%description pcntl
This is a dynamic shared object (DSO) for PHP that will add process
spawning and control support. It supports functions like fork(),
waitpid(), signal() etc.

Warning: this is an experimental module. Also, don't use it in
webserver environment!

%description pcntl -l pl.UTF-8
Moduł PHP umożliwiający tworzenie nowych procesów i kontrolę nad nimi.
Obsługuje funkcje takie jak fork(), waitpid(), signal() i podobne.

Uwaga: to jest moduł eksperymentalny. Ponadto nie jest przeznaczony do
używania z serwerem WWW - nie próbuj tego!

%package pcre
Summary:	PCRE extension module for PHP
Summary(pl.UTF-8):	Moduł PCRE dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(pcre)

%description pcre
This is a dynamic shared object (DSO) for PHP that will add Perl
Compatible Regular Expression support.

%description pcre -l pl.UTF-8
Moduł PHP umożliwiający korzystanie z perlowych wyrażeń regularnych
(Perl Compatible Regular Expressions)

%package pdf
Summary:	PDF creation module module for PHP
Summary(pl.UTF-8):	Moduł do tworzenia plików PDF dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(pdf)

%description pdf
This is a dynamic shared object (DSO) for PHP that will add PDF
support through pdflib.

%description pdf -l pl.UTF-8
Moduł PHP umożliwiający tworzenie plików PDF. Wykorzystuje bibliotekę
pdflib.

%package pgsql
Summary:	PostgreSQL database module for PHP
Summary(pl.UTF-8):	Moduł bazy danych PostgreSQL dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(pgsql)

%description pgsql
This is a dynamic shared object (DSO) for PHP that will add PostgreSQL
database support.

%description pgsql -l pl.UTF-8
Moduł PHP umożliwiający dostęp do bazy danych PostgreSQL.

%description pgsql -l pt_BR.UTF-8
Um módulo para aplicações PHP que usam bancos de dados postgresql.

%package posix
Summary:	POSIX extension module for PHP
Summary(pl.UTF-8):	Moduł POSIX dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(posix)

%description posix
This is a dynamic shared object (DSO) for PHP that will add POSIX
functions support to PHP.

%description posix -l pl.UTF-8
Moduł PHP umożliwiający korzystanie z funkcji POSIX.

%package pspell
Summary:	pspell extension module for PHP
Summary(pl.UTF-8):	Moduł pspell dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(pspell)

%description pspell
This is a dynamic shared object (DSO) for PHP that will add pspell
support to PHP. It allows to check the spelling of a word and offer
suggestions.

%description pspell -l pl.UTF-8
Moduł PHP umożliwiający korzystanie z pspella. Pozwala on na
sprawdzanie pisowni słowa i sugerowanie poprawek.

%package qtdom
Summary:	Qt DOM extension module for PHP
Summary(pl.UTF-8):	Moduł Qt DOM dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(qtdom)

%description qtdom
This PHP module adds Qt DOM functions support.

%description qtdom -l pl.UTF-8
Moduł PHP dodający obsługę funkcji Qt DOM.

%package readline
Summary:	readline extension module for PHP
Summary(pl.UTF-8):	Moduł readline dla PHP
Group:		Libraries
Requires:	%{name}-cli = %{epoch}:%{version}-%{release}
Provides:	php(readline)

%description readline
This PHP module adds support for readline functions (only for cli and
cgi SAPIs).

%description readline -l pl.UTF-8
Moduł PHP dodający obsługę funkcji readline (tylko do SAPI cli i cgi).

%package recode
Summary:	recode extension module for PHP
Summary(pl.UTF-8):	Moduł recode dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	recode >= 3.5d-3
Provides:	php(recode)

%description recode
This is a dynamic shared object (DSO) for PHP that will add recode
support.

%description recode -l pl.UTF-8
Moduł PHP dodający możliwość konwersji kodowania plików (poprzez
bibliotekę recode).

%package shmop
Summary:	Shared Memory Operations extension module for PHP
Summary(pl.UTF-8):	Moduł shmop dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(shmop)

%description shmop
This is a dynamic shared object (DSO) for PHP that will add Shared
Memory Operations support.

Warning: this is an experimental module.

%description shmop -l pl.UTF-8
Moduł PHP umożliwiający korzystanie z pamięci dzielonej.

Uwaga: to jest moduł eksperymentalny.

%package snmp
Summary:	SNMP extension module for PHP
Summary(pl.UTF-8):	Moduł SNMP dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(snmp)

%description snmp
This is a dynamic shared object (DSO) for PHP that will add SNMP
support.

%description snmp -l pl.UTF-8
Moduł PHP dodający obsługę SNMP.

%package sockets
Summary:	sockets extension module for PHP
Summary(pl.UTF-8):	Moduł socket dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(sockets)

%description sockets
This is a dynamic shared object (DSO) for PHP that will add sockets
support.

Warning: this is an experimental module.

%description sockets -l pl.UTF-8
Moduł PHP dodający obsługę gniazdek.

Uwaga: to jest moduł eksperymentalny.

%package sybase
Summary:	Sybase DB extension module for PHP
Summary(pl.UTF-8):	Moduł Sybase DB dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(sybase)
Obsoletes:	php4-sybase-ct
Conflicts:	%{name}-mssql

%description sybase
This is a dynamic shared object (DSO) for PHP that will add Sybase and
MS SQL databases support through SYBDB library. Currently Sybase
module is not maintained. Using Sybase-CT module is recommended
instead.

%description sybase -l pl.UTF-8
Moduł PHP dodający obsługę baz danych Sybase oraz MS SQL poprzez
bibliotekę SYBDB. W chwili obecnej moduł Sybase nie jest wspierany.
Zaleca się używanie modułu Sybase-CT.

%package sybase-ct
Summary:	Sybase-CT extension module for PHP
Summary(pl.UTF-8):	Moduł Sybase-CT dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(sybase-ct)
Obsoletes:	php4-sybase
Conflicts:	%{name}-mssql

%description sybase-ct
This is a dynamic shared object (DSO) for PHP that will add Sybase and
MS SQL databases support through CT-lib.

%description sybase-ct -l pl.UTF-8
Moduł PHP dodający obsługę baz danych Sybase oraz MS SQL poprzez
CT-lib.

%package sysvmsg
Summary:	SysV msg extension module for PHP
Summary(pl.UTF-8):	Moduł SysV msg dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(sysvmsg)

%description sysvmsg
This is a dynamic shared object (DSO) for PHP that will add SysV
message queues support.

%description sysvmsg -l pl.UTF-8
Moduł PHP umożliwiający korzystanie z kolejek komunikatów SysV.

%package sysvsem
Summary:	SysV sem extension module for PHP
Summary(pl.UTF-8):	Moduł SysV sem dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(sysvsem)

%description sysvsem
This is a dynamic shared object (DSO) for PHP that will add SysV
semaphores support.

%description sysvsem -l pl.UTF-8
Moduł PHP umożliwiający korzystanie z semaforów SysV.

%package sysvshm
Summary:	SysV shm extension module for PHP
Summary(pl.UTF-8):	Moduł SysV shm dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(sysvshm)

%description sysvshm
This is a dynamic shared object (DSO) for PHP that will add SysV
Shared Memory support.

%description sysvshm -l pl.UTF-8
Moduł PHP umożliwiający korzystanie z pamięci dzielonej SysV.

%package tokenizer
Summary:	tokenizer extension module for PHP
Summary(pl.UTF-8):	Moduł rozszerzenia tokenizer dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(tokenizer)

%description tokenizer
This is a dynamic shared object (DSO) for PHP that will add tokenizer
support.

%description tokenizer -l pl.UTF-8
Moduł PHP dodający obsługę tokenizera do PHP.

%package wddx
Summary:	wddx extension module for PHP
Summary(pl.UTF-8):	Moduł wddx dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
#Requires:	%{name}-session = %{epoch}:%{version}-%{release}
Requires:	%{name}-xml = %{epoch}:%{version}-%{release}
Provides:	php(wddx)

%description wddx
This is a dynamic shared object (DSO) for PHP that will add wddx
support.

%description wddx -l pl.UTF-8
Moduł PHP umożliwiający korzystanie z wddx.

%package xml
Summary:	XML extension module for PHP
Summary(pl.UTF-8):	Moduł XML dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(xml)

%description xml
This is a dynamic shared object (DSO) for PHP that will add XML
support. This extension lets you create XML parsers and then define
handlers for different XML events.

%description xml -l pl.UTF-8
Moduł PHP umożliwiający parsowanie plików XML i obsługę zdarzeń
związanych z tymi plikami. Pozwala on tworzyć analizatory XML-a i
następnie definiować procedury obsługi dla różnych zdarzeń XML.

%package xmlrpc
Summary:	xmlrpc extension module for PHP
Summary(pl.UTF-8):	Moduł xmlrpc dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(xmlrpc)

%description xmlrpc
This is a dynamic shared object (DSO) for PHP that will add XMLRPC
support.

Warning: this is an experimental module.

%description xmlrpc -l pl.UTF-8
Moduł PHP dodający obsługę XMLRPC.

Uwaga: to jest moduł eksperymentalny.

%package xslt
Summary:	xslt extension module for PHP
Summary(pl.UTF-8):	Moduł xslt dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(xslt)

%description xslt
This is a dynamic shared object (DSO) for PHP that will add xslt
support.

%description xslt -l pl.UTF-8
Moduł PHP umożliwiający korzystanie z technologii xslt.

%package yaz
Summary:	yaz extension module for PHP
Summary(pl.UTF-8):	Moduł yaz dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	yaz >= 1.9
Provides:	php(yaz)

%description yaz
This is a dynamic shared object (DSO) for PHP that will add yaz
support. yaz toolkit implements the Z39.50 protocol for information
retrieval.

%description yaz -l pl.UTF-8
Moduł PHP umożliwiający korzystanie z yaz - implementacji protokołu
Z39.50 służącego do pozyskiwania informacji.

%package yp
Summary:	NIS (yp) extension module for PHP
Summary(pl.UTF-8):	Moduł NIS (yp) dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(yp)

%description yp
This is a dynamic shared object (DSO) for PHP that will add NIS
(Yellow Pages) support.

%description yp -l pl.UTF-8
Moduł PHP dodający wsparcie dla NIS (Yellow Pages).

%package zip
Summary:	zip extension module for PHP
Summary(pl.UTF-8):	Moduł zip dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(zip)

%description zip
This is a dynamic shared object (DSO) for PHP that will add ZZipLib
(read-only access to ZIP archives) support.

%description zip -l pl.UTF-8
Moduł PHP umożliwiający korzystanie z bibliotekli ZZipLib
(pozwalającej na odczyt archiwów ZIP).

%package zlib
Summary:	Zlib extension module for PHP
Summary(pl.UTF-8):	Moduł zlib dla PHP
Group:		Libraries
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php(zlib)

%description zlib
This is a dynamic shared object (DSO) for PHP that will add zlib
compression support to PHP.

%description zlib -l pl.UTF-8
Moduł PHP umożliwiający używanie kompresji zlib.

%prep
%setup -q -n php-%{version}
#%patch43 -p1
%patch40 -p1
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
# Not really needed?
#%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
cp php.ini-dist php.ini
%patch17 -p1
# for ac2.53b/am1.6b - AC_LANG_CXX has AM_CONDITIONAL, so cannot be invoked
# conditionally...
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1

%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%{?with_versioning:%patch39 -p1}
# XXX: I believe this one is obsolete as of 4.4.3
#%patch41 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch45 -p1
%patch46 -p1
%patch47 -p1
%patch48 -p1
%patch49 -p1
%patch50 -p1
%patch51 -p1
%if "%{_lib}" == "lib64"
%patch52 -p1
%endif
%patch53 -p1
%patch54 -p1
%patch55 -p1
%patch56 -p1
%patch57 -p1
%patch58 -p1
%patch59 -p1
%if "%{_lib}" == "libx32"
%patch60 -p1
%endif

%if %{with hardening}
zcat %{SOURCE8} | patch -p1
%endif

cp -f Zend/LICENSE{,.Zend}

%build
API=$(awk '/#define PHP_API_VERSION/{print $3}' main/php.h)
if [ $API != %{php_api_version} ]; then
	echo "Set %%define php_api_version to $API and re-run."
	exit 1
fi

API=$(awk '/#define ZEND_MODULE_API_NO/{print $3}' Zend/zend_modules.h)
if [ $API != %{zend_module_api} ]; then
	echo "Set %%define zend_module_api to $API and re-run."
	exit 1
fi

API=$(awk '/#define ZEND_EXTENSION_API_NO/{print $3}' Zend/zend_extensions.h)
if [ $API != %{zend_extension_api} ]; then
	echo "Set %%define zend_extension_api to $API and re-run."
	exit 1
fi

export EXTENSION_DIR="%{extensionsdir}"
if [ ! -f _built-conf ]; then # configure once (for faster debugging purposes)
	rm -f Makefile.{fcgi,cgi,cli,apxs{1,2}} # now remove Makefile copies
	%{__libtoolize}
	%{__aclocal}
	cp -f /usr/share/automake/config.{sub,guess} .
	./buildconf --force
	touch _built-conf
fi
export PROG_SENDMAIL="/usr/lib/sendmail"

sapis="
%if %{with fcgi}
fcgi
%endif
cgi cli
%if %{with apache1}
apxs1
%endif
%if %{with apache2}
apxs2
%endif
"
for sapi in $sapis; do
	: SAPI $sapi
	[ -f Makefile.$sapi ] && continue # skip if already configured (for faster debugging purposes)

	sapi_args=''
	case $sapi in
	cgi)
		sapi_args='--enable-discard-path --enable-force-cgi-redirect'
		;;
	cli)
		sapi_args='--disable-cgi'
		;;
	fcgi)
		sapi_args='--enable-fastcgi --with-fastcgi=/usr --enable-force-cgi-redirect'
		;;
	apxs1)
		ver=$(rpm -q --qf '%{V}' apache1-devel)
		sapi_args="--with-apxs=%{apxs1} --with-apache-version=$ver"
		;;
	apxs2)
		ver=$(rpm -q --qf '%{V}' apache-devel)
		sapi_args="--with-apxs2=%{apxs2} --with-apache-version=$ver"
		;;
	esac

	%configure \
	$sapi_args \
%if "%{!?configure_cache:0}%{?configure_cache}" == "0"
	--cache-file=config.cache \
%endif
	--with-config-file-path=%{_sysconfdir} \
	--with-config-file-scan-dir=%{_sysconfdir}/conf.d \
	--with-exec-dir=%{_bindir} \
	--%{!?debug:dis}%{?debug:en}able-debug \
	%{?with_zts:--enable-experimental-zts} \
	--enable-inline-optimization \
	--enable-shared \
	--disable-static \
	--enable-bcmath=shared \
	--enable-calendar=shared \
	--enable-ctype=shared \
	--enable-dba=shared \
	--enable-dbx=shared \
	--enable-dio=shared \
	--enable-exif=shared \
	--enable-filepro=shared \
	--enable-ftp=shared \
	--enable-magic-quotes \
	--enable-mbstring=shared,all --enable-mbregex \
	--enable-memory-limit \
	--enable-overload=shared \
	--enable-pcntl=shared \
	--enable-posix=shared \
	%{?with_recode:--with-recode=shared} \
	--enable-safe-mode \
	--enable-session --enable-trans-sid \
	--enable-shmop=shared \
	--enable-sockets=shared \
	--enable-sysvmsg=shared \
	--enable-sysvsem=shared \
	--enable-sysvshm=shared \
	--enable-tokenizer=shared \
	--enable-track-vars \
	%{?with_wddx:--enable-wddx=shared} \
	%{!?with_xml:--disable-xml}%{?with_xml:--enable-xml=shared} \
	%{?with_xslt:--enable-xslt=shared} \
	%{?with_yp:--enable-yp=shared} \
	--with-bz2=shared \
	%{?with_cpdf:--with-cpdflib=shared} \
	--with-crack=shared \
	%{!?with_curl:--without-curl}%{?with_curl:--with-curl=shared} \
	--with-db=shared --with-db%{?with_db3:3}%{!?with_db3:4} \
	--with-dbase=shared \
	%{?with_domxslt:--with-dom-xslt=shared --with-dom-exslt=shared} \
%if %{with xml} || %{with xmlrpc}
	--with-expat-dir=shared,/usr \
%else
	--without-expat-dir \
%endif
	%{?with_fdf:--with-fdftk=shared} \
	--with-filepro=shared \
	--with-freetype-dir=shared \
	%{?with_fribidi:--with-fribidi=shared} \
	--with-gd=shared --enable-gd-native-ttf \
	--with-gdbm \
	--with-gettext=shared \
	--with-gmp=shared \
	--with-hyperwave=shared \
	--with-iconv=shared \
	%{?with_imap:--with-imap=shared --with-imap-ssl --with-kerberos} \
	%{?with_interbase:--with-interbase=shared%{!?with_interbase_inst:,/usr}} \
	%{?with_java:--with-java=%{_libdir}/java} \
	--with-jpeg-dir=/usr \
	%{?with_ldap:--with-ldap=shared} \
	--with-mcal=shared,/usr \
	--with-mcrypt=shared \
	%{?with_mhash:--with-mhash=shared} \
	--with-mime-magic=shared,/usr/share/misc/magic.mime \
	%{?with_ming:--with-ming=shared} \
	%{!?with_mnogosearch:--without-mnogosearch}%{?with_mnogosearch:--with-mnogosearch=shared,/usr} \
	%{?with_msession:--with-msession=shared}%{!?with_msession:--without-msession} \
	%{?with_mssql:--with-mssql=shared} \
	--with-mysql=shared,/usr --with-mysql-sock=/var/lib/mysql/mysql.sock \
	--with-ncurses=shared \
	%{?with_oci8:--with-oci8=shared} \
	%{?with_odbc:--with-unixODBC=shared} \
	%{?with_openssl:--with-openssl} \
	%{?with_oracle:--with-oracle=shared} \
	%{!?with_pcre:--without-pcre-regex}%{?with_pcre:--with-pcre-regex=shared,/usr} \
	%{?with_pdf:--with-pdflib=shared} \
	--with-pear=%{php_pear_dir} \
	%{!?with_pgsql:--without-pgsql}%{?with_pgsql:--with-pgsql=shared,/usr} \
	--with-png-dir=/usr \
	%{?with_qtdom:--with-qtdom=shared} \
	--with-readline=shared \
	--with-regex=php \
	%{?with_snmp:--with-snmp=shared --enable-ucd-snmp-hack} \
	%{?with_pspell:--with-pspell=shared} \
	%{?with_sybase:--with-sybase-ct=shared,/usr --with-sybase=shared,/usr} \
	--with-t1lib=shared \
	--with-tiff-dir=/usr \
	%{?with_xml:--with-dom=shared} \
	%{!?with_xmlrpc:--without-xmlrpc}%{?with_xmlrpc:--with-xmlrpc=shared%{?with_system_xmlrpc_epi:,/usr}} \
	%{?with_xslt:--with-xslt-sablot=shared} --without-sablot-js \
	%{?with_yaz:--with-yaz=shared} \
	--with-zip=shared \
	--with-zlib=shared --with-zlib-dir=shared,/usr \

	cp -f Makefile Makefile.$sapi
	cp -f main/php_config.h php_config.h.$sapi
done

# must make this first, so modules can link against it.
%{__make} libphp_common.la
%{__make} build-modules

# version suffix
v=$(echo %{version} | cut -d. -f1-2)

%if %{with apache1}
%{__make} libtool-sapi LIBTOOL_SAPI=sapi/apache/libphp4.la -f Makefile.apxs1
%endif

%if %{with apache2}
%{__make} libtool-sapi LIBTOOL_SAPI=sapi/apache2handler/libphp4.la -f Makefile.apxs2
%endif

# FCGI
%if %{with fcgi}
cp -af php_config.h.fcgi main/php_config.h
rm -rf sapi/cgi/.libs sapi/cgi/*.lo
%{__make} sapi/cgi/php -f Makefile.fcgi
cp -r sapi/cgi sapi/fcgi
[ "$(echo '<?=php_sapi_name();' | ./sapi/fcgi/php -qn)" = cgi-fcgi ] || exit 1
%endif

# CGI
cp -af php_config.h.cgi main/php_config.h
rm -rf sapi/cgi/.libs sapi/cgi/*.lo
%{__make} sapi/cgi/php -f Makefile.cgi
[ "$(echo '<?=php_sapi_name();' | ./sapi/cgi/php -qn)" = cgi ] || exit 1

# CLI
cp -af php_config.h.cli main/php_config.h
%{__make} sapi/cli/php -f Makefile.cli
[ "$(echo '<?=php_sapi_name();' | ./sapi/cli/php -n)" = cli ] || exit 1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/{php,apache{,1}},%{_sysconfdir}} \
	$RPM_BUILD_ROOT{%{_sbindir},%{_bindir}} \
	$RPM_BUILD_ROOT{/etc/apache/conf.d,/etc/httpd/conf.d} \
	$RPM_BUILD_ROOT%{_mandir}/man1

v=$(echo %{version} | cut -d. -f1-2)

# install the apache modules' files
%{__make} install-headers install-build install-modules install-programs \
	INSTALL_ROOT=$RPM_BUILD_ROOT

libtool --silent --mode=install install libphp_common.la $RPM_BUILD_ROOT%{_libdir}
# fix install paths, avoid evil rpaths
sed -i -e "s|^libdir=.*|libdir='%{_libdir}'|" $RPM_BUILD_ROOT%{_libdir}/libphp_common.la

# install apache1 DSO module
%if %{with apache1}
libtool --silent --mode=install install sapi/apache/libphp4.la $RPM_BUILD_ROOT%{_libdir}/apache1
rm $RPM_BUILD_ROOT%{_libdir}/apache1/libphp4.la

mv $RPM_BUILD_ROOT%{_libdir}/apache1/libphp4{,-$v}.so
ln -s libphp4-$v.so $RPM_BUILD_ROOT%{_libdir}/apache1/mod_php.so
%endif

# install apache2 DSO module
%if %{with apache2}
libtool --silent --mode=install install sapi/apache2handler/libphp4.la $RPM_BUILD_ROOT%{_libdir}/apache
rm $RPM_BUILD_ROOT%{_libdir}/apache/libphp4.la

mv $RPM_BUILD_ROOT%{_libdir}/apache/libphp4{,-$v}.so
ln -s libphp4-$v.so $RPM_BUILD_ROOT%{_libdir}/apache/mod_php.so
%endif

# better solution?
sed -i -e 's|libphp_common.la|$(libdir)/libphp_common.la|' $RPM_BUILD_ROOT%{_libdir}/php/build/acinclude.m4

# install CGI
libtool --silent --mode=install install sapi/cgi/php $RPM_BUILD_ROOT%{_bindir}/php4.cgi

# install FCGI
%if %{with fcgi}
libtool --silent --mode=install install sapi/fcgi/php $RPM_BUILD_ROOT%{_bindir}/php4.fcgi
%endif

# install CLI
libtool --silent --mode=install install sapi/cli/php $RPM_BUILD_ROOT%{_bindir}/php4.cli

install sapi/cli/php.1 $RPM_BUILD_ROOT%{_mandir}/man1/php4.1
ln -sf php4.cli $RPM_BUILD_ROOT%{_bindir}/php4
ln -sf php4.cli $RPM_BUILD_ROOT%{_bindir}/php

%{?with_java:install ext/java/php_java.jar $RPM_BUILD_ROOT%{extensionsdir}}

install php.ini	$RPM_BUILD_ROOT%{_sysconfdir}/php.ini
%if %{with fcgi}
install %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/php-cgi-fcgi.ini
%endif
install %{SOURCE5} $RPM_BUILD_ROOT%{_sysconfdir}/php-cgi.ini
install %{SOURCE7} $RPM_BUILD_ROOT%{_sysconfdir}/php-cli.ini

%if %{with apache1}
install %{SOURCE3} $RPM_BUILD_ROOT/etc/apache/conf.d/70_mod_php4.conf
install %{SOURCE6} $RPM_BUILD_ROOT%{_sysconfdir}/php-apache.ini
%endif

%if %{with apache2}
install %{SOURCE3} $RPM_BUILD_ROOT/etc/httpd/conf.d/70_mod_php4.conf
install %{SOURCE6} $RPM_BUILD_ROOT%{_sysconfdir}/php-apache2handler.ini
%endif

# Generate stub .ini files for each subpackage
install -d $RPM_BUILD_ROOT%{_sysconfdir}/conf.d
generate_inifiles() {
	for so in modules/*.so; do
		mod=$(basename $so .so)
		conf="%{_sysconfdir}/conf.d/$mod.ini"
		# xml needs to be loaded before wddx
		[ "$mod" = "wddx" ] && conf="%{_sysconfdir}/conf.d/xml_$mod.ini"
		echo "+ $conf"
		cat > $RPM_BUILD_ROOT$conf <<-EOF
			; Enable $mod extension module
			extension=$mod.so
		EOF
	done
}
generate_inifiles

# per SAPI ini directories
install -d $RPM_BUILD_ROOT%{_sysconfdir}/{cgi,cli,cgi-fcgi,apache,apache2handler}.d

# for CLI SAPI only
mv $RPM_BUILD_ROOT%{_sysconfdir}/{conf.d/{ncurses,pcntl,readline}.ini,cli.d}

# use system automake and {lib,sh}tool
%if "%{pld_release}" != "ac"
	ln -snf /usr/share/automake/config.{guess,sub} $RPM_BUILD_ROOT%{_libdir}/php/build
	for i in libtool.m4 lt~obsolete.m4 ltoptions.m4 ltsugar.m4 ltversion.m4; do
		ln -snf %{_aclocaldir}/${i} $RPM_BUILD_ROOT%{_libdir}/php/build
	done
	ln -snf %{_datadir}/libtool/config/ltmain.sh $RPM_BUILD_ROOT%{_libdir}/php/build
%else
	ln -snf %{_aclocaldir}/libtool.m4 $RPM_BUILD_ROOT%{_libdir}/php/build
	ln -snf %{_datadir}/libtool/ltmain.sh $RPM_BUILD_ROOT%{_libdir}/php/build
%endif
ln -snf %{_bindir}/shtool $RPM_BUILD_ROOT%{_libdir}/php/build

# as a result of ext/pcre/pcrelib removal in %%prep, ext/pcre/php_pcre.h
# isn't installed by install-headers make target, we do it manually here.
# this header file is required by e.g. filter PECL extension
install -D ext/pcre/php_pcre.h $RPM_BUILD_ROOT%{_includedir}/php/ext/pcre/php_pcre.h

%clean
rm -rf $RPM_BUILD_ROOT

%post -n apache1-mod_php4
if [ "$1" = "1" ]; then
	%service -q apache restart
fi

%postun -n apache1-mod_php4
if [ "$1" = "0" ]; then
	%service -q apache restart
fi

%post -n apache-mod_php4
if [ "$1" = "1" ]; then
	%service -q httpd restart
fi

%postun -n apache-mod_php4
if [ "$1" = "0" ]; then
	%service -q httpd restart
fi

# so tired of typing... so decided to create macros
# macro called at extension post scriptlet
%define	extension_post \
if [ "$1" = "1" ]; then \
	[ ! -f /etc/apache/conf.d/??_mod_php4.conf ] || %service -q apache restart \
	[ ! -f /etc/httpd/conf.d/??_mod_php4.conf ] || %service -q httpd restart \
fi

# macro called at extension postun scriptlet
%define	extension_postun \
if [ "$1" = "0" ]; then \
	[ ! -f /etc/apache/conf.d/??_mod_php4.conf ] || %service -q apache restart \
	[ ! -f /etc/httpd/conf.d/??_mod_php4.conf ] || %service -q httpd restart \
fi

%post	common -p /sbin/ldconfig
%postun	common -p /sbin/ldconfig

%posttrans common
# minimizing apache restarts logics. we restart webserver:
#
# 1. at the end of transaction. (posttrans, feature from rpm 4.4.2)
# 2. first install of extension (post: $1 = 1)
# 2. uninstall of extension (postun: $1 == 0)
#
# the strict internal deps between extensions (and apache modules) and
# common package are very important for all this to work.

# restart webserver at the end of transaction
[ ! -f /etc/apache/conf.d/??_mod_php4.conf ] || %service -q apache restart
[ ! -f /etc/httpd/conf.d/??_mod_php4.conf ] || %service -q httpd restart

%if %{with apache2}
%triggerpostun -n apache-mod_php4 -- apache-mod_php4 < 3:4.4.0-2.16, php4 < 3:4.3.11-4.16
# for fixed php-SAPI.ini, the poor php-apache.ini was never read for apache2
if [ -f %{_sysconfdir}/php-apache.ini.rpmsave ]; then
	cp -f %{_sysconfdir}/php-apache2handler.ini{,.rpmnew}
	mv -f %{_sysconfdir}/php-apache.ini.rpmsave %{_sysconfdir}/php-apache2handler.ini
fi
%endif

%triggerpostun -n apache1-mod_%{name} -- apache1-mod_%{name} < 3:4.4.9-51
sed -i -e 's#modules/libphp4.so#modules/mod_php.so#g' /etc/apache/conf.d/*_mod_php4.conf

%triggerpostun -n apache-mod_%{name} -- apache-mod_%{name} < 3:4.4.9-51
sed -i -e 's#modules/libphp4.so#modules/mod_php.so#g' /etc/httpd/conf.d/*_mod_php4.conf

%post bcmath
%extension_post

%postun bcmath
%extension_postun

%post bzip2
%extension_post

%postun bzip2
%extension_postun

%post calendar
%extension_post

%postun calendar
%extension_postun

%post cpdf
%extension_post

%postun cpdf
%extension_postun

%post crack
%extension_post

%postun crack
%extension_postun

%post ctype
%extension_post

%postun ctype
%extension_postun

%post curl
%extension_post

%postun curl
%extension_postun

%post db
%extension_post

%postun db
%extension_postun

%post dba
%extension_post

%postun dba
%extension_postun

%post dbase
%extension_post

%postun dbase
%extension_postun

%post dbx
%extension_post

%postun dbx
%extension_postun

%post dio
%extension_post

%postun dio
%extension_postun

%post domxml
%extension_post

%postun domxml
%extension_postun

%post exif
%extension_post

%postun exif
%extension_postun

%post fdf
%extension_post

%postun fdf
%extension_postun

%post filepro
%extension_post

%postun filepro
%extension_postun

%post fribidi
%extension_post

%postun fribidi
%extension_postun

%post ftp
%extension_post

%postun ftp
%extension_postun

%post gd
%extension_post

%postun gd
%extension_postun

%post gettext
%extension_post

%postun gettext
%extension_postun

%post gmp
%extension_post

%postun gmp
%extension_postun

%post hyperwave
%extension_post

%postun hyperwave
%extension_postun

%post iconv
%extension_post

%postun iconv
%extension_postun

%post imap
%extension_post

%postun imap
%extension_postun

%post interbase
%extension_post

%postun interbase
%extension_postun

%post java
%extension_post

%postun java
%extension_postun

%post ldap
%extension_post

%postun ldap
%extension_postun

%post mbstring
%extension_post

%postun mbstring
%extension_postun

%post mcal
%extension_post

%postun mcal
%extension_postun

%post mcrypt
%extension_post

%postun mcrypt
%extension_postun

%post mhash
%extension_post

%postun mhash
%extension_postun

%post mime_magic
%extension_post

%postun mime_magic
%extension_postun

%post ming
%extension_post

%postun ming
%extension_postun

%post mnogosearch
%extension_post

%postun mnogosearch
%extension_postun

%post msession
%extension_post

%postun msession
%extension_postun

%post mssql
%extension_post

%postun mssql
%extension_postun

%post mysql
%extension_post

%postun mysql
%extension_postun

%post oci8
%extension_post

%postun oci8
%extension_postun

%post odbc
%extension_post

%postun odbc
%extension_postun

%post oracle
%extension_post

%postun oracle
%extension_postun

%post overload
%extension_post

%postun overload
%extension_postun

%post pcre
%extension_post

%postun pcre
%extension_postun

%post pdf
%extension_post

%postun pdf
%extension_postun

%post pgsql
%extension_post

%postun pgsql
%extension_postun

%post posix
%extension_post

%postun posix
%extension_postun

%post pspell
%extension_post

%postun pspell
%extension_postun

%post qtdom
%extension_post

%postun qtdom
%extension_postun

%post recode
%extension_post

%postun recode
%extension_postun

%post shmop
%extension_post

%postun shmop
%extension_postun

%post snmp
%extension_post

%postun snmp
%extension_postun

%post sockets
%extension_post

%postun sockets
%extension_postun

%post sybase
%extension_post

%postun sybase
%extension_postun

%post sybase-ct
%extension_post

%postun sybase-ct
%extension_postun

%post sysvmsg
%extension_post

%postun sysvmsg
%extension_postun

%post sysvsem
%extension_post

%postun sysvsem
%extension_postun

%post sysvshm
%extension_post

%postun sysvshm
%extension_postun

%post tokenizer
%extension_post

%postun tokenizer
%extension_postun

%post wddx
%extension_post

%postun wddx
%extension_postun

%post xml
%extension_post

%postun xml
%extension_postun

%post xmlrpc
%extension_post

%postun xmlrpc
%extension_postun

%post xslt
%extension_post

%postun xslt
%extension_postun

%post yaz
%extension_post

%postun yaz
%extension_postun

%post yp
%extension_post

%postun yp
%extension_postun

%post zip
%extension_post

%postun zip
%extension_postun

%post zlib
%extension_post

%postun zlib
%extension_postun

# openssl trigger on common package. it removes shared openssl module from php.ini, if it was there.
%triggerun common -- %{name}-openssl < 3:4.4.0-4
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*openssl\.so/d' %{_sysconfdir}/php.ini

%triggerun bcmath -- %{name}-bcmath < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*bcmath\.so/d' %{_sysconfdir}/php.ini

%triggerun bzip2 -- %{name}-bzip2 < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*bz2\.so/d' %{_sysconfdir}/php.ini

%triggerun calendar -- %{name}-calendar < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*calendar\.so/d' %{_sysconfdir}/php.ini

%triggerun cpdf -- %{name}-cpdf < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*cpdf\.so/d' %{_sysconfdir}/php.ini

%triggerun crack -- %{name}-crack < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*crack\.so/d' %{_sysconfdir}/php.ini

%triggerun ctype -- %{name}-ctype < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*ctype\.so/d' %{_sysconfdir}/php.ini

%triggerun curl -- %{name}-curl < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*curl\.so/d' %{_sysconfdir}/php.ini

%triggerun db -- %{name}-db < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*db\.so/d' %{_sysconfdir}/php.ini

%triggerun dba -- %{name}-dba < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*dba\.so/d' %{_sysconfdir}/php.ini

%triggerun dbase -- %{name}-dbase < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*dbase\.so/d' %{_sysconfdir}/php.ini

%triggerun dbx -- %{name}-dbx < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*dbx\.so/d' %{_sysconfdir}/php.ini

%triggerun dio -- %{name}-dio < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*dio\.so/d' %{_sysconfdir}/php.ini

%triggerun domxml -- %{name}-domxml < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*domxml\.so/d' %{_sysconfdir}/php.ini

%triggerun exif -- %{name}-exif < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*exif\.so/d' %{_sysconfdir}/php.ini

%triggerun fdf -- %{name}-fdf < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*fdf\.so/d' %{_sysconfdir}/php.ini

%triggerun filepro -- %{name}-filepro < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*filepro\.so/d' %{_sysconfdir}/php.ini

%triggerun fribidi -- %{name}-fribidi < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*fribidi\.so/d' %{_sysconfdir}/php.ini

%triggerun ftp -- %{name}-ftp < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*ftp\.so/d' %{_sysconfdir}/php.ini

%triggerun gd -- %{name}-gd < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*gd\.so/d' %{_sysconfdir}/php.ini

%triggerun gettext -- %{name}-gettext < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*gettext\.so/d' %{_sysconfdir}/php.ini

%triggerun gmp -- %{name}-gmp < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*gmp\.so/d' %{_sysconfdir}/php.ini

%triggerun hyperwave -- %{name}-hyperwave < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*hyperwave\.so/d' %{_sysconfdir}/php.ini

%triggerun iconv -- %{name}-iconv < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*iconv\.so/d' %{_sysconfdir}/php.ini

%triggerun imap -- %{name}-imap < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*imap\.so/d' %{_sysconfdir}/php.ini

%triggerun interbase -- %{name}-interbase < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*interbase\.so/d' %{_sysconfdir}/php.ini

%triggerun java -- %{name}-java < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*java\.so/d' %{_sysconfdir}/php.ini

%triggerun ldap -- %{name}-ldap < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*ldap\.so/d' %{_sysconfdir}/php.ini

%triggerun mbstring -- %{name}-mbstring < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*mbstring\.so/d' %{_sysconfdir}/php.ini

%triggerun mcal -- %{name}-mcal < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*mcal\.so/d' %{_sysconfdir}/php.ini

%triggerun mcrypt -- %{name}-mcrypt < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*mcrypt\.so/d' %{_sysconfdir}/php.ini

%triggerun mhash -- %{name}-mhash < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*mhash\.so/d' %{_sysconfdir}/php.ini

%triggerun mime_magic -- %{name}-mime_magic < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*mime_magic\.so/d' %{_sysconfdir}/php.ini

%triggerun ming -- %{name}-ming < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*ming\.so/d' %{_sysconfdir}/php.ini

%triggerun mnogosearch -- %{name}-mnogosearch < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*mnogosearch\.so/d' %{_sysconfdir}/php.ini

%triggerun msession -- %{name}-msession < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*msession\.so/d' %{_sysconfdir}/php.ini

%triggerun mssql -- %{name}-mssql < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*mssql\.so/d' %{_sysconfdir}/php.ini

%triggerun mysql -- %{name}-mysql < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*mysql\.so/d' %{_sysconfdir}/php.ini

%triggerun ncurses -- %{name}-ncurses < 3:4.4.2-9.4
if [ -f %{_sysconfdir}/php-cgi.ini ]; then
	%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*ncurses\.so/d' %{_sysconfdir}/php-cgi.ini
fi
if [ -f %{_sysconfdir}/php-cli.ini ]; then
	%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*ncurses\.so/d' %{_sysconfdir}/php-cli.ini
fi

%triggerun oci8 -- %{name}-oci8 < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*oci8\.so/d' %{_sysconfdir}/php.ini

%triggerun odbc -- %{name}-odbc < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*odbc\.so/d' %{_sysconfdir}/php.ini

%triggerun oracle -- %{name}-oracle < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*oracle\.so/d' %{_sysconfdir}/php.ini

%triggerun overload -- %{name}-overload < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*overload\.so/d' %{_sysconfdir}/php.ini

%triggerun pcntl -- %{name}-pcntl < 3:4.4.2-9.4
if [ -f %{_sysconfdir}/php-cgi.ini ]; then
	%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*pcntl\.so/d' %{_sysconfdir}/php-cgi.ini
fi
if [ -f %{_sysconfdir}/php-cli.ini ]; then
	%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*pcntl\.so/d' %{_sysconfdir}/php-cli.ini
fi

%triggerun pcre -- %{name}-pcre < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*pcre\.so/d' %{_sysconfdir}/php.ini

%triggerun pdf -- %{name}-pdf < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*pdf\.so/d' %{_sysconfdir}/php.ini

%triggerun pgsql -- %{name}-pgsql < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*pgsql\.so/d' %{_sysconfdir}/php.ini

%triggerun posix -- %{name}-posix < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*posix\.so/d' %{_sysconfdir}/php.ini

%triggerun pspell -- %{name}-pspell < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*pspell\.so/d' %{_sysconfdir}/php.ini

%triggerun qtdom -- %{name}-qtdom < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*qtdom\.so/d' %{_sysconfdir}/php.ini

%triggerun readline -- %{name}-readline < 3:4.4.2-9.4
if [ -f %{_sysconfdir}/php-cgi.ini ]; then
	%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*readline\.so/d' %{_sysconfdir}/php-cgi.ini
fi
if [ -f %{_sysconfdir}/php-cli.ini ]; then
	%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*readline\.so/d' %{_sysconfdir}/php-cli.ini
fi

%triggerun recode -- %{name}-recode < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*recode\.so/d' %{_sysconfdir}/php.ini

%triggerun shmop -- %{name}-shmop < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*shmop\.so/d' %{_sysconfdir}/php.ini

%triggerun snmp -- %{name}-snmp < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*snmp\.so/d' %{_sysconfdir}/php.ini

%triggerun sockets -- %{name}-sockets < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*sockets\.so/d' %{_sysconfdir}/php.ini

%triggerun sybase -- %{name}-sybase < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*sybase\.so/d' %{_sysconfdir}/php.ini

%triggerun sybase-ct -- %{name}-sybase-ct < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*sybase_ct\.so/d' %{_sysconfdir}/php.ini

%triggerun sysvmsg -- %{name}-sysvmsg < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*sysvmsg\.so/d' %{_sysconfdir}/php.ini

%triggerun sysvsem -- %{name}-sysvsem < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*sysvsem\.so/d' %{_sysconfdir}/php.ini

%triggerun sysvshm -- %{name}-sysvshm < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*sysvshm\.so/d' %{_sysconfdir}/php.ini

%triggerun wddx -- %{name}-wddx < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*wddx\.so/d' %{_sysconfdir}/php.ini

%triggerun xml -- %{name}-xml < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*xml\.so/d' %{_sysconfdir}/php.ini

%triggerun xmlrpc -- %{name}-xmlrpc < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*xmlrpc\.so/d' %{_sysconfdir}/php.ini

%triggerun xslt -- %{name}-xslt < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*xslt\.so/d' %{_sysconfdir}/php.ini

%triggerun yaz -- %{name}-yaz < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*yaz\.so/d' %{_sysconfdir}/php.ini

%triggerun yp -- %{name}-yp < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*yp\.so/d' %{_sysconfdir}/php.ini

%triggerun zip -- %{name}-zip < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*zip\.so/d' %{_sysconfdir}/php.ini

%triggerun zlib -- %{name}-zlib < 3:4.4.0-2.1
%{__sed} -i -e '/^extension[[:space:]]*=[[:space:]]*zlib\.so/d' %{_sysconfdir}/php.ini

%if %{with apache1}
%files -n apache1-mod_php4
%defattr(644,root,root,755)
%doc sapi/apache/CREDITS
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/apache/conf.d/*_mod_php4.conf
%dir %{_sysconfdir}/apache.d
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/php-apache.ini
%attr(755,root,root) %{_libdir}/apache1/mod_php.so
%attr(755,root,root) %{_libdir}/apache1/libphp4-*.so
%endif

%if %{with apache2}
%files -n apache-mod_php4
%defattr(644,root,root,755)
%doc sapi/apache2handler/{CREDITS,README}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/httpd/conf.d/*_mod_php4.conf
%attr(755,root,root) %{_libdir}/apache/mod_php.so

%files -n apache-mod_php4-core
%defattr(644,root,root,755)
%dir %{_sysconfdir}/apache2handler.d
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/php-apache2handler.ini
%attr(755,root,root) %{_libdir}/apache/libphp4-*.so
%endif

%if %{with fcgi}
%files fcgi
%defattr(644,root,root,755)
%doc sapi/cgi/{CREDITS,README.FastCGI}
%attr(755,root,root) %{_bindir}/php4.fcgi
%dir %{_sysconfdir}/cgi-fcgi.d
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/php-cgi-fcgi.ini
%endif

%files cgi
%defattr(644,root,root,755)
%doc sapi/cgi/CREDITS
%attr(755,root,root) %{_bindir}/php4.cgi
%dir %{_sysconfdir}/cgi.d
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/php-cgi.ini

%files cli
%defattr(644,root,root,755)
%doc sapi/cli/{CREDITS,README}
%attr(755,root,root) %{_bindir}/php4.cli
%attr(755,root,root) %{_bindir}/php4
%dir %{_sysconfdir}/cli.d
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/php-cli.ini
%{_mandir}/man1/php4.1*

%files program
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/php

%files common
%defattr(644,root,root,755)
%doc php.ini-*
%doc CREDITS Zend/ZEND_CHANGES
%doc LICENSE Zend/LICENSE.Zend EXTENSIONS NEWS TODO*

%dir %{_sysconfdir}
%dir %{_sysconfdir}/conf.d
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/php.ini
%attr(755,root,root) %{_libdir}/libphp_common-*.so
%dir %{extensionsdir}

%files devel
%defattr(644,root,root,755)
%doc README.UNIX-BUILD-SYSTEM
%doc README.EXT_SKEL README.SELF-CONTAINED-EXTENSIONS
%doc CODING_STANDARDS
%attr(755,root,root) %{_bindir}/phpize
%attr(755,root,root) %{_bindir}/php-config
%attr(755,root,root) %{_libdir}/libphp_common.so
# FIXME: how exactly this is needed? as it contains libdir for apache1 or apache2
%{_libdir}/libphp_common.la
%{_includedir}/php
%dir %{_libdir}/php
%{_libdir}/php/build
%{_mandir}/man1/php-config.1*
%{_mandir}/man1/phpize.1*

%files bcmath
%defattr(644,root,root,755)
%doc ext/bcmath/CREDITS
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/bcmath.ini
%attr(755,root,root) %{extensionsdir}/bcmath.so

%files bzip2
%defattr(644,root,root,755)
%doc ext/bz2/CREDITS
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/bz2.ini
%attr(755,root,root) %{extensionsdir}/bz2.so

%files calendar
%defattr(644,root,root,755)
%doc ext/calendar/CREDITS
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/calendar.ini
%attr(755,root,root) %{extensionsdir}/calendar.so

%if %{with cpdf}
%files cpdf
%defattr(644,root,root,755)
%doc ext/cpdf/CREDITS
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/cpdf.ini
%attr(755,root,root) %{extensionsdir}/cpdf.so
%endif

%files crack
%defattr(644,root,root,755)
%doc ext/crack/CREDITS
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/crack.ini
%attr(755,root,root) %{extensionsdir}/crack.so

%files ctype
%defattr(644,root,root,755)
%doc ext/ctype/{CREDITS,README}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/ctype.ini
%attr(755,root,root) %{extensionsdir}/ctype.so

%if %{with curl}
%files curl
%defattr(644,root,root,755)
%doc ext/curl/CREDITS
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/curl.ini
%attr(755,root,root) %{extensionsdir}/curl.so
%endif

%files db
%defattr(644,root,root,755)
%doc ext/db/CREDITS
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/db.ini
%attr(755,root,root) %{extensionsdir}/db.so

%files dba
%defattr(644,root,root,755)
%doc ext/dba/{CREDITS,README}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/dba.ini
%attr(755,root,root) %{extensionsdir}/dba.so

%files dbase
%defattr(644,root,root,755)
%doc ext/dbase/CREDITS
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/dbase.ini
%attr(755,root,root) %{extensionsdir}/dbase.so

%files dbx
%defattr(644,root,root,755)
%doc ext/dbx/{CREDITS,howto_extend_dbx.html}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/dbx.ini
%attr(755,root,root) %{extensionsdir}/dbx.so

%files dio
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/dio.ini
%attr(755,root,root) %{extensionsdir}/dio.so

%if %{with xml}
%files domxml
%defattr(644,root,root,755)
%doc ext/domxml/{CREDITS,TODO}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/domxml.ini
%attr(755,root,root) %{extensionsdir}/domxml.so
%endif

%if %{with fdf}
%files fdf
%defattr(644,root,root,755)
%doc ext/fdf/CREDITS
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/fdf.ini
%attr(755,root,root) %{extensionsdir}/fdf.so
%endif

%files exif
%defattr(644,root,root,755)
%doc ext/exif/CREDITS
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/exif.ini
%attr(755,root,root) %{extensionsdir}/exif.so

%files filepro
%defattr(644,root,root,755)
%doc ext/filepro/CREDITS
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/filepro.ini
%attr(755,root,root) %{extensionsdir}/filepro.so

%if %{with fribidi}
%files fribidi
%defattr(644,root,root,755)
%doc ext/fribidi/{CREDITS,README}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/fribidi.ini
%attr(755,root,root) %{extensionsdir}/fribidi.so
%endif

%files ftp
%defattr(644,root,root,755)
%doc ext/ftp/CREDITS
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/ftp.ini
%attr(755,root,root) %{extensionsdir}/ftp.so

%files gd
%defattr(644,root,root,755)
%doc ext/gd/CREDITS
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/gd.ini
%attr(755,root,root) %{extensionsdir}/gd.so

%files gettext
%defattr(644,root,root,755)
%doc ext/gettext/CREDITS
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/gettext.ini
%attr(755,root,root) %{extensionsdir}/gettext.so

%files gmp
%defattr(644,root,root,755)
%doc ext/gmp/{CREDITS,README,TODO}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/gmp.ini
%attr(755,root,root) %{extensionsdir}/gmp.so

%files hyperwave
%defattr(644,root,root,755)
%doc ext/hyperwave/CREDITS
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/hyperwave.ini
%attr(755,root,root) %{extensionsdir}/hyperwave.so

%files iconv
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/iconv.ini
%attr(755,root,root) %{extensionsdir}/iconv.so

%if %{with imap}
%files imap
%defattr(644,root,root,755)
%doc ext/imap/CREDITS
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/imap.ini
%attr(755,root,root) %{extensionsdir}/imap.so
%endif

%if %{with interbase}
%files interbase
%defattr(644,root,root,755)
%doc ext/interbase/CREDITS
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/interbase.ini
%attr(755,root,root) %{extensionsdir}/interbase.so
%endif

%if %{with java}
%files java
%defattr(644,root,root,755)
%doc ext/java/{CREDITS,README}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/java.ini
%attr(755,root,root) %{extensionsdir}/java.so
%{extensionsdir}/php_java.jar
%endif

%if %{with ldap}
%files ldap
%defattr(644,root,root,755)
%doc ext/ldap/CREDITS
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/ldap.ini
%attr(755,root,root) %{extensionsdir}/ldap.so
%endif

%files mbstring
%defattr(644,root,root,755)
%doc ext/mbstring/{CREDITS,README,README.libmbfl}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/mbstring.ini
%attr(755,root,root) %{extensionsdir}/mbstring.so

%files mcal
%defattr(644,root,root,755)
%doc ext/mcal/CREDITS
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/mcal.ini
%attr(755,root,root) %{extensionsdir}/mcal.so

%files mcrypt
%defattr(644,root,root,755)
%doc ext/mcrypt/{CREDITS,TODO}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/mcrypt.ini
%attr(755,root,root) %{extensionsdir}/mcrypt.so

%if %{with mhash}
%files mhash
%defattr(644,root,root,755)
%doc ext/mhash/CREDITS
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/mhash.ini
%attr(755,root,root) %{extensionsdir}/mhash.so
%endif

%files mime_magic
%defattr(644,root,root,755)
%doc ext/mime_magic/{CREDITS,TODO}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/mime_magic.ini
%attr(755,root,root) %{extensionsdir}/mime_magic.so

%if %{with ming}
%files ming
%defattr(644,root,root,755)
%doc ext/ming/CREDITS
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/ming.ini
%attr(755,root,root) %{extensionsdir}/ming.so
%endif

%if %{with mnogosearch}
%files mnogosearch
%defattr(644,root,root,755)
%doc ext/mnogosearch/{CREDITS,README}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/mnogosearch.ini
%attr(755,root,root) %{extensionsdir}/mnogosearch.so
%endif

%if %{with msession}
%files msession
%defattr(644,root,root,755)
%doc ext/msession/{CREDITS,README,msession-test.php}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/msession.ini
%attr(755,root,root) %{extensionsdir}/msession.so
%endif

%if %{with mssql}
%files mssql
%defattr(644,root,root,755)
%doc ext/mssql/CREDITS
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/mssql.ini
%attr(755,root,root) %{extensionsdir}/mssql.so
%endif

%files mysql
%defattr(644,root,root,755)
%doc ext/mysql/CREDITS
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/mysql.ini
%attr(755,root,root) %{extensionsdir}/mysql.so

%files ncurses
%defattr(644,root,root,755)
%doc ext/ncurses/CREDITS
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/cli.d/ncurses.ini
%attr(755,root,root) %{extensionsdir}/ncurses.so

%if %{with oci8}
%files oci8
%defattr(644,root,root,755)
%doc ext/oci8/CREDITS
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/oci8.ini
%attr(755,root,root) %{extensionsdir}/oci8.so
%endif

%if %{with odbc}
%files odbc
%defattr(644,root,root,755)
%doc ext/odbc/CREDITS
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/odbc.ini
%attr(755,root,root) %{extensionsdir}/odbc.so
%endif

%if %{with oracle}
%files oracle
%defattr(644,root,root,755)
%doc ext/oracle/CREDITS
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/oracle.ini
%attr(755,root,root) %{extensionsdir}/oracle.so
%endif

%files overload
%defattr(644,root,root,755)
%doc ext/overload/{CREDITS,README}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/overload.ini
%attr(755,root,root) %{extensionsdir}/overload.so

%files pcntl
%defattr(644,root,root,755)
%doc ext/pcntl/{CREDITS,README}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/cli.d/pcntl.ini
%attr(755,root,root) %{extensionsdir}/pcntl.so

%if %{with pcre}
%files pcre
%defattr(644,root,root,755)
%doc ext/pcre/CREDITS
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/pcre.ini
%attr(755,root,root) %{extensionsdir}/pcre.so
%endif

%if %{with pdf}
%files pdf
%defattr(644,root,root,755)
%doc ext/pdf/CREDITS
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/pdf.ini
%attr(755,root,root) %{extensionsdir}/pdf.so
%endif

%if %{with pgsql}
%files pgsql
%defattr(644,root,root,755)
%doc ext/pgsql/{CREDITS,README}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/pgsql.ini
%attr(755,root,root) %{extensionsdir}/pgsql.so
%endif

%files posix
%defattr(644,root,root,755)
%doc ext/posix/CREDITS
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/posix.ini
%attr(755,root,root) %{extensionsdir}/posix.so

%if %{with pspell}
%files pspell
%defattr(644,root,root,755)
%doc ext/overload/{CREDITS,README}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/pspell.ini
%attr(755,root,root) %{extensionsdir}/pspell.so
%endif

%if %{with qtdom}
%files qtdom
%defattr(644,root,root,755)
%doc ext/qtdom/CREDITS
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/qtdom.ini
%attr(755,root,root) %{extensionsdir}/qtdom.so
%endif

%files readline
%defattr(644,root,root,755)
%doc ext/readline/{CREDITS,README.libedit}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/cli.d/readline.ini
%attr(755,root,root) %{extensionsdir}/readline.so

%if %{with recode}
%files recode
%defattr(644,root,root,755)
%doc ext/recode/CREDITS
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/recode.ini
%attr(755,root,root) %{extensionsdir}/recode.so
%endif

# session_mm doesn't work with shared session
#%files session
#%defattr(644,root,root,755)
#%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/session.ini
#%attr(755,root,root) %{extensionsdir}/session.so

%files shmop
%defattr(644,root,root,755)
%doc ext/shmop/{CREDITS,README}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/shmop.ini
%attr(755,root,root) %{extensionsdir}/shmop.so

%if %{with snmp}
%files snmp
%defattr(644,root,root,755)
%doc ext/snmp/CREDITS
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/snmp.ini
%attr(755,root,root) %{extensionsdir}/snmp.so
%endif

%files sockets
%defattr(644,root,root,755)
%doc ext/sockets/CREDITS
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/sockets.ini
%attr(755,root,root) %{extensionsdir}/sockets.so

%if %{with sybase}
%files sybase
%defattr(644,root,root,755)
%doc ext/sybase/CREDITS
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/sybase.ini
%attr(755,root,root) %{extensionsdir}/sybase.so

%files sybase-ct
%defattr(644,root,root,755)
%doc ext/sybase_ct/CREDITS
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/sybase_ct.ini
%attr(755,root,root) %{extensionsdir}/sybase_ct.so
%endif

%files sysvmsg
%defattr(644,root,root,755)
%doc ext/sysvmsg/CREDITS
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/sysvmsg.ini
%attr(755,root,root) %{extensionsdir}/sysvmsg.so

%files sysvsem
%defattr(644,root,root,755)
%doc ext/sysvsem/CREDITS
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/sysvsem.ini
%attr(755,root,root) %{extensionsdir}/sysvsem.so

%files sysvshm
%defattr(644,root,root,755)
%doc ext/sysvshm/CREDITS
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/sysvshm.ini
%attr(755,root,root) %{extensionsdir}/sysvshm.so

%files tokenizer
%defattr(644,root,root,755)
%doc ext/tokenizer/{CREDITS,tokenizer.php}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/tokenizer.ini
%attr(755,root,root) %{extensionsdir}/tokenizer.so

%if %{with wddx}
%files wddx
%defattr(644,root,root,755)
%doc ext/wddx/CREDITS
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*wddx.ini
%attr(755,root,root) %{extensionsdir}/wddx.so
%endif

%if %{with xml}
%files xml
%defattr(644,root,root,755)
%doc ext/xml/CREDITS
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/xml.ini
%attr(755,root,root) %{extensionsdir}/xml.so
%endif

%if %{with xmlrpc}
%files xmlrpc
%defattr(644,root,root,755)
%doc ext/xmlrpc/CREDITS
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/xmlrpc.ini
%attr(755,root,root) %{extensionsdir}/xmlrpc.so
%endif

%if %{with xslt}
%files xslt
%defattr(644,root,root,755)
%doc ext/xslt/{README.XSLT-BACKENDS,TODO}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/xslt.ini
%attr(755,root,root) %{extensionsdir}/xslt.so
%endif

%if %{with yaz}
%files yaz
%defattr(644,root,root,755)
%doc ext/yaz/{CREDITS,README}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/yaz.ini
%attr(755,root,root) %{extensionsdir}/yaz.so
%endif

%if %{with yp}
%files yp
%defattr(644,root,root,755)
%doc ext/yp/CREDITS
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/yp.ini
%attr(755,root,root) %{extensionsdir}/yp.so
%endif

%files zip
%defattr(644,root,root,755)
%doc ext/zip/CREDITS
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/zip.ini
%attr(755,root,root) %{extensionsdir}/zip.so

%files zlib
%defattr(644,root,root,755)
%doc ext/zlib/CREDITS
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/zlib.ini
%attr(755,root,root) %{extensionsdir}/zlib.so
