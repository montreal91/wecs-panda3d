# WECS

WECS stands for World, Entities, Components, Systems, and is an implementation
of an ECS system. Its goal is to put usability first, and not let performance
optimizations compromise it.

Beyond the core, WECS' goal is to accumulate enough game mechanics, so that the
time between imagining a game and getting to the point where you actually work
on your specific game mechanics is a matter of a few minutes of setting up
boilerplate code. In particular, a module for Panda3D is provided.

## In WECS.

A 'World' holds 'Entities' and 'Systems'.
These 'Entities' are made up of 'Components'.
The 'Components' contain an entity's data/variables.
The 'Systems' then 'filter' all the world's entities by their components,
iterates over them and applies logic to component data.

This keeps data and logic seperated, modular, readable and reusable.

Optionally there are 'Aspects',
These are sets of components meant to be reinstanciated as new entities.

## Install
```
  pip install wecs
```

## A Hello World

```
from wecs.core import World, Component, System, and_filter


# Component that describes an entity that prints something
@Component()
class Printer:
    message: str


class Print(System):
    # Filter all entities in the world described as Printer
    entity_filters = {
        'printers' : and_filter([Printer])
    }

    def update(self, entities_by_filter):
        # Iterate over all filtered entities
        for entity in entities_by_filter['printers']:
            # Print their message
            print(entity[Printer].message)


world = World() # Make a world
world.add_system(Print(), 0) # Add to it the print system

printer_entity = world.create_entity() # A new entity
# Make it a Printer, and set it's message.
printer_entity.add_component(Printer(message="Hello World"))
world.update() # Run all added systems
```

## WECS for Panda3D
There are some game mechanics for panda3d that come out of the box:

* Camera modes:
    * First-person
    * Third-person
    * Turntable

* Character controller:
    * Flying/Floating
    * Crouching, Walking, Running, Sprinting and Strafing
    * Bumping, Falling and Jumping
    * Basic NPC movement
    * Stamina

* Animation:
    * Blended animations
    * Basic character controller animation
