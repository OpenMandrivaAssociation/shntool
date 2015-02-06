Summary:	A multi-purpose WAVE data processing and reporting utility
Name:		shntool
Version:	3.0.10
Release:	4
URL:		http://etree.org/shnutils/shntool
Source0:	http://etree.org/shnutils/shntool/dist/src/%{name}-%{version}.tar.gz
Group:		Sound
License:	GPLv2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Suggests:	flac
Suggests:	sox
Suggests:	cuetools
Suggests:	ttaenc
Suggests:	shorten
Suggests:	kexis
Suggests:	bonk
Suggests:	wavpack
Suggests:	mp4als
Suggests:	alac_decoder
Suggests:	mac

%description
A multi-purpose WAVE data processing and reporting utility. File formats are
abstracted from its core, so it can process any file that contains WAVE data,
compressed or not - provided there exists a format module to handle that
particular file type. 

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README
%doc doc/*
%{_bindir}/shn*
%{_mandir}/man1/*.1.*


%changelog
* Thu Sep 22 2011 Andrey Bondrov <abondrov@mandriva.org> 3.0.10-3mdv2011.0
+ Revision: 700852
- Suggest more helper codecs as now we have them

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 3.0.10-2mdv2011.0
+ Revision: 614863
- the mass rebuild of 2010.1 packages

* Thu Apr 29 2010 Ahmad Samir <ahmadsamir@mandriva.org> 3.0.10-1mdv2010.1
+ Revision: 541015
- fix license
- import shntool


