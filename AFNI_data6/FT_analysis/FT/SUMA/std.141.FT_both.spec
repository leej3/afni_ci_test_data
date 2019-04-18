
#define the group
	Group = FT

#define various States
	StateDef = std.smoothwm
	StateDef = std.pial
	StateDef = std.inflated_lh
	StateDef = std.sphere_lh
	StateDef = std.white
	StateDef = std.sphere.reg_lh
	StateDef = std.inf_200_lh
	StateDef = std.inflated_rh
	StateDef = std.sphere_rh
	StateDef = std.sphere.reg_rh
	StateDef = std.inf_200_rh

NewSurface
	SurfaceFormat = ASCII
	SurfaceType = GIFTI
	SurfaceName = ././std.141.lh.smoothwm.gii
	LocalDomainParent = ././SAME
	LabelDset = ././std.141.lh.aparc.a2009s.annot.niml.dset
	SurfaceState = std.smoothwm
	EmbedDimension = 3
	Anatomical = Y
	LocalCurvatureParent = ././SAME

NewSurface
	SurfaceFormat = ASCII
	SurfaceType = GIFTI
	SurfaceName = ././std.141.lh.pial.gii
	LocalDomainParent = ././std.141.lh.smoothwm.gii
	SurfaceState = std.pial
	EmbedDimension = 3
	Anatomical = Y
	LocalCurvatureParent = ././std.141.lh.smoothwm.gii

NewSurface
	SurfaceFormat = ASCII
	SurfaceType = GIFTI
	SurfaceName = ././std.141.lh.inflated.gii
	LocalDomainParent = ././std.141.lh.smoothwm.gii
	SurfaceState = std.inflated_lh
	EmbedDimension = 3
	Anatomical = N
	LocalCurvatureParent = ././std.141.lh.smoothwm.gii

NewSurface
	SurfaceFormat = ASCII
	SurfaceType = GIFTI
	SurfaceName = ././std.141.lh.sphere.gii
	LocalDomainParent = ././std.141.lh.smoothwm.gii
	SurfaceState = std.sphere_lh
	EmbedDimension = 3
	Anatomical = N
	LocalCurvatureParent = ././std.141.lh.smoothwm.gii

NewSurface
	SurfaceFormat = ASCII
	SurfaceType = GIFTI
	SurfaceName = ././std.141.lh.white.gii
	LocalDomainParent = ././std.141.lh.smoothwm.gii
	SurfaceState = std.white
	EmbedDimension = 3
	Anatomical = Y
	LocalCurvatureParent = ././std.141.lh.smoothwm.gii

NewSurface
	SurfaceFormat = ASCII
	SurfaceType = GIFTI
	SurfaceName = ././std.141.lh.sphere.reg.gii
	LocalDomainParent = ././std.141.lh.smoothwm.gii
	SurfaceState = std.sphere.reg_lh
	EmbedDimension = 3
	Anatomical = N
	LocalCurvatureParent = ././std.141.lh.smoothwm.gii

NewSurface
	SurfaceFormat = ASCII
	SurfaceType = GIFTI
	SurfaceName = ././std.141.lh.inf_200.gii
	LocalDomainParent = ././std.141.lh.smoothwm.gii
	SurfaceState = std.inf_200_lh
	EmbedDimension = 3
	Anatomical = N
	LocalCurvatureParent = ././std.141.lh.smoothwm.gii

NewSurface
	SurfaceFormat = ASCII
	SurfaceType = GIFTI
	SurfaceName = ././std.141.rh.smoothwm.gii
	LocalDomainParent = ././SAME
	LabelDset = ././std.141.rh.aparc.a2009s.annot.niml.dset
	SurfaceState = std.smoothwm
	EmbedDimension = 3
	Anatomical = Y
	LocalCurvatureParent = ././SAME

NewSurface
	SurfaceFormat = ASCII
	SurfaceType = GIFTI
	SurfaceName = ././std.141.rh.pial.gii
	LocalDomainParent = ././std.141.rh.smoothwm.gii
	SurfaceState = std.pial
	EmbedDimension = 3
	Anatomical = Y
	LocalCurvatureParent = ././std.141.rh.smoothwm.gii

NewSurface
	SurfaceFormat = ASCII
	SurfaceType = GIFTI
	SurfaceName = ././std.141.rh.inflated.gii
	LocalDomainParent = ././std.141.rh.smoothwm.gii
	SurfaceState = std.inflated_rh
	EmbedDimension = 3
	Anatomical = N
	LocalCurvatureParent = ././std.141.rh.smoothwm.gii

NewSurface
	SurfaceFormat = ASCII
	SurfaceType = GIFTI
	SurfaceName = ././std.141.rh.sphere.gii
	LocalDomainParent = ././std.141.rh.smoothwm.gii
	SurfaceState = std.sphere_rh
	EmbedDimension = 3
	Anatomical = N
	LocalCurvatureParent = ././std.141.rh.smoothwm.gii

NewSurface
	SurfaceFormat = ASCII
	SurfaceType = GIFTI
	SurfaceName = ././std.141.rh.white.gii
	LocalDomainParent = ././std.141.rh.smoothwm.gii
	SurfaceState = std.white
	EmbedDimension = 3
	Anatomical = Y
	LocalCurvatureParent = ././std.141.rh.smoothwm.gii

NewSurface
	SurfaceFormat = ASCII
	SurfaceType = GIFTI
	SurfaceName = ././std.141.rh.sphere.reg.gii
	LocalDomainParent = ././std.141.rh.smoothwm.gii
	SurfaceState = std.sphere.reg_rh
	EmbedDimension = 3
	Anatomical = N
	LocalCurvatureParent = ././std.141.rh.smoothwm.gii

NewSurface
	SurfaceFormat = ASCII
	SurfaceType = GIFTI
	SurfaceName = ././std.141.rh.inf_200.gii
	LocalDomainParent = ././std.141.rh.smoothwm.gii
	SurfaceState = std.inf_200_rh
	EmbedDimension = 3
	Anatomical = N
	LocalCurvatureParent = ././std.141.rh.smoothwm.gii
