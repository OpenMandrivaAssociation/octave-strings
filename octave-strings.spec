%global octpkg strings

Summary:	Additional functions for manipulation and analysis of strings with Octave
Name:		octave-strings
Version:	1.3.0
Release:	2
License:	GPLv3+ and FreeBSD
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/strings/
Source0:	https://downloads.sourceforge.net/octave/strings-%{version}.tar.gz

BuildRequires:  octave-devel >= 3.8.0
BuildRequires:	pkgconfig(libpcre)

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
Additional functions for manipulation and analysis of strings with Octave.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*
%dir %{octpkglibdir}
%{octpkglibdir}/*
#{_metainfodir}/*.metainfo.xml

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

%build
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

