from panda3d.core import Vec3
from panda3d.core import NodePath
from panda3d.core import CollisionSphere

from wecs import panda3d
from wecs import mechanics
from wecs.aspects import Aspect
from wecs.aspects import factory


character = Aspect([panda3d.Clock, panda3d.Position, panda3d.Scene,
                    panda3d.CharacterController, panda3d.Model])


def rebecca_bumper():
    return {
        'bumper': dict(
            shape=CollisionSphere,
            center=Vec3(0.0, 0.0, 1.0),
            radius=0.7,
        ),
    }
def rebecca_lifter():
    return {
        'lifter': dict(
            shape=CollisionSphere,
            center=Vec3(0.0, 0.0, 0.25),
            radius=0.5,
        ),
    }
walking = Aspect([panda3d.WalkingMovement, panda3d.CrouchingMovement, panda3d.SprintingMovement,
                  panda3d.InertialMovement, panda3d.BumpingMovement, panda3d.FallingMovement,
                  panda3d.JumpingMovement],
                 overrides = {
                     panda3d.BumpingMovement: dict(solids=factory(rebecca_bumper)),
                     panda3d.FallingMovement: dict(solids=factory(rebecca_lifter)),
                 },
)
avatar = Aspect([character, walking],
                overrides={panda3d.Model: dict(model_name='rebecca.bam')})


def spectator_bumper():
    return dict(
        solids={
            'bumper': dict(
                shape=CollisionSphere,
                center=Vec3(0.0, 0.0, 0.0),
                radius=0.1,
            ),
        },
    )
spectator = Aspect([character, panda3d.FloatingMovement, panda3d.BumpingMovement],
                   overrides={
                       panda3d.Model: dict(node=factory(lambda:NodePath('spectator'))),
                       panda3d.BumpingMovement: dict(solids=factory(spectator_bumper)),
                   },
)


pc_mind = Aspect([panda3d.Input])
npc_mind = Aspect([panda3d.ConstantCharacterAI])


first_person = Aspect([panda3d.FirstPersonCamera])
third_person = Aspect([panda3d.TurntableCamera, panda3d.TurningBackToCameraMovement,
                       panda3d.CollisionZoom, panda3d.ThirdPersonCamera])


player_character = Aspect([avatar, pc_mind, third_person])
non_player_character = Aspect([avatar, npc_mind])
