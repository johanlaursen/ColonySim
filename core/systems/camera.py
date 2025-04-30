# class CameraProcessor(esper.Processor):
#     def __init__(self, camera_entity):
#         super().__init__()
#         self.camera_entity = camera_entity
#     def process(self, dt):
#         cam = esper.component_for_entity(self.camera_entity, Camera)
#         for ent, (rend,) in esper.get_components(Renderable):
#             # Apply camera transform
#             rend.sprite.x -= cam.x
#             rend.sprite.y -= cam.y
