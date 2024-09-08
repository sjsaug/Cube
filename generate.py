from pygltflib import GLTF2, Scene, Node, Mesh, Primitive, Buffer, BufferView, Accessor, Asset, Material, PbrMetallicRoughness
import numpy as np

vertices = np.array([
    [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],  # back face
    [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]       # front face
], dtype=np.float32).flatten()

indices = np.array([
    0, 1, 2, 2, 3, 0,  # back face
    4, 5, 6, 6, 7, 4,  # front face
    0, 1, 5, 5, 4, 0,  # bottom face
    2, 3, 7, 7, 6, 2,  # top face
    0, 3, 7, 7, 4, 0,  # ;eft face
    1, 2, 6, 6, 5, 1   # right face
], dtype=np.uint16).flatten()

# buffer helper
buffer_data = vertices.tobytes() + indices.tobytes()

# create GLTF model
gltf = GLTF2(
    asset=Asset(version="2.0"),
    buffers=[Buffer(byteLength=len(buffer_data))],
    bufferViews=[
        BufferView(buffer=0, byteOffset=0, byteLength=vertices.nbytes, target=34962),
        BufferView(buffer=0, byteOffset=vertices.nbytes, byteLength=indices.nbytes, target=34963)
    ],
    accessors=[
        Accessor(bufferView=0, byteOffset=0, componentType=5126, count=8, type="VEC3"),
        Accessor(bufferView=1, byteOffset=0, componentType=5123, count=36, type="SCALAR")
    ],
    materials=[
        Material(pbrMetallicRoughness=PbrMetallicRoughness(baseColorFactor=[0, 0, 0, 1]))  # black
    ],
    meshes=[
        Mesh(primitives=[
            Primitive(attributes={"POSITION": 0}, indices=1, material=0)  # black material
        ])
    ],
    nodes=[Node(mesh=0)],
    scenes=[Scene(nodes=[0])],
    scene=0
)

# add buffer data to the mdoel
gltf.set_binary_blob(buffer_data)
gltf.save("cube.glb")