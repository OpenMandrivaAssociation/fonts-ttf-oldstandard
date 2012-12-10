%define pkgname oldstandard

Summary:	Old-style font family
Name:		fonts-ttf-oldstandard
Version:	2.2
Release:	%mkrel 1
License:	OFL
Group:		System/Fonts/True type
URL:		http://www.thessalonica.org.ru/en/fonts.html
Source0:	http://www.thessalonica.org.ru/downloads/%{pkgname}-%{version}.ttf.zip
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
BuildRequires:	freetype-tools
BuildRequires:	dos2unix

%description
Old Standard is a multilingual font family, supposed to be a good companion
for Thessalonica. It is based on Russian and German editions of the late 19th
and early 20th centuries and reproduces the so-called "Modern" style, extremely
popular in its time, but almost completely abandoned later. This project is
currently most mature and stable, although still has a large field
for improvements. The Old Standard font family currently includes three shapes
(regular, italic and bold) and has more than 1400 glyphs in the regular
version.

%prep
%setup -q -c -n %{pkgname}-%{version}
dos2unix OFL-FAQ.txt

%build

%install
%__rm -rf %{buildroot}

%__mkdir_p %{buildroot}%{_xfontdir}/TTF/oldstandard

%__install -m 644 *.ttf %{buildroot}%{_xfontdir}/TTF/oldstandard
ttmkfdir %{buildroot}%{_xfontdir}/TTF/oldstandard -o %{buildroot}%{_xfontdir}/TTF/oldstandard/fonts.dir
%__ln_s fonts.dir %{buildroot}%{_xfontdir}/TTF/oldstandard/fonts.scale

%__mkdir_p %{buildroot}%_sysconfdir/X11/fontpath.d/
%__ln_s ../../..%{_xfontdir}/TTF/oldstandard \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-oldstandard:pri=50

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc FONTLOG.txt OFL.txt OFL-FAQ.txt
%dir %{_xfontdir}/TTF/oldstandard
%{_xfontdir}/TTF/oldstandard/*.ttf
%verify(not mtime) %{_datadir}/fonts/TTF/oldstandard/fonts.dir
%{_xfontdir}/TTF/oldstandard/fonts.scale
%{_sysconfdir}/X11/fontpath.d/ttf-oldstandard:pri=50





%changelog
* Fri Dec 09 2011 Dmitry Mikhirev <dmikhirev@mandriva.org> 2.2-1mdv2012.0
+ Revision: 739416
- Update to 2.2

* Fri Jul 22 2011 Sergey Zhemoitel <serg@mandriva.org> 2.0.2-1
+ Revision: 690992
- imported package fonts-ttf-oldstandard

