# PhysioSentinel Gait V93 — Z-Anatomy/BodyParts3D

V93 changes the default workflow from manual mesh upload to a preconfigured open-atlas pipeline.

## Included
- `rig_map.json`: HALPE26 → human rig segment mapping.
- `ATTRIBUTION_Z_ANATOMY_BODYParts3D.txt`: provenance/license notice.
- V93 UI and retarget payload generation.
- Validation that distinguishes a static GLB from a genuinely rigged/skinned GLB.

## Important technical boundary
A detailed anatomical GLB is not falsely labelled as rigged merely because it contains realistic anatomy. Real skinning requires an armature/skin weights in the source GLB. V93 keeps this distinction explicit.

## Recommended source
Z-Anatomy / BodyParts3D, reduced to skeleton and gait-relevant musculature. The source model is CC BY-SA and derivatives must preserve attribution/share-alike obligations.
