#
# Do NOT build openssl as shared module or
# fsockopen('tls://host',...) will not work!
#
# TODO:
# - make additional headers added by mail patch configurable
# - /var/run/php group not owned
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
%bcond_without	fribidi		# without FriBiDi extension module
%bcond_without	imap		# without IMAP extension module
%bcond_without	interbase	# without InterBase extension module
%bcond_without	ldap		# without LDAP extension module
%bcond_without	mhash		# without mhash extension module
%bcond_without	ming		# without ming extension module
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
%bcond_without	recode		# without recode extension module
%bcond_without	qtdom		# without Qt DOM extension module
%bcond_without	snmp		# without SNMP extension module
%bcond_without	sybase		# without Sybase and Sybase-CT extension modules
%bcond_without	wddx		# without WDDX extension module
%bcond_without	xmlrpc		# without XML-RPC extension module
%bcond_without	xml		# without XML and DOMXML extension modules
%bcond_without	xslt		# without XSLT extension module
%bcond_without	yaz		# without YAZ extension module
%bcond_without	apache1		# disable building apache 1.3.x module
%bcond_without	apache2		# disable building apache 2.x module
%bcond_with	zts		# enable-experimental-zts

%define apxs1		/usr/sbin/apxs1
%define	apxs2		/usr/sbin/apxs

# mm is not thread safe
# ext/session/mod_mm.c:37:3: #error mm is not thread-safe
%if %{with zts}
%undefine	with_mm
%endif

%ifnarch %{ix86} %{x8664} sparc sparcv9 alpha ppc
%undefine	with_interbase
%endif

# x86-only lib
%ifnarch %{ix86}
%undefine	with_msession
%endif

%include	/usr/lib/rpm/macros.php
Summary:	The PHP HTML-embedded scripting language for use with Apache
Summary(fr):	Le langage de script embarque-HTML PHP pour Apache
Summary(pl):	Jêzyk skryptowy PHP - u¿ywany wraz z serwerem Apache
Summary(pt_BR):	A linguagem de script PHP
Summary(ru):	PHP ÷ÅÒÓÉÉ 4 - ÑÚÙË ÐÒÅÐÒÏÃÅÓÓÉÒÏ×ÁÎÉÑ HTML-ÆÁÊÌÏ×, ×ÙÐÏÌÎÑÅÍÙÊ ÎÁ ÓÅÒ×ÅÒÅ
Summary(uk):	PHP ÷ÅÒÓ¦§ 4 - ÍÏ×Á ÐÒÅÐÒÏÃÅÓÕ×ÁÎÎÑ HTML-ÆÁÊÌ¦×, ×ÉËÏÎÕ×ÁÎÁ ÎÁ ÓÅÒ×ÅÒ¦
Name:		php4
Version:	4.4.0
Release:	4.48%{?with_hardening:hardened}
Epoch:		3
Group:		Libraries
License:	PHP
Source0:	http://www.php.net/distributions/php-%{version}.tar.bz2
# Source0-md5:	e85b606fe48198bfcd785e5a5b1c9613
Source1:	FAQ.%{name}
Source2:	zend.gif
Source3:	%{name}-module-install
Source4:	%{name}-mod_php.conf
Source5:	%{name}-cgi-fcgi.ini
Source6:	%{name}-cgi.ini
Source7:	%{name}-apache.ini
Source8:	%{name}-cli.ini
Source9:	http://www.hardened-php.net/hardening-patch-4.3.11-0.3.1.patch.gz
# Source9-md5:	b231e363b60c8749fcafe1e24e8bacbb
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
Patch23:	%{name}-gmp.patch
Patch24:	%{name}-qt.patch
Patch25:	%{name}-no_pear_install.patch
Patch26:	%{name}-zlib.patch
Patch27:	%{name}-db-shared.patch
Patch28:	%{name}-sybase-fix.patch
Patch29:	%{name}-lib64.patch
Patch30:	%{name}-mnogosearch-fix.patch
Patch31:	%{name}-stupidapache_version.patch
Patch32:	%{name}-gd_imagerotate_enable.patch
Patch33:	%{name}-uint32_t.patch
Patch34:	%{name}-install_gd_headers.patch
Patch35:	%{name}-both-apxs.patch
#Icon:		php4.gif
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
%{?with_db3:BuildRequires:	db3-devel >= 3.1}
%{!?with_db3:BuildRequires:	db-devel >= 4.0}
BuildRequires:	elfutils-devel
%if %{with wddx} || %{with xml} || %{with xmlrpc}
BuildRequires:	expat-devel
%endif
%{?with_fdf:BuildRequires:	fdftk-devel}
BuildRequires:	fcgi-devel
BuildRequires:	flex
%if %{with mssql} || %{with sybase}
BuildRequires:	freetds-devel
%endif
BuildRequires:	freetype-devel >= 2.0
%{?with_fribidi:BuildRequires:	fribidi-devel >= 0.10.4}
BuildRequires:	gd-devel >= 2.0.28-2
BuildRequires:	gd-devel(gif)
BuildRequires:	gdbm-devel
BuildRequires:	gmp-devel
%{?with_imap:BuildRequires:	imap-devel >= 1:2001-0.BETA.200107022325.2}
%{?with_imap:BuildRequires:	heimdal-devel >= 0.7}
%{?with_java:BuildRequires:	jdk >= 1.1}
%{?with_cpdf:BuildRequires:	libcpdf-devel >= 2.02r1-2}
BuildRequires:	libjpeg-devel
BuildRequires:	libltdl-devel >= 1.4
BuildRequires:	libmcal-devel
BuildRequires:	libmcrypt-devel >= 2.4.4
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libtiff-devel
BuildRequires:	libtool >= 1.4.3
%{?with_xml:BuildRequires:	libxml2-devel >= 2.2.7}
%{?with_domxslt:BuildRequires:	libxslt-devel >= 1.0.3}
%{?with_mhash:BuildRequires:	mhash-devel}
%{?with_ming:BuildRequires:	ming-devel >= 0.1.0}
%{?with_mm:BuildRequires:	mm-devel >= 1.3.0}
%{?with_mnogosearch:BuildRequires:	mnogosearch-devel >= 3.2.29}
BuildRequires:	mysql-devel >= 3.23.32
BuildRequires:	ncurses-ext-devel
%{?with_ldap:BuildRequires:	openldap-devel >= 2.0}
%if %{with openssl} || %{with ldap}
BuildRequires:	openssl-devel >= 0.9.7d
%endif
BuildRequires:	pam-devel
%{?with_pdf:BuildRequires:	pdflib-devel >= 4.0.0}
BuildRequires:	%{__perl}
%{?with_msession:BuildRequires:	phoenix-devel}
%{?with_pgsql:BuildRequires:	postgresql-devel}
%{?with_pgsql:BuildRequires:	postgresql-backend-devel >= 7.2}
%{?with_qtdom:BuildRequires:	qt-devel >= 2.2.0}
BuildRequires:	readline-devel
%{?with_recode:BuildRequires:	recode-devel >= 3.5d-3}
BuildRequires:	rpm-php-pearprov >= 4.0.2-100
BuildRequires:	rpmbuild(macros) >= 1.230
%{?with_xslt:BuildRequires:	sablotron-devel >= 0.96}
BuildRequires:	sed >= 4.0
BuildRequires:	t1lib-devel
%{?with_snmp:BuildRequires:	net-snmp-devel >= 5.0.7}
%{?with_odbc:BuildRequires:	unixODBC-devel}
%{?with_xmlrpc:BuildRequires:	xmlrpc-epi-devel}
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

%description
PHP is an HTML-embedded scripting language. PHP attempts to make it
easy for developers to write dynamically generated web pages. PHP also
offers built-in database integration for several commercial and
non-commercial database management systems, so writing a
database-enabled web page with PHP is fairly simple. The most common
use of PHP coding is probably as a replacement for CGI scripts. The
mod_php module enables the Apache web server to understand and process
the embedded PHP language in web pages. This package contains php
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
integre dans des pages web. Ce package contient php version
%{version}. Si vous utilisez des applications qui utilisent
specifiquement PHP/FI, vous devrez installer le module PHP/FI inclus
dans le package mod_php. Si vous debutez avec PHP, vous devriez
installer ce package. Vous aurez egalement besoin dinstaller le
serveur web Apache.

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

%description -l ru
PHP4 - ÜÔÏ ÑÚÙË ÎÁÐÉÓÁÎÉÑ ÓËÒÉÐÔÏ×, ×ÓÔÒÁÉ×ÁÅÍÙÈ × HTML-ËÏÄ. PHP
ÐÒÅÄÌÁÇÁÅÔ ÉÎÔÅÒÇÒÁÃÉÀ Ó ÍÎÏÖÅÓÔ×ÏÍ óõâä, ÐÏÜÔÏÍÕ ÎÁÐÉÓÁÎÉÅ ÓËÒÉÐÔÏ×
ÄÌÑ ÒÁÂÏÔÙ Ó ÂÁÚÁÍÉ ÄÁÎÎÙÈ ÏÔÎÏÓÉÔÅÌØÎÏ ÐÒÏÓÔÏ. îÁÉÂÏÌÅÅ ÐÏÐÕÌÑÒÎÏÅ
ÉÓÐÏÌØÚÏ×ÁÎÉÅ PHP - ÚÁÍÅÎÁ ÄÌÑ CGI ÓËÒÉÐÔÏ×.

üÔÏÔ ÐÁËÅÔ ÓÏÄÅÒÖÉÔ ÓÁÍÏÄÏÓÔÁÔÏÞÎÕÀ (CGI) ×ÅÒÓÉÀ ÉÎÔÅÒÐÒÅÔÁÔÏÒÁ ÑÚÙËÁ.
÷Ù ÄÏÌÖÎÙ ÔÁËÖÅ ÕÓÔÁÎÏ×ÉÔØ ÐÁËÅÔ %{name}-common. åÓÌÉ ×ÁÍ ÎÕÖÅÎ
ÉÎÔÅÒÐÒÅÔÁÔÏÒ PHP × ËÁÞÅÓÔ×Å ÍÏÄÕÌÑ apache, ÕÓÔÁÎÏ×ÉÔÅ ÐÁËÅÔ
apache-php.

%description -l uk
PHP4 - ÃÅ ÍÏ×Á ÎÁÐÉÓÁÎÎÑ ÓËÒÉÐÔ¦×, ÝÏ ×ÂÕÄÏ×ÕÀÔØÓÑ × HTML-ËÏÄ. PHP
ÐÒÏÐÏÎÕ¤ ¦ÎÔÅÇÒÁÃ¦À Ú ÂÁÇÁÔØÍÁ óõâä, ÔÏÍÕ ÎÁÐÉÓÁÎÎÑ ÓËÒÉÐÔ¦× ÄÌÑ
ÒÏÂÏÔÉ Ú ÂÁÚÁÍÉ ÄÁÎÉÈ ¤ ÄÏ×ÏÌ¦ ÐÒÏÓÔÉÍ. îÁÊÂ¦ÌØÛ ÐÏÐÕÌÑÒÎÅ
×ÉËÏÒÉÓÔÁÎÎÑ PHP - ÚÁÍ¦ÎÁ ÄÌÑ CGI ÓËÒÉÐÔ¦×.

ãÅÊ ÐÁËÅÔ Í¦ÓÔÉÔØ ÓÁÍÏÄÏÓÔÁÔÎÀ (CGI) ×ÅÒÓ¦À ¦ÎÔÅÒÐÒÅÔÁÔÏÒÁ ÍÏ×É. ÷É
ÍÁ¤ÔÅ ÔÁËÏÖ ×ÓÔÁÎÏ×ÉÔÉ ÐÁËÅÔ %{name}-common. ñËÝÏ ×ÁÍ ÐÏÔÒ¦ÂÅÎ
¦ÎÔÅÒÐÒÅÔÁÔÏÒ PHP × ÑËÏÓÔ¦ ÍÏÄÕÌÑ apache, ×ÓÔÁÎÏ×¦ÔØ ÐÁËÅÔ apache-php.

%package -n apache1-mod_php4
Summary:	php4 DSO module for apache 1.3.x
Summary(pl):	Modu³ DSO (Dynamic Shared Object) php4 dla apache 1.3.x
Group:		Development/Languages/PHP
PreReq:		%{name}-common = %{epoch}:%{version}-%{release}
Requires:	apache1(EAPI) >= 1.3.33-2
Requires:	apache1-mod_mime
Provides:	%{name} = %{epoch}:%{version}-%{release}
Provides:	php = %{epoch}:%{version}-%{release}
Provides:	php4 = %{epoch}:%{version}-%{release}
Obsoletes:	phpfi
Obsoletes:	apache-mod_php < 1:4.1.1
# Obsolete last version when apache module was in main package
Obsoletes:	php4 < 3:4.3.11-4.16

%description -n apache1-mod_php4
php4 as DSO module for apache 1.3.x.

%description -n apache1-mod_php4 -l pl
php4 jako modu³ DSO (Dynamic Shared Object) dla apache 1.3.x.

%package -n apache-mod_php4
Summary:	php4 DSO module for apache 2.x
Summary(pl):	Modu³ DSO (Dynamic Shared Object) php4 dla apache 2.x
Group:		Development/Languages/PHP
PreReq:		%{name}-common = %{epoch}:%{version}-%{release}
Requires:	apache >= 2.0.52-2
Requires:	apache(modules-api) = %{apache_modules_api}
Provides:	%{name} = %{epoch}:%{version}-%{release}
Provides:	php = %{epoch}:%{version}-%{release}
Provides:	php4 = %{epoch}:%{version}-%{release}
Obsoletes:	phpfi
Obsoletes:	apache-mod_php < 1:4.1.1
# Obsolete last version when apache module was in main package
Obsoletes:	php4 < 3:4.3.11-4.16

%description -n apache-mod_php4
php4 as DSO module for apache 2.x.

%description -n apache-mod_php4 -l pl
php4 jako modu³ DSO (Dynamic Shared Object) dla apache 2.x.

%package fcgi
Summary:	php4 as FastCGI program
Summary(pl):	php4 jako program FastCGI
Group:		Development/Languages/PHP
PreReq:		%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-fcgi = %{epoch}:%{version}-%{release}
Provides:	php-program = %{epoch}:%{version}-%{release}
Provides:	%{name}-program = %{epoch}:%{version}-%{release}

%description fcgi
php4 as FastCGI program.

%description fcgi -l pl
php4 jako program FastCGI.

%package cgi
Summary:	php4 as CGI program
Summary(pl):	php4 jako program CGI
Group:		Development/Languages/PHP
PreReq:		%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-cgi = %{epoch}:%{version}-%{release}
Provides:	php-program = %{epoch}:%{version}-%{release}
Provides:	%{name}-program = %{epoch}:%{version}-%{release}

%description cgi
php4 as CGI program.

%description cgi -l pl
php4 jako program CGI.

%package cli
Summary:	php4 as CLI interpreter
Summary(pl):	php4 jako interpreter dzia³aj±cy z linii poleceñ
Group:		Development/Languages/PHP
PreReq:		%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-cli = %{epoch}:%{version}-%{release}
Provides:	php-program = %{epoch}:%{version}-%{release}
Provides:	%{name}-program = %{epoch}:%{version}-%{release}

%description cli
php4 as CLI interpreter.

%description cli -l pl
php4 jako interpreter dzia³aj±cy z linii poleceñ.

%package common
Summary:	Common files needed by all PHP SAPIs
Summary(pl):	Wspólne pliki dla modu³u apache'a i programu CGI
Summary(ru):	òÁÚÄÅÌÑÅÍÙÅ ÂÉÂÌÉÏÔÅËÉ ÄÌÑ php
Summary(uk):	â¦ÂÌ¦ÏÔÅËÉ ÓÐ¦ÌØÎÏÇÏ ×ÉËÏÒÉÓÔÁÎÎÑ ÄÌÑ php
Group:		Libraries
# because of dlclose() bugs in glibc <= 2.3.4 causing SEGVs on exit
Requires:	glibc >= 6:2.3.5
Requires:	sed >= 4.0
Provides:	%{name}-session = %{epoch}:%{version}-%{release}
Provides:	php-common = %{epoch}:%{version}-%{release}
Provides:	php-session = %{epoch}:%{version}-%{release}
Obsoletes:	php-session < 3:4.2.1-2
Obsoletes:	php4-openssl < 3:4.4.0-4

%description common
Common files needed by all PHP SAPIs.

%description common -l pl
Wspólne pliki dla modu³u apacha i programu CGI.

%description common -l ru
üÔÏÔ ÐÁËÅÔ ÓÏÄÅÒÖÉÔ ÏÂÝÉÅ ÆÁÊÌÙ ÄÌÑ ÒÁÚÎÙÈ ×ÁÒÉÁÎÔÏ× ÒÅÁÌÉÚÁÃÉÉ PHP
(ÓÁÍÏÄÏÓÔÁÔÏÞÎÏÊ É × ËÁÞÅÓÔ×Å ÍÏÄÕÌÑ apache).

%description common -l uk
ãÅÊ ÐÁËÅÔ Í¦ÓÔÉÔØ ÓÐ¦ÌØÎ¦ ÆÁÊÌÉ ÄÌÑ Ò¦ÚÎÉÈ ×ÁÒ¦ÁÎÔ¦× ÒÅÁÌ¦ÚÁÃ¦§ PHP
(ÓÁÍÏÄÏÓÔÁÔÎØÏ§ ÔÁ × ÑËÏÓÔ¦ ÍÏÄÕÌÑ apache).

%package devel
Summary:	Files for PHP modules development
Summary(pl):	Pliki do kompilacji modu³ów PHP
Summary(pt_BR):	Arquivos de desenvolvimento para PHP
Summary(ru):	ðÁËÅÔ ÒÁÚÒÁÂÏÔËÉ ÄÌÑ ÐÏÓÔÒÏÅÎÉÑ ÒÁÓÛÉÒÅÎÉÊ PHP
Summary(uk):	ðÁËÅÔ ÒÏÚÒÏÂËÉ ÄÌÑ ÐÏÂÕÄÏ×É ÒÏÚÛÉÒÅÎØ PHP
Group:		Development/Languages/PHP
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	autoconf
Requires:	automake
Provides:	php-devel = %{epoch}:%{version}-%{release}
Obsoletes:	php-devel

%description devel
The php-devel package lets you compile dynamic extensions to PHP.
Included here is the source for the PHP extensions. Instead of
recompiling the whole php4 binary to add support for, say, oracle,
install this package and use the new self-contained extensions
support. For more information, read the file
SELF-CONTAINED-EXTENSIONS.

%description devel -l pl
Pliki potrzebne do kompilacji modu³ów PHP.

%description devel -l pt_BR
Este pacote contém arquivos usados no desenvolvimento de programas ou
módulos PHP.

%description devel -l uk
ðÁËÅÔ php-devel ÄÁ¤ ÍÏÖÌÉ×¦ÓÔØ ËÏÍÐ¦ÌÀ×ÁÔÉ ÄÉÎÁÍ¦ÞÎ¦ ÒÏÚÛÉÒÅÎÎÑ PHP.
äÏ ÐÁËÅÔÕ ×ËÌÀÞÅÎÏ ×ÉÈ¦ÄÎÉÊ ËÏÄ ÄÌÑ ÒÏÚÛÉÒÅÎØ. úÁÍ¦ÓÔØ ÐÏ×ÔÏÒÎÏ§
ËÏÍÐ¦ÌÑÃ¦§ Â¦ÎÁÒÎÏÇÏ ÆÁÊÌÕ php4 ÄÌÑ ÄÏÄÁÎÎÑ, ÎÁÐÒÉËÌÁÄ, Ð¦ÄÔÒÉÍËÉ
oracle, ×ÓÔÁÎÏ×¦ÔØ ÃÅÊ ÐÁËÅÔ ÄÌÑ ËÏÍÐ¦ÌÑÃ¦§ ÏËÒÅÍÉÈ ÒÏÚÛÉÒÅÎØ.
äÅÔÁÌØÎ¦ÛÁ ¦ÎÆÏÒÍÁÃ¦Ñ - × ÆÁÊÌ¦ SELF-CONTAINED-EXTENSIONS.

%description devel -l ru
ðÁËÅÔ php-devel ÄÁÅÔ ×ÏÚÍÏÖÎÏÓÔØ ËÏÍÐÉÌÉÒÏ×ÁÔØ ÄÉÎÁÍÉÞÅÓËÉÅ ÒÁÓÛÉÒÅÎÉÑ
PHP. ðÁËÅÔ ×ËÌÀÞÁÅÔ ÉÓÈÏÄÎÙÊ ËÏÄ ÜÔÉÈ ÒÁÓÛÉÒÅÎÉÊ. ÷ÍÅÓÔÏ ÐÏ×ÔÏÒÎÏÊ
ËÏÍÐÉÌÑÃÉÉ ÂÉÎÁÒÎÏÇÏ ÆÁÊÌÁ php4 ÄÌÑ ÄÏÂÁ×ÌÅÎÉÑ, ÎÁÐÒÉÍÅÒ, ÐÏÄÄÅÒÖËÉ
oracle, ÕÓÔÁÎÏ×ÉÔÅ ÜÔÏÔ ÐÁËÅÔ ÄÌÑ ËÏÍÐÉÌÉÒÏ×ÁÎÉÑ ÏÔÄÅÌØÎÙÈ ÒÁÓÛÉÒÅÎÉÊ.
ðÏÄÒÏÂÎÏÓÔÉ - × ÆÁÊÌÅ SELF-CONTAINED-EXTENSIONS.

%package bcmath
Summary:	bcmath extension module for PHP
Summary(pl):	Modu³ bcmath dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-bcmath = %{epoch}:%{version}-%{release}

%description bcmath
This is a dynamic shared object (DSO) for PHP that will add bc style
precision math functions support.

%description bcmath -l pl
Modu³ PHP umo¿liwiaj±cy korzystanie z dok³adnych funkcji
matematycznych takich jak w programie bc.

%package bzip2
Summary:	Bzip2 extension module for PHP
Summary(pl):	Modu³ bzip2 dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-bzip2 = %{epoch}:%{version}-%{release}

%description bzip2
This is a dynamic shared object (DSO) for PHP that will add bzip2
compression support to PHP.

%description bzip2 -l pl
Modu³ PHP umo¿liwiaj±cy u¿ywanie kompresji bzip2.

%package calendar
Summary:	Calendar extension module for PHP
Summary(pl):	Modu³ funkcji kalendarza dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-calendar = %{epoch}:%{version}-%{release}

%description calendar
This is a dynamic shared object (DSO) for PHP that will add calendar
support.

%description calendar -l pl
Modu³ PHP dodaj±cy wsparcie dla kalendarza.

%package cpdf
Summary:	cpdf extension module for PHP
Summary(pl):	Modu³ cpdf dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-cpdf = %{epoch}:%{version}-%{release}

%description cpdf
This is a dynamic shared object (DSO) for PHP that will add PDF
support through libcpdf library.

%description cpdf -l pl
Modu³ PHP dodaj±cy obs³ugê plików PDF poprzez bibliotekê libcpdf.

%package crack
Summary:	crack extension module for PHP
Summary(pl):	Modu³ crack dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-crack = %{epoch}:%{version}-%{release}

%description crack
This is a dynamic shared object (DSO) for PHP that will add cracklib
support to PHP.

Warning: this is an experimental module.

%description crack -l pl
Modu³ PHP umo¿liwiaj±cy korzystanie z biblioteki cracklib.

Uwaga: to jest modu³ eksperymentalny.

%package ctype
Summary:	ctype extension module for PHP
Summary(pl):	Modu³ ctype dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-ctype = %{epoch}:%{version}-%{release}

%description ctype
This is a dynamic shared object (DSO) for PHP that will add ctype
support.

%description ctype -l pl
Modu³ PHP umo¿liwiaj±cy korzystanie z funkcji ctype.

%package curl
Summary:	curl extension module for PHP
Summary(pl):	Modu³ curl dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-curl = %{epoch}:%{version}-%{release}

%description curl
This is a dynamic shared object (DSO) for PHP that will add curl
support.

%description curl -l pl
Modu³ PHP umo¿liwiaj±cy korzystanie z biblioteki curl.

%package db
Summary:	Old xDBM extension module for PHP
Summary(pl):	Modu³ xDBM dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-db = %{epoch}:%{version}-%{release}

%description db
This is an old dynamic shared object (DSO) for PHP that will add DBM
databases support.

Warning: this module is deprecated and does not support database
locking correctly. Please use DBA extension which is a fully
operational superset.

%description db -l pl
Stary modu³ PHP dodaj±cy obs³ugê baz danych DBM.

Uwaga: ten modu³ jest przestarza³y i nie obs³uguje poprawnie
blokowania bazy danych. Zamiast niego lepiej u¿ywaæ rozszerzenia DBA,
które obs³uguje nadzbiór funkcjonalno¶ci tego modu³u.

%package dba
Summary:	DBA extension module for PHP
Summary(pl):	Modu³ DBA dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-dba = %{epoch}:%{version}-%{release}

%description dba
This is a dynamic shared object (DSO) for PHP that will add flat-file
databases (DBA) support.

%description dba -l pl
Modu³ dla PHP dodaj±cy obs³ugê dla baz danych opartych na plikach
(DBA).

%package dbase
Summary:	DBase extension module for PHP
Summary(pl):	Modu³ DBase dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-dbase = %{epoch}:%{version}-%{release}

%description dbase
This is a dynamic shared object (DSO) for PHP that will add DBase
support.

%description dbase -l pl
Modu³ PHP ze wsparciem dla DBase.

%package dbx
Summary:	DBX extension module for PHP
Summary(pl):	Modu³ DBX dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-dbx = %{epoch}:%{version}-%{release}

%description dbx
This is a dynamic shared object (DSO) for PHP that will add DB
abstraction layer. DBX supports odbc, mysql, pgsql, mssql, fbsql and
more.

%description dbx -l pl
Modu³ PHP dodaj±cy warstwê abstrakcji do obs³ugi baz danych. DBX
obs³uguje bazy odbc, mysql, pgsql, mssql, fbsql i inne.

%package dio
Summary:	Direct I/O extension module for PHP
Summary(pl):	Modu³ Direct I/O dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-dio = %{epoch}:%{version}-%{release}

%description dio
This is a dynamic shared object (DSO) for PHP that will add direct
file I/O support.

%description dio -l pl
Modu³ PHP dodaj±cy obs³ugê bezpo¶rednich operacji I/O na plikach.

%package domxml
Summary:	DOM XML extension module for PHP
Summary(pl):	Modu³ DOM XML dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-domxml = %{epoch}:%{version}-%{release}

%description domxml
This is a dynamic shared object (DSO) for PHP that will add DOM XML
support.

Warning: this is an experimental module.

%description domxml -l pl
Modu³ PHP dodaj±cy obs³ugê DOM XML.

Uwaga: to jest modu³ eksperymentalny.

%package exif
Summary:	exif extension module for PHP
Summary(pl):	Modu³ exif dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-exif = %{epoch}:%{version}-%{release}

%description exif
This is a dynamic shared object (DSO) for PHP that will add EXIF tags
support in image files.

%description exif -l pl
Modu³ PHP dodaj±cy obs³ugê znaczników EXIF w plikach obrazków.

%package fdf
Summary:	FDF extension module for PHP
Summary(pl):	Modu³ FDF dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-fdf = %{epoch}:%{version}-%{release}

%description fdf
This PHP module adds support for PDF Forms through Adobe FDFTK
library.

%description fdf -l pl
Modu³ PHP dodaj±cy obs³ugê formularzy PDF poprzez bibliotekê Adobe
FDFTK.

%package filepro
Summary:	filePro extension module for PHP
Summary(pl):	Modu³ filePro dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-filepro = %{epoch}:%{version}-%{release}

%description filepro
This is a dynamic shared object (DSO) for PHP that will add support
for read-only access to filePro databases.

%description filepro -l pl
Modu³ PHP dodaj±cy mo¿liwo¶æ dostêpu (tylko do odczytu) do baz danych
filePro.

%package fribidi
Summary:	FriBiDi extension module for PHP
Summary(pl):	Modu³e FriBiDi dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-fribidi = %{epoch}:%{version}-%{release}

%description fribidi
This extension is basically a wrapper for the FriBidi implementation
of the Unicode Bidi algorithm. The need for such an algorithm rises
from the bidirectional language usage done by applications.
Arabic/Hebrew embedded within English is such a case.

%description fribidi -l pl
To rozszerzenie to g³ównie interfejs do implementacji FriBiDi
algorytmu Unicode Bidi. Taki algorytm jest potrzebny w przypadku
u¿ywania dwukierunkowego pisma w aplikacjach - na przyk³ad przy
tek¶cie arabskim lub hebrajskim osadzonym wewn±trz angielskiego.

%package ftp
Summary:	FTP extension module for PHP
Summary(pl):	Modu³ FTP dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-ftp = %{epoch}:%{version}-%{release}

%description ftp
This is a dynamic shared object (DSO) for PHP that will add FTP
support.

%description ftp -l pl
Modu³ PHP dodaj±cy obs³ugê protoko³u FTP.

%package gd
Summary:	GD extension module for PHP
Summary(pl):	Modu³ GD dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	gd >= 2.0.28-2
Requires:	gd(gif)
Provides:	%{name}-gd(gif) = %{epoch}:%{version}-%{release}
Provides:	php-gd = %{epoch}:%{version}-%{release}

%description gd
This is a dynamic shared object (DSO) for PHP that will add GD
support, allowing you to create and manipulate images with PHP.

%description gd -l pl
Modu³ PHP umo¿liwiaj±cy korzystanie z biblioteki GD, pozwalaj±cej na
tworzenie i obróbkê obrazków.

%package gettext
Summary:	gettext extension module for PHP
Summary(pl):	Modu³ gettext dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-gettext = %{epoch}:%{version}-%{release}

%description gettext
This is a dynamic shared object (DSO) for PHP that will add gettext
support.

%description gettext -l pl
Modu³ PHP dodaj±cy obs³ugê lokalizacji przez gettext.

%package gmp
Summary:	gmp extension module for PHP
Summary(pl):	Modu³ gmp dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-gmp = %{epoch}:%{version}-%{release}

%description gmp
This is a dynamic shared object (DSO) for PHP that will add arbitrary
length number support with GNU MP library.

%description gmp -l pl
Modu³ PHP umo¿liwiaj±cy korzystanie z biblioteki gmp do obliczeñ na
liczbach o dowolnej d³ugo¶ci.

%package hyperwave
Summary:	Hyperwave extension module for PHP
Summary(pl):	Modu³ Hyperwave dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-hyperwave = %{epoch}:%{version}-%{release}

%description hyperwave
This is a dynamic shared object (DSO) for PHP that will add Hyperwave
support.

%description hyperwave -l pl
Modu³ PHP dodaj±cy obs³ugê Hyperwave.

%package iconv
Summary:	iconv extension module for PHP
Summary(pl):	Modu³ iconv dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-iconv = %{epoch}:%{version}-%{release}

%description iconv
This is a dynamic shared object (DSO) for PHP that will add iconv
support.

%description iconv -l pl
Modu³ PHP dodaj±cy obs³ugê iconv.

%package imap
Summary:	IMAP extension module for PHP
Summary(pl):	Modu³ IMAP dla PHP
Summary(pt_BR):	Um módulo para aplicações PHP que usam IMAP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-imap = %{epoch}:%{version}-%{release}

%description imap
This is a dynamic shared object (DSO) for PHP that will add IMAP
support.

%description imap -l pl
Modu³ PHP dodaj±cy obs³ugê skrzynek IMAP.

%description imap -l pt_BR
Um módulo para aplicações PHP que usam IMAP.

%package interbase
Summary:	InterBase/Firebird database module for PHP
Summary(pl):	Modu³ bazy danych InterBase/Firebird dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-interbase = %{epoch}:%{version}-%{release}
%{?with_interbase_inst:Autoreq:	false}

%description interbase
This is a dynamic shared object (DSO) for PHP that will add InterBase
and Firebird database support.

%description interbase -l pl
Modu³ PHP umo¿liwiaj±cy dostêp do baz danych InterBase i Firebird.

%package java
Summary:	Java extension module for PHP
Summary(pl):	Modu³ Javy dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-java = %{epoch}:%{version}-%{release}

%description java
This is a dynamic shared object (DSO) for PHP that will add Java
support to PHP. This extension provides a simple and effective means
for creating and invoking methods on Java objects from PHP.

Note: it requires setting LD_LIBRARY_PATH to JRE directories
containing JVM libraries (e.g. libjava.so, libverify.so and libjvm.so
for Sun's JRE) before starting Apache or PHP interpreter.

%description java -l pl
Modu³ PHP dodaj±cy wsparcie dla Javy. Umo¿liwia odwo³ywanie siê do
obiektów Javy z poziomu PHP.

Uwaga: modu³ wymaga ustawienia LD_LIBRARY_PATH na katalogi JRE
zawieraj±ce biblioteki JVM (np. libjava.so, libverify.so i libjvm.so
dla JRE Suna) przed uruchomieniem Apache'a lub interpretera PHP.

%package ldap
Summary:	LDAP extension module for PHP
Summary(pl):	Modu³ LDAP dla PHP
Summary(pt_BR):	Um módulo para aplicações PHP que usam LDAP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-ldap = %{epoch}:%{version}-%{release}

%description ldap
This is a dynamic shared object (DSO) for PHP that will add LDAP
support.

%description ldap -l pl
Modu³ PHP dodaj±cy obs³ugê LDAP.

%description ldap -l pt_BR
Um módulo para aplicações PHP que usam LDAP.

%package mbstring
Summary:	mbstring extension module for PHP
Summary(pl):	Modu³ mbstring dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-mbstring = %{epoch}:%{version}-%{release}

%description mbstring
This is a dynamic shared object (DSO) for PHP that will add multibyte
string support.

%description mbstring -l pl
Modu³ PHP dodaj±cy obs³ugê ci±gów znaków wielobajtowych.

%package mcal
Summary:	mcal extension module for PHP
Summary(pl):	Modu³ mcal dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-mcal = %{epoch}:%{version}-%{release}

%description mcal
This is a dynamic shared object (DSO) for PHP that will add mcal
(Modular Calendar Access Library) support.

%description mcal -l pl
Modu³ PHP umo¿liwiaj±cy korzystanie z biblioteki mcal (daj±cej dostêp
do kalendarzy).

%package mcrypt
Summary:	mcrypt extension module for PHP
Summary(pl):	Modu³ mcrypt dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-mcrypt = %{epoch}:%{version}-%{release}

%description mcrypt
This is a dynamic shared object (DSO) for PHP that will add mcrypt
support.

%description mcrypt -l pl
Modu³ PHP dodaj±cy mo¿liwo¶æ szyfrowania poprzez bibliotekê mcrypt.

%package mhash
Summary:	mhash extension module for PHP
Summary(pl):	Modu³ mhash dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-mhash = %{epoch}:%{version}-%{release}

%description mhash
This is a dynamic shared object (DSO) for PHP that will add mhash
support.

%description mhash -l pl
Modu³ PHP udostêpniaj±cy funkcje mieszaj±ce z biblioteki mhash.

%package mime_magic
Summary:	mime_magic extension module for PHP
Summary(pl):	Modu³ mime_magic dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	/usr/share/file/magic.mime
Provides:	php-mime_magic = %{epoch}:%{version}-%{release}

%description mime_magic
This PHP module adds support for MIME type lookup via file magic
numbers using magic.mime database.

%description mime_magic -l pl
Modu³ PHP dodaj±cy obs³ugê wyszukiwania typów MIME wed³ug magicznych
znaczników plików z u¿yciem bazy danych magic.mime.

%package ming
Summary:	ming extension module for PHP
Summary(pl):	Modu³ ming dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-ming = %{epoch}:%{version}-%{release}

%description ming
This is a dynamic shared object (DSO) for PHP that will add ming
(Flash - .swf files) support.

%description ming -l pl
Modu³ PHP dodaj±cy obs³ugê plików Flash (.swf) poprzez bibliotekê
ming.

%package mnogosearch
Summary:	mnoGoSearch extension module for PHP
Summary(pl):	Modu³ mnoGoSearch dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-mnogosearch = %{epoch}:%{version}-%{release}

%description mnogosearch
This is a dynamic shared object (DSO) for PHP that will allow you to
access mnoGoSearch free search engine.

%description mnogosearch -l pl
Modu³ PHP dodaj±cy pozwalaj±cy na dostêp do wolnodostêpnego silnika
wyszukiwarki mnoGoSearch.

%package msession
Summary:	msession extension module for PHP
Summary(pl):	Modu³ msession dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-msession = %{epoch}:%{version}-%{release}

%description msession
This is a dynamic shared object (DSO) for PHP that will allow you to
use msession. msession is a high speed session daemon which can run
either locally or remotely. It is designed to provide consistent
session management for a PHP web farm.

%description msession -l pl
Modu³ PHP dodaj±cy umo¿liwiaj±cy korzystanie z demona msession. Jest
to demon szybkiej obs³ugi sesji, który mo¿e dzia³aæ lokalnie lub na
innej maszynie. S³u¿y do zapewniania spójnej obs³ugi sesji dla farmy
serwerów.

%package mssql
Summary:	MS SQL extension module for PHP
Summary(pl):	Modu³ MS SQL dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-mssql = %{epoch}:%{version}-%{release}

%description mssql
This is a dynamic shared object (DSO) for PHP that will add MS SQL
databases support through FreeTDS library.

%description mssql -l pl
Modu³ PHP dodaj±cy obs³ugê baz danych MS SQL poprzez bibliotekê
FreeTDS.

%package mysql
Summary:	MySQL database module for PHP
Summary(pl):	Modu³ bazy danych MySQL dla PHP
Summary(pt_BR):	Um módulo para aplicações PHP que usam bancos de dados MySQL
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-mysql = %{epoch}:%{version}-%{release}

%description mysql
This is a dynamic shared object (DSO) for PHP that will add MySQL
database support.

%description mysql -l pl
Modu³ PHP umo¿liwiaj±cy dostêp do bazy danych MySQL.

%description mysql -l pt_BR
Um módulo para aplicações PHP que usam bancos de dados MySQL.

%package ncurses
Summary:	ncurses module for PHP
Summary(pl):	Modu³ ncurses dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-cli = %{epoch}:%{version}-%{release}
Requires:	%{name}-cli = %{epoch}:%{version}-%{release}
Provides:	php-ncurses = %{epoch}:%{version}-%{release}

%description ncurses
This PHP module adds support for ncurses functions (only for cli and
cgi SAPIs).

%description ncurses -l pl
Modu³ PHP dodaj±cy obs³ugê funkcji ncurses (tylko do SAPI cli i cgi).

%package oci8
Summary:	Oracle 8 database module for PHP
Summary(pl):	Modu³ bazy danych Oracle 8 dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-oci8 = %{epoch}:%{version}-%{release}
Autoreq:	false

%description oci8
This is a dynamic shared object (DSO) for PHP that will add Oracle 7
and Oracle 8 database support through Oracle8 Call-Interface (OCI8).

%description oci8 -l pl
Modu³ PHP umo¿liwiaj±cy dostêp do bazy danych Oracle 7 i Oracle 8
poprzez interfejs Oracle8 Call-Interface (OCI8).

%package odbc
Summary:	ODBC extension module for PHP
Summary(pl):	Modu³ ODBC dla PHP
Summary(pt_BR):	Um módulo para aplicações PHP que usam bases de dados ODBC
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	unixODBC >= 2.1.1-3
Provides:	php-odbc = %{epoch}:%{version}-%{release}

%description odbc
This is a dynamic shared object (DSO) for PHP that will add ODBC
support.

%description odbc -l pl
Modu³ PHP ze wsparciem dla ODBC.

%description odbc -l pt_BR
Um módulo para aplicações PHP que usam ODBC.

%package oracle
Summary:	Oracle 7 database module for PHP
Summary(pl):	Modu³ bazy danych Oracle 7 dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-oracle = %{epoch}:%{version}-%{release}
Autoreq:	false

%description oracle
This is a dynamic shared object (DSO) for PHP that will add Oracle 7
database support.

%description oracle -l pl
Modu³ PHP umo¿liwiaj±cy dostêp do bazy danych Oracle 7.

%package overload
Summary:	Overload extension module for PHP
Summary(pl):	Modu³ Overload dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-overload = %{epoch}:%{version}-%{release}

%description overload
This is a dynamic shared object (DSO) for PHP that will add user-space
object overloading support.

Warning: this is an experimental module.

%description overload -l pl
Modu³ PHP umo¿liwiaj±cy przeci±¿anie obiektów.

Uwaga: to jest modu³ eksperymentalny.

%package pcntl
Summary:	Process Control extension module for PHP
Summary(pl):	Modu³ Process Control dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-program = %{epoch}:%{version}-%{release}
Requires:	%{name}-program = %{epoch}:%{version}-%{release}
Provides:	php-pcntl = %{epoch}:%{version}-%{release}

%description pcntl
This is a dynamic shared object (DSO) for PHP that will add process
spawning and control support. It supports functions like fork(),
waitpid(), signal() etc.

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
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-pcre = %{epoch}:%{version}-%{release}

%description pcre
This is a dynamic shared object (DSO) for PHP that will add Perl
Compatible Regular Expression support.

%description pcre -l pl
Modu³ PHP umo¿liwiaj±cy korzystanie z perlowych wyra¿eñ regularnych
(Perl Compatible Regular Expressions)

%package pdf
Summary:	PDF creation module module for PHP
Summary(pl):	Modu³ do tworzenia plików PDF dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-pdf = %{epoch}:%{version}-%{release}

%description pdf
This is a dynamic shared object (DSO) for PHP that will add PDF
support through pdflib.

%description pdf -l pl
Modu³ PHP umo¿liwiaj±cy tworzenie plików PDF. Wykorzystuje bibliotekê
pdflib.

%package pgsql
Summary:	PostgreSQL database module for PHP
Summary(pl):	Modu³ bazy danych PostgreSQL dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-pgsql = %{epoch}:%{version}-%{release}

%description pgsql
This is a dynamic shared object (DSO) for PHP that will add PostgreSQL
database support.

%description pgsql -l pl
Modu³ PHP umo¿liwiaj±cy dostêp do bazy danych PostgreSQL.

%description pgsql -l pt_BR
Um módulo para aplicações PHP que usam bancos de dados postgresql.

%package posix
Summary:	POSIX extension module for PHP
Summary(pl):	Modu³ POSIX dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-posix = %{epoch}:%{version}-%{release}

%description posix
This is a dynamic shared object (DSO) for PHP that will add POSIX
functions support to PHP.

%description posix -l pl
Modu³ PHP umo¿liwiaj±cy korzystanie z funkcji POSIX.

%package pspell
Summary:	pspell extension module for PHP
Summary(pl):	Modu³ pspell dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-pspell = %{epoch}:%{version}-%{release}

%description pspell
This is a dynamic shared object (DSO) for PHP that will add pspell
support to PHP. It allows to check the spelling of a word and offer
suggestions.

%description pspell -l pl
Modu³ PHP umo¿liwiaj±cy korzystanie z pspella. Pozwala on na
sprawdzanie pisowni s³owa i sugerowanie poprawek.

%package qtdom
Summary:	Qt DOM extension module for PHP
Summary(pl):	Modu³ Qt DOM dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-qtdom = %{epoch}:%{version}-%{release}

%description qtdom
This PHP module adds Qt DOM functions support.

%description qtdom -l pl
Modu³ PHP dodaj±cy obs³ugê funkcji Qt DOM.

%package readline
Summary:	readline extension module for PHP
Summary(pl):	Modu³ readline dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-cli = %{epoch}:%{version}-%{release}
Requires:	%{name}-cli = %{epoch}:%{version}-%{release}
Provides:	php-readline = %{epoch}:%{version}-%{release}

%description readline
This PHP module adds support for readline functions (only for cli and
cgi SAPIs).

%description readline -l pl
Modu³ PHP dodaj±cy obs³ugê funkcji readline (tylko do SAPI cli i cgi).

%package recode
Summary:	recode extension module for PHP
Summary(pl):	Modu³ recode dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	recode >= 3.5d-3
Provides:	php-recode = %{epoch}:%{version}-%{release}

%description recode
This is a dynamic shared object (DSO) for PHP that will add recode
support.

%description recode -l pl
Modu³ PHP dodaj±cy mo¿liwo¶æ konwersji kodowania plików (poprzez
bibliotekê recode).

%package session
Summary:	session extension module for PHP
Summary(pl):	Modu³ session dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-session = %{epoch}:%{version}-%{release}

%description session
This is a dynamic shared object (DSO) for PHP that will add session
support.

%description session -l pl
Modu³ PHP dodaj±cy obs³ugê sesji.

%package shmop
Summary:	Shared Memory Operations extension module for PHP
Summary(pl):	Modu³ shmop dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-shmop = %{epoch}:%{version}-%{release}

%description shmop
This is a dynamic shared object (DSO) for PHP that will add Shared
Memory Operations support.

Warning: this is an experimental module.

%description shmop -l pl
Modu³ PHP umo¿liwiaj±cy korzystanie z pamiêci dzielonej.

Uwaga: to jest modu³ eksperymentalny.

%package snmp
Summary:	SNMP extension module for PHP
Summary(pl):	Modu³ SNMP dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-snmp = %{epoch}:%{version}-%{release}

%description snmp
This is a dynamic shared object (DSO) for PHP that will add SNMP
support.

%description snmp -l pl
Modu³ PHP dodaj±cy obs³ugê SNMP.

%package sockets
Summary:	sockets extension module for PHP
Summary(pl):	Modu³ socket dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-sockets = %{epoch}:%{version}-%{release}

%description sockets
This is a dynamic shared object (DSO) for PHP that will add sockets
support.

Warning: this is an experimental module.

%description sockets -l pl
Modu³ PHP dodaj±cy obs³ugê gniazdek.

Uwaga: to jest modu³ eksperymentalny.

%package sybase
Summary:	Sybase DB extension module for PHP
Summary(pl):	Modu³ Sybase DB dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-sybase = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-sybase-ct

%description sybase
This is a dynamic shared object (DSO) for PHP that will add Sybase and
MS SQL databases support through SYBDB library. Currently Sybase module
is not maintained. Using Sybase-CT module is recommended instead.

%description sybase -l pl
Modu³ PHP dodaj±cy obs³ugê baz danych Sybase oraz MS SQL poprzez
bibliotekê SYBDB. W chwili obecnej modu³ Sybase nie jest wspierany.
Zaleca siê u¿ywanie modu³u Sybase-CT.

%package sybase-ct
Summary:	Sybase-CT extension module for PHP
Summary(pl):	Modu³ Sybase-CT dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-sybase-ct = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-sybase

%description sybase-ct
This is a dynamic shared object (DSO) for PHP that will add Sybase and
MS SQL databases support through CT-lib.

%description sybase-ct -l pl
Modu³ PHP dodaj±cy obs³ugê baz danych Sybase oraz MS SQL poprzez
CT-lib.

%package sysvmsg
Summary:	SysV msg extension module for PHP
Summary(pl):	Modu³ SysV msg dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-sysvmsg = %{epoch}:%{version}-%{release}

%description sysvmsg
This is a dynamic shared object (DSO) for PHP that will add SysV
message queues support.

%description sysvmsg -l pl
Modu³ PHP umo¿liwiaj±cy korzystanie z kolejek komunikatów SysV.

%package sysvsem
Summary:	SysV sem extension module for PHP
Summary(pl):	Modu³ SysV sem dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-sysvsem = %{epoch}:%{version}-%{release}

%description sysvsem
This is a dynamic shared object (DSO) for PHP that will add SysV
semaphores support.

%description sysvsem -l pl
Modu³ PHP umo¿liwiaj±cy korzystanie z semaforów SysV.

%package sysvshm
Summary:	SysV shm extension module for PHP
Summary(pl):	Modu³ SysV shm dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-sysvshm = %{epoch}:%{version}-%{release}

%description sysvshm
This is a dynamic shared object (DSO) for PHP that will add SysV
Shared Memory support.

%description sysvshm -l pl
Modu³ PHP umo¿liwiaj±cy korzystanie z pamiêci dzielonej SysV.

%package wddx
Summary:	wddx extension module for PHP
Summary(pl):	Modu³ wddx dla PHP
Group:		Libraries
PreReq:		%{name}-session = %{epoch}:%{version}-%{release}
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-wddx = %{epoch}:%{version}-%{release}

%description wddx
This is a dynamic shared object (DSO) for PHP that will add wddx
support.

%description wddx -l pl
Modu³ PHP umo¿liwiaj±cy korzystanie z wddx.

%package xml
Summary:	XML extension module for PHP
Summary(pl):	Modu³ XML dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-xml = %{epoch}:%{version}-%{release}

%description xml
This is a dynamic shared object (DSO) for PHP that will add XML
support. This extension lets you create XML parsers and then define
handlers for different XML events.

%description xml -l pl
Modu³ PHP umo¿liwiaj±cy parsowanie plików XML i obs³ugê zdarzeñ
zwi±zanych z tymi plikami. Pozwala on tworzyæ analizatory XML-a i
nastêpnie definiowaæ procedury obs³ugi dla ró¿nych zdarzeñ XML.

%package xmlrpc
Summary:	xmlrpc extension module for PHP
Summary(pl):	Modu³ xmlrpc dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-xmlrpc = %{epoch}:%{version}-%{release}

%description xmlrpc
This is a dynamic shared object (DSO) for PHP that will add XMLRPC
support.

Warning: this is an experimental module.

%description xmlrpc -l pl
Modu³ PHP dodaj±cy obs³ugê XMLRPC.

Uwaga: to jest modu³ eksperymentalny.

%package xslt
Summary:	xslt extension module for PHP
Summary(pl):	Modu³ xslt dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-xslt = %{epoch}:%{version}-%{release}

%description xslt
This is a dynamic shared object (DSO) for PHP that will add xslt
support.

%description xslt -l pl
Modu³ PHP umo¿liwiaj±cy korzystanie z technologii xslt.

%package yaz
Summary:	yaz extension module for PHP
Summary(pl):	Modu³ yaz dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	yaz >= 1.9
Provides:	php-yaz = %{epoch}:%{version}-%{release}

%description yaz
This is a dynamic shared object (DSO) for PHP that will add yaz
support. yaz toolkit implements the Z39.50 protocol for information
retrieval.

%description yaz -l pl
Modu³ PHP umo¿liwiaj±cy korzystanie z yaz - implementacji protoko³u
Z39.50 s³u¿±cego do pozyskiwania informacji.

%package yp
Summary:	NIS (yp) extension module for PHP
Summary(pl):	Modu³ NIS (yp) dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-yp = %{epoch}:%{version}-%{release}

%description yp
This is a dynamic shared object (DSO) for PHP that will add NIS
(Yellow Pages) support.

%description yp -l pl
Modu³ PHP dodaj±cy wsparcie dla NIS (Yellow Pages).

%package zip
Summary:	zip extension module for PHP
Summary(pl):	Modu³ zip dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-zip = %{epoch}:%{version}-%{release}

%description zip
This is a dynamic shared object (DSO) for PHP that will add ZZipLib
(read-only access to ZIP archives) support.

%description zip -l pl
Modu³ PHP umo¿liwiaj±cy korzystanie z bibliotekli ZZipLib
(pozwalaj±cej na odczyt archiwów ZIP).

%package zlib
Summary:	Zlib extension module for PHP
Summary(pl):	Modu³ zlib dla PHP
Group:		Libraries
Requires(post,preun):	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	php-zlib = %{epoch}:%{version}-%{release}

%description zlib
This is a dynamic shared object (DSO) for PHP that will add zlib
compression support to PHP.

%description zlib -l pl
Modu³ PHP umo¿liwiaj±cy u¿ywanie kompresji zlib.

%prep
%setup -q -n php-%{version}
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
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%if "%{_lib}" == "lib64"
%patch29 -p1
%endif
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1

%if %{with hardening}
zcat %{SOURCE9} | patch -p1
%endif

# new apr
sed -i -e 's#apr-config#apr-1-config#g' sapi/apache*/*.m4
sed -i -e 's#apu-config#apu-1-config#g' sapi/apache*/*.m4

%build
CFLAGS="%{rpmcflags} -DEAPI=1 -I/usr/X11R6/include"
%if %{with apache2}
# Apache2 CFLAGS. harmless for other SAPIs.
CFLAGS="$CFLAGS $(%{_bindir}/apr-1-config --cppflags --includes) $(%{_bindir}/apu-1-config --includes)"
%endif

EXTENSION_DIR="%{extensionsdir}"; export EXTENSION_DIR
if [ ! -f _built-conf ]; then # configure once (for faster debugging purposes)
	./buildconf --force
	%{__libtoolize}
	%{__aclocal}
	%{__autoconf}
	touch _built-conf
fi
PROG_SENDMAIL="/usr/lib/sendmail"; export PROG_SENDMAIL

sapis="
fcgi cgi cli
%if %{with apache1}
apxs1
%endif
%if %{with apache2}
apxs2
%endif
"
for sapi in $sapis; do
	[ -f Makefile.$sapi ] && continue # skip if already configured (for faster debugging purposes)

	%configure \
	`
	case $sapi in
	cgi)
		echo --enable-discard-path
	;;
	cli)
		echo --disable-cgi
	;;
	fcgi)
		echo --enable-fastcgi --with-fastcgi=/usr
	;;
	apxs1)
		ver=%(rpm -q --qf '%%{version}' apache1-apxs)
		echo --with-apxs=%{apxs1} --with-apache-version=$ver
	;;
	apxs2)
		ver=%(rpm -q --qf '%%{version}' apache-apxs)
		echo --with-apxs2=%{apxs2} --with-apache-version=$ver
	;;
	esac
	` \
	--cache-file=config.cache \
	%{?with_zts:--enable-experimental-zts} \
	--with-config-file-path=%{_sysconfdir} \
	--with-config-file-scan-dir=%{_sysconfdir}/conf.d \
	--with-exec-dir=%{_bindir} \
	--%{!?debug:dis}%{?debug:en}able-debug \
	--enable-shared \
	--disable-static \
	--enable-magic-quotes \
	--enable-memory-limit \
	--enable-track-vars \
	--enable-safe-mode \
	\
	--enable-bcmath=shared \
	--enable-calendar=shared \
	--enable-ctype=shared \
	--enable-dba=shared \
	--enable-dbx=shared \
	--enable-dio=shared \
	--enable-exif=shared \
	--enable-ftp=shared \
	--enable-filepro=shared \
	--enable-mbstring=shared,all --enable-mbregex \
	--enable-overload=shared \
	--enable-pcntl=shared \
	--enable-posix=shared \
	--enable-session --enable-trans-sid \
	--enable-shmop=shared \
	--enable-sysvmsg=shared \
	--enable-sysvsem=shared \
	--enable-sysvshm=shared \
	--enable-sockets=shared \
	%{?with_recode:--with-recode=shared} \
	%{?with_mm:--with-mm} \
	%{?with_wddx:--enable-wddx=shared} \
	%{!?with_xml:--disable-xml}%{?with_xml:--enable-xml=shared} \
	%{?with_xslt:--enable-xslt=shared} \
	--enable-yp=shared \
	--with-bz2=shared \
	%{?with_cpdf:--with-cpdflib=shared} \
	--with-crack=shared \
	%{!?with_curl:--without-curl}%{?with_curl:--with-curl=shared} \
	--with-db=shared \
	%{?with_db3:--with-db3}%{!?with_db3:--with-db4} \
	--with-dbase=shared \
	%{?with_xml:--with-dom=shared} \
	%{?with_domxslt:--with-dom-xslt=shared --with-dom-exslt=shared} \
%if %{with xml} || %{with xmlrpc}
	--with-expat-dir=shared,/usr \
%else
	--without-expat-dir \
%endif
	%{?with_fdf:--with-fdftk=shared} \
	%{?with_fribidi:--with-fribidi=shared} \
	--with-iconv=shared \
	--with-filepro=shared \
	--with-freetype-dir=shared \
	--with-gettext=shared \
	--with-gd=shared,/usr --enable-gd-native-ttf \
	--with-gdbm \
	--with-gmp=shared \
	--with-hyperwave=shared \
	%{?with_imap:--with-imap=shared --with-imap-ssl --with-kerberos} \
	%{?with_interbase:--with-interbase=shared%{!?with_interbase_inst:,/usr}} \
	%{?with_java:--with-java=%{_libdir}/java} \
	--with-jpeg-dir=/usr \
	%{?with_ldap:--with-ldap=shared} \
	--with-mcal=shared,/usr \
	--with-mcrypt=shared \
	%{?with_mhash:--with-mhash=shared} \
	--with-mime-magic=shared,/usr/share/file/magic.mime \
	%{?with_ming:--with-ming=shared} \
	%{!?with_mnogosearch:--without-mnogosearch}%{?with_mnogosearch:--with-mnogosearch=shared,/usr} \
	%{?with_msession:--with-msession=shared}%{!?with_msession:--without-msession} \
	%{?with_mssql:--with-mssql=shared} \
	--with-mysql=shared,/usr --with-mysql-sock=/var/lib/mysql/mysql.sock \
	--with-ncurses=shared \
	%{?with_oci8:--with-oci8=shared} \
	%{?with_openssl:--with-openssl} \
	%{?with_oracle:--with-oracle=shared} \
	%{!?with_pcre:--without-pcre-regex}%{?with_pcre:--with-pcre-regex=shared} \
	%{?with_pdf:--with-pdflib=shared} \
	--with-pear=%{php_pear_dir} \
	%{!?with_pgsql:--without-pgsql}%{?with_pgsql:--with-pgsql=shared,/usr} \
	--with-png-dir=/usr \
	%{?with_pspell:--with-pspell=shared} \
	--with-readline=shared \
	--with-regex=php \
	%{?with_qtdom:--with-qtdom=shared} \
	--without-sablot-js \
	%{?with_snmp:--with-snmp=shared --enable-ucd-snmp-hack} \
	%{?with_sybase:--with-sybase-ct=shared,/usr --with-sybase=shared,/usr} \
	--with-t1lib=shared \
	--with-tiff-dir=/usr \
	%{?with_odbc:--with-unixODBC=shared} \
	%{!?with_xmlrpc:--without-xmlrpc}%{?with_xmlrpc:--with-xmlrpc=shared,/usr} \
	%{?with_xslt:--with-xslt-sablot=shared} \
	%{?with_yaz:--with-yaz=shared} \
	--with-zip=shared \
	--with-zlib=shared \
	--with-zlib-dir=shared,/usr

	cp -f Makefile Makefile.$sapi

	# left for debugging purposes
	cp -f main/php_config.h php_config.h.$sapi
done

# for now session_mm doesn't work with shared session module...
# --enable-session=shared
# %{!?with_mm:--with-mm=shared,no}%{?with_mm:--with-mm=shared}

%{__make} build-modules

%{__make} libphp_common.la
# fix install paths, avoid evil rpaths
sed -i -e "s|^libdir=.*|libdir='%{_libdir}'|" libphp_common.la

%if %{with apache1}
%{__make} libtool-sapi LIBTOOL_SAPI=sapi/apache/libphp4.la -f Makefile.apxs1
sed -i -e "
s|^libdir=.*|libdir='%{_libdir}/apache1'|;
s|^(relink_command=.* -rpath )[^ ]*/libs |$1%{_libdir}/apache1 |" sapi/apache/libphp4.la
%endif

%if %{with apache2}
%{__make} libtool-sapi LIBTOOL_SAPI=sapi/apache2handler/libphp4.la -f Makefile.apxs2
sed -i -e "
s|^libdir=.*|libdir='%{_libdir}/apache'|;
s|^(relink_command=.* -rpath )[^ ]*/libs |$1%{_libdir}/apache |" sapi/apache2handler/libphp4.la
%endif

# for fcgi: -DDISCARD_PATH=0 -DENABLE_PATHINFO_CHECK=1 -DFORCE_CGI_REDIRECT=0
# -DHAVE_FILENO_PROTO=1 -DHAVE_FPOS=1 -DHAVE_LIBNSL=1(die) -DHAVE_SYS_PARAM_H=1
# -DPHP_FASTCGI=1 -DPHP_FCGI_STATIC=1 -DPHP_WRITE_STDOUT=1
%{__make} sapi/cgi/php -f Makefile.fcgi \
	CFLAGS_CLEAN="%{rpmcflags} -DDISCARD_PATH=0 -DENABLE_PATHINFO_CHECK=1 -DFORCE_CGI_REDIRECT=0 -DHAVE_FILENO_PROTO=1 -DHAVE_FPOS=1 -DHAVE_LIBNSL=1 -DHAVE_SYS_PARAM_H=1 -DPHP_FASTCGI=1 -DPHP_FCGI_STATIC=1 -DPHP_WRITE_STDOUT=1"
cp -r sapi/cgi sapi/fcgi
rm -rf sapi/cgi/.libs sapi/cgi/*.lo

# notes:
# -DENABLE_CHROOT_FUNC=1 (cgi,fcgi) is used in ext/standard/dir.c (libphp_common)
# -DPHP_WRITE_STDOUT is used also for cli, but not set by its config.m4
%{__make} sapi/cgi/php -f Makefile.cgi \
	CFLAGS_CLEAN="%{rpmcflags} -DDISCARD_PATH=1 -DENABLE_PATHINFO_CHECK=1 -DFORCE_CGI_REDIRECT=0 -DPHP_WRITE_STDOUT=1"

# CLI
%{__make} sapi/cli/php -f Makefile.cli

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/{php,apache{,1}},%{_sysconfdir}/{apache,cgi}} \
	$RPM_BUILD_ROOT/home/services/{httpd,apache}/icons \
	$RPM_BUILD_ROOT{%{_sbindir},%{_bindir}} \
	$RPM_BUILD_ROOT/var/run/php \
	$RPM_BUILD_ROOT{/etc/apache/conf.d,/etc/httpd/httpd.conf} \
	$RPM_BUILD_ROOT%{_mandir}/man1

# install apache1 DSO module
%if %{with apache1}
# TODO: use libtool here
install sapi/apache/.libs/libphp4.so $RPM_BUILD_ROOT%{_libdir}/apache1/libphp4.so
%endif

# install apache2 DSO module
%if %{with apache2}
# TODO: use libtool here
install sapi/apache2handler/.libs/libphp4.so $RPM_BUILD_ROOT%{_libdir}/apache/libphp4.so
%endif

libtool --silent --mode=install install libphp_common.la $RPM_BUILD_ROOT%{_libdir}

# install the apache modules' files
make install-headers install-build install-modules install-programs \
	INSTALL_ROOT=$RPM_BUILD_ROOT

# install CGI
libtool --silent --mode=install install sapi/cgi/php $RPM_BUILD_ROOT%{_bindir}/php4.cgi

# install FCGI
libtool --silent --mode=install install sapi/fcgi/php $RPM_BUILD_ROOT%{_bindir}/php4.fcgi

# install CLI
libtool --silent --mode=install install sapi/cli/php $RPM_BUILD_ROOT%{_bindir}/php4.cli

install sapi/cli/php.1 $RPM_BUILD_ROOT%{_mandir}/man1/php4.1
ln -sf php4.cli $RPM_BUILD_ROOT%{_bindir}/php4

%{?with_java:install ext/java/php_java.jar $RPM_BUILD_ROOT%{extensionsdir}}

install php.ini	$RPM_BUILD_ROOT%{_sysconfdir}/php.ini
install %{SOURCE5} $RPM_BUILD_ROOT%{_sysconfdir}/php-cgi-fcgi.ini
install %{SOURCE6} $RPM_BUILD_ROOT%{_sysconfdir}/php-cgi.ini
install %{SOURCE7} $RPM_BUILD_ROOT%{_sysconfdir}/php-apache.ini
install %{SOURCE7} $RPM_BUILD_ROOT%{_sysconfdir}/php-apache2handler.ini
install %{SOURCE8} $RPM_BUILD_ROOT%{_sysconfdir}/php-cli.ini

install %{SOURCE2} php.gif $RPM_BUILD_ROOT/home/services/httpd/icons
install %{SOURCE2} php.gif $RPM_BUILD_ROOT/home/services/apache/icons
install %{SOURCE3} $RPM_BUILD_ROOT%{_sbindir}
install %{SOURCE4} $RPM_BUILD_ROOT/etc/apache/conf.d/70_mod_php4.conf
install %{SOURCE4} $RPM_BUILD_ROOT/etc/httpd/httpd.conf/70_mod_php4.conf
install %{SOURCE1} .

cp -f Zend/LICENSE{,.Zend}

# Generate stub .ini files for each subpackage
install -d $RPM_BUILD_ROOT%{_sysconfdir}/conf.d
for so in modules/*.so; do
	mod=$(basename $so .so)
	cat > $RPM_BUILD_ROOT%{_sysconfdir}/conf.d/${mod}.ini <<EOF
; Enable ${mod} extension module
extension=${mod}.so
EOF
done

# Not in all SAPI, so don't need the .ini fragments.
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/conf.d/{ncurses,pcntl,readline}.ini

%clean
rm -rf $RPM_BUILD_ROOT

# minimizing apache restarts logics:
#
# 1. we restart webserver after extension install only:
# 1.1 if it's first install (post: $1 = 1)
# 1.2 or uninstall of extension (postun: $1 == 0)
# 2. the upgrades are handled by common package:
# 2.1 webserver is restarted only if common package was upgraded (postun: $1 = 1)
#
# note that this creates "delay" when webserver is restarted, ie the
# actual restart is done by *previous* version of php-common package
# (the one being just postun'ed).
#
# the strict internal deps between extensions (and apache modules) and
# common package are very important for all this to work. also conf.d
# without conf.d this would be more complex.

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
	[ ! -f /etc/httpd/httpd.conf/??_mod_php4.conf ] || %service -q httpd restart \
fi

# macro called at extension postun scriptlet
%define	extension_postun \
if [ "$1" = "0" ]; then \
	[ ! -f /etc/apache/conf.d/??_mod_php4.conf ] || %service -q apache restart \
	[ ! -f /etc/httpd/httpd.conf/??_mod_php4.conf ] || %service -q httpd restart \
fi

%post	common -p /sbin/ldconfig
%postun	common
/sbin/ldconfig
# extension_post here is all correct.
%extension_post

# compensate missing restart of earlier -common package.
%triggerpostun common -- %{name}-common < 3:4.4.0-4.42
[ ! -f /etc/apache/conf.d/??_mod_php4.conf ] || %service -q apache restart
[ ! -f /etc/httpd/httpd.conf/??_mod_php4.conf ] || %service -q httpd restart

%if %{with apache2}
%triggerpostun -- php4 < 3:4.3.11-4.16
# for fixed php-SAPI.ini, the poor php-apache.ini was never read for apache2
if [ -f %{_sysconfdir}/php-apache.ini.rpmsave ]; then
	cp -f %{_sysconfdir}/php-apache2handler.ini{,.rpmnew}
	mv -f %{_sysconfdir}/php-apache.ini.rpmsave %{_sysconfdir}/php-apache2handler.ini
fi
# extra trigger, if they did not upgrade to 3:4.4.0-2 but still had old php-apache.ini
%triggerpostun -n apache-mod_php4 -- apache-mod_php4 < 3:4.4.0-2.16
# for fixed php-SAPI.ini, the poor php-apache.ini was never read for apache2
if [ -f %{_sysconfdir}/php-apache.ini.rpmsave ]; then
	cp -f %{_sysconfdir}/php-apache2handler.ini{,.rpmnew}
	mv -f %{_sysconfdir}/php-apache.ini.rpmsave %{_sysconfdir}/php-apache2handler.ini
fi
%endif

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

%post ncurses
# NOTE: only for cli/cgi
if [ -f %{_sysconfdir}/php-cgi.ini ]; then
	%{_sbindir}/php4-module-install install ncurses %{_sysconfdir}/php-cgi.ini
fi
if [ -f %{_sysconfdir}/php-cli.ini ]; then
	%{_sbindir}/php4-module-install install ncurses %{_sysconfdir}/php-cli.ini
fi

%preun ncurses
if [ "$1" = "0" ]; then
	if [ -f %{_sysconfdir}/php-cgi.ini ]; then
		[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove ncurses %{_sysconfdir}/php-cgi.ini
	fi
	if [ -f %{_sysconfdir}/php-cli.ini ]; then
		[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove ncurses %{_sysconfdir}/php-cli.ini
	fi
fi

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

%post pcntl
# NOTE: only for cli/cgi
if [ -f %{_sysconfdir}/php-cgi.ini ]; then
	%{_sbindir}/php4-module-install install pcntl %{_sysconfdir}/php-cgi.ini
fi
if [ -f %{_sysconfdir}/php-cli.ini ]; then
	%{_sbindir}/php4-module-install install pcntl %{_sysconfdir}/php-cli.ini
fi

%preun pcntl
if [ "$1" = "0" ]; then
	if [ -f %{_sysconfdir}/php-cgi.ini ]; then
		[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove pcntl %{_sysconfdir}/php-cgi.ini
	fi
	if [ -f %{_sysconfdir}/php-cli.ini ]; then
		[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove pcntl %{_sysconfdir}/php-cli.ini
	fi
fi

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

%post readline
# NOTE: only for cli/cgi
if [ -f %{_sysconfdir}/php-cgi.ini ]; then
	%{_sbindir}/php4-module-install install readline %{_sysconfdir}/php-cgi.ini
fi
if [ -f %{_sysconfdir}/php-cli.ini ]; then
	%{_sbindir}/php4-module-install install readline %{_sysconfdir}/php-cli.ini
fi

%preun readline
if [ "$1" = "0" ]; then
	if [ -f %{_sysconfdir}/php-cgi.ini ]; then
		[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove readline %{_sysconfdir}/php-cgi.ini
	fi
	if [ -f %{_sysconfdir}/php-cli.ini ]; then
		[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove readline %{_sysconfdir}/php-cli.ini
	fi
fi

%post recode
%extension_post

%postun recode
%extension_postun

%post session
%extension_post

%postun session
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
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove openssl %{_sysconfdir}/php.ini

%triggerun bcmath -- %{name}-bcmath < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove bcmath %{_sysconfdir}/php.ini

%triggerun bzip2 -- %{name}-bzip2 < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove bz2 %{_sysconfdir}/php.ini

%triggerun calendar -- %{name}-calendar < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove calendar %{_sysconfdir}/php.ini

%triggerun cpdf -- %{name}-cpdf < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove cpdf %{_sysconfdir}/php.ini

%triggerun crack -- %{name}-crack < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove crack %{_sysconfdir}/php.ini

%triggerun ctype -- %{name}-ctype < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove ctype %{_sysconfdir}/php.ini

%triggerun curl -- %{name}-curl < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove curl %{_sysconfdir}/php.ini

%triggerun db -- %{name}-db < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove db %{_sysconfdir}/php.ini

%triggerun dba -- %{name}-dba < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove dba %{_sysconfdir}/php.ini

%triggerun dbase -- %{name}-dbase < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove dbase %{_sysconfdir}/php.ini

%triggerun dbx -- %{name}-dbx < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove dbx %{_sysconfdir}/php.ini

%triggerun dio -- %{name}-dio < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove dio %{_sysconfdir}/php.ini

%triggerun domxml -- %{name}-domxml < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove domxml %{_sysconfdir}/php.ini

%triggerun exif -- %{name}-exif < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove exif %{_sysconfdir}/php.ini

%triggerun fdf -- %{name}-fdf < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove fdf %{_sysconfdir}/php.ini

%triggerun filepro -- %{name}-filepro < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove filepro %{_sysconfdir}/php.ini

%triggerun fribidi -- %{name}-fribidi < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove fribidi %{_sysconfdir}/php.ini

%triggerun ftp -- %{name}-ftp < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove ftp %{_sysconfdir}/php.ini

%triggerun gd -- %{name}-gd < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove gd %{_sysconfdir}/php.ini

%triggerun gettext -- %{name}-gettext < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove gettext %{_sysconfdir}/php.ini

%triggerun gmp -- %{name}-gmp < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove gmp %{_sysconfdir}/php.ini

%triggerun hyperwave -- %{name}-hyperwave < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove hyperwave %{_sysconfdir}/php.ini

%triggerun iconv -- %{name}-iconv < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove iconv %{_sysconfdir}/php.ini

%triggerun imap -- %{name}-imap < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove imap %{_sysconfdir}/php.ini

%triggerun interbase -- %{name}-interbase < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove interbase %{_sysconfdir}/php.ini

%triggerun java -- %{name}-java < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove java %{_sysconfdir}/php.ini

%triggerun ldap -- %{name}-ldap < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove ldap %{_sysconfdir}/php.ini

%triggerun mbstring -- %{name}-mbstring < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove mbstring %{_sysconfdir}/php.ini

%triggerun mcal -- %{name}-mcal < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove mcal %{_sysconfdir}/php.ini

%triggerun mcrypt -- %{name}-mcrypt < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove mcrypt %{_sysconfdir}/php.ini

%triggerun mhash -- %{name}-mhash < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove mhash %{_sysconfdir}/php.ini

%triggerun mime_magic -- %{name}-mime_magic < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove mime_magic %{_sysconfdir}/php.ini

%triggerun ming -- %{name}-ming < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove ming %{_sysconfdir}/php.ini

%triggerun mnogosearch -- %{name}-mnogosearch < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove mnogosearch %{_sysconfdir}/php.ini

%triggerun msession -- %{name}-msession < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove msession %{_sysconfdir}/php.ini

%triggerun mssql -- %{name}-mssql < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove mssql %{_sysconfdir}/php.ini

%triggerun mysql -- %{name}-mysql < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove mysql %{_sysconfdir}/php.ini

%triggerun oci8 -- %{name}-oci8 < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove oci8 %{_sysconfdir}/php.ini

%triggerun odbc -- %{name}-odbc < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove odbc %{_sysconfdir}/php.ini

%triggerun oracle -- %{name}-oracle < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove oracle %{_sysconfdir}/php.ini

%triggerun overload -- %{name}-overload < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove overload %{_sysconfdir}/php.ini

%triggerun pcre -- %{name}-pcre < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove pcre %{_sysconfdir}/php.ini

%triggerun pdf -- %{name}-pdf < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove pdf %{_sysconfdir}/php.ini

%triggerun pgsql -- %{name}-pgsql < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove pgsql %{_sysconfdir}/php.ini

%triggerun posix -- %{name}-posix < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove posix %{_sysconfdir}/php.ini

%triggerun pspell -- %{name}-pspell < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove pspell %{_sysconfdir}/php.ini

%triggerun qtdom -- %{name}-qtdom < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove qtdom %{_sysconfdir}/php.ini

%triggerun recode -- %{name}-recode < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove recode %{_sysconfdir}/php.ini

%triggerun session -- %{name}-session < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove session %{_sysconfdir}/php.ini

%triggerun shmop -- %{name}-shmop < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove shmop %{_sysconfdir}/php.ini

%triggerun snmp -- %{name}-snmp < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove snmp %{_sysconfdir}/php.ini

%triggerun sockets -- %{name}-sockets < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove sockets %{_sysconfdir}/php.ini

%triggerun sybase -- %{name}-sybase < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove sybase %{_sysconfdir}/php.ini

%triggerun sybase-ct -- %{name}-sybase-ct < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove sybase_ct %{_sysconfdir}/php.ini

%triggerun sysvmsg -- %{name}-sysvmsg < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove sysvmsg %{_sysconfdir}/php.ini

%triggerun sysvsem -- %{name}-sysvsem < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove sysvsem %{_sysconfdir}/php.ini

%triggerun sysvshm -- %{name}-sysvshm < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove sysvshm %{_sysconfdir}/php.ini

%triggerun wddx -- %{name}-wddx < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove wddx %{_sysconfdir}/php.ini

%triggerun xml -- %{name}-xml < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove xml %{_sysconfdir}/php.ini

%triggerun xmlrpc -- %{name}-xmlrpc < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove xmlrpc %{_sysconfdir}/php.ini

%triggerun xslt -- %{name}-xslt < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove xslt %{_sysconfdir}/php.ini

%triggerun yaz -- %{name}-yaz < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove yaz %{_sysconfdir}/php.ini

%triggerun yp -- %{name}-yp < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove yp %{_sysconfdir}/php.ini

%triggerun zip -- %{name}-zip < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove zip %{_sysconfdir}/php.ini

%triggerun zlib -- %{name}-zlib < 3:4.4.0-2.1
[ ! -x %{_sbindir}/php4-module-install ] || %{_sbindir}/php4-module-install remove zlib %{_sysconfdir}/php.ini

%if %{with apache1}
%files -n apache1-mod_php4
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/apache/conf.d/*_mod_php4.conf
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/php-apache.ini
%attr(755,root,root) %{_libdir}/apache1/libphp4.so
/home/services/apache/icons/*
%endif

%if %{with apache2}
%files -n apache-mod_php4
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/httpd/httpd.conf/*_mod_php4.conf
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/php-apache2handler.ini
%attr(755,root,root) %{_libdir}/apache/libphp4.so
/home/services/httpd/icons/*
%endif

%files fcgi
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/php4.fcgi
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/php-cgi-fcgi.ini

%files cgi
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/php4.cgi
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/php-cgi.ini

%files cli
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/php4.cli
# TODO
# - what about _bindir/php symlink?
# - do it same way link /usr/src/linux is done, ie each package updates symlink
%attr(755,root,root) %{_bindir}/php4
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/php-cli.ini
%{_mandir}/man1/php4.1*

%files common
%defattr(644,root,root,755)
%doc php.ini-*
%doc CODING_STANDARDS CREDITS Zend/ZEND_CHANGES
%doc LICENSE Zend/LICENSE.Zend EXTENSIONS NEWS TODO*
%doc README.EXT_SKEL README.SELF-CONTAINED-EXTENSIONS

%dir %{_sysconfdir}
%dir %{_sysconfdir}/conf.d
%attr(644,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/php.ini
%attr(770,root,http) %dir %verify(not group mode) /var/run/php
%attr(755,root,root) %{_sbindir}/php4-module-install
%attr(755,root,root) %{_libdir}/libphp_common-*.so
%dir %{extensionsdir}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/phpize
%attr(755,root,root) %{_bindir}/php-config
%attr(755,root,root) %{_libdir}/libphp_common.so
# FIXME: how exactly this is needed? as it contains libdir for apache1 or apache2
%{_libdir}/libphp_common.la
%{_includedir}/php
%{_libdir}/php/build
%{_mandir}/man1/php-config.1*
%{_mandir}/man1/phpize.1*

%files bcmath
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/bcmath.ini
%attr(755,root,root) %{extensionsdir}/bcmath.so

%files bzip2
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/bz2.ini
%attr(755,root,root) %{extensionsdir}/bz2.so

%files calendar
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/calendar.ini
%attr(755,root,root) %{extensionsdir}/calendar.so

%if %{with cpdf}
%files cpdf
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/cpdf.ini
%attr(755,root,root) %{extensionsdir}/cpdf.so
%endif

%files crack
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/crack.ini
%attr(755,root,root) %{extensionsdir}/crack.so

%files ctype
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/ctype.ini
%attr(755,root,root) %{extensionsdir}/ctype.so

%if %{with curl}
%files curl
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/curl.ini
%attr(755,root,root) %{extensionsdir}/curl.so
%endif

%files db
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/db.ini
%attr(755,root,root) %{extensionsdir}/db.so

%files dba
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/dba.ini
%attr(755,root,root) %{extensionsdir}/dba.so

%files dbase
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/dbase.ini
%attr(755,root,root) %{extensionsdir}/dbase.so

%files dbx
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/dbx.ini
%attr(755,root,root) %{extensionsdir}/dbx.so

%files dio
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/dio.ini
%attr(755,root,root) %{extensionsdir}/dio.so

%if %{with xml}
%files domxml
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/domxml.ini
%attr(755,root,root) %{extensionsdir}/domxml.so
%endif

%if %{with fdf}
%files fdf
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/fdf.ini
%attr(755,root,root) %{extensionsdir}/fdf.so
%endif

%files exif
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/exif.ini
%attr(755,root,root) %{extensionsdir}/exif.so

%files filepro
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/filepro.ini
%attr(755,root,root) %{extensionsdir}/filepro.so

%if %{with fribidi}
%files fribidi
%defattr(644,root,root,755)
%doc ext/fribidi/{CREDITS,README}
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/fribidi.ini
%attr(755,root,root) %{extensionsdir}/fribidi.so
%endif

%files ftp
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/ftp.ini
%attr(755,root,root) %{extensionsdir}/ftp.so

%files gd
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/gd.ini
%attr(755,root,root) %{extensionsdir}/gd.so

%files gettext
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/gettext.ini
%attr(755,root,root) %{extensionsdir}/gettext.so

%files gmp
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/gmp.ini
%attr(755,root,root) %{extensionsdir}/gmp.so

%files hyperwave
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/hyperwave.ini
%attr(755,root,root) %{extensionsdir}/hyperwave.so

%files iconv
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/iconv.ini
%attr(755,root,root) %{extensionsdir}/iconv.so

%if %{with imap}
%files imap
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/imap.ini
%attr(755,root,root) %{extensionsdir}/imap.so
%endif

%if %{with interbase}
%files interbase
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/interbase.ini
%attr(755,root,root) %{extensionsdir}/interbase.so
%endif

%if %{with java}
%files java
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/java.ini
%attr(755,root,root) %{extensionsdir}/java.so
%{extensionsdir}/php_java.jar
%endif

%if %{with ldap}
%files ldap
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/ldap.ini
%attr(755,root,root) %{extensionsdir}/ldap.so
%endif

%files mbstring
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/mbstring.ini
%attr(755,root,root) %{extensionsdir}/mbstring.so

%files mcal
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/mcal.ini
%attr(755,root,root) %{extensionsdir}/mcal.so

%files mcrypt
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/mcrypt.ini
%attr(755,root,root) %{extensionsdir}/mcrypt.so

%if %{with mhash}
%files mhash
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/mhash.ini
%attr(755,root,root) %{extensionsdir}/mhash.so
%endif

%files mime_magic
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/mime_magic.ini
%attr(755,root,root) %{extensionsdir}/mime_magic.so

%if %{with ming}
%files ming
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/ming.ini
%attr(755,root,root) %{extensionsdir}/ming.so
%endif

%if %{with mnogosearch}
%files mnogosearch
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/mnogosearch.ini
%attr(755,root,root) %{extensionsdir}/mnogosearch.so
%endif

%if %{with msession}
%files msession
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/msession.ini
%attr(755,root,root) %{extensionsdir}/msession.so
%endif

%if %{with mssql}
%files mssql
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/mssql.ini
%attr(755,root,root) %{extensionsdir}/mssql.so
%endif

%files mysql
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/mysql.ini
%attr(755,root,root) %{extensionsdir}/mysql.so

%files ncurses
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/ncurses.so

%if %{with oci8}
%files oci8
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/oci8.ini
%attr(755,root,root) %{extensionsdir}/oci8.so
%endif

%if %{with odbc}
%files odbc
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/odbc.ini
%attr(755,root,root) %{extensionsdir}/odbc.so
%endif

%if %{with oracle}
%files oracle
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/oracle.ini
%attr(755,root,root) %{extensionsdir}/oracle.so
%endif

%files overload
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/overload.ini
%attr(755,root,root) %{extensionsdir}/overload.so

%files pcntl
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/pcntl.so

%if %{with pcre}
%files pcre
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/pcre.ini
%attr(755,root,root) %{extensionsdir}/pcre.so
%endif

%if %{with pdf}
%files pdf
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/pdf.ini
%attr(755,root,root) %{extensionsdir}/pdf.so
%endif

%if %{with pgsql}
%files pgsql
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/pgsql.ini
%attr(755,root,root) %{extensionsdir}/pgsql.so
%endif

%files posix
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/posix.ini
%attr(755,root,root) %{extensionsdir}/posix.so

%if %{with pspell}
%files pspell
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/pspell.ini
%attr(755,root,root) %{extensionsdir}/pspell.so
%endif

%if %{with qtdom}
%files qtdom
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/qtdom.ini
%attr(755,root,root) %{extensionsdir}/qtdom.so
%endif

%files readline
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/readline.so

%if %{with recode}
%files recode
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/recode.ini
%attr(755,root,root) %{extensionsdir}/recode.so
%endif

# session_mm doesn't work with shared session
#%files session
#%defattr(644,root,root,755)
#%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/session.ini
#%attr(755,root,root) %{extensionsdir}/session.so

%files shmop
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/shmop.ini
%attr(755,root,root) %{extensionsdir}/shmop.so

%if %{with snmp}
%files snmp
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/snmp.ini
%attr(755,root,root) %{extensionsdir}/snmp.so
%endif

%files sockets
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/sockets.ini
%attr(755,root,root) %{extensionsdir}/sockets.so

%if %{with sybase}
%files sybase
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/sybase.ini
%attr(755,root,root) %{extensionsdir}/sybase.so

%files sybase-ct
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/sybase_ct.ini
%attr(755,root,root) %{extensionsdir}/sybase_ct.so
%endif

%files sysvmsg
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/sysvmsg.ini
%attr(755,root,root) %{extensionsdir}/sysvmsg.so

%files sysvsem
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/sysvsem.ini
%attr(755,root,root) %{extensionsdir}/sysvsem.so

%files sysvshm
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/sysvshm.ini
%attr(755,root,root) %{extensionsdir}/sysvshm.so

%if %{with wddx}
%files wddx
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/wddx.ini
%attr(755,root,root) %{extensionsdir}/wddx.so
%endif

%if %{with xml}
%files xml
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/xml.ini
%attr(755,root,root) %{extensionsdir}/xml.so
%endif

%if %{with xmlrpc}
%files xmlrpc
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/xmlrpc.ini
%attr(755,root,root) %{extensionsdir}/xmlrpc.so
%endif

%if %{with xslt}
%files xslt
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/xslt.ini
%attr(755,root,root) %{extensionsdir}/xslt.so
%endif

%if %{with yaz}
%files yaz
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/yaz.ini
%attr(755,root,root) %{extensionsdir}/yaz.so
%endif

%files yp
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/yp.ini
%attr(755,root,root) %{extensionsdir}/yp.so

%files zip
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/zip.ini
%attr(755,root,root) %{extensionsdir}/zip.so

%files zlib
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/conf.d/zlib.ini
%attr(755,root,root) %{extensionsdir}/zlib.so
