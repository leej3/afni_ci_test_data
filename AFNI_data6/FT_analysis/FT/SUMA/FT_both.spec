# delimits comments

# Creation information:
#     user    : taylorpa3
#     date    : Wed Oct 10 00:34:08 EDT 2018
#     machine : cn3124
#     pwd     : /data/NIMH_SSCC/ptaylor/test_fs_bootcamp3/FT/SUMA
#     command : @SUMA_Make_Spec_FS -NIFTI -fspath ./FT -sid FT

# define the group
        Group = FT

# define various States
        StateDef = smoothwm
        StateDef = pial
        StateDef = inflated_lh
        StateDef = inflated_rh
        StateDef = occip.patch.3d
        StateDef = occip.patch.flat_lh
        StateDef = occip.patch.flat_rh
        StateDef = occip.flat.patch.3d_lh
        StateDef = occip.flat.patch.3d_rh
        StateDef = fusiform.patch.flat_lh
        StateDef = fusiform.patch.flat_rh
        StateDef = full.patch.3d
        StateDef = full.patch.flat_lh
        StateDef = full.patch.flat_rh
        StateDef = full.flat.patch.3d_lh
        StateDef = full.flat.patch.3d_rh
        StateDef = full.flat_lh
        StateDef = full.flat_rh
        StateDef = flat.patch_lh
        StateDef = flat.patch_rh
        StateDef = sphere_lh
        StateDef = sphere_rh
        StateDef = white
        StateDef = sphere.reg_lh
        StateDef = sphere.reg_rh
        StateDef = rh.sphere.reg_lh
        StateDef = rh.sphere.reg_rh
        StateDef = lh.sphere.reg_lh
        StateDef = lh.sphere.reg_rh
        StateDef = pial-outer-smoothed
        StateDef = inf_200

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = GIFTI
        SurfaceName = lh.smoothwm.gii
        LocalDomainParent = SAME
        SurfaceState = smoothwm
        EmbedDimension = 3
        Anatomical = Y
        LabelDset = lh.aparc.a2009s.annot.niml.dset

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = GIFTI
        SurfaceName = lh.pial.gii
        LocalDomainParent = lh.smoothwm.gii
        SurfaceState = pial
        EmbedDimension = 3
        Anatomical = Y

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = GIFTI
        SurfaceName = lh.inflated.gii
        LocalDomainParent = lh.smoothwm.gii
        SurfaceState = inflated_lh
        EmbedDimension = 3
        Anatomical = N

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = GIFTI
        SurfaceName = lh.sphere.gii
        LocalDomainParent = lh.smoothwm.gii
        SurfaceState = sphere_lh
        EmbedDimension = 3
        Anatomical = N

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = GIFTI
        SurfaceName = lh.white.gii
        LocalDomainParent = lh.smoothwm.gii
        SurfaceState = white
        EmbedDimension = 3
        Anatomical = Y

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = GIFTI
        SurfaceName = lh.sphere.reg.gii
        LocalDomainParent = lh.smoothwm.gii
        SurfaceState = sphere.reg_lh
        EmbedDimension = 3
        Anatomical = N

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = GIFTI
        SurfaceName = lh.inf_200.gii
        LocalDomainParent = lh.smoothwm.gii
        SurfaceState = inf_200
        EmbedDimension = 3
        Anatomical = N

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = GIFTI
        SurfaceName = rh.smoothwm.gii
        LocalDomainParent = SAME
        SurfaceState = smoothwm
        EmbedDimension = 3
        Anatomical = Y
        LabelDset = rh.aparc.a2009s.annot.niml.dset

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = GIFTI
        SurfaceName = rh.pial.gii
        LocalDomainParent = rh.smoothwm.gii
        SurfaceState = pial
        EmbedDimension = 3
        Anatomical = Y

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = GIFTI
        SurfaceName = rh.inflated.gii
        LocalDomainParent = rh.smoothwm.gii
        SurfaceState = inflated_rh
        EmbedDimension = 3
        Anatomical = N

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = GIFTI
        SurfaceName = rh.sphere.gii
        LocalDomainParent = rh.smoothwm.gii
        SurfaceState = sphere_rh
        EmbedDimension = 3
        Anatomical = N

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = GIFTI
        SurfaceName = rh.white.gii
        LocalDomainParent = rh.smoothwm.gii
        SurfaceState = white
        EmbedDimension = 3
        Anatomical = Y

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = GIFTI
        SurfaceName = rh.sphere.reg.gii
        LocalDomainParent = rh.smoothwm.gii
        SurfaceState = sphere.reg_rh
        EmbedDimension = 3
        Anatomical = N

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = GIFTI
        SurfaceName = rh.inf_200.gii
        LocalDomainParent = rh.smoothwm.gii
        SurfaceState = inf_200
        EmbedDimension = 3
        Anatomical = N

