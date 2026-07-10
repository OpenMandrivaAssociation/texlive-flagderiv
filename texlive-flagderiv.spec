%global tl_name flagderiv
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.10
Release:	%{tl_revision}.1
Summary:	Flag style derivation package
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/flagderiv
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/flagderiv.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/flagderiv.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/flagderiv.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The flagderiv package is used to create mathematical derivations using
the flag/flagpole notation. The package features an intuitive command
syntax, opening and closing multiple flagpoles, different comment
styles, customizable symbols and label namespaces.

