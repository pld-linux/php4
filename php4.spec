Summary:	The PHP HTML-embedded scripting language for use with Apache.
Summary(pl):	Jêzyk skryptowy PHP -- u¿ywany wraz z serwerem Apache.
Name:		php
Version:	4.0b4pl1
Release:	1
Group:		Libraries
Group(pl):	X11/Programowanie/Biblioteki
Group:		Biblioteki
License:	GPL
Source0:	http://www.php.net/distributions/%{name}-%{version}.tar.gz
Source1:	FAQ.php
Source2:	php.ini
Source3:	zend.gif
Icon:		php4.gif
URL:		http://www.php.net/
BuildRequires:	apache-devel
BuildRequires:	zlib-devel
BuildRequires:	mysql-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%description
PHP is an HTML-embedded scripting language.  PHP attempts to make it easy
for developers to write dynamically generated web pages.  PHP also offers
built-in database integration for several commercial and non-commercial
database management systems, so writing a database-enabled web page with
PHP is fairly simple.  The most common use of PHP coding is probably as a
replacement for CGI scripts.  The mod_php module enables the Apache web
server to understand and process the embedded PHP language in web pages.
This package contains PHP.  If you use applications which specifically rely
on PHP/FI (PHP v2 and earlier), you should instead install the PHP/FI
module contained in the phpfi package.  If you're just starting with PHP,
you should install this package.  You'll also need to install the Apache
web server.

%description -l pl
PHP jest jêzykiem skryptowym

%prep
%setup -q 

%build
./buildconf
%configure \
	--with-apxs=%{_sbindir}/apxs \
	--with-config-file-path=%{_sysconfdir}/httpd \
	--enable-safe-mode \
	--with-exec-dir=%{_bindir} \
	--disable-debug \
	--with-zlib \
	--enable-magic-quotes \
	--enable-track-vars \
	--without-gd \
	--with-mysql \
	--enable-shared 
make


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/apache,%{_sysconfdir}/httpd} \
		$RPM_BUILD_ROOT/home/httpd/html/icons

install .libs/*.so	$RPM_BUILD_ROOT%{_libdir}/apache
install %{SOURCE2}	$RPM_BUILD_ROOT%{_sysconfdir}/httpd/php.ini
install %{SOURCE3} 	$RPM_BUILD_ROOT/home/httpd/html/icons

strip --strip-unneeded	$RPM_BUILD_ROOT%{_libdir}/apache/*.so

install  %{SOURCE1}	.
gzip -9nf CODING_STANDARDS CREDITS FAQ* 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {CODING_STANDARDS,CREDITS,FAQ*}.gz  

%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd/*
%attr(755,root,root) %{_libdir}/apache/libphp4.so
