#version 150

uniform sampler2D p3d_Texture0;
uniform sampler2D p3d_Texture1;

uniform sampler2D mytexture1;
uniform sampler2D mytexture2;
uniform sampler2D bunnytex;

// Input from vertex shader
in vec2 texcoord;
in vec4 p3d_Color;

// Output to the screen
out vec4 p3d_FragColor;

void main() {
    
  vec4 color;
  vec4 v1 = texture(mytexture2, texcoord);
  vec4 v2 = texture(mytexture1, texcoord);
  vec4 v3 = texture(bunnytex, texcoord);
  color = mix(v1,v2,v3.x);
  
  //color = textureGrad(mytexture1, texcoord, uv, uv);
  //vec4 color = textureGrad(mytexture2, texcoord, uv2, uv2);
  
  p3d_FragColor = color; //color.bgra;
}
