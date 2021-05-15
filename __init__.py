import bpy
from mathutils import Vector
import addon_utils

bl_info = {
    "name": "Rigify Part Adder",
    "author": "BlenderBoi",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "Shift-A in Edit Armature Mode",
    "description": "This addon add rigify's building block into a menu accessible in edit armature mode with shift a, this addon will enable rigify if it is not already enabled.",
    "warning": "",
    "doc_url": "",
    "category": "Armature",
}

rigify_parts = [
"basic.copy_chain",
"basic.pivot",
"basic.raw_copy",
"basic.super_copy",
"experimental.super_chain",
"faces.super_face",
"limbs.arm",
"limbs.front_paw",
"limbs.leg",
"limbs.paw",
"limbs.rear_paw",
"limbs.simple_tentacle",
"limbs.super_finger",
"limbs.super_limb",
"limbs.super_palm",
"spines.basic_spine",
"spines.basic_tail",
"spines.super_head",
"spines.super_spine"
]

class RPA_OT_Bone_Adder(bpy.types.Operator):

    bl_idname = "rigify_part_adder.bone_add"
    bl_label = "Add Bone"


    @classmethod
    def poll(cls, context):
        return context.mode =="EDIT_ARMATURE"


    def execute(self, context):

        bpy.ops.armature.bone_primitive_add()



        return {'FINISHED'}



class RPA_OT_Rigify_Part_Adder(bpy.types.Operator):

    bl_idname = "rigify_part_adder.add"
    bl_label = "Add Rigify Part"

    metarig_type: bpy.props.StringProperty()

    @classmethod
    def poll(cls, context):
        return context.mode =="EDIT_ARMATURE"

    def execute(self, context):

        bpy.ops.armature.metarig_sample_add(metarig_type=self.metarig_type)

        if self.metarig_type == "faces.super_face":
            bpy.ops.view3d.snap_selected_to_cursor(use_offset=True)
        else:
            bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)

        return {'FINISHED'}



class RIGIFY_PARTS_ADD_Menu_basic(bpy.types.Menu):
    bl_label = "Rigify Parts"
    bl_idname = "RIGIFY_PARTS_MT_add_basic_menu"


    @classmethod
    def poll(cls, context):
        return context.mode =="EDIT_ARMATURE"


    def draw(self, context):

        layout = self.layout

        for rigify_type in rigify_parts:

            if "basic." in rigify_type:
                layout.operator("rigify_part_adder.add", text=rigify_type.replace("_", " ").replace(".", " ").capitalize()).metarig_type = rigify_type



class RIGIFY_PARTS_ADD_Menu_limbs(bpy.types.Menu):
    bl_label = "Rigify Parts"
    bl_idname = "RIGIFY_PARTS_MT_add_limbs_menu"


    @classmethod
    def poll(cls, context):
        return context.mode =="EDIT_ARMATURE"


    def draw(self, context):

        layout = self.layout

        for rigify_type in rigify_parts:

            if "limbs." in rigify_type:
                layout.operator("rigify_part_adder.add", text=rigify_type.replace("_", " ").replace(".", " ").capitalize()).metarig_type = rigify_type


class RIGIFY_PARTS_ADD_Menu_spines(bpy.types.Menu):
    bl_label = "Rigify Parts"
    bl_idname = "RIGIFY_PARTS_MT_add_spines_menu"


    @classmethod
    def poll(cls, context):
        return context.mode =="EDIT_ARMATURE"


    def draw(self, context):

        layout = self.layout

        for rigify_type in rigify_parts:


            if "spines." in rigify_type:
                layout.operator("rigify_part_adder.add", text=rigify_type.replace("_", " ").replace(".", " ").capitalize()).metarig_type = rigify_type

class RIGIFY_PARTS_ADD_Menu_faces(bpy.types.Menu):
    bl_label = "Rigify Parts"
    bl_idname = "RIGIFY_PARTS_MT_add_faces_menu"


    @classmethod
    def poll(cls, context):
        return context.mode =="EDIT_ARMATURE"


    def draw(self, context):

        layout = self.layout

        for rigify_type in rigify_parts:

            if "faces." in rigify_type:
                layout.operator("rigify_part_adder.add", text=rigify_type.replace("_", " ").replace(".", " ").capitalize()).metarig_type = rigify_type



class RIGIFY_PARTS_ADD_Menu_experimental(bpy.types.Menu):
    bl_label = "Rigify Parts"
    bl_idname = "RIGIFY_PARTS_MT_add_experimental_menu"


    @classmethod
    def poll(cls, context):
        return context.mode =="EDIT_ARMATURE"


    def draw(self, context):

        layout = self.layout

        for rigify_type in rigify_parts:

            if "experimental." in rigify_type:
                layout.operator("rigify_part_adder.add", text=rigify_type.replace("_", " ").replace(".", " ").capitalize()).metarig_type = rigify_type



class RIGIFY_PARTS_ADD_Menu_master(bpy.types.Menu):
    bl_label = "Add Rigify Parts"
    bl_idname = "RIGIFY_PARTS_MT_add_master_menu"


    @classmethod
    def poll(cls, context):
        return context.mode =="EDIT_ARMATURE"


    def draw(self, context):

        layout = self.layout

        # context.window_manager.rigify_active_type = 1
        layout.operator_context = "INVOKE_DEFAULT"
        layout.operator("rigify_part_adder.bone_add", text="Bone")
        layout = self.layout
        layout.menu("RIGIFY_PARTS_MT_add_basic_menu", text="Basic")
        layout.menu("RIGIFY_PARTS_MT_add_limbs_menu", text="Limbs")
        layout.menu("RIGIFY_PARTS_MT_add_spines_menu", text="Spines")
        layout.menu("RIGIFY_PARTS_MT_add_faces_menu", text="Faces")
        layout.menu("RIGIFY_PARTS_MT_add_experimental_menu", text="Experimental")






addon_keymaps = []

classes = [RIGIFY_PARTS_ADD_Menu_master, RIGIFY_PARTS_ADD_Menu_basic, RIGIFY_PARTS_ADD_Menu_limbs, RIGIFY_PARTS_ADD_Menu_spines, RPA_OT_Rigify_Part_Adder, RIGIFY_PARTS_ADD_Menu_faces, RIGIFY_PARTS_ADD_Menu_experimental, RPA_OT_Bone_Adder]

def register():


    for mod in addon_utils.modules():
        if mod.bl_info.get('name', (-1, -1, -1)) == "Rigify":
            if not addon_utils.check(mod.__name__)[1]:
                addon_utils.enable(mod.__name__, default_set=True, handle_error=None)



    for cls in classes:
        bpy.utils.register_class(cls)



    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon



    if kc:

        km = kc.keymaps.new(name = "3D View", space_type="VIEW_3D")
        kmi = km.keymap_items.new("wm.call_menu", type="A", value="PRESS", shift=True, ctrl=True)
        kmi.properties.name = "RIGIFY_PARTS_MT_add_master_menu"
        addon_keymaps.append([km, kmi])



def unregister():


    for cls in classes:
        bpy.utils.unregister_class(cls)

    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)

    addon_keymaps.clear()


if __name__ == "__main__":
    register()
