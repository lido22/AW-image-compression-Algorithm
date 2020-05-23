image = imread('lens.png');
flat = image(:);
dimensions = size(image);
len = dimensions(1)*dimensions(2)
prop = zeros(1,256);
for i= 1:len
    prop[flat(i)+1] = prop[flat(i)+1)]+1;
end
for i=flat
    prop(i+1) = prop(i+1)/len;
end

dict = huffmandict(flat,prop);

