Summary:	A multi-purpose WAVE data processing and reporting utility
Name:		shntool
Version:	3.0.10
Release:	%mkrel 1
URL:		http://etree.org/shnutils/shntool
Source0:	http://etree.org/shnutils/shntool/dist/src/%{name}-%{version}.tar.gz
Group:		Sound
License:	GPLv2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Suggests:	flac
Suggests:	sox
Suggests:	cuetools

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
