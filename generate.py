from pygltflib import GLTF2, Scene, Node, Mesh, Primitive, Buffer, BufferView, Accessor, Asset, Material, PbrMetallicRoughness
import numpy as np

# define vertice, normals and indices for a cube to fix incorrect winding order of the cube
vertices = np.array([
    [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],  # back face
    [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1],      # front face
    [-1, -1, -1], [-1, -1, 1], [-1, 1, 1], [-1, 1, -1],  # left face
    [1, -1, -1], [1, -1, 1], [1, 1, 1], [1, 1, -1],      # right face
    [-1, -1, -1], [-1, -1, 1], [1, -1, 1], [1, -1, -1],  # bottom face
    [-1, 1, -1], [-1, 1, 1], [1, 1, 1], [1, 1, -1]       # top face
], dtype=np.float32).flatten()

normals = np.array([
    [0, 0, -1], [0, 0, -1], [0, 0, -1], [0, 0, -1],  # back face
    [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1],     # front face
    [-1, 0, 0], [-1, 0, 0], [-1, 0, 0], [-1, 0, 0], # left face
    [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0],     # right face
    [0, -1, 0], [0, -1, 0], [0, -1, 0], [0, -1, 0], # bottom face
    [0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0]      # top face
], dtype=np.float32).flatten()

indices = np.array([
    0, 1, 2, 2, 3, 0,  # back face
    4, 5, 6, 6, 7, 4,  # front face
    8, 9, 10, 10, 11, 8,  # left face
    12, 13, 14, 14, 15, 12,  # right face
    16, 17, 18, 18, 19, 16,  # bottom face
    20, 21, 22, 22, 23, 20   # top face
], dtype=np.uint16).flatten()

# buffer helper
buffer_data = vertices.tobytes() + normals.tobytes() + indices.tobytes()

# create GLTF model
gltf = GLTF2(
    asset=Asset(version="2.0"),
    buffers=[Buffer(byteLength=len(buffer_data))],
    bufferViews=[
        BufferView(buffer=0, byteOffset=0, byteLength=vertices.nbytes, target=34962),
        BufferView(buffer=0, byteOffset=vertices.nbytes, byteLength=normals.nbytes, target=34962),
        BufferView(buffer=0, byteOffset=vertices.nbytes + normals.nbytes, byteLength=indices.nbytes, target=34963)
    ],
    accessors=[
        Accessor(bufferView=0, byteOffset=0, componentType=5126, count=24, type="VEC3"),  # vertices
        Accessor(bufferView=1, byteOffset=0, componentType=5126, count=24, type="VEC3"),  # normals
        Accessor(bufferView=2, byteOffset=0, componentType=5123, count=36, type="SCALAR")  # indices
    ],
    materials=[
        Material(pbrMetallicRoughness=PbrMetallicRoughness(baseColorFactor=[0, 0, 0, 1]))  # black
    ],
    meshes=[
        Mesh(primitives=[
            Primitive(attributes={"POSITION": 0, "NORMAL": 1}, indices=2, material=0)  # black material
        ])
    ],
    nodes=[Node(mesh=0)],
    scenes=[Scene(nodes=[0])],
    scene=0
)

# add buffer data to the model
gltf.set_binary_blob(buffer_data)

# save to .glb file
gltf.save("cube.glb")