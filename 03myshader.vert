#version 150

// Uniform inputs
uniform mat4 p3d_ModelViewProjectionMatrix;
uniform vec4 position;

// Vertex inputs
in vec2 p3d_MultiTexCoord0;
in vec4 p3d_Vertex;

in vec3 p3d_Tangent;
//in vec4 p3d_Color;

// Output to fragment shader
out vec2 texcoord;
out vec4 p3d_Color;

void main() {
  gl_Position = p3d_ModelViewProjectionMatrix * p3d_Vertex;
  
  texcoord = p3d_MultiTexCoord0;
}
