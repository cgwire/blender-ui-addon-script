bl_info = {
    "name": "Simple Addon Example",
    "author": "Your Name",
    "version": (1, 0),
    "blender": (4, 0, 0),
    "location": "View3D > Sidebar > Simple Tab",
    "description": "A simple example addon that prints a message",
    "category": "3D View",
}

import bpy


# Operator: the actual action (prints message to console)
class SIMPLEADDON_OT_hello(bpy.types.Operator):
    bl_idname = "simple_addon.say_hello"
    bl_label = "Say Hello"
    bl_description = "Prints a message to the console"

    def execute(self, context):
        self.report({"INFO"}, "Hello from Blender Addon!")
        print("Hello from Blender Addon!")
        return {"FINISHED"}


# Panel: where the button appears
class SIMPLEADDON_PT_panel(bpy.types.Panel):
    bl_label = "Simple Addon Panel"
    bl_idname = "SIMPLEADDON_PT_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Simple"

    def draw(self, context):
        layout = self.layout
        layout.operator("simple_addon.say_hello")


# Register/unregister
def register():
    bpy.utils.register_class(SIMPLEADDON_OT_hello)
    bpy.utils.register_class(SIMPLEADDON_PT_panel)


def unregister():
    bpy.utils.unregister_class(SIMPLEADDON_PT_panel)
    bpy.utils.unregister_class(SIMPLEADDON_OT_hello)


if __name__ == "__main__":
    register()
