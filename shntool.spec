Summary:	A multi-purpose WAVE data processing and reporting utility
Name:	shntool
Version:	3.0.10
Release:	4
Url:		http://shnutils.freeshell.org/shntool/
Source0:	http://shnutils.freeshell.org/shntool/dist/src/%{name}-%{version}.tar.gz
Group:	Sound
License:	GPLv2
Suggests:	alac_decoder
Suggests:	bonk
Suggests:	cuetools
Suggests:	flac
Suggests:	kexis
Suggests:	mac
Suggests:	mp4als
Suggests:	shorten
Suggests:	sox
Suggests:	ttaenc
Suggests:	wavpack

%description
A multi-purpose WAVE data processing and reporting utility. File formats are
abstracted from its core, so it can process any file that contains WAVE data,
compressed or not - provided there exists a format module to handle that
particular file type. 

%files
%doc AUTHORS ChangeLog COPYING NEWS README
%doc doc/*
%{_bindir}/shn*
%{_mandir}/man1/*.1.*

#-----------------------------------------------------------------------------

%prep
%autosetup -p1


%build
%configure
%make_build


%install
%make_install
